# sleep time.After — канал

**Источник:** go-interview/golang #9

Реализовать `sleep(seconds int)` через `time.After` (без `time.Sleep`).

```go
func sleep(s int) {
	// ...
}
```

## Эталонное решение

```go
func sleep(s int) {
	<-time.After(time.Duration(s) * time.Second)
}
```

`time.After` возвращает `<-chan time.Time`; чтение блокирует goroutine до истечения таймера.
