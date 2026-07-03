# counter 1000 — data race без sync

**Источник:** go-interview/popular_tasks #8

Что не так? Как исправить? Как без пакета `sync`?

```go
var counter int
for i := 0; i < 1000; i++ {
	go func() {
		counter++
	}()
}
// counter == 1000 ?
```

## Эталонное решение

**Проблемы:**
1. **Data race** — параллельный `counter++` (read-modify-write) без синхронизации.
2. Main **не ждёт** goroutine — `counter` читают до завершения воркеров.

**С sync:** `sync.WaitGroup` + `sync.Mutex` или `atomic.AddInt64`.

**Без sync:** `atomic` всё равно stdlib — если «без sync» = без mutex: **`sync/atomic`**. Иначе — канал-счётчик с одной owning goroutine.

Итог: `counter` **≤ 1000**, часто **значительно меньше**.
