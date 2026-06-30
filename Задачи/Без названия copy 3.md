```go
package main

import "fmt"

func generator(ch chan int, done chan struct{}) {
	val := 0
	dif := 0
	// допишите код функции
loop:
	for {
		select {

		case <-done:
			break loop
		default:
			val += dif
			dif += 1
			ch <- val
		}
	}
}

func main() {
	// канал для получения значений
	ch := make(chan int)
	// канал для оповещения о конце работы, тип значений не важен
	done := make(chan struct{})

	go func() {
		// достаточно закрыть канал, чтобы из него прочиталось значение
		// это удобно, если его слушают несколько горутин
		defer close(done)

		for i := 0; i < 15; i++ {
			fmt.Print(<-ch, " ")
		}
	}()

	generator(ch, done)
}


```