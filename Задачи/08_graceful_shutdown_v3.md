# Graceful Shutdown

В сервисах на golang в секции main часто необходимо реализовать правильное завершение приложения.

```go
package main

import (
	"log"
	"os"
	"os/signal"
	"sync"
	"syscall"

	"myproject/mydb"
	"myproject/myhttp"
	"myproject/myservice"
)

// FIXME

// database, service и httpSrv implement interface
type graceful interface {
	Close() error
}

func main() {
	// init
	database := mydb.New()                          // connect to db
	srv := myservice.New(database)                  // start business-logic service
	httpSrv := myhttp.Serve("/", srv.HandleRequest) // start http server

	grace := []graceful{database, srv, httpSrv}

	// wait for exit signal
	stopChan := make(chan os.Signal, 1)
	signal.Notify(stopChan, os.Interrupt, syscall.SIGTERM)
	<-stopChan

	// close services
	var wg sync.WaitGroup
	wg.Add(len(grace))
	for _, g := range grace {
		func(g graceful) {
			if err := g.Close(); err != nil {
				log.Printf("error closing service: %s\n", err)
			}
			wg.Done()
		}(g)
	}
}
```

Основная задача в том, чтобы закрыть в верной последовательности. Если закрыть сервер позже базы данных, то можно нагенерить ошибок для клиента.

## Вариант решения

Явно указать последовательность закрытия сервисов.

```go
package main

import (
	"log"
	"os"
	"os/signal"
	"syscall"

	"myproject/mydb"
	"myproject/myhttp"
	"myproject/myservice"
)

type graceful interface {
	Close() error
}

func main() {
	database := mydb.New()
	srv := myservice.New(database)
	httpSrv := myhttp.Serve("/", srv.HandleRequest)

	grace := []graceful{httpSrv, srv, database} // <- меняем порядок

	stopChan := make(chan os.Signal, 1)
	signal.Notify(stopChan, os.Interrupt, syscall.SIGTERM)
	<-stopChan

	for _, g := range grace {
		if err := g.Close(); err != nil { // <- закрываем последовательно
			log.Printf("error closing service: %s\n", err)
		}
	}
}
```

## Варианты развития

1. Что делать, если сервер закрывается долго, а нам уже нужно завершить приложение (например чтобы побыстрее рестартнуть контейнер) - можно добавить контекст с таймаутом (но может быть опасно, если ждем завершения каких-то неатомарных операций с базой)
```go
func main() {

	// ...

	timer := time.NewTicker(5 * time.Second)
	graceDone := make(chan struct{})
	go func() {
		var err error
		for _, g := range grace {
			err = errors.Join(err, g.Close())
		}
		if err != nil {
			fmt.Printf("Error closing services: %s\n", err)
		}
		close(graceDone)
	}()

	select {
	case <-graceDone:
		return
	case <-timer.C:
		fmt.Println("Timeout when closing services")
		return
	}
}
```
2. Eсть ли вариант ускорить закрытие? - можно построить дерево зависимостей и последовательно закрывать каждый уровень начиная с корня, при этом зависимости внутри одного уровня можно закрывать параллельно
```go
package main

import (
	"errors"
	"log"
	"os"
	"os/signal"
	"sync"
	"syscall"

	"myproject/msgq"
	"myproject/mydb"
	"myproject/mygrpc"
	"myproject/myhttp"
	"myproject/myservice"
)

type graceful interface {
	Close() error
}

type graceGroup []graceful

func (g graceGroup) Close() error {
	var wg sync.WaitGroup
	wg.Add(len(g))
	var err error
	for _, srv := range g {
		func(srv graceful) {
			if cErr := srv.Close(); cErr != nil {
				err = errors.Join(err, cErr)
			}
		}(srv)
	}
	wg.Wait()

	return err
}

func main() {
	database := mydb.New()
	broker := msgq.New()
	srv := myservice.New(database, broker)
	httpSrv := myhttp.Serve("/", srv.HandleRequest)
	grpcSrv := mygrpc.Serve(srv)

	grace := []graceful{
		graceGroup([]graceful{httpSrv, grpcSrv}),
		srv,
		graceGroup([]graceful{database, broker}),
	}

	stopChan := make(chan os.Signal, 1)
	signal.Notify(stopChan, os.Interrupt, syscall.SIGTERM)
	<-stopChan

	for _, g := range grace {
		if err := g.Close(); err != nil {
			log.Printf("error closing service: %s\n", err)
		}
	}
}
```