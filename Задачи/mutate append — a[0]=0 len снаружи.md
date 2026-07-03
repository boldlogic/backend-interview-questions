1. Что будет в результате выполнения?

mutate := func(a []int) {
  a[0] = 0
  a = append(a, 1)
  fmt.Println(a)
}
a := []int{1, 2, 3, 4}
mutate(a)
fmt.Println(a)
