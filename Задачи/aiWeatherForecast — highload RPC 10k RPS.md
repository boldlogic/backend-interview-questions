# aiWeatherForecast — highload RPC 10k RPS

**Собес:** [[record_water]] · ~46:53

```go
// Есть функция которая через нейронную сеть вычисляет прогноз погоды за ~1 секунду
// Есть highload RPC ручка с нагрузкой 10k RPS
// Необходимо реализовать код этой ручки

package main
import (
    "fmt"
    "math/rand"
    "net/http"
    "time"
)

// aiWeatherForecast через нейронную сеть вычисляет прогноз погоды за ~1 секунду
func aiWeatherForecast() int {
    time.Sleep(1 * time.Second)
    return rand.Intn(70) - 30
}

func main() {
    http.HandleFunc("/weather", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "{\"temperature\": %d}\n", aiWeatherForecast())
    })

    if err := http.ListenAndServe(":3333", nil); err != nil {
        panic(err)
    }
}
```

## Мое решение

```go
// Есть функция которая через нейронную сеть вычисляет прогноз погоды за ~1 секунду
// Есть highload RPC ручка с нагрузкой 10k RPS
// Необходимо реализовать код этой ручки

package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"sync"
	"time"
)

type Cache struct {
	Value int
	mu    sync.RWMutex
	TTL   time.Time
}

// aiWeatherForecast через нейронную сеть вычисляет прогноз погоды за ~1 секунду
func aiWeatherForecast() int {
	time.Sleep(1 * time.Second)
	return rand.Intn(70) - 30
}

const defaultTTL time.Duration = 60 * time.Second

func main() {

	c := new(Cache)

	http.HandleFunc("/weather", func(w http.ResponseWriter, r *http.Request) {
		value := 0
		var ttl time.Time

		c.mu.RLock()
		value = c.Value
		ttl = c.TTL
		c.mu.RUnlock()

		if time.Now().Before(ttl) {
			fmt.Fprintf(w, "{\"temperature\": %d}\n", value)
			return
		}

		c.mu.Lock()

		if time.Now().After(c.TTL) {
			c.Value = aiWeatherForecast()
			c.TTL = time.Now().Add(defaultTTL)
		}
		value = c.Value
		c.mu.Unlock()

		fmt.Fprintf(w, "{\"temperature\": %d}\n", value)
	})

	if err := http.ListenAndServe(":3333", nil); err != nil {
		panic(err)
	}
}

```

