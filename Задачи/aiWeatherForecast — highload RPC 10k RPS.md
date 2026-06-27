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
