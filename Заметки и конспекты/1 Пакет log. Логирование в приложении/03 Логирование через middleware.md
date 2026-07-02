---
title: Логирование через middleware
source: yandex-practicum
course: go-developer
converted: 2026-05-28
part: 1
прочитано: 2026-05-28
---

# Логирование через middleware

В этом уроке покажем, как реализовать логирование с использованием стороннего пакета `zap`, чтобы регистрировать сведения о запросах и ответах.

Для демонстрации возможностей пакета `zap` создадим приложение, которое имеет только один эндпоинт `/ping` и при обращении к нему возвращает `pong`:

```go
package main

import (
    "fmt"
    "net/http"

    "go.uber.org/zap"
)

var sugar zap.SugaredLogger

func main() {
    // создаём предустановленный регистратор zap
    logger, err := zap.NewDevelopment()
    if err != nil {
        // вызываем панику, если ошибка
        panic(err)
    }
    defer logger.Sync()

    // делаем регистратор SugaredLogger
    sugar = *logger.Sugar()

    http.Handle("/ping", pingHandler())

    addr := "127.0.0.1:8080"
    // записываем в лог, что сервер запускается
    sugar.Infow(
        "Starting server",
        "addr", addr,
    )
    if err := http.ListenAndServe(addr, nil); err != nil {
        // записываем в лог ошибку, если сервер не запустился
        sugar.Fatalw(err.Error(), "event", "start server")
    }
}

// хендлер для /ping
func pingHandler() http.Handler {
    fn := func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        _, _ = fmt.Fprintf(w, "pong\n")
    }
    return http.HandlerFunc(fn)
}
```

Запустим сервер:

```go
$go run main.go
2022-11-18T00:09:33.999+0300
INFO    zap-logger-project/main.go:26    Starting server    {"addr": "127.0.0.1:8080"}
```

Теперь в другом терминале выполним команду `curl --include localhost:8080/ping`:

```
$curl --include localhost:8080/ping
HTTP/1.1 200 OK
Date: Mon, 31 Oct 2022 18:21:33 GMT
Content-Length: 5
Content-Type: text/plain; charset=utf-8

pong
```

При запуске `curl` обратной связи не будет:

```go
$go run main.go
2022-11-18T00:09:33.999+0300
INFO    zap-logger-project/main.go:26    Starting server    {"addr": "127.0.0.1:8080"}
```

## Сведения о запросе

Чтобы сведения о запросе отражались в логере, нужно зарегистрировать детали запроса: URI, метод и время, затраченное на его выполнение. Для этого напишем функцию-оболочку `WithLogging()`, которая оборачивает `http.Handler`, добавляет дополнительный код для регистрации сведений и возвращает новый `http.Handler`. Это и есть `middleware`.

```go
// WithLogging добавляет дополнительный код для регистрации сведений о запросе
// и возвращает новый http.Handler.
func WithLogging(h http.Handler) http.Handler {
    logFn := func(w http.ResponseWriter, r *http.Request) {
        // функция Now() возвращает текущее время
        start := time.Now()

        // эндпоинт /ping
        uri := r.RequestURI
        // метод запроса
        method := r.Method

        // точка, где выполняется хендлер pingHandler
        h.ServeHTTP(w, r) // обслуживание оригинального запроса

        // Since возвращает разницу во времени между start
        // и моментом вызова Since. Таким образом можно посчитать
        // время выполнения запроса.
        duration := time.Since(start)

        // отправляем сведения о запросе в zap
        sugar.Infoln(
            "uri", uri,
            "method", method,
            "duration", duration,
        )

    }
    // возвращаем функционально расширенный хендлер
    return http.HandlerFunc(logFn)
}
```

Теперь в функции `main` нужно обернуть обработчик `pingHandler()` функцией `WithLogging()`:

```
http.Handle("/ping", WithLogging(pingHandler()))
```

Сделано! Запустим сервер и, как в прошлый раз, выполним в другом терминале команду `curl --include localhost:8080/ping`. Там, где запустили сервер, будет вот такой вывод в stdout:

```go
go run main.go
2022-11-18T01:20:43.511+0300
INFO    zap-logger-project/main.go:28   Starting server {"addr": "127.0.0.1:8080"}
2022-11-18T01:20:48.332+0300
INFO    zap-logger-project/main.go:62   uri /ping method GET duration 4.417µs
```

## Сведения об ответе

Теперь добавим в логер детали ответа: код статуса и размер содержимого. Это будет немного сложнее, потому что нужно каким-то образом получить эти детали после вызова обработчика `ServeHTTP(w http.ResponseWriter, r *http.Request)`.

Первый аргумент `w http.ResponseWriter` отвечает за запись тела ответа и кода состояния. Он реализует интерфейс `http.ResponseWriter`:

```go
type ResponseWriter interface {
    Header() Header
    Write([]byte) (int, error)
    WriteHeader(statusCode int)
}
```

Идея состоит в том, чтобы внедрить собственную реализацию в методы интерфейса `http.ResponseWriter`:

- `Write()` — метод для получения размера ответа;
- `WriteHeader()` — метод для получения кода состояния.

```go
type (
    // берём структуру для хранения сведений об ответе
    responseData struct {
        status int
        size int
    }

    // добавляем реализацию http.ResponseWriter
    loggingResponseWriter struct {
        http.ResponseWriter // встраиваем оригинальный http.ResponseWriter
        responseData *responseData
    }
)

func (r *loggingResponseWriter) Write(b []byte) (int, error) {
    // записываем ответ, используя оригинальный http.ResponseWriter
    size, err := r.ResponseWriter.Write(b)
    r.responseData.size += size // захватываем размер
    return size, err
}

func (r *loggingResponseWriter) WriteHeader(statusCode int) {
    // записываем код статуса, используя оригинальный http.ResponseWriter
    r.ResponseWriter.WriteHeader(statusCode)
    r.responseData.status = statusCode // захватываем код статуса
}
```

Готово! Переопределили два метода из интерфейса `http.ResponseWriter`: внутри каждого из них вызвали оригинальный метод, а затем добавили дополнительную функциональность, чтобы сохранить нужные сведения в структуре `responseData`.

Теперь осталось обновить функцию `WithLogging()`, используя `loggingResponseWriter`:

```go
func WithLogging(h http.Handler) http.Handler {
    logFn := func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()

        responseData := &responseData {
            status: 0,
            size: 0,
        }
        lw := loggingResponseWriter {
            ResponseWriter: w, // встраиваем оригинальный http.ResponseWriter
            responseData: responseData,
        }
        h.ServeHTTP(&lw, r) // внедряем реализацию http.ResponseWriter

        duration := time.Since(start)

        sugar.Infoln(
            "uri", r.RequestURI,
            "method", r.Method,
            "status", responseData.status, // получаем перехваченный код статуса ответа
            "duration", duration,
            "size", responseData.size, // получаем перехваченный размер ответа
        )
    }
    return http.HandlerFunc(logFn)
}
```

Вот и всё! Запустим сервер и посмотрим логи. Для этого снова потребуется два терминала. В первом запускаем сервер, во втором выполняем команду `curl --include localhost:8080/ping`:

```go
$ go run main.go
2022-11-18T01:36:23.259+0300
INFO    zap-logger-project/main.go:28    Starting server {"addr": "127.0.0.1:8080"}
2022-11-18T01:36:35.672+0300
INFO    zap-logger-project/main.go:68    uri /ping method GET status 200 duration 9.5µs size 5
```

## Обучаем Алису

Создадим новый файл `internal/logger/logger.go`, в котором будет содержаться синглтон логера:

```
> ~/dev/alice-skill
       |
       |--- cmd
       |     |--- skill
       |            |--- flags.go
       |            |--- main.go
       |            |--- main_test.go
       |--- internal
       |       |--- logger
       |              |--- logger.go
       |--- go.mod
       |--- go.sum
```

Расположение пакета `logger` в директории `internal` не позволит никакому другому коду, кроме того, который находится в директории `~/dev/alice-skill`, использовать объекты этого пакета.

В файл `logger.go` поместим следующий код:

```go
package logger

import (
    "net/http"

    "go.uber.org/zap"
)

// Log будет доступен всему коду как синглтон.
// Никакой код навыка, кроме функции InitLogger, не должен модифицировать эту переменную.
// По умолчанию установлен no-op-логер, который не выводит никаких сообщений.
var Log *zap.Logger = zap.NewNop()

// Initialize инициализирует синглтон логера с необходимым уровнем логирования.
func Initialize(level string) error {
    // преобразуем текстовый уровень логирования в zap.AtomicLevel
    lvl, err := zap.ParseAtomicLevel(level)
    if err != nil {
        return err
    }
    // создаём новую конфигурацию логера
    cfg := zap.NewProductionConfig()
    // устанавливаем уровень
    cfg.Level = lvl
    // создаём логер на основе конфигурации
    zl, err := cfg.Build()
    if err != nil {
        return err
    }
    // устанавливаем синглтон
    Log = zl
    return nil
}

// RequestLogger — middleware-логер для входящих HTTP-запросов.
func RequestLogger(h http.HandlerFunc) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        Log.Debug("got incoming HTTP request",
            zap.String("method", r.Method),
            zap.String("path", r.URL.Path),
        )
        h(w, r)
    })
}
```

Чтобы иметь возможность задавать уровень логирования, поправим файл `cmd/skill/flag.go`:

```go
package main

import (
    "flag"
    "os"
)

var (
    flagRunAddr  string
    flagLogLevel string
)

func parseFlags() {
    flag.StringVar(&flagRunAddr, "a", ":8080", "address and port to run server")
    flag.StringVar(&flagLogLevel, "l", "info", "log level")
    flag.Parse()

    if envRunAddr := os.Getenv("RUN_ADDR"); envRunAddr != "" {
        flagRunAddr = envRunAddr
    }
    if envLogLevel := os.Getenv("LOG_LEVEL"); envLogLevel != "" {
        flagLogLevel = envLogLevel
    }
}
```

Теперь нужно инициализировать логер при запуске сервера. Для этого обновим код в файле `cmd/skill/main.go`. Добавим в секцию `import` пакет с логером:

```go
import (
    "net/http"

    "go.uber.org/zap"

    "github.com/bluegopher/alice-skill/internal/logger"
)
```

После этого можно инициализировать логер в функции `run()`:

```go
func run() error {
    if err := logger.Initialize(flagLogLevel); err != nil {
        return err
    }

    logger.Log.Info("Running server", zap.String("address", flagRunAddr))
    // оборачиваем хендлер webhook в middleware с логированием
    return http.ListenAndServe(flagRunAddr, logger.RequestLogger(webhook))
}

func webhook(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodPost {
        logger.Log.Debug("got request with bad method", zap.String("method", r.Method))
        w.WriteHeader(http.StatusMethodNotAllowed)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    _, _ = w.Write([]byte(`
          {
            "response": {
              "text": "Извините, я пока ничего не умею"
            },
            "version": "1.0"
          }
        `))
    logger.Log.Debug("sending HTTP 200 response")
}
```

Теперь при запуске сервера вывод будет примерно таким:

```
$ ./skill -a :8081 -l debug
2022-11-19T12:30:04.242Z    INFO    skill/main.go:11    Running server    {"address": ":8081"}
```

А при получении запроса — таким:

```
2022-11-19T12:30:15.242Z    DEBUG    logger/logger.go:24    got incoming HTTP request    {"method": ":POST", "path": "/"}
2022-11-19T12:30:15.243Z    DEBUG    skill/main.go:32    sending HTTP 200 response
```