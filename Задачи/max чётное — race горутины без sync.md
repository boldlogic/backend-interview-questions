```go
// Находим максимальное четное число
//
// Исходный вариант со скрина:
//
//	package main
//
//	import "fmt"
//
//	func main() {
//		var max int
//
//		for i := 1000; i > 0; i-- {
//			go func() {
//				if i%2 == 0 && i > max {
//					max = i
//				}
//			}()
//		}
//
//		fmt.Printf("Maximum is %d", max)
//	}
//
// Что ломает исходник (go 1.26):
//   - гонка на max — несколько горутин пишут без синхронизации;
//   - main не ждёт горутины — fmt.Printf почти всегда до завершения воркеров.
//
// Захват i в closure: на Go < 1.22 все горутины видели одно и то же i (часто 0).
// С Go 1.22+ переменная цикла создаётся заново на каждой итерации — здесь это уже не баг.
// go func(i int) { ... }(i) остаётся явным стилем для совместимости со старыми версиями.

package main

import (
	"fmt"
	"sync"
)

func main() {
	var max int

	wg := sync.WaitGroup{}
	mu := sync.Mutex{}

	for i := 1000; i > 0; i-- {
		wg.Add(1)
		go func() {
			defer wg.Done()

			if i%2 != 0 {
				return
			}

			mu.Lock()
			defer mu.Unlock()
			if i > max {
				max = i
			}

		}()
	}
	wg.Wait()

	fmt.Printf("Maximum is %d", max)
}


```