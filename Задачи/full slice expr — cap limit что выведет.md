# full slice expr — cap limit, что выведет

**Источник:** go-interview/golang #16

Что выведет программа?

```go
package main

import "fmt"

func main() {
	a := [5]int{1, 2, 3, 4, 5}
	t := a[3:4:4]
	fmt.Println(t[0])
}
```

## Эталонное решение

```
4
```

`a[3:4:4]` — full slice expression: len=1 (элемент `4`), **cap=4-3=1** (не до конца массива). `t[0]` — единственный элемент среза, значение `4`.

Отличие от `a[3:4]`: cap был бы `5-3=2`, append мог бы перезаписать `a[4]` без realloc.
