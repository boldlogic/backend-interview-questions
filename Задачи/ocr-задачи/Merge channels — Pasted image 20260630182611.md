# OCR: Merge channels — условие

Источник: `Задачи/Merge channels.md`
Скрин: `![[Картинки/Pasted image 20260630182611.png]]`

## Условие

Написать код функции, которая делает merge N каналов. Весь входной поток перенаправляется в один канал.

## Шаблон на скрине

```go
package main

func merge(cs ...<-chan int) <-chan int {
```
