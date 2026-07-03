# WaitGroup sema — Inc Dec на канале

**Источник:** go-interview/popular_tasks #6

Кастомный «семафор» на буферизованном канале: `Inc(k)` кладёт `k` токенов, `Dec(k)` забирает. Дождаться завершения 5 goroutine.

```go
type sema chan struct{}

func New(n int) sema { return make(sema, n) }

func (s sema) Inc(k int) { /* ... */ }
func (s sema) Dec(k int) { /* ... */ }
```

## Эталонное решение

```go
func (s sema) Inc(k int) {
	for i := 0; i < k; i++ {
		s <- struct{}{}
	}
}

func (s sema) Dec(k int) {
	for i := 0; i < k; i++ {
		<-s
	}
}

sem := New(len(numbers))
for _, num := range numbers {
	go func(n int) {
		fmt.Println(n)
		sem.Inc(1)
	}(num)
}
sem.Dec(len(numbers))
```

`Dec(n)` блокируется, пока все goroutine не вызовут `Inc(1)` — аналог `WaitGroup` без `sync`.
