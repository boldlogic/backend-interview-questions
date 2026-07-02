---
title: "Использование HTTP-клиента"
source: yandex-practicum
course: go-developer
converted: 2026-05-28
part: 1
---

# Использование HTTP-клиента

HTTP-клиенты используются для парсинга данных, работы со сторонним API, тестирования HTTP-серверов, микросервисной архитектуры и так далее.

Самый простой способ сделать HTTP-запрос средствами стандартной библиотеки Go выглядит так:

```go
response, err := http.Get("http://example.com/index.html")
if err != nil {
    fmt.Println(err)
}
```

Функция `http.Get(url string)` возвращает указатель на структуру `http.Response` (ответ сервера) и `error` (ошибку, если что-то пошло не так). В URL-параметре указывают HTTP- или HTTPS-протокол.

## Ответ сервера

Структура типа `http.Response` содержит заголовки ответа, тело и дополнительную информацию. В уроке «Создание HTTP-сервера» вы научились устанавливать кода статуса и заголовки ответа. Эти данные хранятся в полях `StatusCode` и `Header` соответственно.

Для примера посмотрим, что возвращает запрос `practicum.yandex.ru`:

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    response, err := http.Get("https://practicum.yandex.ru")
    if err != nil {
        fmt.Println(err)
    }
    fmt.Printf("Status Code: %d\r\n", response.StatusCode)
    for k, v := range response.Header {
      // заголовок может иметь несколько значений,
      // но для простоты запросим только первое
        fmt.Printf("%s: %v\r\n", k, v[0])
    }
}
```

Программа выведет примерно следующее:

```
Status Code: 200
X-Request-Id: 1663854943634850-3617306141716402244
Date: Thu, 22 Sep 2022 13:55:45 GMT
Set-Cookie: _yasc=6xwp8F8yEKot/1Zso72AZeQrdloTNG4Cl/s+EnMNncw3og==; domain=.yandex.ru; path=/; expires=Sat, 22-Oct-2022 13:55:43 GMT; secure
Vary: Accept-Encoding
Etag: W/"742df-+H+2A9iCP7aCMRNI7y9HsHaKzfI"
Keep-Alive: timeout=5
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Powered-By: Express
Content-Security-Policy:
Content-Type: text/html; charset=utf-8
Report-To: {"group":"default-group","endpoints":[{"url":"https://csp.yandex.net/csp?from=wirth&project=practicum"}],"max_age":1800,"include_subdomains":true}
```

Здесь есть по крайней мере один знакомый вам по предыдущим урокам заголовок — `Content-Type: text/html; charset=utf-8`.

Как правило, нет необходимости обрабатывать все заголовки ответа. Значения конкретного заголовка можно узнать методом `(h Header) Values(key string) []string`, а самое первое значение — методом `(h Header) Get(key string) string`.

```go
contentType := response.Header.Get("Content-Type")
// это может быть, например, "application/json; charset=UTF-8"
```

Тело ответа представлено в поле `Response.Body` интерфейсом потокового чтения `io.ReadCloser`, который содержит два метода: `Read(p []byte) (n int, err error)` (интерфейс Reader) и `Close() error` (интерфейс Closer). Если клиент успешно получил ответ, то нужно закрыть `Body` независимо от того, прочитаете вы его или нет.

Получить тело ответа в виде `[]byte` можно функцией `io.ReadAll(r Reader) ([]byte, error)`:

```go
response, err := http.Get("http://example.com")
if err != nil {
    fmt.Println(err)
    return
}
body, err := io.ReadAll(response.Body)
response.Body.Close()
if err != nil {
    fmt.Println(err)
    return
}
```

Содержимое ответа должно соответствовать значению заголовка `Content-Type`. Если, например, `Content-Type` равен `text/html; charset=utf-8`, это значит, что тело ответа содержит текст в формате HTML и кодировке UTF-8.

Если нужно отправить запрос методом `POST`, можно использовать функцию `Post(url, contentType string, body io.Reader) (resp *Response, err error)`.

```go
data := `{"name": "Иванов Иван", "email": "ivan@example.com"}`
resp, err := http.Post("https://example.com/adduser", "application/json", strings.NewReader(data))
if err != nil {
    return err
}
```

## Клиент

За отправку запросов отвечают методы типа `http.Client`, а функции `http.Get()` и `http.Post()` — обёртки над вызовом этих методов у глобальной переменной `http.DefaultClient`.

Вот как с помощью `http.Client` можно обратиться к серверу и получить `http.Response`:

```go
client := &http.Client{}
response, err := client.Get("https://golang.org")
```

При использовании собственного клиента можно указать специфические настройки, что позволяет отправлять запросы с разными настройками единовременно.

Рассмотрим поля для настройки клиента.

`Timeout time.Duration` — максимальная задержка ответа, после которой клиент отменяет запрос. Если это поле имеет нулевое значение, то лимит на ожидание не установлен.

```go
client := http.Client{
   Timeout: time.Second * 1, // интервал ожидания: 1 секунда
}
```

Часто в ответе на запрос сервер возвращает перенаправление на другой адрес, и таких перенаправлений может быть несколько. Например, `http://example.com` → `https://example.com` → `https://www.example.com`. По умолчанию клиент переходит только по 10 адресам. Поле `CheckRedirect func(req *Request, via []*Request) error` позволяет контролировать редиректы.

```go
    client := &http.Client{
        CheckRedirect: func(req *http.Request, via []*http.Request) error {
            fmt.Println(req.URL)
            return nil
        },
    }
    response, err := client.Get("http://ya.ru")
```

Например, для сайта `http://ya.ru` программа может вывести:

```
https://ya.ru/
https://ya.ru/?nr=1
```

Или запросить капчу: `https://ya.ru/showcaptcha?cc=1&...`.

За отправку запроса и получение ответа по сети отвечает интерфейс `RoundTripper`. Стандартная библиотека предоставляет реализацию этого интерфейса структурой `http.Transport`, где можно указать тайм-ауты соединения и другие низкоуровневые настройки.

По умолчанию используется глобальная переменная `http.DefaultTransport`. При необходимости можно задать свой вариант реализации через поле `http.Client.Transport`.

Структура `http.Transport` позволяет переиспользовать уже открытые TCP-подключения (их называют HTTP keep-alive), поэтому `http.Client` обычно применяют повторно, а не создают заново для каждого запроса. К тому же один экземпляр клиента можно параллельно использовать из разных горутин.

Чтобы TCP-соединение использовалось повторно, клиент должен обязательно прочитать тело ответа до конца и закрыть `response.Body`, даже если оно не нужно.

```go
// io.Discard выступает в качестве приёмника ненужных данных
_, err := io.Copy(io.Discard, response.Body)
response.Body.Close()
if err != nil {
    fmt.Println(err)
}
```

## Запрос

Если для отправки запроса недостаточно методов `client.Get()` или `client.Post()`, то можно сформировать нужный запрос `*http.Request` и отправить его с помощью метода `(c *Client) Do(req *Request) (*Response, error)`.

Для создания запроса используется функция `NewRequest(method, url string, body io.Reader) (*Request, error)`, где `method` — имя метода запроса, `url` — адрес. Третьим параметром указывается переменная интерфейсного типа `io.Reader`, из которой будет прочитано тело запроса. Если тело запроса отправлять не нужно (например, для метода `GET`), можно указывать значение `nil`.

Вот как может выглядеть запрос к локальному HTTP-серверу с использованием `client.Do()`:

```go
request, err := http.NewRequest(http.MethodGet, "http://localhost:8080", nil)
if err != nil {
   panic(err)
}
response, err := client.Do(request)
if err != nil {
    panic(err)
}
io.Copy(os.Stdout, response.Body) // вывод ответа в консоль
response.Body.Close()
```

В созданном `*http.Request` можно установить значения заголовков через поле `Header` типа `http.Header`. Чтобы задать содержимое заголовка, используют один из двух методов:

- `(h Header) Set(key, value string)` — установить значение заголовка;
- `(h Header) Add(key, value string)` — добавить значение заголовка к уже существующим.

В примере ниже запрос будет иметь заголовок `MyHeader` c двумя значениями — `Hello` и `Привет`.

```go
req, err := http.NewRequest(http.MethodGet, `http://localhost:8080`, nil)
if err != nil {
   panic(err)
}
req.Header.Set(`MyHeader`, "Hello")
req.Header.Add(`MyHeader`, "Привет")
response, err := client.Do(req)
```

Рассмотрим три примера `POST`-запроса с часто встречающимися заголовками `"Content-Type"`.

1. `"application/json"`

Данные передаются в формате JSON. В качестве `io.Reader` используется `bytes.Buffer`, а `"Content-Type"` равен `"application/json"`. Чаще всего этот подход можно встретить в современных REST API, где запросы и ответы передаются в JSON-формате.

```go
var body = []byte(`{"message":"Hello"}`)
request, err := http.NewRequest(http.MethodPost, url, bytes.NewBuffer(body))
if err != nil {
    // обрабатываем ошибку
}
request.Header.Set("Content-Type", "application/json; charset=UTF-8")
response, err := client.Do(request)
```

1. `"multipart/form-data"`

Этот формат используется браузерами для отправки файлов.

```go
file, _ := os.Open(filename) // открываем файл
defer file.Close() // не забываем закрыть
body := &bytes.Buffer{} // создаём буфер
// на основе буфера конструируем multipart.Writer из пакета mime/multipart
writer := multipart.NewWriter(body)
// готовим форму для отправки файла на сервер
part, err := writer.CreateFormFile("uploadfile", filename)
if err != nil {
    // обрабатываем ошибку
}
// копируем файл в форму
// multipart.Writer отформатирует данные и запишет в предоставленный буфер
_, err = io.Copy(part, file)
if err != nil {
    // обрабатываем ошибку
}
writer.Close()

// пишем запрос
request, err := http.NewRequest(http.MethodPost, url, body)
if err != nil {
    // обрабатываем ошибку
}
// добавляем заголовок запроса
request.Header.Set("Content-Type", writer.FormDataContentType())
response, err := client.Do(request)
```

1. `"application/x-www-form-urlencoded"`

Это простой способ добавить к запросу параметры в формате `ключ=значение`. Данные кодируются в виде строки `key1=value1&key2=value2`. При `GET`-запросе параметры указываются после адреса: `example.com/endpoint?key1=value1&key2=value2`. Этот формат кодировки по умолчанию используется в браузерах.

```go
// готовим контейнер для данных
// используем тип url.Values из пакета net/url
data := url.Values{}
// устанавливаем данные
data.Set("key1", "value1")
data.Set("key2", "value2")
// пишем запрос
request, err := http.NewRequest(http.MethodPost, url, strings.NewReader(data.Encode()))
if err != nil {
    // обрабатываем ошибку
}
// устанавливаем заголовки
request.Header.Set("Content-Type", "application/x-www-form-urlencoded")
request.Header.Set("Content-Length", strconv.Itoa(len(data.Encode())))
response, err := client.Do(request)
```

## Куки

**Куки (cookies)** — это способ хранения информации на стороне клиента. Это может быть информация о действиях пользователя, регистрационные данные, токены и так далее. Управлять куками можно как на стороне клиента, так и на стороне сервера. Кука привязывается к домену, и дальше в заголовок любого запроса добавляются куки, сохранённые для этого домена.

В стандартной библиотеке Go с куками можно работать через структуру `http.Cookie`. Вот её обязательные поля:

- `Name string` — имя куки.
- `Value string` — значение куки.

А вот опциональные:

- `Path string` — путь URL, начиная с которого распространяется действие куки.
- `Domain string` — хост. Если он не задан, то берётся доменная часть адреса.
- `Expires time.Time` — дата и время, когда истекает срок действия куки. После этого кука удаляется.
- `MaxAge int` — время жизни куки в секундах. Если значение равно 0, то атрибут не указан. Это альтернатива полю `Expires`.
- `Secure bool` — если `true`, то кука будет доступна только по протоколу HTTPS.
- `HttpOnly bool` — если `true`, то кука будет недоступна для чтения из JavaScript, при этом браузер всё равно будет отправлять её на сервер.

На стороне сервера можно получить и установить куки, используя следующие методы и функции:

- `(r *Request) Cookie(name string) (*Cookie, error)` — получить структуру куки с указанным именем.
- `(r *Request) Cookies() []*Cookie` — получить список всех кук.
- `http.SetCookie(w ResponseWriter, cookie *Cookie)` — установить куку в ответ сервера.

Для клиента есть такие методы:

- `(r *Request) AddCookie(c *Cookie)` — добавить в запрос нужные куки.
- `(r *Response) Cookies() []*Cookie` — получить куки из ответа сервера.

```go
client := &http.Client{}
req, err := http.NewRequest(http.MethodGet, `http://localhost:8080`, nil)
if err != nil {
    panic(err)
}
req.AddCookie(&http.Cookie{
   Name: "ID",
   Value: "3675",
})
req.AddCookie(&http.Cookie{
   Name: "Token",
   Value: "TEST_TOKEN",
   MaxAge: 360,
})
response, err := client.Do(req)
```

Можно самостоятельно указывать куки и обновлять их в соответствии с ответами сервера, но лучше использовать пакет `net/http/cookiejar`. Он позволяет автоматически обновлять куки, полученные от сервера, и отправлять их при каждом запросе.

Для этого нужно определить поле `Jar` в переменной типа `http.Client`:

```go
jar, err := cookiejar.New(nil)
if err != nil {
   panic(err)
}
client := &http.Client{
   Jar: jar,
}

req, err := http.NewRequest(http.MethodGet, `http://localhost:8080`, nil)
if err != nil {
    panic(err)
}
cookie := &http.Cookie{
    Name:   "Token",
    Value:  "TEST_TOKEN",
    MaxAge: 300,
}
req.AddCookie(cookie)
response, err := client.Do(req)
```

При использовании `Jar` клиент после запроса запомнит куки, полученные от сервера, и добавит их в следующий запрос к этому доменному имени.

## Применение

На практике HTTP-клиент — это больше, чем просто имитация браузера или cURL. Клиент используют в сложных информационных системах, так как он может обращаться к сторонним сервисам, разнообразным специализированным Web API или вашим собственным микросервисам.

Напишем пример кода — консольный клиент, способный прочитать в stdin очень длинный URL, отправить его методом `POST` «Сервису сокращения URL» и получить ответ — короткий псевдоним.

Если вы выбрали трек «Сервис сокращения URL», вы можете сохранить код в файле `main.go` поддиректории `cmd/client` вашего проекта. Тогда у вас всегда будет под рукой программа для проверки сервиса.

```go
package main

import (
    "bufio"
    "fmt"
    "io"
    "net/http"
    "net/url"
    "os"
    "strconv"
    "strings"
)

func main() {
    endpoint := "http://localhost:8080/"
    // контейнер данных для запроса
    data := url.Values{}
    // приглашение в консоли
    fmt.Println("Введите длинный URL")
    // открываем потоковое чтение из консоли
    reader := bufio.NewReader(os.Stdin)
    // читаем строку из консоли
    long, err := reader.ReadString('\n')
    if err != nil {
        panic(err)
    }
    long = strings.TrimSuffix(long, "\n")
    // заполняем контейнер данными
    data.Set("url", long)
    // добавляем HTTP-клиент
    client := &http.Client{}
    // пишем запрос
    // запрос методом POST должен, помимо заголовков, содержать тело
    // тело должно быть источником потокового чтения io.Reader
    request, err := http.NewRequest(http.MethodPost, endpoint, strings.NewReader(data.Encode()))
    if err != nil {
        panic(err)
    }
    // в заголовках запроса указываем кодировку
    request.Header.Add("Content-Type", "application/x-www-form-urlencoded")
    // отправляем запрос и получаем ответ
    response, err := client.Do(request)
    if err != nil {
        panic(err)
    }
    // выводим код ответа
    fmt.Println("Статус-код ", response.Status)
    defer response.Body.Close()
    // читаем поток из тела ответа
    body, err := io.ReadAll(response.Body)
    if err != nil {
        panic(err)
    }
    // и печатаем его
    fmt.Println(string(body))
}
```

## Дополнительные материалы

- [go.dev/net/http/cookiejar](https://pkg.go.dev/net/http/cookiejar) — документация пакета `cookiejar`.
- [go.dev | Type Client](https://pkg.go.dev/net/http#Client) — описание HTTP-клиента.
- [Golang By Example | Cookies in Go](https://golangbyexample.com/cookies-golang/) — о куках в Go.