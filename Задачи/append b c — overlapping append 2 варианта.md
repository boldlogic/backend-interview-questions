1. Расскажи подробно что происходит

# Вариант 1
-----------
package main

import "fmt"

func main() {
    a := []int{1,2}
    a = append(a, 3)
    b := append(a, 4)
    c := append(a, 5)

    fmt.Println(b)
    fmt.Println(c)
}

# Вариант 2
-----------
package main

import "fmt"

func main() {
    a := []int{1,2}
    a = append(a, 3)
    a = append(a, 7)
    b := append(a, 4)
    c := append(a, 5)

    fmt.Println(b)
    fmt.Println(c)
}


============================
