# square pointer — x после square

**Источник:** go-interview/golang #12

Какое значение `x` после `square(&x)`?

```go
func square(x *float64) {
	*x = *x * *x
}

func main() {
	x := 1.5
	square(&x)
	fmt.Println(x)
}
```

## Эталонное решение

```
2.25
```

Указатель передаётся по значению, но **указывает на ту же переменную** в `main`; разыменование меняет `x` снаружи.
