1. Что выведется?
2. Зная обо всех таких нюансах, которые могут возникнуть, какие есть рекомендации?

# Вариант 1
-----------
func mod(a []int) {
  for i := range a {
    a[i] = 5
  }
  fmt.Println(a)
}
func main() {
  sl := []int{1, 2, 3, 5}
  mod(sl)
  fmt.Println(sl)
}

# Вариант 2
-----------
func mod(a []int) {
  for i := range a {
    a[i] = 5
  }
  fmt.Println(a)
}
func main() {
  sl := make([]int, 4, 8)
  sl[0] = 1
  sl[1] = 2
  sl[2] = 3
  sl[3] = 5
  mod(sl)
  fmt.Println(sl)
}

# Вариант 3
-----------
func mod(a []int) {
  a = append(a, 125)
  for i := range a {
    a[i] = 5
  }
  fmt.Println(a)
}
func main() {
  sl := make([]int, 4, 8)
  sl[0] = 1
  sl[1] = 2
  sl[2] = 3
  sl[3] = 5
  mod(sl)
  fmt.Println(sl)
}

# Вариант 4
-----------
func mod(a []int) {
  a = append(a, 125)
  for i := range a {
    a[i] = 5
  }
  fmt.Println(a)
}
func main() {
  sl := []int{1, 2, 3, 4, 5}
  mod(sl)
  fmt.Println(sl)
}
