# OCR: worker pool — HTTP GET max 3 параллельно

Источник: `Задачи/worker pool — HTTP GET max 3 параллельно.md`
Скрин: `![[Картинки/Pasted image 20260630155921.png]]`

```go
func (p *workerPool) DoWork(url string) {
	p.jobs <- url
}

func makePool(n int) *workerPool {
	pool := &workerPool{
		jobs: make(chan string),
	}
	for i := 0; i < n; i++ {
		pool.wg.Add(1)
		go func() {
			defer pool.wg.Done()
			for url := range pool.jobs {
				resp, err := http.Get(url)
				if err != nil {
					log.Printf("Error fetching url %s: %v", url, err)
					continue
				}
				body, err := ioutil.ReadAll(resp.Body)
				if err != nil {
					log.Printf("Error reading response body: %v", err)
				}
				resp.Body.Close()
				fmt.Println("Response body: %s, from url: %s", string(body), url)
			}
		}()
	}
	return pool
}
```
