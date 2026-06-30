```go
// что выведет программа
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func SetAge(p *Person, age int) {
	p.Age = age
}

func main() {
	people := make(map[string]Person)
	people["John"] = Person{Name: "John"}
	// исходная строка
	// SetAge(&people["John"], 27) // берем адрес от мапы

	// ,но адрес у мапы взять нельзя поэтому не скомпилируется
	// фикс:
	person, ok := people["John"]
	if ok {
		SetAge(&person, 27)
		people["John"] = person

	}

	fmt.Printf("Name: %s, Age: %d\n", people["John"].Name, people["John"].Age)
}


```