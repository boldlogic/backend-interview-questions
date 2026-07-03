1. Что выведет код?

func main() {
  fmt.Println("start")
  for i := 1; i < 4; i++ {
    defer fmt.Println(i)
  }
  fmt.Println("end")
}
