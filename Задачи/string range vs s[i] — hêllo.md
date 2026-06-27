# string range vs s[i] — hêllo

**Собес:** [[alfa go]] · ~48:08

По чему будем итерироваться?

```go


package main

import "fmt"

func main() {
    s := "hêllo"
    for i := range s {
        fmt.Printf("position %d: %c\n", i, s[i])
    }
    fmt.Printf("len=%d\n", len(s))
}
```
