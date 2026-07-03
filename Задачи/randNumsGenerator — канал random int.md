# randNumsGenerator — канал random int

**Источник:** go-interview/popular_tasks #2

Написать генератор: функция возвращает `<-chan int`, пишет `n` случайных чисел и закрывает канал.

```go
func randNumsGenerator(n int) <-chan int {
	// ...
}

func main() {
	for num := range randNumsGenerator(10) {
		fmt.Println(num)
	}
}
```

## Эталонное решение

```go
func randNumsGenerator(n int) <-chan int {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	out := make(chan int)
	go func() {
		for i := 0; i < n; i++ {
			out <- r.Intn(n)
		}
		close(out)
	}()
	return out
}
```

Паттерн: goroutine + `close` после отправки. Небуферизованный канал — backpressure на consumer.
