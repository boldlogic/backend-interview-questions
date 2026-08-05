[Вопросы для собеседования](README.md)

# ООП (Java)

Универсальная теория ООП (определения, принципы, is-a/has-a, композиция/агрегация, связывание) — в общем вопроснике банка (`20. Теория программирования`). Здесь — **как это выглядит в Java**.

+ [Инкапсуляция в Java](#Инкапсуляция-в-Java)
+ [Наследование в Java](#Наследование-в-Java)
+ [Полиморфизм в Java](#Полиморфизм-в-Java)
+ [Абстракция в Java (`abstract`)](#Абстракция-в-Java-abstract)
+ [Композиция и агрегация в Java](#Композиция-и-агрегация-в-Java)
+ [Связывание методов в Java](#Связывание-методов-в-Java)

## Инкапсуляция в Java

Модификаторы доступа (`private` / package / `protected` / `public`) задают, что снаружи видно от класса. `private` поля и методы — только внутри класса; публичный API (`call`, `ring`) — часть инкапсуляции.

```java
public class AbstractPhone {

    private int year;
    private String company;
    public AbstractPhone (int year, String company) {
        this.year = year;
        this.company = company;
    }
    private void openConnection(){
        //findComutator
        //openNewConnection...
    }
    public void call() {
        openConnection();
        System.out.println("Вызываю номер");
    }

    public void ring() {
        System.out.println("Дзынь-дзынь");
    }

}
```

Сокрытие `openConnection` позволяет менять реализацию, не ломая клиентов. Полностью закрытый класс без публичных методов бесполезен.

[к оглавлению](#ООП-Java)

## Наследование в Java

`extends`, `super`, `@Override`. Пример цепочки: беспроводной телефон → сотовый → смартфон.

```java
public abstract class WirelessPhone extends AbstractPhone {

    private int hour;

    public WirelessPhone(int year, int hour) {
        super(year);
        this.hour = hour;
    }
}
```

```java
public class CellPhone extends WirelessPhone {
    public CellPhone(int year, int hour) {
        super(year, hour);
    }

    @Override
    public void call(int outputNumber) {
        System.out.println("Вызываю номер " + outputNumber);
    }

    @Override
    public void ring(int inputNumber) {
        System.out.println("Вам звонит абонент " + inputNumber);
    }
}
```

```java
public class Smartphone extends CellPhone {

    private String operationSystem;

    public Smartphone(int year, int hour, String operationSystem) {
        super(year, hour);
        this.operationSystem = operationSystem;
    }
    
    public void install(String program){
        System.out.println("Устанавливаю " + program + "для" + operationSystem);
    }

}
```

[к оглавлению](#ООП-Java)

## Полиморфизм в Java

Вызов через ссылку базового типа; runtime выбирает реализацию потомка (`@Override`).

```java
public class User {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public void callAnotherUser(int number, AbstractPhone phone) {
        phone.call(number);
    }
}
```

```java
public class ThomasEdisonPhone extends AbstractPhone {

    public ThomasEdisonPhone(int year) {
        super(year);
    }

    @Override
    public void call(int outputNumber) {
        System.out.println("Вращайте ручку");
        System.out.println("Сообщите номер абонента, сэр");
    }

    @Override
    public void ring(int inputNumber) {
        System.out.println("Телефон звонит");
    }
}
```

```java
public class Phone extends AbstractPhone {

    public Phone(int year) {
        super(year);
    }

    @Override
    public void call(int outputNumber) {
        System.out.println("Вызываю номер" + outputNumber);
    }

    @Override
    public void ring(int inputNumber) {
        System.out.println("Телефон звонит");
    }
}
```

```java
public class VideoPhone extends AbstractPhone {

    public VideoPhone(int year) {
        super(year);
    }

    @Override
    public void call(int outputNumber) {
        System.out.println("Подключаю видеоканал для абонента " + outputNumber);
    }

    @Override
    public void ring(int inputNumber) {
        System.out.println("У вас входящий видеовызов..." + inputNumber);
    }
}
```

```java
AbstractPhone firstPhone = new ThomasEdisonPhone(1879);
AbstractPhone phone = new Phone(1984);
AbstractPhone videoPhone=new VideoPhone(2018);
User user = new User("Андрей");
user.callAnotherUser(224466,firstPhone);
user.callAnotherUser(224466,phone);
user.callAnotherUser(224466,videoPhone);
```

Один вызов `callAnotherUser` — разные реализации `call` в зависимости от фактического типа.

[к оглавлению](#ООП-Java)

## Абстракция в Java (`abstract`)

`abstract class` + `abstract` метод без тела; наследник обязан реализовать.

```java
abstract class Animal {
    public abstract void animalSound();

    public void sleep() {
        System.out.println("Zzz");
    }
}

class Pig extends Animal {
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }
}

class MyMainClass {
    public static void main(String[] args) {
        Pig myPig = new Pig();
        myPig.animalSound();
        myPig.sleep();
    }
}
```

Отдельно: keyword `interface` (контракт без состояния до default/static методов) — типичный follow-up на Java-собесе.

[к оглавлению](#ООП-Java)

## Композиция и агрегация в Java

Композиция — часть создаётся внутри владельца (`new` в конструкторе), жизненный цикл связан:

```java
class Engine {
    private final int horsepower;
    
    Engine(int horsepower) {
      this.horsepower = horsepower;
    }
}

class Car {
    private final Engine engine;
    
    Car(int horsepower) {
        this.engine = new Engine(horsepower);
    }
}
```

Агрегация — зависимость приходит снаружи (DI):

```java
class Driver {
    private final String name;
    
    Driver(String name) {
      this.name = name;
    }
}

class Car {
    private Driver driver;
    
    Car(Driver driver) {
        this.driver = driver;
    }
}
```

Ориентир: `new` внутри ≈ композиция; объект снаружи ≈ агрегация. Часто предпочтительнее DI через конструктор (тестируемость, DIP).

[к оглавлению](#ООП-Java)

## Связывание методов в Java

Общая теория early/late binding — в банке (`20`). В Java для **instance-методов** по умолчанию **позднее (динамическое)** связывание.

Исключения — **раннее** связывание, если метод:
- `final`
- `static`
- `private` (private-методы final по смыслу диспетчеризации)

`@Override` помогает компилятору проверить сигнатуру при переопределении.

[к оглавлению](#ООП-Java)

# Источники
+ [DevColibri](https://devcolibri.com/%d1%87%d1%82%d0%be-%d1%82%d0%b0%d0%ba%d0%be%d0%b5-%d0%be%d0%be%d0%bf-%d0%b8-%d1%81-%d1%87%d0%b5%d0%bc-%d0%b5%d0%b3%d0%be-%d0%b5%d0%b4%d1%8f%d1%82/)
+ [Хабрахабр](https://habrahabr.ru/post/87119/)
+ [Википедия](https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование)

[Вопросы для собеседования](README.md)
