---
размечено: true
теория: true
лайвкодинг: false
опыт: true
---

# Lunar Rails Техничка water

- **Видео:** `Lunar Rails Техничка_water.mp4`
- **Аудио:** [Lunar Rails Техничка_water.mp3](../audio/Lunar Rails Техничка_water.mp3)
- **Длительность:** 54:43
- **Язык (детект):** ru
- **Модель:** faster-whisper / small
- **Распознано:** 2026-06-30 17:55 UTC
- **Разметка:** после реплики интервьюера — одна строка:
  - `> 📎 **База:** …` — **теория**; ссылка на `1–10.*.md`
  - `> 📎 **Задача:** …` — **практика** (live coding, SQL, code review)
  - Статусы: ✅ в банке, ⚠️ частично, ❌ нет, 🔧 упражнение

## Транскрипт

**[00:00]** Эй, мы все в?

**[00:03]** Я думаю, да.

**[00:06]** У вас там?

**[00:07]** Да.

**[00:08]** Там мы идем.

**[00:09]** Это все Alberta?

**[00:11]** Мы ждем для кого-то еще?

**[00:12]** Нет, это все.

**[00:14]** Отлично.

**[00:15]** Я просто сделаю quick introduction.

**[00:16]** Станислав, здесь у нас Alberta

**[00:19]** и Rodrigo,

**[00:21]** с 40-х годами,

**[00:23]** и Луна Рейлз.

**[00:25]** Вы будете разговаривать о software engineer role.

**[00:27]** Я буду еще в интернете, если вы нужны меня.

**[00:29]** Но мы будем разговаривать.

**[00:31]** Отлично.

**[00:32]** Спасибо.

**[00:33]** Спасибо, Станислав.

**[00:36]** Станислав, как ты?

**[00:38]** Я тоже, спасибо.

**[00:40]** Что с тобой?

**[00:41]** Хорошо.

**[00:42]** Ну, в первую очередь,

**[00:44]** у нас есть AI note taker.

**[00:46]** Мы с Патом, но это

**[00:48]** рекомендует звонить,

**[00:50]** и это

**[00:51]** это сделает нотки.

**[00:53]** Я надеюсь, что ты не умеешь.

**[00:56]** Так,

**[00:58]** Let me introduce ourselves.

**[01:00]** My name is Alberto.

**[01:02]** I'm CTO at

**[01:04]** Lunar Rails.

**[01:06]** Here with me

**[01:08]** I have Rodrigo,

**[01:09]** who is a senior developer

**[01:12]** at Clover Labs.

**[01:14]** I'll explain a bit more later,
> 📎 **База:** ✅ [[6. БД#EXPLAIN и EXPLAIN ANALYZE]]

**[01:16]** but Clover Labs

**[01:18]** is a group

**[01:22]** within Lunar Rails,

**[01:23]** because Lunar Rails

**[01:25]** Это группа компаний, в которых мы делаем много криптовалитных вещей.

**[01:32]** У нас есть оттенцовая платформа,

**[01:35]** и оттенцовая платформа,

**[01:36]** пеймэндпроцессы,

**[01:39]** в Биткоин, Lightning, Ethereum.

**[01:43]** У нас есть много сервисов,

**[01:48]** которые мы дали криптовалитам,

**[01:51]** и, более специально, в Биткоин.

**[01:53]** Мы как бы в биткоинсантрике компаниях, но не только в Биткоинсантрике.

**[01:57]** Так что, и эта роль

**[02:02]** — это для Луна рейсов, как бы все.

**[02:08]** Специально мы ищем кто-то,

**[02:11]** чтобы помогать на платформах,

**[02:15]** оттенцовых платформах.

**[02:16]** Мы просто построили маленькую версию,

**[02:21]** и мы будем добавить больше футов.

**[02:24]** Так что, это такая роль, что мы ищем.

**[02:28]** Открываем.

**[02:32]** Классно.

**[02:34]** Про интервью.

**[02:37]** Если ты не хочешь, то начнём с тебя,

**[02:40]** дать нам интервью про себя,

**[02:42]** ваша релеванная история,

**[02:44]** что-то, что ты считаешь релеванной,

**[02:46]** то мы сделаем полчаса,

**[02:50]** У нас есть много технических вопросов, о программе в целом,

**[02:56]** или о рандомтехнических вещах.

**[03:01]** В конце интервью, у вас есть время, чтобы спросить вопросы,

**[03:07]** о том, что вы хотите узнать о нас или о компании.

**[03:11]** Да, это выглядит хорошо.

**[03:14]** Итак, если у вас нет смысла начать с вашей собственной интервью,

**[03:20]** 巿рад!

**[03:21]** Да, точно.

**[03:22]** Я Станислав.

**[03:23]** Я профессиональный инженер с Fukushima,

**[03:27]** в domu принципов,

**[03:29]** по-моему, производительных амбекантов,

**[03:30]** социальных relax and fixation systems.

**[03:32]** У меня есть erosion roles,

**[03:34]** где я работал на Fintech,

**[03:36]** и фильмоспортажных ​​прочтี้ и все это ее.

**[03:37]** У меня есть демо-процессор,

**[03:39]** с Mitcheon, Pequod, Ethereum,

**[03:41]** и Mochira, сейчас, например.

**[03:44]** Я был в Кутера вершиной 5 первых лет,

**[03:48]** 5 года, а translate.

**[03:50]** about about the centralize systems.

**[03:52]** Since then I've been passionate about applying that technology to

**[03:58]** will financially use cases.

**[04:00]** I'm particularly interested in mechanics
> 📎 **База:** ✅ [[7. HTTP, сети#REST principles / gRPC vs HTTP?]]

**[04:04]** ability and clean architecture.

**[04:06]** So, for example, the OTC training platform, they're developing really

**[04:10]** lines with my background and interests.

**[04:12]** Oh, you're muted.

**[04:16]** Yeah.

**[04:20]** Или вы слышите меня?

**[04:22]** Да.

**[04:23]** Окей.

**[04:24]** У меня иногда Google Meet hides the mic buttons,

**[04:27]** так что я не знаю, если вы меня заметили.

**[04:29]** В любом случае, я не хочу сказать,

**[04:32]** потому что у меня есть your CV

**[04:33]** передо мной.

**[04:34]** Вы начали

**[04:36]** в Глобо,

**[04:38]** а потом в Атлассиан,

**[04:40]** так что ничего не выживали.

**[04:42]** И тогда, то есть,

**[04:44]** вы начали работать в Глобо.

**[04:46]** Это потому, что это

**[04:48]** это тест для вас,

**[04:50]** или просто вы соединили компания

**[04:52]** и вы разработали интерс afterwards.

**[04:54]** Вы хотите

**[04:55]** жить в Кутуспейске

**[04:56]** для любых,

**[04:57]** или

**[04:58]** что-то

**[04:59]** это ситуация?

**[05:01]** Да.

**[05:02]** Я начал

**[05:03]** как личный интерес.

**[05:04]** А теперь,

**[05:05]** прежде чем,

**[05:06]** в Биткоин,

**[05:07]** в блокчейне,

**[05:08]** я не знал,

**[05:09]** что я делаю,

**[05:10]** прежде чем,

**[05:11]** прежде чем,

**[05:12]** прежде чем,

**[05:13]** прежде чем,

**[05:14]** прежде чем,

**[05:15]** прежде чем,

**[05:16]** прежде чем,

**[05:17]** прежде чем,

**[05:18]** прежде чем,

**[05:19]** прежде чем,

**[05:20]** прежде чем,

**[05:21]** прежде чем,

**[05:22]** прежде чем,

**[05:23]** прежде чем,

**[05:24]** прежде чем,

**[05:25]** прежде чем,

**[05:26]** прежде чем,

**[05:27]** прежде чем,

**[05:28]** прежде чем,

**[05:29]** прежде чем,

**[05:30]** прежде чем,

**[05:31]** прежде чем,

**[05:32]** прежде чем,

**[05:33]** прежде чем,

**[05:34]** прежде чем,

**[05:35]** прежде чем,

**[05:36]** прежде чем,

**[05:37]** прежде чем,

**[05:38]** прежде чем,

**[05:39]** прежде чем,

**[05:40]** прежде чем,

**[05:41]** прежде чем,

**[05:44]** прежде чем,

**[05:45]** прежде чем,

**[05:46]** прежде чем,

**[05:47]** прежде чем,

**[05:48]** Голланд депт, как все твои задачи об Голланд.

**[05:53]** У нас есть некоторые предыдущие Голланд, но мы тоже имеем некоторые, которые вывозят в Node.js TypeScript.

**[06:01]** Вы хотите продолжить голланд рут, или у вас есть проблемы с пандемией ваших видов,

**[06:12]** и больше участвовать в множественном языке, а в то же время, как и ваша предыдущая голланд?

**[06:20]** Да, я больше участвовал в Голланде, в которой я построил большие системы,

**[06:25]** но я больше комфортно работаю с TypeScript, в Куре и в Аддат-Лассинх,

**[06:30]** например, я коллаборировал с командами, используя TypeScript,

**[06:33]** где я работаю в бак-энд-сервисах, так что, да, нет проблем.

**[06:38]** Окей, круто.

**[06:45]** Да, я не знаю, если я burdened с тебя.

**[06:47]** Не так ли есть что-то, что ты хочешь сказать о вашей карьере или study?

**[06:54]** Угу, что-то интересное.

**[06:56]** Я могу добавить интересное информацию о моих проектах, если вы хотите.

**[07:08]** Да, не так.

**[07:09]** Да, конечно, скуп comet?

**[07:12]** У тебя может быть что-то, что ты пацаны проекта, что вы разработали,

**[07:18]** или что-то, что вы можете, что вы любите, что вы любите,

**[07:22]** вы можете, как вы думаете, это всё.

**[07:24]** Ну, конечно, не проблема.

**[07:27]** Я думаю, что один из самых интересных проектов,

**[07:29]** которые я работал в листочке,

**[07:31]** это Smart Routing Engine,

**[07:33]** в Веркурии.

**[07:34]** Это у нас есть сервис, который

**[07:36]** соединяет с другими ликвиатурными

**[07:38]** сцеплями,

**[07:39]** анализирует их рейт,

**[07:42]** пизм,

**[07:43]** физическая структура,

**[07:44]** и автоматически выбирает

**[07:46]** наиболее эффективный раунд для каждого рейда.

**[07:49]** И мы использовали ассакрона-спроцесса,

**[07:52]** с кашей с рейдерами,

**[07:53]** чтобы выхватить субсекундные решетные времена,

**[07:57]** которые улучшивали уникальные конверсии

**[07:59]** по примерно 8-10%.

**[08:03]** Это очень эффективный проект для нашей компании.

**[08:07]** Например, еще один проект, который я очень понравился,

**[08:09]** был с Лопольщиной в адаптере сервис.

**[08:12]** Мы построили универсальные интерпры

**[08:14]** с обеими не-эпиамами,

**[08:16]** сfalse-саттендорами,

**[08:18]** с цифровым объектом.

**[08:19]** История для криптически,

**[08:21]** мы выбрали 2-3-4 дня.

**[08:24]** У нас и обеих проектов

**[08:27]** очень трудно.

**[08:28]** И о том, что мы об дизайне,

**[08:31]** визуально-безыльной

**[08:32]** выступлению системы,

**[08:34]** и то, что было интересно.

**[08:41]** Спасибо.

**[08:42]** Подписаны на эти вопросы,

**[08:44]** Or maybe we can move on to the technical part of the interview?

**[08:50]** Yeah, let's move on.

**[08:53]** Okay, so I'm gonna just ask a bunch of random questions about programming, right?

**[09:00]** Some of them you might find too easy, or some of them will be hard,

**[09:03]** some of them are very specific, or others are open a bit,

**[09:06]** but it's just to have a conversation about programming, right?

**[09:09]** Okay.

**[09:10]** So, first one.

**[09:14]** How would you define the difference between a process and always process and a thread?

**[09:27]** You mean the difference between process and thread, yes?

**[09:31]** Yeah, like a process as in a Linux process and a thread that you can find in any programming language

**[09:41]** or application.

**[09:44]** Yeah, I think a process is like an independent unit of execution that has its own resources,

**[09:52]** for example memory space, file descriptors, system resources.

**[09:58]** And each process runs in isolation from others using virtual memory.

**[10:04]** So communication between processes requires mechanisms like IPC,

**[10:10]** circuits, signals, sharing memory, it's something like that.

**[10:14]** If we talk about thread, a thread is a smaller unit of execution within a process.

**[10:22]** And to multiple threads share the same memory and resources of a parent process,

**[10:27]** which makes context switching faster and communication easier.

**[10:31]** But, of course, we have some challenging moments with currency issues,

**[10:38]** race conditions, something like that.
> 📎 **База:** ✅ [[1. GO - Часто#Что такое дедлок и рейс кондишион, и `-race`]]

**[10:41]** Cool.

**[10:43]** Speaking about these race conditions, how would you solve these kind of situations?

**[10:52]** In general, race conditions happen to multiple threads,

**[10:58]** or, if we talk about Golung, for example, guardians, access shared data,

**[11:04]** we need to use some synchronization primitives like Utexs, or AirWim Utexs,

**[11:11]** or Atomics, etc.
> 📎 **База:** ✅ [[2. GO - Средне#`atomic` vs mutex]]

**[11:14]** If we talk about Golung, we can use channel-based communication,

**[11:20]** just use to synchronize guardians and pass data safely.

**[11:25]** And, yeah, something like that.

**[11:28]** Atomic operations, immutable data on copies.

**[11:33]** How would you debug?

**[11:36]** What is your process for debugging if you find, for example, a race condition?

**[11:44]** Yeah, that's a good question.

**[11:46]** I think when debugging, I started with reproducing this problem.

**[11:56]** So, first of all, I just tried to produce the issue in a controlled environment.

**[12:05]** Ideally, maybe with the same input or conditions that triggered it.

**[12:11]** Of course, I would check logs and metrics,

**[12:16]** using Prometheus, Rufana, just to check some anomalies.

**[12:25]** What else? I can add some targeted instrumentation.

**[12:33]** If logs aren't enough, I can add temporary debug logs, metrics,

**[12:40]** around suspicious areas.

**[12:42]** And, of course, if we talk about Golung, I can use some instruments

**[12:47]** for profiling, like Beprof, or trace,

**[12:51]** for debugging instruments.

**[12:53]** And I can use Golung Flags, like RACE,

**[12:59]** to detect conditions in runtime.

**[13:03]** So, something like that.

**[13:10]** Still speaking about concurrency,

**[13:13]** what's the difference between synchronous and asynchronous execution?

**[13:20]** How would you define asynchronous execution?

**[13:26]** Synchronous execution means tasks run one after another.

**[13:33]** Each operation must complete before the next one starts.

**[13:37]** And, on the other hand, synchronous execution means tasks

**[13:41]** can run independently or in a parallel.

**[13:43]** The caller doesn't wait for the completion,

**[13:46]** and the call can continue doing other work.

**[13:49]** Да, это хорошая définition, я думаю.

**[14:02]** Что в программе, что в мутабилитете?

**[14:06]** И как это помогает?

**[14:12]** Как это помогает в конкуренции?

**[14:18]** Мутабилитет means that once a data structure is created,

**[14:23]** its state can be changed,

**[14:26]** and in concurrent programming,

**[14:31]** imutability helps because multiple threads

**[14:34]** or garages can simply read the same data without transition,

**[14:38]** and they cannot modify it,

**[14:42]** and then it can only read it,

**[14:44]** and there is no risk of risk conditions

**[14:46]** since the data never changes.

**[14:48]** Да.

**[14:53]** Ок,

**[14:57]** Maybe moving on to a different topic.

**[15:03]** Что...

**[15:05]** ...

**[15:07]** ...

**[15:09]** ...

**[15:11]** ...

**[15:14]** ...

**[15:19]** Так что дейтабейсиндексы, то есть дейтастоктуры, которые improvement the speed of data retrieval operations on a table.

**[15:28]** И они работают как оптимизм лукап-табель.

**[15:32]** Так что, вместо каждой станики, дейтабейсиндексы можно quickly locate the needed records using the index structure.

**[15:42]** И ты обычно используешь индексы и колонны, которые часто используют в конструкциях, such as queer, join, over-the-buy, closes, to speed up queries.
> 📎 **База:** ✅ [[6. БД#Виды JOIN запросов: INNER vs LEFT]]

**[15:55]** Но также у нас есть конс, such as indexes come with trade-offs, they consume extra storage and slow down write operations.

**[16:05]** И если мы поставим индексы на все станики, то мы можем slowing down our operations.

**[16:14]** Потому что индекс must always be updated.

**[16:20]** Да, перфект.

**[16:23]** И о тесте.

**[16:28]** Что-то другое между индексами и индексами?

**[16:33]** Что это за статистик?

**[16:35]** Для того, чтобы решить, что нужно индексами или индексами тестов, чтобы тестить эту пунктуру?

**[16:42]** Интест в реферсе сингл, isolated, piece of logic, usually function, for example, or a method without external dependencies, like databases.

**[16:54]** Интервейсиндексы чекают, как multiple components work together.

**[16:58]** Например, в тесте на сервисе, это интервейс, database, message broker, external API.

**[17:05]** Так что, обычно моя стратегия для использования тестов для корпуса logic,

**[17:11]** какие-то алгоритмы, эффективные функции,

**[17:15]** и использовать интервейсиндес для критиковых баундров, как databases, squares,

**[17:21]** API and points, message processing.

**[17:24]** И также мы, конечно, можем Combine both,

**[17:27]** для индексов для логика, крики, интервейсиндес для системы, для реабилити.

**[17:33]** Ты уже говорил о том, что,

**[17:43]** если системы в производстве станут слегка?

**[17:52]** В производстве.

**[17:55]** Если системы в производстве станут всегда старые,

**[18:01]** ophyт maritime,

**[18:05]** мы может наCommin,

**[18:08]** мы должны прямо наthen.

**[18:12]** Мы, конечно, все, что мы говорили,

**[18:15]** мы не будем разобраться,

**[18:18]** но нам нужно обновлять,

**[18:20]** мы не будем опекать,

**[18:22]** чтобы identifier,

**[18:25]** Проблемы, лодонекс, логов и трейсов используют OpenTelemetry, например.

**[18:35]** Также можно использовать профильный аплодисмент,

**[18:42]** используя пипрофин-гол, например,

**[18:44]** или я могу профильный database, например,

**[18:48]** используя explainanalyze, например.

**[18:51]** Так, да.

**[18:55]** Да, может быть, мы можем идти дальше к крипто-возвращения.

**[19:04]** Давайте начнем с теоретических вопросов.

**[19:07]** Что-то другое между encoding и encryption?

**[19:15]** Так, encoding — это часть конвертирования,

**[19:18]** данные в различных моментах,

**[19:20]** так как это может быть, например,

**[19:21]** сейфовый транспорт.

**[19:23]** Например, 8.0, да.

**[19:26]** И это не для безопасности.

**[19:29]** Так, encryption — это часть конвертирования,

**[19:32]** используя крипто-возвращение.

**[19:35]** Крипто-возвращение — это часть конвертирования.

**[19:37]** И это часть конвертирования.

**[19:38]** Так, чтобы только формия,

**[19:40]** или часть конвертирования,

**[19:41]** смогли выиграть это.

**[19:42]** И это стратегизм,

**[19:45]** что, уверенно, это безопасность.

**[19:49]** Ок, и Speaking of encryption —

**[19:52]** что-то...

**[19:54]** Я mean, there is many algorithms for encryption,

**[19:59]** but they all belong to two different groups.

**[20:03]** Can you...

**[20:05]** Does it come to your mind,

**[20:06]** what these two groups are?

**[20:09]** Two groups for encryption,

**[20:11]** I think even symmetric encryption.

**[20:16]** Да, that's what I mean.

**[20:18]** Can you briefly explain the difference?

**[20:22]** Sure.

**[20:24]** Symmetric encryption uses the same key,

**[20:29]** for the encryption.

**[20:30]** Symmetric encryption uses public and private key,

**[20:33]** but here public key encrypts,

**[20:35]** and only the private key encrypts.

**[20:38]** Да, perfect.

**[20:39]** How about hashing?

**[20:41]** What's hashing?

**[20:43]** Does it relate to encryption in any way?

**[20:48]** Да, I think hashing is one-way process,

**[20:52]** that we would set it into fixed-length string,

**[20:54]** and hold a hazard digest.

**[20:57]** And, unlike encryption,

**[20:59]** it cannot be reversed to get the original data.

**[21:05]** So it's mainly used for data integrity verification,

**[21:08]** or password storage,

**[21:10]** which is it?

**[21:11]** Да, exactly.

**[21:17]** Может, давайте поговорим о блокчейнах.

**[21:25]** Что...

**[21:27]** Что...

**[21:29]** Опять-таки, это два большие типы блокчейнах.

**[21:33]** Вы знаете, что это?

**[21:35]** В том числе трансляция.

**[21:38]** Как вы классифируете блокчейнах,

**[21:41]** в двух больших группах?

**[21:46]** Вы имеете в виду трансляцию,

**[21:48]** а не аккаунт,

**[21:50]** это это?

**[21:52]** Да, это то, что я имею в виду.

**[21:54]** Так,

**[21:56]** трансляция в виду в биткои.

**[22:00]** В принципе, трансляция,

**[22:02]** как вы видите,

**[22:04]** предыдущие выхода и в ватке.

**[22:06]** В мега-моде используется

**[22:07]** в течение всего

**[22:09]** глобальных ванных,

**[22:11]** и обрадует,

**[22:12]** как вы видите,

**[22:13]** в каждой трансляции.

**[22:15]** Да.

**[22:19]** И, как вы поняли, что у вас есть бит-клин-аддресс, как это будет?

**[22:37]** Бит-клин-аддресс.

**[22:38]** Бит-клин-аддресс — это уникальный идентифайер, который

**[22:41]** приводит от публики, которые represent a destination for return transactions.

**[22:46]** И это, в основном, есть и hashed version of the public key, encoded in formats like base50hx

**[22:59]** or bench32, error detection and readability.

**[23:06]** Да, хорошо.

**[23:10]** Ради, может быть, мы можем перейти на какие-то голландские вопросы?

**[23:14]** Что ты думаешь?

**[23:15]** Да, конечно.

**[23:17]** Ну, давайте посмотрим, потому что мы уже говорили о них.

**[23:24]** Как у них голландская память?

**[23:29]** Есть два разных части, как heap and stack.

**[23:36]** Голландская память автоматически используется в коллекте.

**[23:42]** И это обладает память на heap.

**[23:44]** Для динамичных объектов, как мы используем это,

**[23:47]** и эти объекты не могут быть приятными.

**[23:50]** И габридж коллекторный голландский картридер,

**[23:54]** он не знает, что здесь.

**[23:56]** Он встанет на протяжении программы.

**[24:01]** Окей.

**[24:02]** И ты знаешь, что отличие между слайдом и рейдом в Голланде?

**[24:09]** Рейдом — это фиксирование.

**[24:13]** Это фиксирование, которое можно найти в полном времени.

**[24:16]** И это динамичная часть.

**[24:19]** Но слайдом — это светлая область,

**[24:22]** как у рейдов.

**[24:23]** Как у них есть пункт,

**[24:24]** как у рейдов,

**[24:25]** как у ленга,

**[24:26]** как у кокосов.

**[24:28]** Слайдом — динамичный слайд.

**[24:30]** И они могут выживаться или сжигаться.

**[24:33]** Отлично.

**[24:34]** И ты можешь мне сказать о интерфейсах?

**[24:37]** Как они используют и компонент?

**[24:43]** Да.

**[24:44]** Конечно.

**[24:45]** Интерфейсов

**[24:46]** redefined a set of methods signatures

**[24:50]** that a type must implement.

**[24:53]** For example, raising standards.

**[24:56]** But signatures that a type must implement

**[24:59]** without specifying how those methods are implemented.

**[25:03]** Of course.

**[25:04]** And it provides a way to achieve

**[25:08]** polymorphism

**[25:09]** and decoupling between components.

**[25:12]** A type implicitly implements an interface

**[25:14]** to define all these methods

**[25:16]** and there is no need for explicit declarations.

**[25:18]** Okay.

**[25:20]** So anyone,

**[25:22]** as long as he feels the interface,

**[25:24]** can be used.

**[25:26]** Any type.

**[25:30]** You mean exactly...

**[25:34]** So you don't have to infer it from anything.

**[25:37]** You just use it,

**[25:39]** as long as you implement the interface.

**[25:42]** Yeah.

**[25:47]** So Go doesn't use inheritance

**[25:50]** and it provides some composition

**[25:52]** and implicit implementation.

**[25:54]** As long as a type

**[25:57]** provides the methods defined by an interface,

**[25:59]** it doesn't really satisfy that interface.

**[26:02]** That's something like that.

**[26:04]** Cool.

**[26:05]** And can you tell me about

**[26:08]** the concept of zero values in Conan?

**[26:12]** Yeah.

**[26:14]** Zero values

**[26:16]** by default

**[26:19]** variables has a zero value

**[26:21]** and it's the value

**[26:23]** a variable holds

**[26:25]** when declared

**[26:27]** but not explicitly in choice.

**[26:29]** So zero value depends on the type.

**[26:32]** Of course.

**[26:33]** So the number of types has zero,

**[26:35]** Boolean has a false string,

**[26:37]** has a pointer,

**[26:39]** has a new.

**[26:42]** Cool.

**[26:44]** Can you tell me a bit about

**[26:47]** buffered and unbuffered channels?

**[26:50]** What's the difference there?

**[26:53]** So buffered channels

**[26:56]** have a defined capacity,

**[27:00]** have some buffer in this structure,

**[27:03]** so a sender can send up

**[27:05]** that number of values without blocking.

**[27:07]** And the send blocks

**[27:09]** only when the buffer is full

**[27:11]** and receive blocks only when it's empty.

**[27:14]** And for that kind,

**[27:16]** unbuffered channels have no capacity.

**[27:18]** So send operation blocks

**[27:20]** until another grouting resists

**[27:22]** on the channel and vice versa.

**[27:26]** Good.

**[27:28]** And lastly,

**[27:30]** what is the first statement used for?

**[27:33]** The first statement

**[27:35]** is useful

**[27:37]** just to

**[27:39]** Sorry, I mean select or defer.
> 📎 **База:** ✅ [[1. GO - Часто#Зачем нужен select]]

**[27:43]** Differ.

**[27:45]** This construction is useful

**[27:47]** to schedule a function call

**[27:49]** to run after the

**[27:51]** surrounding function completes

**[27:53]** regardless of how it exits.

**[27:55]** So it's commonly used

**[27:57]** for cleanup tasks

**[27:59]** like closing files,

**[28:01]** locking indexes, releasing sources

**[28:03]** something like that.

**[28:05]** And deferred calls executed

**[28:07]** in leaf over.

**[28:09]** Okay.

**[28:11]** Cool, cool.

**[28:13]** Yep.

**[28:15]** That's it from my side.

**[28:17]** Okay.

**[28:19]** Let's move to some more general

**[28:21]** questions about

**[28:23]** work.

**[28:25]** So, I mean

**[28:27]** as developers

**[28:29]** it's very common to have

**[28:31]** technical disagreements

**[28:33]** with your teammates, you know,

**[28:35]** for the quest discussions.

**[28:37]** Can you remember

**[28:39]** one specific example of a difficult one

**[28:41]** that we will approach

**[28:43]** solving it?

**[28:45]** Yep.

**[28:47]** That's a good question.

**[28:52]** I can share one example

**[28:54]** at last.

**[28:56]** For example, during the development of

**[28:58]** some tasks,

**[29:00]** we had a disagreement about

**[29:02]** whether to use Kafka or Rabbit
> 📎 **База:** ✅ [[8. Интеграции#Kafka / RabbitMQ?]]

**[29:04]** MQ.

**[29:06]** It was a more architectural

**[29:08]** specific problem

**[29:10]** for the vectorization pipeline

**[29:12]** and some teammates preferred

**[29:14]** Rabbit for its simplicity

**[29:16]** where I advocated

**[29:18]** for Kafka due to it

**[29:20]** its higher output

**[29:22]** and better scalability

**[29:24]** for our asynchronous processing needs

**[29:26]** and

**[29:28]** I remember that I

**[29:30]** approached it by organizing

**[29:32]** a short technical discussion where we

**[29:34]** compared both options using real metrics

**[29:36]** like message,

**[29:38]** volume, latency, operational complexity

**[29:40]** and

**[29:42]** I also

**[29:44]** prepared a small benchmark to demonstrate Kafka's

**[29:46]** performance under our expected load

**[29:48]** and after

**[29:50]** reviewing the data together

**[29:52]** the team agreed that Kafka was a better fit

**[29:54]** for our use case and this experience

**[29:56]** just reinforced me

**[29:58]** for me that the best way

**[30:00]** to resolve technical disagreements

**[30:02]** is through

**[30:04]** data-driven discussion.

**[30:06]** Some respectful,

**[30:08]** of course, communication, collaborative

**[30:10]** decision-making

**[30:12]** something like that.

**[30:14]** Yeah, totally agree.

**[30:16]** It's sometimes hard to

**[30:18]** some developers

**[30:20]** myself include, we get attached

**[30:22]** to some technology

**[30:24]** right?

**[30:26]** Is there any instance

**[30:28]** when you

**[30:30]** felt this yourself

**[30:32]** like I'd like to use this technique because

**[30:34]** I use it because whatever reason

**[30:36]** I really love with it

**[30:38]** but then you had to give up and say

**[30:40]** okay, this is not what the team wants.

**[30:47]** So yeah, that was the question.

**[30:49]** Yeah, if there's any instance

**[30:51]** when

**[30:53]** this happened that you

**[30:55]** were pushing for a particular technology

**[30:57]** or whatever because you liked it

**[30:59]** for whatever reason and then the team decided to go

**[31:01]** in some other direction

**[31:06]** Yeah, that actually

**[31:12]** happened at Mercurio maybe

**[31:14]** I initially

**[31:16]** wanted to use JPC for internal service communication

**[31:18]** our payment acquisition system

**[31:20]** because I really

**[31:22]** liked the performance and the

**[31:24]** typing.

**[31:26]** However, some of our important genes

**[31:28]** are external integrations

**[31:30]** for like heavily on REST APIs

**[31:32]** and introducing JPC everywhere

**[31:34]** would have like

**[31:36]** complicated interoperability

**[31:38]** so down delivery

**[31:40]** and after discussion

**[31:42]** with the team, we decided to keep

**[31:44]** REST for internal

**[31:46]** and cross-team communication

**[31:48]** and use JPC only for internal

**[31:50]** hyper-com services where it makes sense

**[31:52]** so yeah.

**[31:56]** Okay, cool.

**[32:00]** So this is, well, you're already used

**[32:02]** to working remotely

**[32:06]** you know, there's

**[32:08]** a bit of a challenge with communication

**[32:10]** sometimes, different time zones

**[32:12]** lots of writing

**[32:14]** Is there any

**[32:16]** any good practice

**[32:18]** anything

**[32:20]** you have in mind to make

**[32:22]** these communications smooth?

**[32:26]** Yeah

**[32:28]** I think

**[32:30]** from my experience working in

**[32:34]** distributed teams across multiple time zones

**[32:38]** I think the team

**[32:44]** need to use some clear write communication

**[32:46]** so I also

**[32:48]** I always try to write

**[32:50]** consistent structure messages

**[32:52]** for example, it's lack or documentation

**[32:54]** so others can easily

**[32:56]** follow-ups as accordingly

**[32:58]** of course

**[33:00]** I think it's best

**[33:02]** practice to use regular

**[33:04]** icing updates

**[33:06]** just using short daily weekly updates

**[33:08]** shared channels helped

**[33:10]** that can help everyone stay

**[33:12]** aligned about

**[33:14]** constant meetings

**[33:16]** what else

**[33:18]** maybe some over communication

**[33:20]** on context

**[33:22]** for example, opening PRs

**[33:24]** or technical discussions

**[33:26]** I include

**[33:28]** for example, reasoning, trade-offs

**[33:30]** examples of teammates can review effectively

**[33:32]** even when I'm on the head

**[33:34]** and

**[33:36]** of course we need to respect time zones

**[33:38]** so of course

**[33:40]** I plan meetings only when

**[33:42]** there exists and record

**[33:44]** important sessions for those

**[33:46]** who can join

**[33:48]** yeah, that sounds great

**[33:52]** I think this is something

**[33:54]** we all try to apply

**[33:56]** we don't have

**[33:58]** many different time zones

**[34:00]** we are concentrated

**[34:02]** in the

**[34:04]** Europe, Dubai

**[34:06]** time zones

**[34:08]** but yeah

**[34:10]** of course

**[34:12]** a lot of asynchronous and written communication

**[34:14]** so yeah

**[34:16]** we have to be very mindful of all that

**[34:22]** how about

**[34:24]** requirements

**[34:26]** some projects are different

**[34:28]** from others but sometimes it's inevitable

**[34:30]** that you start doing something

**[34:32]** and

**[34:34]** requirements change

**[34:36]** while you are in the middle

**[34:38]** or even when you are done with it

**[34:40]** is there anything

**[34:42]** you do

**[34:44]** to avoid change

**[34:46]** or when change is inevitable

**[34:48]** I mean not to avoid change

**[34:50]** but to avoid waste

**[34:52]** and when change is inevitable

**[34:54]** how do you deal with it

**[35:01]** usually

**[35:03]** I handle

**[35:05]** changing requirements

**[35:11]** just use

**[35:13]** maybe early alignment

**[35:15]** with small iterations

**[35:17]** just to try to clarify

**[35:19]** requirements early

**[35:21]** and deliver in smaller milestones

**[35:23]** or featured flags

**[35:25]** I think this way

**[35:27]** if priority is

**[35:29]** shipped

**[35:31]** adjustments are cheaper and faster

**[35:33]** also

**[35:35]** I expect close cooperation

**[35:37]** with product, I keep

**[35:39]** for example regular communication

**[35:41]** with product managers to understand the reasoning

**[35:43]** behind changes and adapt technical scope accordingly

**[35:49]** what about technical side

**[35:51]** I try to

**[35:53]** design services and companies

**[35:55]** to be loosely coupled

**[35:57]** so changes in one area

**[35:59]** don't require large refactors

**[36:01]** elsewhere

**[36:03]** of course I try to

**[36:05]** document assumptions and decisions

**[36:07]** and tickets of PRs

**[36:09]** so when requirements change

**[36:11]** it's clear what needs to be

**[36:13]** revisited

**[36:18]** sounds good

**[36:20]** yeah all of that

**[36:22]** sounds reasonable

**[36:24]** especially I think the part about

**[36:26]** doing stuff in small increments

**[36:28]** and showing it

**[36:30]** what helps avoid waste the most

**[36:39]** just a couple more

**[36:41]** I mean

**[36:43]** it's about your progress

**[36:47]** we do mostly back-end stuff

**[36:51]** some of our clients

**[36:53]** interweb through APIs

**[36:55]** but we also have a few frontends

**[36:57]** for back-offices

**[36:59]** we don't do a lot of front-end work

**[37:01]** but do you feel comfortable

**[37:03]** doing front-end work

**[37:05]** like

**[37:07]** so that is not public facing

**[37:09]** so it doesn't have to be the perfect UX

**[37:11]** or it's just

**[37:13]** changing slightly

**[37:15]** adding a small part of the screen

**[37:17]** to add a new feature

**[37:19]** have you ever done it

**[37:21]** do you feel comfortable

**[37:23]** yes

**[37:25]** I'm comfortable

**[37:27]** I'm comfortable working with

**[37:29]** front-end code when needed

**[37:31]** because

**[37:33]** in class and mercury I occasionally

**[37:35]** contributed internal dashboards

**[37:37]** and panels

**[37:39]** so the other tools

**[37:41]** mostly small UI adjustments

**[37:43]** so

**[37:45]** in my experience

**[37:47]** I've cooperated closely with front-end teams

**[37:49]** so using type script and tracks

**[37:51]** so I think that will be no problem

**[37:53]** okay

**[37:55]** I must say because

**[37:57]** we don't have a very big team

**[37:59]** we have a few

**[38:01]** some front-end specialists

**[38:03]** but we try to avoid silos as well

**[38:05]** because

**[38:07]** sometimes

**[38:09]** that makes sense

**[38:11]** but most of the times

**[38:13]** it doesn't

**[38:15]** again we don't do a lot of front-end work

**[38:17]** it's mostly back-end

**[38:19]** but when we do it's nice

**[38:21]** if the person can do

**[38:23]** some front-end work

**[38:25]** and finally

**[38:28]** about the

**[38:30]** so

**[38:32]** as I mentioned earlier

**[38:34]** our projects

**[38:36]** are written in

**[38:38]** mostly they are Golan

**[38:40]** or TypeScript

**[38:42]** we have a bit of a .NET

**[38:44]** as well we have a bit of Python

**[38:46]** but it's mostly Golan and TypeScript

**[38:52]** so

**[38:54]** this

**[38:56]** the most immediate need we have

**[38:58]** is for

**[39:00]** is to help in the

**[39:02]** let me give you a bit more context

**[39:04]** we have some products that are

**[39:06]** quite mature

**[39:08]** for example we have a Lightning Painting Processor

**[39:12]** in which Rodrigo

**[39:14]** works most of his time

**[39:16]** so this is mature, this is being used

**[39:18]** so we are very conscious about not breaking it

**[39:20]** monitoring performance

**[39:22]** that kind of thing

**[39:24]** so it has

**[39:26]** some sort of

**[39:28]** complexity already

**[39:30]** introduced

**[39:32]** cues

**[39:34]** here and there to make it faster

**[39:36]** whatever

**[39:38]** on the other hand we have

**[39:40]** for example the OTC trading

**[39:42]** OTC trading

**[39:44]** is very low frequency

**[39:46]** you know what OTC is

**[39:48]** it's low frequency but high volume

**[39:50]** so they started

**[39:52]** with a very manual process

**[39:54]** even putting stuff in spreadsheets

**[39:56]** something like that

**[39:58]** they started

**[40:00]** building the platform to automate

**[40:02]** but this is in a very early stage

**[40:04]** and

**[40:06]** we approach projects

**[40:08]** we start simple

**[40:10]** we see

**[40:12]** if the project is used, where the bottlenecks are

**[40:14]** and then we optimize

**[40:16]** so our trading platform at the moment is very simple

**[40:18]** it's just a Node.js app

**[40:20]** with a database

**[40:22]** with some liquidity providers etc

**[40:24]** but this is

**[40:26]** for now this is the TypeScript

**[40:28]** this is a TypeScript project

**[40:30]** and again

**[40:32]** it's simple

**[40:34]** it will probably

**[40:36]** evolve into something bigger

**[40:38]** but

**[40:40]** our

**[40:42]** most interesting stuff

**[40:44]** at the moment is the Lightning Processor

**[40:48]** anyway

**[40:50]** what I'm going to

**[40:52]** If I gave you these two

**[40:54]** which one would you prefer to work on?

**[41:01]** Yes

**[41:03]** I'm very interested in working on

**[41:05]** OTC trading platform

**[41:07]** because I really enjoy

**[41:09]** building systems from the ground up

**[41:11]** designing clean architecture

**[41:13]** getting all those gradually scaling

**[41:15]** then easy scrolls

**[41:17]** like that

**[41:22]** Cool, yeah, that makes sense

**[41:24]** I was curious

**[41:26]** about again, there's no right or wrong answer

**[41:28]** Sure

**[41:30]** Yeah

**[41:32]** any more questions?

**[41:34]** Yeah, I have one question

**[41:38]** What is your motivation

**[41:40]** for changing companies

**[41:42]** because of growth

**[41:44]** and what are your expectations

**[41:46]** on joining loaner rates

**[41:48]** in terms of

**[41:50]** value

**[41:52]** what do you expect to

**[41:54]** get out of?

**[41:56]** Yeah, that's a

**[41:58]** totally great question

**[42:00]** I think my motivation

**[42:02]** for changing companies

**[42:04]** my current companies

**[42:06]** to take

**[42:08]** because of its growth

**[42:10]** just to take new technical challenges

**[42:12]** working environment

**[42:14]** where you can have

**[42:16]** a stronger impact

**[42:18]** on production direction

**[42:20]** So at Mercury

**[42:22]** I'm not a lot about large-scale

**[42:24]** crew-to-payment systems

**[42:26]** but I'm now looking for a place

**[42:28]** where I can contribute more directly

**[42:30]** to building new products from the ground up

**[42:32]** to work in more

**[42:34]** like a dynamic environment

**[42:36]** So yeah

**[42:38]** in terms of expectations

**[42:40]** I'm looking for a role

**[42:42]** where I can keep growing

**[42:44]** as a client engineer

**[42:46]** staying in the crew-to-space

**[42:48]** contributing to system design, scalability

**[42:50]** pushing in such forward

**[42:52]** in practical

**[42:54]** So yeah

**[42:56]** Cool, thank you

**[42:58]** Great

**[43:00]** So yeah

**[43:02]** we don't have any more questions

**[43:04]** Thank you for

**[43:06]** I know it's a bit difficult

**[43:08]** to be given

**[43:10]** like this

**[43:12]** battery of technical questions

**[43:14]** But it's your turn now

**[43:16]** Is there anything

**[43:18]** we are curious about

**[43:20]** or want to comment

**[43:22]** in general, whatever

**[43:24]** whatever

**[43:26]** you want to talk about now

**[43:28]** Yeah

**[43:30]** Interesting

**[43:32]** how does globalization

**[43:34]** maybe work between the Lunar Rails

**[43:36]** and

**[43:38]** 40 package teams

**[43:40]** just to be more

**[43:42]** understanding

**[43:44]** how it works internal

**[43:46]** Yeah

**[43:48]** So for 40

**[43:50]** So I don't know how much

**[43:54]** did George

**[43:56]** introduce you for the acres

**[43:58]** or

**[44:00]** because

**[44:04]** this position in principle is for Lunar Rails

**[44:06]** we used to have

**[44:08]** like a small team

**[44:10]** dedicated for 40 acres

**[44:12]** which is another company

**[44:14]** within the Lunar Rails

**[44:16]** Group

**[44:18]** Yeah

**[44:20]** 40 acres is like

**[44:22]** it has a license in El Salvador

**[44:24]** So

**[44:26]** we started

**[44:28]** developing this

**[44:30]** product which is called Fortiswap

**[44:32]** which is about

**[44:34]** trustless

**[44:36]** swaps between

**[44:38]** between different Bitcoin layers

**[44:40]** like lightning to Bitcoin

**[44:42]** vice versa

**[44:44]** Liquid

**[44:46]** So this is a product we built

**[44:50]** we are in the process of

**[44:52]** promoting it and that

**[44:54]** but 40 acres doesn't really have

**[44:58]** how to say

**[45:00]** independent team anymore

**[45:02]** it's all part of the same

**[45:04]** Lunar Rails team which handles also

**[45:06]** the trading platform

**[45:10]** On the other hand

**[45:12]** Payment processor, I mentioned

**[45:14]** this is a separate team, this is

**[45:16]** Roberts team

**[45:18]** How many of you

**[45:20]** are there in that team now?

**[45:22]** You are five

**[45:24]** Right

**[45:26]** So the Lunar Rails team

**[45:28]** at the moment is

**[45:30]** there is

**[45:32]** one developer, one platform engineer

**[45:34]** one contractor

**[45:36]** and myself

**[45:38]** I try to write code

**[45:40]** but this is not always

**[45:42]** possible for me

**[45:44]** so we are trying to expand this team

**[45:46]** with at least two more developers

**[45:48]** you know

**[45:50]** Again, we do this

**[45:52]** as a kind of startup

**[45:54]** we did the project StarSimple

**[45:56]** see what our clients want

**[45:58]** this is how we built Fortiswap

**[46:00]** for example, see what our clients

**[46:02]** want

**[46:04]** and go from there, right?

**[46:06]** So yeah

**[46:08]** This team, the Fortiacres team

**[46:10]** Lunar Rails team is the same one

**[46:12]** it's very small at the moment

**[46:14]** we are looking to grow it

**[46:16]** at least

**[46:18]** it should be four or five people

**[46:20]** next year

**[46:22]** but still we are going to be small

**[46:24]** we are

**[46:26]** there is a certain advantage

**[46:28]** in having a small team

**[46:30]** in agility and you know

**[46:32]** adapting to change

**[46:34]** I don't know if I answered your question

**[46:36]** Of course

**[46:38]** this was really interesting

**[46:40]** to explain

**[46:42]** so what about

**[46:44]** OTC trading platform

**[46:46]** can you share more

**[46:48]** about the current technical challenges

**[46:50]** or priorities of this product

**[46:52]** or where you

**[46:54]** where you see the biggest opportunity

**[46:56]** for improvements, for example

**[46:58]** right now

**[47:00]** I mean this platform

**[47:02]** Lunar Rails already has clients

**[47:04]** for OTC trading

**[47:06]** but I mentioned they are not happy

**[47:08]** with how they do it

**[47:10]** they do a lot of manual work

**[47:12]** so we built something

**[47:14]** that solves

**[47:18]** the basic use case

**[47:20]** which is changing

**[47:22]** crypto to crypto

**[47:24]** like Bitcoin to stablecoins mainly

**[47:26]** and Ethereum

**[47:30]** we took some shortcuts

**[47:32]** I don't know if you are familiar with Fireblocks

**[47:36]** it's a cost of the solution

**[47:38]** so behind the trading platform

**[47:40]** we use Fireblocks

**[47:42]** to keep the money safe

**[47:44]** in the long term

**[47:46]** Fireblocks is very expensive

**[47:48]** and we want

**[47:50]** in the long term we want to probably

**[47:54]** swap it

**[47:56]** for another cost of the solution

**[47:58]** actually we have another

**[48:00]** group in Lunar Rails

**[48:02]** that does custody

**[48:04]** but we are going to

**[48:06]** probably improve it in the next year

**[48:08]** I think there is a big opportunity there

**[48:10]** to shape

**[48:12]** a custody solution

**[48:14]** which will also sell to some other people

**[48:16]** so that's one part

**[48:18]** we probably

**[48:20]** want to overhaul the custody part

**[48:24]** and we integrated

**[48:26]** just one liquidity provider

**[48:28]** so we want

**[48:30]** to integrate more

**[48:32]** and of course

**[48:34]** you mentioned you did some sort of engine

**[48:36]** for quick

**[48:38]** routing

**[48:40]** we'll have to do

**[48:42]** I don't know what our brands will be

**[48:44]** if it's the same way

**[48:46]** if we have to be so quick or not

**[48:48]** but we'll have to do something

**[48:50]** to handle multiple providers

**[48:52]** and choose the best one for clients

**[48:54]** so this is something you've already done

**[48:58]** what else

**[49:00]** there is

**[49:02]** a number of other

**[49:07]** we want to add Fiat support

**[49:09]** but this is a bit trickier

**[49:11]** because

**[49:13]** you need to

**[49:15]** interact with banks

**[49:17]** you need to get licenses

**[49:19]** in the jurisdictions you want to operate

**[49:21]** for those banks

**[49:23]** you need to get them to agree

**[49:25]** to do business with you

**[49:27]** and some of them don't want

**[49:29]** because

**[49:31]** they don't want to touch crypto or whatever

**[49:35]** so yeah, lots of

**[49:37]** we're going to be doing a lot of that as well

**[49:39]** like integrating Fiat currencies

**[49:43]** and there is also some other random ideas

**[49:45]** like for example

**[49:49]** we've seen this

**[49:51]** this opportunity

**[49:53]** we are partnering with someone

**[49:57]** so they want to do

**[49:59]** they want to be

**[50:01]** they want to do

**[50:03]** cross-border

**[50:05]** payments in Fiat

**[50:07]** like Swift

**[50:09]** they want to

**[50:11]** do something better than Swift

**[50:13]** but what they do is basically

**[50:15]** they use Lightning

**[50:17]** as payment rates

**[50:19]** like the sender and the receiver
> 📎 **База:** ✅ [[2. GO - Средне#Передача и возврат: значение vs указатель? / Value vs pointer receiver]]

**[50:21]** let's say someone wants to export

**[50:23]** some goods to another country

**[50:25]** so

**[50:27]** in order to get paid

**[50:29]** they have a bank account

**[50:31]** and the guide that dies paying

**[50:33]** they also pay in their local Fiat currency

**[50:35]** so what the idea here is

**[50:37]** to have an OTC desk

**[50:39]** on each side

**[50:41]** and send the money between them

**[50:43]** using Lightning

**[50:45]** because it's so fast

**[50:47]** and

**[50:49]** we can do it within seconds

**[50:51]** so this is another project

**[50:55]** this is something we will probably

**[50:57]** add to our trading platform

**[50:59]** basically Lightning support

**[51:01]** right?

**[51:03]** these other ideas

**[51:05]** like mass payouts

**[51:07]** we've identified this opportunity

**[51:09]** with

**[51:13]** pages like OnlyFans

**[51:15]** sometimes they have to pay

**[51:17]** let's say content creators

**[51:19]** they live in different places

**[51:21]** they cannot send Fiat

**[51:23]** so maybe they have to send

**[51:25]** a thousand crypto payments

**[51:27]** that's another opportunity

**[51:29]** we are exploring

**[51:31]** we have a bunch of

**[51:33]** ideas

**[51:35]** and projects in the pipeline

**[51:39]** suddenly we don't have

**[51:41]** a team to deliver all that

**[51:43]** that's why we are looking to hire

**[51:45]** so yeah

**[51:47]** I don't know if I gave you

**[51:49]** like an overview

**[51:51]** on the payment process

**[51:53]** they have Lightning and Bitcoin

**[51:55]** they want to integrate

**[51:57]** Ethereum and stable coins as well

**[51:59]** so to provide a proper crypto payment

**[52:01]** processor

**[52:03]** but again they already have

**[52:05]** a bunch of clients

**[52:07]** so yeah we are just

**[52:09]** looking to expand and get more money

**[52:15]** yep thanks for

**[52:17]** overview it's really interesting for changes

**[52:19]** I think

**[52:23]** what about team processes

**[52:25]** right now

**[52:27]** screen planning, code reviews, deployments

**[52:29]** something like that

**[52:33]** as I mentioned

**[52:35]** the team is

**[52:37]** like two developers and a platform engineer

**[52:39]** so we don't have a lot of process

**[52:41]** because it doesn't

**[52:43]** make a lot of sense

**[52:45]** we have a product manager

**[52:47]** so we do ad hoc

**[52:49]** when we need

**[52:51]** we do a meeting with the devs

**[52:53]** we explain requirements

**[52:55]** we use

**[52:57]** just simple

**[52:59]** we have a board

**[53:01]** where we try

**[53:03]** to put all the tasks

**[53:05]** a developer picks up the next

**[53:09]** creates a PR

**[53:11]** we use it

**[53:15]** we deploy to prod

**[53:19]** constantly

**[53:21]** but we don't really have formal processes

**[53:23]** because we don't have a big team

**[53:25]** I don't know how much

**[53:27]** we have for example we don't have daily standards

**[53:29]** or anything like that

**[53:31]** we have like a weekly

**[53:33]** update meeting

**[53:35]** where we talk about what we achieved last week

**[53:37]** what we are going to work on next week

**[53:39]** without question

**[53:41]** changes

**[53:43]** that's how we handle it at the moment

**[53:45]** I don't know, as a team grows

**[53:47]** we'll probably have to add some process

**[53:49]** but we like to keep it

**[53:51]** as lean as possible

**[53:55]** yeah, that would make my sense

**[53:57]** of course

**[53:59]** so

**[54:01]** I think I don't have any questions right now

**[54:03]** and thank you

**[54:05]** really much for explaining

**[54:07]** I appreciate it

**[54:09]** yeah, thank you for the time

**[54:11]** again, we know it's a bit tough

**[54:13]** to

**[54:15]** get into this battle of

**[54:17]** technical questions

**[54:19]** I hope

**[54:21]** the intention here is to get to know each other

**[54:23]** and

**[54:25]** I'll talk to

**[54:27]** we'll talk to George

**[54:29]** and he'll be in talk with you

**[54:31]** for the next steps

**[54:33]** yeah, no problem

**[54:35]** so I think that was great conversation

**[54:37]** thank you for your time too

**[54:39]** have a nice day

**[54:41]** thank you, bye bye

## Сопоставление с базой

> Разметка по смыслу вопроса интервьюера. ✅ — точная карточка, ⚠️ — частично, ❌ — нет, 🔧 — практика.

### Теория

| Время | Вопрос (кратко) | Статус | Пункт |
|-------|-----------------|--------|-------|
| — | EXPLAIN, REST, context/cancel, race, atomic, JOIN, select, Kafka | ✅ | [[6. БД#EXPLAIN и EXPLAIN ANALYZE]] · [[7. HTTP, сети#REST principles / gRPC vs HTTP?]] · [[1. GO - Часто#Что такое дедлок и рейс кондишион, и `-race`]] · [[8. Интеграции#Kafka / RabbitMQ?]] |
| — | value vs pointer receiver | ✅ | [[2. GO - Средне#Передача и возврат: значение vs указатель? / Value vs pointer receiver]] |

### Без разметки

| Время | Тема | Статус |
|-------|------|--------|
| 10:27 | OS context switching (не Go context) | ❌ |
