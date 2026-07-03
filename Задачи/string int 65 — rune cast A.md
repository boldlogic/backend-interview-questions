# string int 65 — rune cast A

**Источник:** go-interview/golang #15

Что выведет?

```go
package main

import "fmt"

func main() {
	i := 65
	fmt.Println(string(i))
}
```

## Эталонное решение

```
A
```

`string(i)` при `i` типа **int** конвертирует число в **Unicode code point** (rune), не в десятичную строку `"65"`. 65 = `'A'`.

Для `"65"` нужно `strconv.Itoa(i)` или `fmt.Sprintf("%d", i)`.
