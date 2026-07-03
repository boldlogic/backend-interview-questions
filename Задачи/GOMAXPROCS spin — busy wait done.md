# GOMAXPROCS spin — busy wait done

**Источник:** go-interview/popular_tasks #7

Дойдёт ли до `fmt.Println("finished")`? Если нет — как исправить?

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	runtime.GOMAXPROCS(1)

	done := false

	go func() {
		done = true
	}()

	for !done {
	}
	fmt.Println("finished")
}
```

## Эталонное решение

**Зависит от версии Go и планировщика** — busy loop без `runtime.Gosched`/block может **не отдать** P другой goroutine → **deadlock** или бесконечный spin (race на `done` без sync).

Исправления (любое):
- `runtime.Gosched()` в цикле;
- `time.Sleep(time.Millisecond)`;
- `sync/atomic` + `for !atomic.Load(&done)`;
- `select` на channel;
- убрать `GOMAXPROCS(1)`.

На собесе: **spin-wait без cooperative/preemptive yield — антипаттерн**; плюс data race на `done`.
