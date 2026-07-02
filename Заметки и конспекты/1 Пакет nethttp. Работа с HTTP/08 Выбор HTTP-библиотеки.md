---
title: "Выбор HTTP-библиотеки"
source: yandex-practicum
course: go-developer
converted: 2026-05-28
part: 1
---

# Выбор HTTP-библиотеки

В этом уроке рассмотрим два типа HTTP-библиотек:

- клиентские — позволяют отправлять запросы;
- серверные — позволяют принимать запросы.

## Клиентские библиотеки

Представьте, что вам поставили задачу: сделать код читабельным при сложных последовательных запросах, быстро разработать алгоритм загрузки файлов или настроить механизм повторения и лимитирования запросов.

Простые запросы с помощью пакета `net/http` реализовать легко:

```go
resp, err := http.Get("https://yandex.ru/")

resp, err := http.Post("http://yandex-example.ru/upload", "image/png", &buf)

resp, err := http.PostForm("http://yandex-example.com/form",
    url.Values{"key": {"Value"}, "id": {"123"}})
```

Но чтобы добавить, например, авторизацию, нужно написать дополнительный код, который выглядит сложнее:

```go
package main

import (
    "fmt"
    "io"
    "log"
    "net/http"
)

var bearer = "Bearer <Token>"

func main() {
    // создаём новый запрос
    req, err := http.NewRequest("GET", "https://yandex.ru", nil)
    if err != nil {
        log.Println(err)
        return
    }

    // добавляем авторизацию
    req.Header.Add("Authorization", bearer)

    // создаём клиент
    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        log.Println("Error on response.\n[ERROR] -", err)
        return
    }
    defer resp.Body.Close()

    if resp.StatusCode != http.StatusOK {
        log.Println("Bad status code on response: ", resp.StatusCode)
        return
    }

    body, err := io.ReadAll(resp.Body)
    // продолжаем работу
    fmt.Println(body)
}
```

А что, если нужно использовать запросы с параметрами, тайм-ауты и прочие настройки? Всё это усложняет код — читать его становится трудно. К тому же уходит много времени на решение второстепенных задач вместо основной.

И вот тут как раз пригодятся готовые решения. На Go написано много пакетов для выполнения HTTP-запросов. Актуальный список можно посмотреть на [Awesome Go](https://github.com/avelino/awesome-go#http-clients).

Перечислим самые популярные из них:

Конкретных рекомендаций по выбору пакета нет. Всё зависит от того, какую задачу вы хотите решить. Если вы знаете Python и хотите ближе познакомиться с Go, выбирайте пакет `grequests`. Для высоконагруженных проектов подойдёт `heimdall`, а если вы начинающий разработчик, выбирайте `resty`.

#### Библиотека resty

Для примера перепишем запрос к серверу с использованием библиотеки `resty`. Она поддерживает много дополнительных функций:

- запросы `GET`, `POST`, `PUT`, `PATCH`, `OPTIONS`;
- автоматическую сериализацию и десериализацию структур: `SetError()` для ошибок, `SetResult()` для результата;
- лимитирование запросов;
- максимальное одновременное количество запросов;
- простую загрузку нескольких файлов.

```go
package main

import (
    "fmt"
    "github.com/go-resty/resty/v2"
)

func main() {
    // создаём новый клиент
    client := resty.New()

    resp, err := client.R().
        SetAuthToken("Bearer <TOKEN>").
        Get("https://my-example-site.ru")

    fmt.Println("Исследуем объект Response:")
    fmt.Println("Error      :", err)
    fmt.Println("Status Code:", resp.StatusCode())
    fmt.Println("Status     :", resp.Status())
    fmt.Println("Time       :", resp.Time())
    fmt.Println("Received At:", resp.ReceivedAt())
    fmt.Println("Body       :\n", resp)
    fmt.Println("----")
}
```

Такой код читать легче, не правда ли?

Можно настроить автоматическую конвертацию ошибок и результата в объект — методами `SetError()` и `SetResult()`. Например, так:

```go
package main

import (
    "fmt"
    "github.com/go-resty/resty/v2"
    "time"
)

// MyApiError — описание ошибки при неверном запросе.
type MyApiError struct {
    Code      int       `json:"code"`
    Message   string    `json:"message"`
    Timestamp time.Time `json:"timestamp"`
}

// Post — модель, описание основного объекта.
type Post struct {
    UserID int    `json:"userId"`
    ID     int    `json:"id"`
    Title  string `json:"title"`
    Text   string `json:"text"`
}

func main() {
    client := resty.New()

    var responseErr MyApiError
    var post Post

    _, err := client.R().
        SetError(&responseErr).
        SetResult(&post).
        Get("https://jsonplaceholder.typicode.com/posts/1")

    if err != nil {
        fmt.Println(responseErr)
        panic(err)
        return
    }

    fmt.Println(post)
}
```

Пока не обращайте внимание на JSON-конструкции, в следующих уроках расскажем о них подробнее.

Можно передавать параметры URL в понятном виде:

```go
package main

import (
    "fmt"
    "github.com/go-resty/resty/v2"
)

func main() {
    client := resty.New()

    resp, err := client.R().SetPathParams(map[string]string{
        "postID": "1",
    }).Get("https://jsonplaceholder.typicode.com/posts/{postID}")

    if err != nil {
        panic(err)
    }

    fmt.Println(resp)
}
```

Можно в несколько строчек реализовать повторную отправку запроса в случае ошибки и отправлять `POST`-запросы разными способами:

```go
package main

import (
    "fmt"
    "github.com/go-resty/resty/v2"
    "time"
)

func main() {
    client := resty.New()

    client.
        // устанавливаем количество повторений
        SetRetryCount(3).
        // длительность ожидания между попытками
        SetRetryWaitTime(30 * time.Second).
        // длительность максимального ожидания
        SetRetryMaxWaitTime(90 * time.Second)

    resp, err := client.R().
      SetHeader("Content-Type", "application/json").
      SetBody(`{"title":"foo", "body":"bar", "userId": 7}`).
      Post("https://jsonplaceholder.typicode.com/posts")

    if err != nil {
        panic(err)
    }
    fmt.Println(resp)

    // другой вариант POST-запроса
    // если передаётся map, то по умолчанию используется JSON
    resp, err = client.R().
      SetBody(map[string]interface{}{"title":"My title", "body":"Content", "userId": 7}).
      Post("https://jsonplaceholder.typicode.com/posts")

    if err != nil {
        panic(err)
    }
    fmt.Println(resp)
}
```


## Обучаем Алису

Заменим содержимое файла `cmd/skill/main_test.go` на новый код:

```go
package main

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/go-resty/resty/v2"
    "github.com/stretchr/testify/assert"
)

func TestWebhook(t *testing.T) {
    // тип http.HandlerFunc реализует интерфейс http.Handler
    // это поможет передать хендлер тестовому серверу
    handler := http.HandlerFunc(webhook)
    // запускаем тестовый сервер, будет выбран первый свободный порт
    srv := httptest.NewServer(handler)
    // останавливаем сервер после завершения теста
    defer srv.Close()

    // ожидаемое содержимое тела ответа при успешном запросе
    successBody := `{
        "response": {
            "text": "Извините, я пока ничего не умею"
        },
        "version": "1.0"
    }`

    // описываем набор данных: метод запроса, ожидаемый код ответа, ожидаемое тело
    testCases := []struct {
        method       string
        expectedCode int
        expectedBody string
    }{
        {method: http.MethodGet, expectedCode: http.StatusMethodNotAllowed, expectedBody: ""},
        {method: http.MethodPut, expectedCode: http.StatusMethodNotAllowed, expectedBody: ""},
        {method: http.MethodDelete, expectedCode: http.StatusMethodNotAllowed, expectedBody: ""},
        {method: http.MethodPost, expectedCode: http.StatusOK, expectedBody: successBody},
    }

    for _, tc := range testCases {
        t.Run(tc.method, func(t *testing.T) {
            // делаем запрос с помощью библиотеки resty к адресу запущенного сервера,
            // который хранится в поле URL соответствующей структуры
            req := resty.New().R()
            req.Method = tc.method
            req.URL = srv.URL

            resp, err := req.Send()
            assert.NoError(t, err, "error making HTTP request")

            assert.Equal(t, tc.expectedCode, resp.StatusCode(), "Response code didn't match expected")
            // проверяем корректность полученного тела ответа, если мы его ожидаем
            if tc.expectedBody != "" {
                assert.JSONEq(t, tc.expectedBody, string(resp.Body()))
            }
        })
    }
}
```

Посмотрите на строчку `srv := httptest.NewServer(handler)`: мы запускаем тестовый сервер с хендлером в качестве обработчика запросов. Это настоящий HTTP-сервер, запрос к которому можно отправить с помощью любого HTTP-клиента, что мы и делаем в обновлённом тесте.

Вывод результатов теста никак не изменится — это говорит о том, что тесты продолжают выполнять свою задачу, как и раньше.

## Серверные библиотеки

Итак, ваши друзья хотят сделать интернет-магазин по продаже автомобилей. Машин у них немного. В приложение вам нужно добавить две функции:

- показать определённую машину;
- показать все автомобили на одной странице.


Решить эту задачу можно с помощью пакета `net/http` в одном файле:

```go
package main

import (
    "io"
    "net/http"
    "strings"
)

var cars = map[string]string{
    "id1": "Renault Logan",
    "id2": "Renault Duster",
    "id3": "BMW X6",
    "id4": "BMW M5",
    "id5": "VW Passat",
    "id6": "VW Jetta",
    "id7": "Audi A4",
    "id8": "Audi Q7",
}

// carsListFunc — вспомогательная функция для вывода всех машин.
func carsListFunc() []string {
    var list []string
    for _, c := range cars {
        list = append(list, c)
    }
    return list
}

// carFunc — вспомогательная функция для вывода определённой машины.
func carFunc(id string) string {
    if c, ok := cars[id]; ok {
        return c
    }
    return "unknown identifier " + id
}

func carsHandle(rw http.ResponseWriter, r *http.Request) {
    carsList := carsListFunc()
    io.WriteString(rw, strings.Join(carsList, ", "))
}

func carHandle(rw http.ResponseWriter, r *http.Request) {
    carID := r.URL.Query().Get("id")
    if carID == "" {
        http.Error(rw, "carID param is missed", http.StatusBadRequest)
        return
    }
    rw.Write([]byte(carFunc(carID)))
}

func main() {
    // определяем хендлер, который выводит все машины
    http.HandleFunc("/cars", carsHandle)
    // определяем хендлер, который выводит определённую машину
    http.HandleFunc("/car", carHandle)

    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

На первый взгляд, это элегантное решение, но в реальных проектах требуются и другие возможности:

- добавлять пагинацию (постраничный вывод), если будет больше 50 машин;
- использовать вместо запросов `/car?id=123` красивый URL `/car/lada-priora-black-2021`;
- поддерживать RESTful и разделять запросы `GET`, `POST`, `PUT`, `DELETE`;
- поддерживать логи для ошибок;
- предоставлять документацию по работе с API;
- разграничивать права доступа для пользователей: администратор, модератор, посетитель.

Кроме этого, в других проектах может понадобиться:

- поддержка статических файлов,
- поддержка `CORS`,
- поддержка `OPTIONS`,
- JWT,
- rate limiter,
- и многое другое.

Реально ли всё это сделать с помощью пакета `net/http`? Да. Но нужно ли изобретать велосипед и отлавливать ошибки?

В Go есть готовые роутеры и фреймворки для решения подобных задач. Вот некоторые из них:

На Awesome Go можно посмотреть другие [фреймворки](https://github.com/avelino/awesome-go#web-frameworks) и [роутеры](https://github.com/avelino/awesome-go#routers).

Выбор пакета зависит от конкретной задачи. Для разработки проекта «на коленке» подойдёт `buffalo`, для бэкенд-микросервиса — `gin` или `chi`, для решения проблем highload — `fasthttp` (хотя часто проблема RPS — в базах данных или алгоритмах).

Так как вы разрабатываете бэкенд-сервис, перепишем сервер для магазина автомобилей, используя роутер `chi` — чтобы разобраться с его базовыми возможностями.

## Роутер chi

Итак, встречайте — роутер `chi`:

- лёгкий, быстрый, надёжный;
- на 100% совместим с `net/http`;
- разработан для модульных и композитных API;
- автоматически генерирует документацию с помощью пакета `docgen`;
- обходится без внешних зависимостей.

```go
package main

import (
    "fmt"
    "io"
    "net/http"

    "github.com/go-chi/chi/v5"
)

func main() {
    r := chi.NewRouter()
    r.Get("/", func(rw http.ResponseWriter, r *http.Request) {
        rw.Write([]byte("chi"))
    })
    r.Get("/item/{id}", func(rw http.ResponseWriter, r *http.Request) {
        // получаем значение URL-параметра id
        id := chi.URLParam(r, "id")
        io.WriteString(rw, fmt.Sprintf("item = %s", id))
    })
    // r передаётся как http.Handler
    http.ListenAndServe(":8080", r)
}
```

Можно использовать в `chi` написанные ранее хендлеры — они будут полностью совместимы.

## Роутинг

В пакете `chi` есть дополнительные возможности для настройки маршрутизации запросов, то есть для роутинга.

В частности, можно объединять обработчики запросов в древовидную структуру методом `Route()`. Например, так:

```
r.Get("/cars", carsHandle) // GET /cars
r.Get("/cars/{brand}", brandHandle) // GET /cars/renault
r.Get("/cars/{brand}/{model}", modelHandle) // GET /cars/renault/duster

// то же самое можно описать, используя Route
r.Route("/cars", func(r chi.Router) {
    r.Get("/", carsHandle) // GET /cars
    // Route можно вкладывать один в другой
    r.Route("/{brand}", func(r chi.Router) {
        r.Get("/", brandHandle)     // GET /cars/renault
        r.Get("/{model}", modelHandle) // GET /cars/renault/duster
    })
})
```

Ещё `Route()` позволяет группировать разные HTTP-методы для одного и того же запроса:

```
r.Post("/car", newCar)           // POST /car
r.Get("/car/{id}", getCar)       // GET /car/1234
r.Put("/car/{id}", updateCar)    // PUT /car/1234
r.Delete("/car/{id}", deleteCar) // DELETE /car/1234

// то же самое, используя Router
r.Route("/car", func(r chi.Router) {
    r.Post("/", newCar)      // POST /car
    r.Route("/{id}", func(r chi.Router) {
        r.Get("/", getCar)       // GET /car/1234
        r.Put("/", updateCar)    // PUT /car/1234
        r.Delete("/", deleteCar) // DELETE /car/1234
    })
})
```

## Middleware

В уроке про HTTP-сервер вы познакомились с концепцией `middleware`. Напомним, что `middleware` — это функции-фильтры для обработки запросов. Они совершают дополнительные действия (аутентификация, логирование, сжатие и другие) и не мешают выполнению основного обработчика. Например, они помогают проверять авторизацию пользователя: если посетитель не авторизован, `middleware` перенаправляют его на страницу авторизации.

В пакете `chi` есть встроенные `middleware` — можно использовать их или написать свои.

Вот некоторые из встроенных `middleware`:

- `AllowContentType` — допускает запросы только c определёнными заголовками `Content-Type`.
- `BasicAuth` — реализует базовую (Basic) схему аутентификации.
- `Compress` — сжимает тело ответа в соответствии с заголовком запроса `Accept-Encoding`.
- `Logger` — отвечает за логирование запросов.
- `RealIP` — устанавливает `RemoteAddr` запроса в соответствии с заголовком `X-Forwarded-For` или `X-Real-IP`.
- `Recoverer` — восстанавливается после `panic`, регистрирует `panic` и обратную трассировку, возвращает статус `HTTP 500` (внутренняя ошибка сервера), если это возможно.

Подключить `middleware` можно функцией `Use(middlewares ...func(http.Handler) http.Handler)`. Если подключается несколько функций, то они будут выполняться в том же порядке, в каком были добавлены.

Посмотрите на пример использования:

```go
import (
    // ...

    "github.com/go-chi/chi/v5/middleware"
    "github.com/go-chi/chi/v5"
)

func main() {
    r := chi.NewRouter()

    r.Use(middleware.RealIP)
    r.Use(middleware.Logger)
    r.Use(middleware.Recoverer)
    // или
    // r.Use(middleware.RealIP, middleware.Logger, middleware.Recoverer)

    // ...
}
```

А вот так может выглядеть собственная `middleware`-функция, которая фиксирует время выполнения запросов:

```go
func TimerTrace(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        // перед началом выполнения функции сохраняем текущее время
        start := time.Now()
        // вызываем следующий обработчик
        next.ServeHTTP(w, r)
        // после завершения замеряем время выполнения запроса
        duration := time.Since(start)
        // сохраняем или сразу обрабатываем полученный результат
        // ...
    })
}
```

## Тестирование хендлеров с роутером chi

Теперь вернёмся к примеру с машинами и протестируем сервер, который использует роутер `chi`. Для простоты проверим только один обработчик на поиск машины по бренду и модели: `/cars/{brand}/{model}`.

```go
package main

import (
    "net/http"

    "github.com/go-chi/chi/v5"
)

var cars = map[string]string{
    "id1": "Renault Logan",
    "id2": "Renault Duster",
    "id3": "BMW X6",
    "id4": "BMW M5",
    "id5": "VW Passat",
    "id6": "VW Jetta",
    "id7": "Audi A4",
    "id8": "Audi Q7",
}

func modelHandle(rw http.ResponseWriter, r *http.Request) {
    car := strings.ToLower(chi.URLParam(r, "brand") + ` ` +
                           chi.URLParam(r, "model"))
    for _, c := range cars {
        if strings.ToLower(c) == car {
            io.WriteString(rw, c)
            return
        }
    }
    http.Error(rw, "unknown model: "+car, http.StatusNotFound)
}

func CarRouter() chi.Router {
    r := chi.NewRouter()

    r.Get("/cars/{brand}/{model}", modelHandle) // GET /cars/renault/duster
    return r
}

func main() {
    http.ListenAndServe(":8080", CarRouter())
}
```

Можно запустить эту программу и отправлять запросы через клиент, а можно воспользоваться функцией `httptest.NewServer` и передать ей `CarRouter`.

Также напишем общую функцию для отправки тестовых запросов — `testRequest`:

```go
// model_test.go
package main

import (
    "io"
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/require"
)

func testRequest(t *testing.T, ts *httptest.Server, method,
                    path string) (*http.Response, string) {
    req, err := http.NewRequest(method, ts.URL+path, nil)
    require.NoError(t, err)

    resp, err := ts.Client().Do(req)
    require.NoError(t, err)
    defer resp.Body.Close()

    respBody, err := io.ReadAll(resp.Body)
    require.NoError(t, err)

    return resp, string(respBody)
}

func TestRouter(t *testing.T) {
    ts := httptest.NewServer(CarRouter())
    defer ts.Close()
    // ниже добавим тестовые запросы
    // ...
}
```

Осталось добавить тестовую таблицу и сравнить полученный ответ с эталоном для каждого указанного в ней запроса.

```go
func TestRouter(t *testing.T) {
    ts := httptest.NewServer(CarRouter())
    defer ts.Close()

    var testTable = []struct {
        url    string
        want   string
        status int
    }{
        {"/cars/renault/Logan", "Renault Logan", http.StatusOK},
        {"/cars/audi/a4", "Audi A4", http.StatusOK},
        // проверим на ошибочный запрос
        {"/cars/audi/a6", "unknown model: audi a6\n", http.StatusNotFound},
        {"/cars/BMW/M5", "BMW M5", http.StatusOK},
        {"/cars/bmw/X6", "BMW X6", http.StatusOK},
        {"/cars/Vw/Passat", "VW Passat", http.StatusOK},
    }
    for _, v := range testTable {
        resp, get := testRequest(t, ts, "GET", v.url)
        assert.Equal(t, v.status, resp.StatusCode)
        assert.Equal(t, v.want, get)
    }
}
```

В этом уроке вы познакомились с клиентской библиотекой `resty` и научились применять её для отправки HTTP-запросов. Также вы разобрали примеры использования серверной библиотеки `chi`, которая расширяет возможности маршрутизации при разработке веб-сервера.

## Дополнительные материалы

- [go.dev | resty](https://pkg.go.dev/github.com/go-resty/resty/v2) — документация пакета `resty`.
- [go.dev | chi](https://pkg.go.dev/github.com/go-chi/chi/v5) — документация роутера `chi`.
- [go.dev | middleware](https://pkg.go.dev/github.com/go-chi/chi/middleware) — список доступных `middleware` для роутера `chi`.
- [GitHub | HTTP clients](https://github.com/avelino/awesome-go#http-clients) — список клиентских пакетов на Awesome Go.
- [GitHub | Routers](https://github.com/avelino/awesome-go#routers) — список серверных пакетов на Awesome Go.
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — бесплатный тестовый API.