# HandleFile — semaphore и WaitGroup

**Собес:** [[СимберСофт]] · ~31:18–39:12

Максимально оптимально обработать ~10 000 файлов через `HandleFile`, ограничив число одновременных goroutine.

## Решение

```go
//Есть filesList := []string{"log1.log", "file3.log"} // и так 10 000 файлов

func handleFile(fileName string) {

}


func main() {
	filesList := []string{"log1.log", "file3.log"}
	var wg sync.WaitGroup
	sem := make(chan struct{}, 10)
	wg.Add(len(filesList))
	for _, file := range filesList {
		sem <- struct{}{}
		go func(f string) {
			defer wg.Done()
			defer func() { <-sem }()
			HandleFile(f)
		}(file)
	}

	wg.Wait()
}
```
