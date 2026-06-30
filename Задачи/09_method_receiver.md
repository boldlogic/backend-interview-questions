# Первый вопрос: что выведет этот код 
# ответ: синтаксис методов - это синтаксический сахар, по сути код будет таким
`Set(b BasicStruct, s string)`

```go
package main

import "fmt"

type BasicStruct struct {
	Value string
}

func (b BasicStruct) Set(s string) {
	b.Value = s
}

func (b BasicStruct) Get() string {
	return b.Value
}

type Doer interface {
	Set(string)
	Get() string
}

func doChangeAndPrint(d Doer) {
	d.Set("bar")
	fmt.Println(d.Get())
}

func main() {
	bs := BasicStruct{Value: "foo"}
	doChangeAndPrint(bs)
}

```

# Второй вопрос
# если сделать так
```go
    bs := &BasicStruct{Value: "foo"} // взят указатель 
    doChangeAndPrint(bs)

```
# то что будет напечатано? "foo" или "bar"? почему?


#третий вопрос (не показывать сразу кандидату): как "исправить"?
# ответ:
```go
    func (b *BasicStruct) Set(s string)
```
# речь про value/pointer receiver


