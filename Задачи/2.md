Мое решение
```go
package main

import (
	"io"
	"log"
	"net/http"
	"sync"
)

//worker pool. организовать запуск не более 3 параллельных воркеров,
// которые выполняют запросы на все урл массива урл и выполнить
// гет запрос на каждый урл. вывести боди ответа в втдоут в текстововм

var urls = []string{"https://google.com", "https://ya.ru"}

func main() {

	pool := makePool(3)
	for _, url := range urls {
		log.Printf("запуск, %s", url)
		pool.DoWork(url)
	}
	pool.shutdown()

}

type Pool struct {
	jobs chan string
	wg   sync.WaitGroup
}

func (p *Pool) shutdown() {
	close(p.jobs)
    p.wg.Wait()
}

func makePool(n int) *Pool {
	pool := Pool{
		jobs: make(chan string, 10),
	}
	for i := 0; i < n; n++ {
		pool.wg.Add(1)
		go func() {
			pool.consume(i)
		}()
	}

	return &pool

}

func (p *Pool) consume(id int) {
	defer p.wg.Done()

	for v := range p.jobs {
		resp, err := http.Get(v)
		if err != nil {
			log.Printf("ошибка запроса, worker: %d", id)
			continue
		}
		body, err := io.ReadAll(resp.Body)
		resp.Body.Close()
		if err != nil {
			log.Printf("ошибка парсинга, worker: %d", id)
			continue
		}
		log.Print(body)
	}

}

func (p *Pool) DoWork(url string) {
	//эту функцию добавляем потому что есть в исходной задаче. Это продюсер
	select {
	case p.jobs <- url:
		return

	}

}

```


решение с собеса
![[Pasted image 20260630155921.png]]