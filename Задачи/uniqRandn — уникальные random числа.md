# uniqRandn — уникальные random числа

**Собес:** [[alfa go]] · ~28:46

```go
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    fmt.Println(uniqRandn(10))
}

// Написать функцию, которая возвращает слайс с заданным количеством случайных уникальных чисел
func uniqRandn(n int) []int {

    num := rand.Int()
}
```
## решение

```go
// Требуется реализовать функцию uniqRandn, которая генерирует слайс длины n уникальных, рандомных чисел.
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println(uniqRandn(10))
}

func uniqRandn(n int) []int {
	if n < 0 {
		return nil
	}
	res := make([]int, 0, n)
	dedup := make(map[int]struct{}, n)
	for len(res) < n {
		d := rand.Int()

		if _, ok := dedup[d]; !ok {
			dedup[d] = struct{}{}
			res = append(res, d)
		}
	}
	return res
}

```

![[Pasted image 20260630171044.png]] 