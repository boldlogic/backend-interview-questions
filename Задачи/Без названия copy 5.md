```go
package main

import (
	"fmt"
	"time"
)

func main() {
	// напишите код программы
	oTicker := time.NewTicker(time.Duration(200) * time.Millisecond)
	defer oTicker.Stop()
	dotTicker := time.NewTicker(time.Duration(1) * time.Second)
	defer dotTicker.Stop()
	timer := time.NewTimer(time.Duration(4) * time.Second)
	for {
		select {
		case <-oTicker.C:
			fmt.Println("o")
		case <-dotTicker.C:
			fmt.Println(".")
		case <-timer.C:
			return
		}
	}

}


```