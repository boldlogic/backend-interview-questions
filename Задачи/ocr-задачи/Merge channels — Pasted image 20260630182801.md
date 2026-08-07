# OCR: Merge channels — решение на скрине

Источник: `Задачи/Merge channels.md`
Скрин: `![[Картинки/Pasted image 20260630182801.png]]`

```go
package main

func merge(cs ...<-chan int) <-chan int {
	res_ch := make(chan int)
	wg := sync.WaitGroup{}

	wg.Add(len(cs))
	for _, ch := range cs {
		go func(ch <-chan int) {
			defer wg.Done()
			for _, val := range ch {
				res_ch <- val
			}
		}(ch)
	}

	go func() {
		wg.Wait()
		close(res_ch)
	}()

	return res_ch
}
```
