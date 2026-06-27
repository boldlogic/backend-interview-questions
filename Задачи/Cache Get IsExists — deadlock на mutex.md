# Cache Get → IsExists — deadlock на mutex

**Собес:** [[СимберСофт]] · ~40:43–45:07

In-memory cache: `Get` и `IsExists` — какие ошибки? **Что произойдёт при вызове `Get`?**

```go
func (c *Cache) Get(key string) string {
	c.mu.Lock()
	defer c.mu.Unlock()

	if c.IsExists(key) {
		return "value"
	}
	return "zero-value"
}


func (c *Cache) IsExists(key string) bool {
	c.mu.Lock()
	defer c.mu.Unlock()
	// Проверка
}
```

## Решение

### Что произойдёт при `Get`

**Deadlock:** `Get` держит `c.mu`, внутри вызывается `IsExists` → второй `Lock()` на том же `sync.Mutex`. Mutex в Go **не reentrant**, goroutine блокирует сама себя на `IsExists` и никогда не дойдёт до `Unlock` в `Get`.

(На собесе: «заблокируется вот здесь» — в `IsExists`, «не сможем проверить».)

### Другие замечания к сниппету

- `IsExists` **не компилируется** — нет `return` (только комментарий `// Проверка`).
- На собесе ещё обсуждали пару **get + set**; в этом фрагменте видны только `Get` и `IsExists`.

### Как переписать (как на собесе ~44:22–44:57)

1. **Убрать вызов `IsExists` из `Get`** — проверку делать под уже взятым lock, не звать другой публичный метод с lock.
2. Общую логику — в **unexported** helper **без** mutex; `Get` и `IsExists` каждый один раз `Lock`/`Unlock` и вызывают helper.

`RWMutex` на собесе не предлагали как основной fix («не очень»); вложенный lock проблему не снимает.

```go
func (c *Cache) Get(key string) string {
	c.mu.Lock()
	defer c.mu.Unlock()

	if c.exists(key) {
		return "value"
	}
	return "zero-value"
}

func (c *Cache) IsExists(key string) bool {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.exists(key)
}

// exists — только под уже взятым c.mu или из методов выше.
func (c *Cache) exists(key string) bool {
	// Проверка
	return false
}
```

**Минимальный fix только в `Get`:** убрать `c.IsExists(key)`, оставить `// проверка` inline в теле `Get` — без helper, если логика не переиспользуется.
