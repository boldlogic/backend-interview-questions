# Задача

```go
package main

/* TODO: write an application to launch the Service (with graceful shutdown).

Fatal error handling requirements:
- print error message to stderr 
- exit application with status code 1

Hint: log.Fatal prints error message and calls os.Exit(1)
*/

func main() {
  // TODO: error handling and graceful shutdown 

  q, err:=NewSendQueue()
  // TODO
  s, err:=StartService(q)
  // TODO

  sigs := make(chan os.Signal, 1)
  signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
  <-sigs

}

type Service struct{}
func StartService(*SendQueue) (*Service, error) {}
func (*Service) Stop() error {}

type SendQueue struct{}
func NewSendQueue() (*SendQueue, error) {}
func (*SendQueue) Close() error {}

```

# Вариант решения

Используется паттерн `func Main() error`

```go
func main() {
  if err := Main(); err != nil {
    log.Fatal(err)
  }
}

func Main() (err error) {
  q, err := NewSendQueue()
  if err != nil {
    return fmt.Errorf("init send queue: %s", err)
  }
  defer func() {
    if e := q.Close(); e != nil {
      err = errors.Join(err, fmt.Errorf("close send queue: %s", e))
    }
  }()

  s, err := StartService(q)
  if err != nil {
    return fmt.Errorf("start service: %s", err)
  }
  defer func() {
    if e := s.Stop(); e != nil {
      err = errors.Join(err, fmt.Errorf("stop service: %s", e))
    }
  }()

  sigs := make(chan os.Signal, 1)
  signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)
  <-sigs

  return nil
}

type Service struct{}

func StartService(*SendQueue) (*Service, error) {
  return nil, nil
}

func (*Service) Stop() error {
  return errors.New("some error")
}

type SendQueue struct{}

func NewSendQueue() (*SendQueue, error) {
  return nil, nil
}

func (*SendQueue) Close() error {
  return errors.New("some error")
}

```