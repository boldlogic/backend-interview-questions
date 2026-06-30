![[Pasted image 20260630182611.png]]



Мое решение
```go

// You can edit this code!
// Click here and start typing.
package main

import (
	"fmt"
	"sync"
)

func main() {
	fmt.Println("Hello, 世界")
	a := make(chan int)
	b := make(chan int)

	res := make(chan int)

	wg := sync.WaitGroup{}

	wg.Add(4)

	go func() {
		defer wg.Done()
		merge(res, a, b)
	}()

	go func() {
		defer wg.Done()
		a <- 1
		close(a)
	}()
	go func() {
		defer wg.Done()
		b <- 2
		b <- 3
		close(b)
	}()

	go func() {
		defer wg.Done()
		for v := range res {
			fmt.Println(v)
		}
	}()

	wg.Wait()
}

func merge(out chan<- int, cs ...<-chan int) {
	// func merge(cs ...<-chan int) <-chan int {
	//давай рассуждать.
	// Мы не можем вернуть результирующий канал пока не вычитаем вмерживаемые
	// сколько данных в вмерживаемых внутри функции судить не можем
	// соответственно мейкать его здесь как буф/небуф - блокировка потому что не вычитали все и не отдали результирующий канал
	// значит итоговый нужно мейкать раньше вне этой функции
	wg := sync.WaitGroup{}

	for i := range cs {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for v := range cs[i] {
				out <- v
			}
		}()

	}
	wg.Wait()
	close(out)

}

```


решение с собеса

![[Pasted image 20260630182801.png]]