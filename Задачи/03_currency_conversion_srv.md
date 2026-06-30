# Задача на исправление бага и обсуждение простого сервиса

```go
package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

// FIXME:
func main() {
	rates, err := readConversionRates()
	if err != nil {
		log.Fatalf("read intial conversion rates values: %s", err)
	}

	// background task to update conversion rates
	go func() {
		for {
			time.Sleep(time.Minute)
			rates, err = readConversionRates()
			if err != nil {
				log.Printf("ERR: update conversion rates: %s", err)
			}
		}
	}()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// parse 'from' and 'value' from query params
		from := "RUB" 
		val := 140.0

		rate, ok := rates[from]
		if !ok {
			http.NotFound(w, r)
			return
		}

		convVal := val / rate

		fmt.Fprint(w, convVal)
	})

	if err := http.ListenAndServe(":8080", nil); err != http.ErrServerClosed {
		log.Fatal(err)
	}
}

// readConversionRates reads rates from a file or an external service (relatively long-running function).
func readConversionRates() (map[string]float64, error) {
	
	// resp, err := http.Get("https://exmaple.org/conv-rates")
	// ... 

	time.Sleep(100 * time.Millisecond)

	return map[string]float64{
		"USD": 1.0,
		"RUB": 70.0,
	}, nil
}
````

## О задаче

Это набросок вэб сервиса конвертации валюты в USD с периодическим обновлением данных.

В коде как минимум один баг - нет синхронизации доступа к мапе _rates_ (data race, хэндлер читает, горутина обновления пишет).

__Основная задача - пофиксить data race баг.__


## Доп вопросы

Помимо основной задачи, в процессе обсуждения можно спросить:

- сколько горутин в этом приложении? (вопрос-подсказка)
- есть ли у кандидата опыт простого нагрузочного тестирования? Какие инструменты использует или слышал (ab, jmeter, yandex tank, wrk)
- что такое graceful shutdown?
- как можно искать data race баги в go? (-race) 
- Mutex и RWMutext - в чём разница?


## Примерный ход обсуждения

Кода не мало, нужно дать время кандидату познакомиться с ним и попросить рассказть, что этот код делает.
Перед тем как идти дальше, убеждаемся, что кандидат понимат, что это вэб сервис с обновлением данных в бэкграунде.

Дальше просим найти ошибки и возможно, прокомментировать код (хорошие кандидаты обычно и так это делают).
Если нужны подсказки, можно задать наводящий вопрос - "сколько горутин в этом приложении" (много).

Когда баг найден, или мы подсказали в чём он, просим пофиксить.
Можно спросить, как можно в go обнаруживать подобные ошибки (флаг -race)

Ещё в коде есть проблема, которая связана с багом, иногда кандидаты обращают внимание на неё, а не на data race:
```go
	rates, err = readConversionRates() //  в случае ошибки переменная rates "обнулится" (или будет каким-то "недоделанным"" объектом)
	if err != nil {
		log.Printf("ERR: update conversion rates: %s", err)
	}
``` 
В таком случае можно попросить кандидата начать с исправления этой проблемы (бизнес требование - в случае ошибки оставляем предыдущую версию данных)


## Вариант решения

Добавляем мьютекс и дальше используем его в горутине обновления данных и в хэндлере. 

```go
	tmpRates, err := readConversionRates() //  важно, что здесь мьютеск не лочится, читаем во врменную переменную
	if err != nil {
		log.Printf("ERR: update conversion rates: %s", err)
		continue
	}
	mu.Lock()
	rate = tmpRates // мьютекс защищает запись в rates
	mu.Unlock()

...

	mu.Lock()	// можно использовать RWMutex, тогда здесь RLock/RUnlock
	rate, ok := rates[from]
	mu.Unlock()

```


## Типичные проблемы при исправлении бага

### Мьютексом обрамляется лишний код  

```go
	mu.Lock()
	rates, err = readConversionRates()
    mu.Unlock()

```
У этого решения проблема - мьютекс лочится на время выполнения readConversionRates(), а нужно защитить только операцию записи в переменную _rates_.
Наводящий вопрос - "выкатили, сделали нагрузочное тестирование, видим проблему - пики response time раз в минуту" (заодно можно спросить про опыт в нагрузочном тестировании - ab, hey, jmeter, yandex tank, etc)

### Мьютекс разблокируется в defer

```go
	mu.Lock()
    defer mu.Unlock()
	rates, err = readConversionRates()

```

у нас тут цикл for, defer не сработает


### Мьютекс используется неправильно

Нередко мьютексом лочат только запись в _rates_ , а чтение в хэндлере - нет.


### Advanced 

Можно пообсужадать, как будет такой баг будет себя проявлять.
Некоторые думают, что тут будет паника вида "fatal error: concurrent map writes", путают этот кейс с кейсом concurrent map write (https://go.dev/doc/faq#atomic_maps). 
Это не так, тут конкуретная запись не в саму мапу, а в переменную _rates_.  Т.е. если бы это была не мапа, а слайс, баг был бы тот же.

Всё-таки, как будет баг себя проявлять? 
На эту тему есть документ [The Go Memory Model](https://go.dev/ref/mem).
Ответ зависит от имплементации go и платформы. Тут я могу ошибаться, потому что в этой доке есть проблемы и неточности, но вот возможные варианты:

- в рез-те оптимизации, обновления переменной _rates_ может не происходить
- если на платформе запись в переменную _rates_ не атомарная операци, может произойти системное исключение/сигнал, который заставит паниковать рантайм

Можно поговорить с кандадатом про Memory Model, про то, что это всё любопытно, но надо просто делать нормально, т.е. делать синхронизацию через мьютексы, каналы и т.п. 

