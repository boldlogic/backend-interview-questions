# Sleep с прерыванием через контекст 

```go
package main

import (
	"context"
	"log"
	"time"
)

// Sleep is interruptible verion of time.Sleep.
// Returns false if context was cancelled,
func Sleep(context.Context, time.Duration) bool {
	// TODO: implement
	return false
}

func main() {
	ctx, _ := context.WithTimeout(context.Background(), time.Millisecond)

	if !Sleep(ctx, time.Second) {
		log.Print("interrupted")
	}
}
````
