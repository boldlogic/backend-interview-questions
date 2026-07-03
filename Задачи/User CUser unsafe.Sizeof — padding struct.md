1. Что будет в результате выполнения теста?

type User struct {
  Valid bool
  Id int64
  Number int32
}
type CUser struct {
  Id int64
  Number int32
  Valid bool
}
func TestSize(t *testing.T) {
  user := User{}
  cuser := CUser{}
  if unsafe.Sizeof(user) == unsafe.Sizeof(cuser) {
    t.Log("structs size are equal")
  }
}
