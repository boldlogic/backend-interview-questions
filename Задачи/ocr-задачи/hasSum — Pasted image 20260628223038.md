# OCR: hasSum — два числа сумма в слайсе

Источник: `Задачи/hasSum — два числа сумма в слайсе.md`
Скрин: `![[Картинки/Pasted image 20260628223038.png]]`

```go
package main

import "fmt"

func hasSum(items []int, sum int) bool {
	if len(items) <= 1 {
		return false
	}
	// TODO: implement this
	seen := make(map[int]struct{}, len(items))

	for _, v := range items {
		need := sum - v
		if _, ok := seen[need]; ok {
			return true
		}
		seen[v] = struct{}{}
	}

	return false
}

// time: O(n)
// mem: O(n)

func main() {
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 11)) // -> true
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 12)) // -> false
	fmt.Println(hasSum([]int{3}, 3))           // -> false
	fmt.Println(hasSum([]int{3, 4}, 6))        // -> false
	fmt.Println(hasSum([]int{3, 3}, 6))        // -> true
	fmt.Println(hasSum([]int{}, 6))            // -> false
}
```
