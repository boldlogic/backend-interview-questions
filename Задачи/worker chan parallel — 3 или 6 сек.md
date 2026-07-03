# worker chan parallel — 3 или 6 сек

**Источник:** go-interview/popular_tasks #10

Сколько секунд выведет? Как сделать ~3 сек?

```go
func worker() chan int {
	ch := make(chan int)
	go func() {
		time.Sleep(3 * time.Second)
		ch <- 42
	}()
	return ch
}

func main() {
	timeStart := time.Now()
	_, _ = <-worker(), <-worker()
	println(int(time.Since(timeStart).Seconds()))
}
```

## Эталонное решение

**~6 секунд** — второй `<-worker()` начинается **после** завершения первого (comma operator / sequential receive).

Параллельно (~3 сек):
```go
w1, w2 := worker(), worker()
_, _ = <-w1, <-w2
```
или `sync.WaitGroup` / два `<-` в разных goroutine.

На собесе: создание `worker()` уже запускает goroutine — оба sleep идут параллельно, если **оба вызова** сделаны до блокирующего receive.
