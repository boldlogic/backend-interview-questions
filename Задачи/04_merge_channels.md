# Объединение нескольких каналов 

```go
package main

func merge(chs ...chan int) chan int {
	// TODO: implement
}

func main() {
	ch1 := startProducerA()
	ch2 := startProducerB()

	for el := range merge(ch1, ch2) {
		println(el)
	}
}
````
