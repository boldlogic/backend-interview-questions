# Graceful Shutdown

В сервисах на golang в секции main часто необходимо реализовать правильное завершение приложения. Это задачка про это.

```go
func main() {
    database := NewDatabaseClient()
    service := MyCoolService(database)
	httpServer := http.NewServer()
	httpServer.Register("/", svc.HandleRequest)
	httpServer.ListenAndServeNonBlocking()
    // write code for graceful shutdown
}

// MyCoolService и NewDatabaseClient реализуют интерфейс
type Closable interface {
    Close()
}
```

Основная задача в том, чтобы закрыть в верной последовательности. Если закрыть сервер позже базы данных, то можно нагенерить ошибок для клиента.

## Эталонное решение

```go
func main() {
    database := NewDatabaseClient()
    service := MyCoolService(database)
	httpServer := http.NewServer()
	httpServer.Register("/", svc.HandleRequest)
	httpServer.ListenAndServeNonBlocking()
    // ждём сигнала
    <- signal.Notify(signal.SIGINT, signal.SIGTERM)
    // закрываем входящие запросы
    httpServer.Close()  
    // завершаем обработку сервисом, потому что там могут быть background с базой
    service.Close()
    // закрываем коннект к базе
    database.Close()
}
```
