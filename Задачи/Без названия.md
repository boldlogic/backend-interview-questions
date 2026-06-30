```go
package main

import "fmt"

// что выведет программа?

type Person struct {
	Name string
	Age  int
}

//в Go указатели передаются по значению
// (копируется сам адрес),
// поэтому переприсвоение p внутри функции
// снаружи не видно.
func SetAge(p *Person, age int) {
	p = &Person{
		Name: p.Name,
		Age:  age,
	}
	//p -другая переменная просто с тем же адресом
	// не меняет исходную структуру. Локальная p теперь указывает на новую структуру

}

//решение :
// делаем p.Age=age.

func main() {
	p := &Person{Name: "John"} //хранит адрес структуры
	SetAge(p, 27)              //передается копия адреса

	fmt.Printf("Name: %s, Age: %d\n", p.Name, p.Age)
}

```