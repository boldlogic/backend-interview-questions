1. Что будет содержать s после инициализации?
2. Что произойдет в println для слайса и для мапы?

func a(s []int) {
    s = append(s, 37)
}

func b(m map[int]int) {
    m[3] = 33
}

func main() {
    s := make([]int, 3, 8)
    m := make(map[int]int, 8)

    // add to slice
    a(s)
    println(s[3]) //?

    // add to map
    b(m)
    println(m[3]) //?
}
