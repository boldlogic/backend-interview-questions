# OCR: Defer

Источник: `Задачи/Defer.md`
Скрин: `![[Pasted image 20260705172510.png]]`

```go
func deferExample() int {
	a := 10
	defer func(val int) {
		fmt.Println("first:", val)
	}(a)
	a = 20
	defer func(val int) {
		fmt.Println("second:", val)
	}(a)
	a = 30
	fmt.Println("exiting:", a)
	return a
}
```
