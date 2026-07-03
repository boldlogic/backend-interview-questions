# swap pointers — x y через указатели

**Источник:** go-interview/golang #11

`swap(&x, &y)` должно дать `x=2, y=1`.

```go
func main() {
	x := 1
	y := 2
	swap(&x, &y)
	fmt.Println(x, y)
}

func swap(a, b *int) {
	// ...
}
```

## Эталонное решение

```go
func swap(a, b *int) {
	*a, *b = *b, *a
}
```

Множественное присваивание: правая часть вычисляется до записи.
