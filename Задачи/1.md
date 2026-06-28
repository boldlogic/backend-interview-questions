```go
package main

import "fmt"


func hasSum(items []int, sum int) bool {
	return false
}

func main() {
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 11)) // -> true
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 12)) // -> false
	fmt.Println(hasSum([]int{3}, 3))           // -> false
	fmt.Println(hasSum([]int{3, 4}, 6))        // -> false
	fmt.Println(hasSum([]int{3, 3}, 6))        // -> true
	fmt.Println(hasSum([]int{}, 6))            // -> false
}

```

## Мое решение
Неправильно понял задачу
```go
package main

import "fmt"

//проверяет есть ли в слайсе два разных числа которые дают сумму. Одно число дважды не может учитываться

func hasSum(items []int, sum int) bool {
	//Мои мысли: нужно выделить уникальные и только по ним проходиться
	if len(items) < 2 {
		return false
	}
	unique := make(map[int]struct{}, len(items))

	for i := 0; i < len(items); i++ {
		if _, ok := unique[items[i]]; ok {
			continue
		}

		for k := range unique {
			if k+items[i] == sum {
				return true
			}

		}

		unique[items[i]] = struct{}{}

	}

	return false
}

func main() {
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 11)) // -> true
	fmt.Println(hasSum([]int{3, 2, 8, 5}, 12)) // -> false
	fmt.Println(hasSum([]int{3}, 3))           // -> false
	fmt.Println(hasSum([]int{3, 4}, 6))        // -> false
	fmt.Println(hasSum([]int{3, 3}, 6))        // -> true
	fmt.Println(hasSum([]int{}, 6))            // -> false
}

```

## решение

![[Pasted image 20260628223038.png]]