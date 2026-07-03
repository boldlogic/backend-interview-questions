# intersection slices — map counter

**Источник:** go-interview/popular_tasks #1

На вход два неупорядоченных слайса `[]int`. Вернуть **пересечение** с учётом кратности (если в `a` два `2` и в `b` один `2` — в результате один `2`).

```go
func intersection(a, b []int) []int {
	// ...
}

// intersection([]int{23, 3, 1, 2}, []int{6, 2, 4, 23}) -> [2 23]
// intersection([]int{1, 1, 1}, []int{1, 1, 1, 1}) -> [1 1 1]
```

## Эталонное решение

```go
func intersection(a, b []int) []int {
	counter := make(map[int]int)
	var result []int
	for _, x := range a {
		counter[x]++
	}
	for _, x := range b {
		if counter[x] > 0 {
			counter[x]--
			result = append(result, x)
		}
	}
	return result
}
```

O(len(a)+len(b)) по времени, O(min(len(a), len(b))) по памяти для map. Альтернатива: sort + two pointers без extra map, но O(n log n).
