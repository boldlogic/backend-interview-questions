# subslice большого буфера — утечка памяти

**Собес:** [[alfa go]] · ~38:49

```go
// Предположим, что мы делаем пользовательскую реализацию двоичного протокола. Сообщение может содержать по миллиону байт
// В нашем коде мы используем эти сообщения, но для аудита нам необходимо сохранять последние 1000 типов сообщений.
// Тип содержится в первых 5 байтах сообщения. Что тут может пойти не так?
package main

import "fmt"

func main() {
	consumeMessages()
}

func consumeMessages() {
	for {
		msg := receiveMessage()
		// Do something with msg
		storeMessageType(getMessageType(msg)) // Сохраняем последние 1000 типов сообщений в памяти
	}
}

func getMessageType(msg []byte) []byte {
	return msg[:5]
}

```