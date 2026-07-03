# changePointer — p = &v локально

**Источник:** go-interview/popular_tasks #9

Что выведет? Как получить `5` и `3`?

```go
func main() {
	v := 5
	p := &v
	println(*p)

	changePointer(p)
	println(*p)
}

func changePointer(p *int) {
	v := 3
	p = &v
}
```

## Эталонное решение

```
5
5
```

`p` в `changePointer` — **копия** указателя; `p = &v` меняет только локальную копию, не `p` в `main`.

Чтобы вывести `5` и `3`:
```go
func changePointer(p **int) {
	v := 3
	*p = &v
}
// changePointer(&p)
```
или проще: `*p = 3` без переприсвоения `p`.

См. также: `SetAge — переприсвоение указателя`.
