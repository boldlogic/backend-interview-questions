# pipeline squares — naturals в квадраты

**Источник:** go-interview/popular_tasks #4

Конвейер: goroutine пишет числа 0..10 в `naturals`, вторая читает, возводит в квадрат, пишет в `squares`. Main читает `squares`. Закрыть каналы, чтобы не deadlock.

```go
func main() {
	naturals := make(chan int)
	squares := make(chan int)
	// producer → naturals
	// stage: naturals → squares
	// consumer: range squares
}
```

## Эталонное решение

```go
go func() {
	for x := 0; x <= 10; x++ {
		naturals <- x
	}
	close(naturals)
}()

go func() {
	for x := range naturals {
		squares <- x * x
	}
	close(squares)
}()

for x := range squares {
	fmt.Println(x)
}
```

Классический pipeline: каждая стадия `range` + `close` downstream после EOF upstream.
