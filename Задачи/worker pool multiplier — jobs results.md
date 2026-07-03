# worker pool multiplier — jobs results

**Источник:** go-interview/popular_tasks #5

Worker pool: 3 воркера, 5 jobs, функция `multiplier(x) = x*10`. Jobs и results — каналы.

```go
func worker(id int, f func(int) int, jobs <-chan int, results chan<- int) {
	for j := range jobs {
		results <- f(j)
	}
}

// numJobs=5, workers=3, multiplier x*10
// ожидание: 10 20 30 40 50 (порядок в results может отличаться)
```

## Эталонное решение

```go
const numJobs = 5
jobs := make(chan int, numJobs)
results := make(chan int, numJobs)

multiplier := func(x int) int { return x * 10 }

for w := 1; w <= 3; w++ {
	go worker(w, multiplier, jobs, results)
}

for j := 1; j <= numJobs; j++ {
	jobs <- j
}
close(jobs)

for i := 1; i <= numJobs; i++ {
	fmt.Println(<-results)
}
```

`close(jobs)` — сигнал воркерам выйти из `range`. Буфер results = numJobs — можно собрать без deadlock.
