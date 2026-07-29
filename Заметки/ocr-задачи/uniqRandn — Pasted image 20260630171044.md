# OCR: uniqRandn — уникальные random числа

Источник: `Задачи/uniqRandn — уникальные random числа.md`
Скрин: `![[Картинки/Pasted image 20260630171044.png]]`

```go
import (
)

func main() {
	fmt.Println(uniqRandn(10))
}

func uniqRandn(n int) []int {
	res := make([]int, 0, n)
	hash := make(map[int]struct{}, n)

	for len(res) < n {
		rand := rand.Intn(n)
		if _, found := hash[rand]; ok {
			continue
		}

		hash[rand] = struct{}{}
	}

	return res
}
```
