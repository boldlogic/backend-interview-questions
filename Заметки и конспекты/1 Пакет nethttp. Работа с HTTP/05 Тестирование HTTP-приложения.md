---
title: "Тестирование HTTP-приложения"
source: yandex-practicum
course: go-developer
converted: 2026-05-28
part: 1
---

# Тестирование HTTP-приложения

- Если ваш проект покрыт тестами, вам реже нужно пользоваться отладчиком — просто добавьте ещё один тест-кейс, и баг проявится сам.
- Благодаря тестам код становится более живучим и устойчивым к сбоям, так как проходит дополнительные проверки.
- Тесты позволяют убедиться, что вы ничего не сломали своими изменениями.
- Тесты — это ещё и отличная документация, которая не устаревает.
- Работать с любым проектом проще и приятнее, когда в нём есть тесты: всегда понятно, в каком он состоянии.

Написание тестов — такой же непрерывный процесс, как и добавление к программе новой функциональности. По мере того как растёт объём кода, должно увеличиваться и количество тестов. Новые тесты проверяют работу новых функций, а старые — контролируют, что уже существующий код по-прежнему работает корректно.

Сначала поговорим о том, как тесты устроены в Go. Расскажем о методах пакета `testing`, возможноcтях команды `go test` и сторонней библиотеки `testify`. Затем покажем, как протестировать HTTP-сервер и проверить работу хендлеров с помощью пакета `httptest`.

## Тесты

Для запуска тестов используется команда `go test`. Она ищет файлы, название которых заканчивается на `_test.go`, и запускает в них функции вида:

```go
func TestXxx(t *testing.T)
```

Префикс `Test` обязателен — после него, как правило, следует имя тестируемой функции.

Рекомендуется размещать файлы `*_test.go` в одной директории с тестируемым пакетом. Тестовые файлы не влияют на сам пакет, так как игнорируются при сборке программы.

Тип `*testing.T` предоставляет доступ к нескольким базовым методам:

- `Errorf(...)` — записывает сообщение в `error`-лог и помечает тест как непройденный. Исполнение теста продолжается.
- `Fatalf(...)` — делает то же самое. Но исполнение теста немедленно завершается. Этот метод часто используется в рабочих проектах при обработке ошибок.
- `Skipf(...)` — пропускает тест и выводит сообщение. Используется, когда окружение для теста не задано. Типичный сценарий — пропускать интеграционные тесты при локальном запуске, когда нет доступа к внешним сервисам.
- `Logf(...)` — позволяет выводить лог-сообщения внутри теста. Преимущество перед методами пакета `fmt` в том, что из лога сразу видно, к какому тесту относится сообщение.

Всё это реализовано в пакете `testing` стандартной библиотеки.

Для примера напишем тест для функции, которая считает сумму переданных ей целых чисел.

В некоторых примерах есть опечатки и неточности. Это сделано намеренно: будем искать ошибки в коде с помощью тестов 😉

```go
// sum.go
package sum

// Sum возвращает сумму элементов.
func Sum(values ...int) int {
    var sum int
    for _, v := range values {
        sum += v
    }
    return sum
}
```

```go
// sum_test.go
package sum

import "testing"

func TestSum(t *testing.T) {
    if sum := Sum(1, 2); sum != 3 {
        t.Errorf("sum expected to be 3; got %d", sum)
    }
}
```

В этом тесте проверяется сумма двух конкретных чисел, но хотелось бы проверить множество разных вариантов, в том числе пограничные случаи. Например, что будет, если передать функции только одно число? А если передать отрицательные числа?

Для этого удобно использовать **таблицу тестов**. Это слайс, элементы которого содержат входящие параметры и соответствующий ожидаемый результат. Тестовая функция по очереди выполняет один и тот же код для каждого элемента и сравнивает полученное значение с эталонным результатом.

Переделаем файл `sum_test.go` таким образом:

```go
// sum_test.go
package sum

import "testing"

func TestSum(t *testing.T) {
    tests := []struct { // добавляем слайс тестов
        name   string
        values []int
        want   int
    }{
        {
            name:   "simple test #1", // описываем каждый тест:
            values: []int{1, 2},      // значения, которые будет принимать функция,
            want:   3,                // и ожидаемый результат
        },
        {
            name:   "one",
            values: []int{1},
            want:   1,
        },
        {
            name:   "with negative values",
            values: []int{-1, -2, 3},
            want:   0,
        },
        {
            name:   "with negative zero",
            values: []int{-0, 3},
            want:   3,
        },
        {
            name:   "a lot of values",
            values: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                          14, 15, 16, 17, 18, 18},
            want:   189,
        },
    }
    for _, test := range tests { // цикл по всем тестам
        t.Run(test.name, func(t *testing.T) {
            if sum := Sum(test.values...); sum != test.want {
                t.Errorf("Sum() = %d, want %d", sum, test.want)
            }
        })
    }
}
```

Метод `t.Run(name string, f func(t *testing.T)) bool` используется для запуска вложенных тестов (подтестов). Первым аргументом передаётся имя подтеста, а вторым — функция, которая будет запущена в отдельной горутине. По умолчанию `t.Run()` ожидает завершения работы функции. Если тест обнаружит ошибку, это будет выглядеть примерно так:

```
--- FAIL: TestSum (0.00s)
    --- FAIL: TestSum/a_lot_of_values (0.00s)
        sum_test.go:41: Sum() = 189, want 190
```

В первую очередь `t.Run()` нужен для создания подтестов, которые можно запускать отдельно. Но использовать его необязательно — если убрать `t.Run()`, функциональность теста не изменится:

```go
for _, test := range tests {
    if sum := Sum(test.values...); sum != test.want {
        t.Errorf("%s: Sum() = %d, want %d", test.name, sum, test.want)
    }
}
```

Таблица тестов позволяет проверять работу функции за счёт подстановки различных параметров и при необходимости добавлять новые проверки.

## Команда go test

Написали тест — теперь нужно его запустить. Для этого достаточно сохранить его в файл `sum_test.go` и выполнить `go test` в той же директории. Когда требуется запустить только определённые тесты или проверить сразу несколько пакетов, нужно передать команде `go test` дополнительные параметры.

Итого есть два режима запуска тестов:

- `go test` запускает все тесты в текущей директории;
- `go test [package list]` запускает тесты в нескольких указанных пакетах.

Чтобы запустить тесты в нескольких пакетах, команде `go test` надо передать пути импорта этих пакетов, разделённые пробелами. Например, `go test . github.com/username/packagename github.com/username/packagename2` запустит тесты в текущей директории и ещё двух пакетах, а `go test ./...` выполнит тесты во всех пакетах всех поддиректорий.

На первый взгляд, команды `go test` и `go test .` очень похожи, но между ними есть одно принципиальное различие. Если вы запустите `go test .` два раза подряд, то получите такой вывод:

```go
$ go test .
ok      sum     0.002s
$ go test .
ok      sum     (cached)
```

Дело в том, что в режиме тестирования пакетов `go test [package list]` кеширует результат прогона тестов и, если код и тесты не были изменены, второй раз показывает закешированный результат.

Избежать использования кеша можно двумя способами:

- При запуске `go test` указать флаг `-count` cо значением `1`. Флаг `-count` определяет, сколько раз нужно запустить каждый тест (по умолчанию — один), соответственно, `-count 1` не меняет количество запусков (если сравнивать со значением по умолчанию), но выключает кеширование.
- Перед началом теста запустить команду `go clean -testcache`. Она очистит кеш.

По умолчанию команда `go test` запускает все тесты пакета. При желании можно запускать их выборочно, используя параметр `-run` с регулярным выражением. Тогда будут выполняться только те тесты, имя которых удовлетворяет регулярному выражению. Например:

- `go test -run Sum` — запустит все тесты, в имени которых есть `Sum`: `TestSum`, `TestSumFloat` и другие.
- `go test -run Sum$` — запустит все тесты, имя которых заканчивается на `Sum`.
- `go test -run ^TestSum$` — запустит только тест с именем `TestSum`.

С помощью `-run` можно даже управлять запуском подтестов `t.Run`. Для этого нужно после имени теста через слеш указать регулярное выражение для подтестов:

- `go test -v -run "Sum/^with negative values$"` — запустит только подтест с именем `with negative values`.
- `go test -v -run "Sum/negative"` — запустит только подтесты с `negative` в имени.

Параметр `-v` выводит в консоль cписок запущенных тестов и время выполнения каждого из них. Так можно проверить, какие именно тесты и подтесты были запущены:

```go
// пример вывода go test .
ok      sum     0.002s

// пример вывода go test -v .
=== RUN   TestSum
--- PASS: TestSum (0.00s)
PASS
ok      sum     0.002s
```

## Библиотека testify

Тесты могут включать в себя множество проверок, в том числе сравнение JSON-объектов и массивов. И каждая проверка требует времени на написание соответствующего кода. Упростить разработку тестов помогает сторонняя библиотека `testify`, которая часто используется для тестирования Go-пакетов.

Установить библиотеку можно командой `go get github.com/stretchr/testify`.

Вот какие пакеты из этой библиотеки могут вам пригодиться:

- `assert` — содержит функции, которые проверяют выполнение условий, сравнивают числа, строки и более сложные объекты (JSON, YAML). Эти функции возвращают значение типа `bool`. Если проверяемое условие не выполнено, тест выдаёт ошибку, но продолжает свою работу.
- `require` — содержит тот же набор функций, но они не возвращают значения. Если проверка не пройдена, работа теста прекращается.

Функции пакета `assert` выполняют следующие действия:

- проверяют на `true` или `false`;
- сравнивают два значения;
- проверяют возвращаемые ошибки: на наличие, отсутствие или наследование от заранее известной ошибки;
- проверяют одно значение: на `nil`, ноль и так далее.

Посмотрите на примеры функций:

```
// проверяет, что myCompare() возвращает true
assert.True(t, myCompare())

// сравнивает числа, строки
assert.Equal(t, Mul(2, 3), 6)

// сравнивает два JSON-объекта
// обратите внимание, что ключи в JSON расположены в разном порядке
assert.JSONEq(t, `{"name": "Alice", "role": "Admin"}`,
                 `{"role": "Admin", "name": "Alice"}`)

// проверяет, что объект не nil, "", false, 0 и что длина слайса не равна 0
assert.NotEmpty(t, GetList())

// сравнивает элементы в двух массивах, если неважен их порядок
assert.ElementsMatch(t, []int{1, 2, 3, 4}, []int{2, 3, 4, 1})

// проверяет, что err равна nil
assert.NoError(t, err)
```

В случае ошибки будет отображаться информация о тесте, причина ошибки, а также ожидаемое и полученное значение. Поэтому необязательно добавлять для каждой проверки дополнительный параметр — строковое сообщение.

Если всё-таки нужно выводить дополнительную информацию об ошибке, можно указать строку форматирования и подставляемые значения, как в `fmt.Printf()`:

```
assert.Equal(t, Mul(2, 3), 6, "Почему-то %d x %d != %d", 2, 3, 6)

assert.False(t, MyFunc(50), "MyFunc(50) должна возвращать false")
```

Напомним код для тестирования функции `Sum()`, которая рассматривалась в начале урока:

```go
for _, test := range tests { // цикл по всем тестам
    t.Run(test.name, func(t *testing.T) {
        if sum := Sum(test.values...); sum != test.want {
            t.Errorf("Sum() = %d, want %d", sum, test.want)
        }
    })
}
```

Используя пакет `assert`, код можно переписать так:

```go
for _, test := range tests {
    t.Run(test.name, func(t *testing.T) {
        assert.Equal(t, Sum(test.values...), test.want)
    })
}
```

Начинающие Go-разработчики используют для сравнения результатов только функцию `Equal()`. Но не забывайте, что кроме неё в библиотеке `testify` есть множество других функций для сравнения значений различных типов данных: ошибок, JSON-объектов, слайсов и так далее.

Вот пример более сложной проверки:

```
    if assert.NotNil(t, object) {
        // удостовериться, что объект существует,
        // и затем безопасно проверять значения в нём
        assert.Equal(t, "Something", object.Value)
    }
```

Если в случае ошибки нужно прекратить выполнение теста, то лучше использовать аналогичные функции из пакета `require`.

Например, если использовать `assert`, то тест ниже сообщит о двух ошибках:

```go
func TestSum(t *testing.T) {
    assert.Equal(t, 7, Sum(3, 4, 1))
    assert.Equal(t, 7, Sum(1, 2, 3, 4))
}
```

```
--- FAIL: TestSum (0.00s)
    sum_test.go:19:
                Error Trace:    /.../sum_test.go:19
                Error:          Not equal:
                                expected: 7
                                actual  : 8
                Test:           TestSum
    sum_test.go:20:
                Error Trace:    /.../sum_test.go:20
                Error:          Not equal:
                                expected: 7
                                actual  : 10
                Test:           TestSum
FAIL
FAIL    sum     0.004s
FAIL
```

При замене `assert` на `require` выполнение теста остановится после первой ошибки:

```go
func TestSum(t *testing.T) {
    require.Equal(t, 7, Sum(3, 4, 1))
    require.Equal(t, 7, Sum(1, 2, 3, 4))
}
```

```
--- FAIL: TestSum (0.00s)
    sum_test.go:19:
                Error Trace:    /.../sum_test.go:19
                Error:          Not equal:
                                expected: 7
                                actual  : 8
                Test:           TestSum
FAIL
FAIL    sum     0.003s
FAIL
```

![[attachments/img-001.gif]]


## Тестирование HTTP-сервера

В стандартной библиотеке Go для тестирования сервера и клиента есть пакет `net/http/httptest`. Покажем, как с помощью этого пакета организовать проверку обработчика запросов.

Допустим, есть сервер с простым хендлером, который при обращении к нему выводит `{"status":"ok"}`.

```go
// handler.go
package main

import "net/http"

func StatusHandler(rw http.ResponseWriter, r *http.Request) {
    rw.Header().Set("Content-Type", "application/json")
    rw.WriteHeader(http.StatusOK)
    // намеренно добавлена ошибка в JSON
    rw.Write([]byte(`{"status":"ok}`))
}
```

```go
// main.go
package main

import (
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/status", StatusHandler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Создаём файл `handler_test.go` с тестовой функцией `TestStatusHandler`. Лучше сразу использовать таблицу тестов, поэтому определяем массив структур, который содержит:

- название теста,
- желаемый ответ: код статуса,тело ответа,заголовок `Content-Type`.

Эталонный ответ описываем в отдельной структуре `want`.

```go
package main

import "testing"

func TestStatusHandler(t *testing.T) {
    type want struct {
        code        int
        response    string
        contentType string
    }
    tests := []struct {
        name string
        want want
    }{
        {
            name: "positive test #1",
            want: want{
                code:        200,
                response:    `{"status":"ok"}`,
                contentType: "application/json",
            },

        },
    }
    for _, test := range tests {
        t.Run(test.name, func(t *testing.T) {
            // здесь будет запрос и проверка ответа
        })
    }
}
```

Чтобы каждый раз не писать тест с нуля, вы можете генерировать шаблон. Например, в GoLand или Visual Studio Code можно кликнуть правой кнопкой мыши и выбрать “Go: Generate Unit Tests For Function”.

Особенность пакета `httptest` заключается в том, что он проверяет работу отдельных обработчиков — без запуска самого сервера.

Общая схема тестирования обработчика выглядит так:

1. Создать запрос для обработчика функцией `httptest.NewRequest(method, target string, body io.Reader) *http.Request`.
2. Вызвать функцию `NewRecorder() *ResponseRecorder`, которая возвращает переменную типа `*httptest.ResponseRecorder`. Она будет использоваться для получения ответа. Тип `ResponseRecorder` реализует интерфейс `http.ResponseWriter`.
3. Вызвать проверяемый обработчик, которому передаются запрос и переменная для получения ответа.
4. Вызвать метод `(rw *ResponseRecorder) Result() *http.Response`, чтобы получить ответ типа `*http.Response`.
5. Проверить параметры ответа с ожидаемыми значениями.

Реализуем эти шаги в примере теста:

```go
package main

import (
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/require"
    "io"
    "net/http"
    "net/http/httptest"
    "testing"
)

func TestStatusHandler(t *testing.T) {
    type want struct {
        code        int
        response    string
        contentType string
    }
    tests := []struct {
        name string
        want want
    }{
        {
            name: "positive test #1",
            want: want{
                code:        200,
                response:    `{"status":"ok"}`,
                contentType: "application/json",
            },
        },
    }
    for _, test := range tests {
        t.Run(test.name, func(t *testing.T) {
            request := httptest.NewRequest(http.MethodGet, "/status", nil)
            // создаём новый Recorder
            w := httptest.NewRecorder()
            StatusHandler(w, request)

            res := w.Result()
            // проверяем код ответа
            assert.Equal(t, res.StatusCode, test.want.code)
            // получаем и проверяем тело запроса
            defer res.Body.Close()
            resBody, err := io.ReadAll(res.Body)

            require.NoError(t, err)
            assert.JSONEq(t, string(resBody), test.want.response)
            assert.Equal(t, res.Header.Get("Content-Type"), test.want.contentType)
        })
    }
}
```

Обратите внимание на метод `httptest.NewRequest`. В тестах он используется вместо `http.NewRequest`. Отличие в том, что метод из пакета `httptest` в случае ошибки вызывает функцию `panic()`.

Запускаем тест в консоли командой `go test -v` и получаем ответ:

```
--- FAIL: TestStatusHandler (0.00s)
    --- FAIL: TestStatusHandler/positive_test_#1 (0.00s)
        handler_test.go:46:
            Error Trace:    /home/.../handler_test.go:46
            Error:          Expected value ('{"status":"ok}') is not valid json.
                            JSON parsing error: 'unexpected end of JSON input'
            Test:           TestStatusHandler/positive_test_#1
```

Ура, вот и ошибка! В JSON не хватает кавычек `"` после `ok`.

Исправляем и запускаем тест второй раз:

```go
$ go test -v
=== RUN   TestStatusHandler
=== RUN   TestStatusHandler/positive_test_#1
--- PASS: TestStatusHandler (0.00s)
    --- PASS: TestStatusHandler/positive_test_#1 (0.00s)
PASS
ok      handlers        0.004s
```

Таким образом, используя пакет `httptest`, мы нашли и исправили ошибку в обработчике запросов простейшего сервера. Плюс такого подхода в том, что можно без запуска сервера проверить работу отдельных обработчиков. Но в этом и минус: мы не можем проверить реальную работу сервера. Чтобы протестировать сервер в рабочих условиях, нужно отправлять запросы с использованием HTTP-клиента и обрабатывать полученные ответы.

## Обучаем Алису

В этом уроке вы узнали, как устроены тесты в Go. Теперь расскажем, как внедрять их в реальный проект, — на примере навыка для Алисы.

Создадим файл `cmd/skill/main_test.go`, в котором будут лежать тесты для хендлера. Должна получиться такая структура проекта:

```
 > ~/dev/alice-skill
      |
      |--- cmd
      |     |--- skill
      |            |--- main.go
      |            |--- main_test.go
      |--- internal
      |--- go.mod
```

В файл `main_test.go` поместим следующий код:

```go
package main

import (
    "net/http"
    "net/http/httptest"
    "testing"

    "github.com/stretchr/testify/assert"
)

func TestWebhook(t *testing.T) {
    // описываем ожидаемое тело ответа при успешном запросе
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
            r := httptest.NewRequest(tc.method, "/", nil)
            w := httptest.NewRecorder()

            // вызовем хендлер как обычную функцию, без запуска самого сервера
            webhook(w, r)

            assert.Equal(t, tc.expectedCode, w.Code, "Код ответа не совпадает с ожидаемым")
            // проверим корректность полученного тела ответа, если мы его ожидаем
            if tc.expectedBody != "" {
                // assert.JSONEq помогает сравнить две JSON-строки
                assert.JSONEq(t, tc.expectedBody, w.Body.String(), "Тело ответа не совпадает с ожидаемым")
            }
        })
    }
}
```

Поскольку для тестов используется сторонняя библиотека `testify`, нужно обновить список внешних зависимостей проекта. Для этого выполним команду `$ go mod tidy`. Она сама найдёт в коде новые зависимости, определит их подходящие версии и запишет необходимые метаданные в файлы `go.mod` и `go.sum`.

Теперь начнём тестирование. Чтобы запустить все доступные тесты, выполним из корня проекта команду `$ go test -v ./...`.

В консоли получим такой результат:

```
=== RUN   Test_webhook
--- PASS: Test_webhook (0.00s)
=== RUN   Test_webhook/GET
    --- PASS: Test_webhook/GET (0.00s)
=== RUN   Test_webhook/PUT
    --- PASS: Test_webhook/PUT (0.00s)
=== RUN   Test_webhook/DELETE
    --- PASS: Test_webhook/DELETE (0.00s)
=== RUN   Test_webhook/POST
    --- PASS: Test_webhook/POST (0.00s)

PASS

Process finished with the exit code 0
```

Слово `PASS` в конце вывода означает, что все тесты завершились успешно. То есть код работает ровно так, как и задумано.

## Дополнительные материалы

- [go.dev/testing](https://pkg.go.dev/testing) — документация пакета `testing`.
- [go.dev/net/http/httptest](https://pkg.go.dev/net/http/httptest) — документация пакета `httptest`.
- [go.dev | Testing flags](https://pkg.go.dev/cmd/go#hdr-Testing_flags) — о команде `go test` и флагах.
- [GitHub | Testify — Thou Shalt Write Tests](https://github.com/stretchr/testify) — библиотека `testify`.
- [Ilija Eftimov | Testing in Go: go test](https://ieftimov.com/posts/testing-in-go-go-test/) — о тестировании в Go.
- [YouTube | Unit testing HTTP servers](https://www.youtube.com/watch?v=hVFEV-ieeew) — выпуск “justforfunc: Programming in Go” о тестировании сервера.