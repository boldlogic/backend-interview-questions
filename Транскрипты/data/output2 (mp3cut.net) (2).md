---
размечено: true
теория: true
лайвкодинг: true
опыт: true
---

# output2 (mp3cut.net) (2)

- **Файл:** `output2 (mp3cut.net) (2).mp3`
- **Длительность:** 41:39
- **Язык (детект):** ru
- **Модель:** faster-whisper / small
- **Распознано:** 2026-08-01 10:06 UTC


- **Разметка:** после реплики интервьюера — одна строка:
  - `> 📎 **База:** …` — **теория**; ссылка на банк
  - `> 📎 **Задача:** …` — **практика** (live coding, code review)
  - Статусы: ✅ в банке, ⚠️ частично, ❌ нет, 🔧 упражнение

## Транскрипт

**[00:00]** Okay, okay, that's fair.

**[00:02]** So basically, this project is about mostly GNI.

**[00:08]** RAG, you know that idea, retrieved argumented generation,

**[00:13]** this is like a baseline for this project.

**[00:15]** And basically this project is about taxes, right?

**[00:17]** So basically it's sourcing taxes.

**[00:20]** So something similar probably to your current area of business, right?

**[00:28]** But it's like mostly about agentic AI systems, right?

**[00:32]** With RAG, vector databases, data engineering, data analysis,

**[00:38]** with like also not only like basic data, but also the structured ones.

**[00:44]** So something like Databricks, it's also really good to know for this project.

**[00:51]** Basically what they are searching for.

**[00:54]** So they are searching for someone who's really good in Python, right?

**[00:56]** This is a base for them.

**[00:58]** And also they want somebody, someone who is able to create a whole,

**[01:04]** like a agenting AI flow, because they want to rebuild the processes.

**[01:08]** So basically they have processes inside and they would like to rebuild them

**[01:12]** to something what is like cheaper.

**[01:14]** Yeah, in the end it's cheaper because you don't need to use a lot of people.

**[01:17]** It's mostly automated.

**[01:18]** So this is the idea for this project.

**[01:20]** This is the description, which I received from HR for this position.

**[01:25]** Is this interesting for you?

**[01:27]** Yeah.

**[01:29]** So basically if you can tell me about current projects.

**[01:33]** For example, if you have any advanced projects with AI, ML, GenAI,

**[01:41]** this is the best.
> 📎 **База:** ✅ [[16. Опыт и soft skills#Один проект за 2–3 минуты]] · GenAI/RAG опыт

**[01:43]** And you can tell me what you did in this project,

**[01:46]** what was your part, what was the project overall.

**[01:49]** Basically what kind of technologies

**[01:55]** was incorporated.

**[01:58]** Maybe you have some kind of, I don't know, algorithms,

**[02:02]** which are not unusual, unusual algorithm,

**[02:04]** maybe models from hacking phase or custom ones.

**[02:06]** Anything that is interesting from a technical point of view.

**[02:09]** So basically with that information,

**[02:11]** I will be able to check some boxes in this form.

**[02:15]** So we will be able to proceed easier later.

**[02:18]** So if you can tell me about the most advanced project with, I don't know,

**[02:22]** vector databases, vector stores and so on.

**[02:25]** And you can use the names of libraries,

**[02:28]** and anything that is technical.

**[02:30]** It's mostly about this technical stuff behind.

**[02:32]** And exactly what you did in this project.

**[02:34]** Maybe what was your role, like a position,

**[02:36]** because this is the initial thing,

**[02:38]** which I need to figure out during this conversation

**[02:40]** to assign it to the specific level.

**[02:42]** Like level inside a PWC to offer you a right position.

**[02:48]** So I need to figure out maybe from experience,

**[02:51]** maybe from your knowledge and so on.

**[02:53]** So if you can tell me about the project,

**[02:55]** what was your role and so on.

**[02:57]** All right.

**[02:59]** So I can tell you about my most advanced project.

**[03:03]** It's called FinRAG.

**[03:05]** And it's exactly the last project I'm working on.

**[03:11]** It's a regulatory and risk intelligence platform

**[03:15]** for a midsize investment bank.

**[03:19]** It's basically a large-scale RAG system

**[03:22]** that indexes around 8000 regulatory documents

**[03:29]** and about 180 million structured financial records.

**[03:36]** My main responsibility there is retrieval and impedance.

**[03:41]** So I designed the hybrid retrieval pipeline

**[03:44]** that combines dancing basins from Amazon

**[03:48]** Drucker Titan basins V2

**[03:51]** with a BM25 keyword search

**[03:54]** in OpenSearch serverless.

**[03:58]** Refuse both scores using reciprocal run fusion

**[04:02]** and then apply coherent rank V3.5

**[04:05]** for the final out of five chunk selection before generation.

**[04:11]** I also optimized the index design and latency.

**[04:19]** For example, OpenSearch had a cool start spike

**[04:23]** up to 8 seconds.

**[04:25]** So I added an index forming lambda

**[04:28]** that fires synthetic queries every 15 minutes,

**[04:32]** which brought P9 client latency

**[04:35]** under 600 milliseconds.

**[04:41]** And what kind of vector store have you used?

**[04:44]** There is like a vector store in any cloud

**[04:47]** or maybe it was your own vector store

**[04:50]** from title library host somewhere.
> 📎 **База:** ⚠️ [[17. Data Python ML#RAG: retrieval-augmented generation]] · vector store / OpenSearch

**[04:53]** Because you need to have vector store, right?

**[04:55]** To do this, also this searching mechanism,

**[04:59]** this algorithm for keywords and so on.

**[05:02]** It was in any...

**[05:04]** Yeah, it was Amazon OpenSearch serverless.

**[05:08]** Okay, okay.

**[05:10]** And I don't know if I'm familiar with that.

**[05:12]** It's like ready to use like a vector store

**[05:14]** or you need to host something.

**[05:16]** Because I'm not doing Amazon.

**[05:18]** I never had a chance to do that.

**[05:20]** I'm mostly Azure guy or GCP.

**[05:23]** So it's like a service,

**[05:25]** which you can just create a resource

**[05:29]** and it's already database.

**[05:31]** Or it's like you need to host something there.

**[05:35]** In AWS, it's the managed service.

**[05:38]** So we don't need to host anything manually.

**[05:42]** Okay, so it's out of the box like a solution.

**[05:45]** You can create it and use it.

**[05:47]** Okay, yeah, sorry.

**[05:49]** Yeah, you can continue.

**[05:54]** Okay, so I was talking about

**[06:01]** at a warming drop.

**[06:05]** And then...

**[06:07]** Like sources and...

**[06:09]** Yeah.

**[06:12]** The system runs fully on AWS.

**[06:16]** S3 for storage.

**[06:18]** EKS for microservice.

**[06:21]** Bedrock for LLMs.

**[06:23]** We used to call the 3.5 sonnet in Haiku.

**[06:27]** And long graph for orchestration.

**[06:30]** We also log every query,

**[06:32]** retrieve chunk and response

**[06:34]** to DynamoDB for auditability.

**[06:38]** So overall

**[06:42]** it's a production grade Rack platform

**[06:44]** with strong compliance

**[06:46]** and performance constraints.

**[06:49]** I'd say it's quite close to

**[06:51]** what you described.

**[06:54]** Structured data

**[06:56]** and vector databases.

**[06:58]** Okay, so how many nodes

**[07:00]** do you have in this flow?

**[07:03]** Like in long graph, right?

**[07:05]** You have nodes and how many?

**[07:07]** In the end, I would like to understand

**[07:09]** how complicated is this system, right?

**[07:11]** So basically how many nodes do you have

**[07:13]** in this system?
> 📎 **База:** ❌ LangGraph · число nodes / сложность графа

**[07:16]** Во-втор-втор-во-втор

**[07:18]** It was another colleague

**[07:20]** who did

**[07:26]** a self-critical loop.

**[07:28]** But

**[07:30]** as far as I know

**[07:32]** long graph for orchestration part

**[07:34]** was

**[07:36]** worth

**[07:39]** 10-12 nodes

**[07:41]** depending on the query type.

**[07:43]** The simple loop path

**[07:45]** might be

**[07:47]** 5 nodes

**[07:49]** or execution, retrieval,

**[07:51]** rank, generation

**[07:53]** and audit login.

**[07:55]** The more advanced

**[07:57]** document or

**[07:59]** template queries

**[08:01]** edit self-critique

**[08:03]** and retrieval nodes

**[08:05]** for the full graph became more complex.

**[08:07]** Okay.

**[08:09]** So right now I will have

**[08:11]** some more technical questions

**[08:13]** from

**[08:15]** databases,

**[08:17]** Python,

**[08:19]** async programming.

**[08:21]** And then

**[08:23]** we have Rack.

**[08:25]** Sorry, I missed

**[08:27]** several seconds.

**[08:29]** Oh, yeah.

**[08:31]** So basically I will ask

**[08:33]** you some questions, right?

**[08:35]** From different areas like

**[08:37]** databases, Python,

**[08:39]** concurrent programming,

**[08:41]** Rack,

**[08:43]** агентик workflows,

**[08:45]** агентик

**[08:47]** life cycle management,

**[08:49]** system design if you will have time,

**[08:51]** maybe something about cloud.

**[08:53]** So let's start from the beginning.

**[08:55]** The easiest question

**[08:57]** about databases.

**[08:59]** So maybe can you tell me

**[09:01]** what is that transaction?

**[09:03]** Like in the database what is it,

**[09:05]** what need to be

**[09:07]** involved in this process,

**[09:09]** what do you want to keep

**[09:11]** like before and after?
> 📎 **База:** ✅ [[02. БД - Часто#ACID и транзакции]]

**[09:13]** So basically

**[09:15]** transaction in a database

**[09:17]** is basically

**[09:19]** sequence of operations

**[09:21]** that are executed

**[09:23]** as a single logical

**[09:25]** unit of work.

**[09:27]** The main idea is to

**[09:29]** either

**[09:31]** operations succeed

**[09:33]** or none of them do.

**[09:37]** So the database

**[09:39]** is consistent.

**[09:41]** It follows

**[09:43]** the ICID

**[09:45]** properties.

**[09:47]** I remember

**[09:49]** atomicity,

**[09:51]** consistency,

**[09:53]** isolation

**[09:55]** and this

**[09:57]** durability.

**[10:00]** Good, really good.

**[10:02]** That's good.

**[10:04]** Maybe you can tell me

**[10:06]** what is index in database

**[10:08]** or data structure

**[10:10]** for index in this old-fashioned

**[10:12]** database.

**[10:14]** Right now there are new versions

**[10:16]** of indexes for non-escalable

**[10:18]** databases, but I'm not asking

**[10:20]** about this one, I'm asking about

**[10:22]** old-fashioned index

**[10:24]** from SQL database.
> 📎 **База:** ✅ [[02. БД - Часто#Что такое индексы БД и зачем они нужны?]] · B-tree

**[10:26]** Sure.

**[10:28]** In traditional relational databases

**[10:30]** index is basically

**[10:32]** a separate data structure

**[10:34]** that helps the engine

**[10:36]** scanning the whole table.

**[10:38]** The classic implementation is

**[10:40]** B3 or more precisely

**[10:42]** B plus minus 3.

**[10:46]** It gets keys

**[10:48]** sorted and

**[10:50]** starts pointers to the actual

**[10:52]** table rows.

**[10:54]** Because it's not balanced

**[10:56]** the lookup, insert

**[10:58]** and delete operations are

**[11:00]** very significant time.

**[11:02]** That's why it's the default

**[11:04]** index type

**[11:06]** for mySQL

**[11:08]** and so on.

**[11:12]** Okay, and do you know maybe

**[11:14]** the data structure?

**[11:16]** What is

**[11:18]** how does indexes

**[11:20]** build, what is the structure

**[11:22]** of this

**[11:24]** whole structure basically?
> 📎 **База:** ✅ [[02. БД - Часто#B-tree и физическое хранение на диске]] · B+ tree leaf/internal

**[11:26]** Do you know maybe, do you have idea

**[11:28]** what can it be?

**[11:33]** So in B plus minus 3

**[11:35]** that is starting

**[11:37]** internal nodes

**[11:39]** and leaf nodes.

**[11:41]** Internal nodes only keep

**[11:43]** keys and pointers to child nodes

**[11:45]** while leaf nodes

**[11:47]** hold the actual key values

**[11:49]** and pointers to the table rows.

**[11:51]** Okay.

**[11:53]** All these are linked

**[11:55]** together in

**[11:59]** a link list.

**[12:01]** So range scans

**[12:03]** very fast.

**[12:05]** Okay.

**[12:07]** Sorry for interrupting.

**[12:09]** It's enough.

**[12:11]** Right now I will have some tasks.

**[12:13]** It's mostly about Python.

**[12:15]** It's only about Python right now.

**[12:17]** And I will send you

**[12:19]** a screenshot

**[12:21]** and

**[12:23]** your task is to do

**[12:25]** code review.

**[12:27]** Basically you need to find

**[12:29]** two big mistakes

**[12:31]** in this code.

**[12:33]** Which are not safe

**[12:35]** in this code.
> 📎 **Задача:** 🔧 Python code review · SQL injection + connection leak · ✅ [[02. БД - Часто#SQL injection и параметризованные запросы]] · ⚠️ [[18. Python#Context managers (with / contextlib)]]

**[12:37]** And you just need to tell me

**[12:39]** what is wrong and how to fix that.

**[13:13]** Are you able to see that

**[13:15]** screenshot?

**[13:17]** Yes.

**[13:19]** So basically

**[13:21]** the queries are correct.

**[13:23]** You don't need to check the SQL.

**[13:25]** Only the Python part

**[13:27]** of this endpoint.

**[13:38]** So as I see here

**[13:44]** SQL injection

**[13:52]** I see

**[13:54]** unsafe stream

**[13:59]** computation

**[14:01]** using queries

**[14:03]** instead of

**[14:14]** parameterized queries.

**[14:16]** Also I see

**[14:18]** mismanagement

**[14:20]** or lack of

**[14:22]** ...

**[14:24]** ...

**[14:27]** ...

**[14:57]** ...

**[14:59]** ...

**[15:01]** ...

**[15:03]** ...

**[15:09]** ...

**[15:11]** ...

**[15:13]** ...

**[15:18]** ...

**[15:31]** ...

**[15:33]** ...

**[15:35]** ...

**[15:37]** ...

**[15:39]** ...

**[15:41]** ...

**[15:43]** ...

**[15:45]** ...

**[15:47]** second issue is a missing input foundation and fix is to wrap it in a function or use the connection pool to ensure it closes properly.

**[16:14]** И если мы не хотим уходить контакт для этого, то мы можем путь в статус.

**[16:22]** Потому что мы умелless have a connection-pull.

**[16:25]** Мы можем путь конакт по-г Joey для этого.

**[16:28]** Так что мы хотим уходить конакт по-г Joey для того, чтобы иметь конакт,

**[16:32]** мы хотим уходить его для того, чтобы ух habit, и так далее.

**[16:34]** Но если мы хотим уходить толькоOneConnection, то мы можем делать.

**[16:37]** Мы имеем два разныхls, что мы можем делать ровно.

**[16:40]** Мы можем его использовать вBeat.

**[16:46]** Они выглядят по-другому, но в итоге они имеют то же эффект.

**[16:53]** Можете мне сказать, что это?

**[16:55]** Как же я знаю.

**[17:02]** Если мы не используем коннекционный пуль, то мы у нас есть еще один пуль.

**[17:10]** Сначала мы можем открыть и закрыть коннекционный пуль с контентом.

**[17:16]** Так что это всегда есть, даже если эксцепция случится.

**[17:20]** Второй пуль, если мы собираем коннекционный пуль.

**[17:26]** Мы можем использовать сейфы с локом или симфором.

**[17:31]** Для того, чтобы избежать кондиционных пуль, когда в multiples requests

**[17:35]** trying to use it at the same time.

**[17:37]** Но в конце концов, мы не имеем эту проблему.

**[17:44]** Потому что это как пас-тпи.

**[17:47]** Так что эта проблему будет новая тазка.

**[17:52]** Мы не нужны для этого, потому что мы созданы новую коннекцию

**[17:57]** для database, для каждого request.

**[18:01]** Вторая идея, это просто использовать try and accept

**[18:06]** для закрыть коннекционный пуль с контентом.

**[18:43]** Это довольно основная вещь, потому что это API.

**[18:47]** Это не функция, это не нормальная функция, это API.

**[18:50]** И это будет новая тазка.

**[18:52]** Я имею еще одну вопрос.

**[18:54]** Это о генераторе.

**[18:57]** И вопрос, что мы увидим, когда мы собираем эту проблему и почему?
> 📎 **База:** ⚠️ [[20. Теория программирования#Итераторы и ленивые последовательности]] · generator / next()

**[19:07]** Ок, так что, как я помню...

**[19:19]** Я не знаю...

**[19:34]** Вы можете повторить эту вопросу?

**[19:36]** В принципе, что будет happen?

**[19:39]** И почему?

**[19:40]** Мы собираем эту проблему и что будет happen?

**[19:43]** Вы сможете видеть...

**[19:45]** Вторую проблему.

**[19:47]** Ок, я не знаю...

**[19:51]** Ок.

**[19:55]** Мы собираем генератору, то есть, генератор объект,

**[20:04]** и передиived nextE justo до следующего публики,

**[20:15]** employed Its nexus,

**[20:22]** every spec apply everything

**[20:34]** Получается, что lifelink,

**[20:37]** ере как тип boblsink,

**[20:39]** travailler Ok Design.

**[20:40]** Дьявол ,

**[20:41]** ежедневно и так далее,

**[20:42]** и чужой поз Switzerland,

**[20:44]** Я скажу, что это валипаж.

**[20:51]** Нет, это не будет.

**[20:54]** Смотри, с генератором, с этой крошкой, мы созданы генератором объекта.

**[21:00]** Так что, в принципе, бодиа этой крошки будет в фанкции следующей.

**[21:03]** Пока ты не станешь на фанкции следующей,

**[21:07]** ты не станешь на фанкции внутри этой крошки,

**[21:12]** потому что в селлде это не фанкция, это же объект-самплент.

**[21:18]** Объект-зайп-оп-генератор.

**[21:19]** Бодио-кроша будет функцией «НЕХТ».

**[21:23]** Нейма будет именем для кроша.

**[21:24]** Это крош, который вы можете видеть над «Принт-хэллоу».

**[21:29]** Это просто объект-инсажение.

**[21:33]** Это визуальная функция.

**[21:36]** Не крош-фанкция, как крош с бодием, который вы можете видеть над «ОБАФ».

**[21:40]** Это трик «БЕХАНИТ».

**[21:46]** Бодио-хэллоу нужно работать с «НЕХТ» на крошах.

**[21:50]** Тогда вы получите эту цель.

**[21:54]** В Питоне мы имеем два строительного механизма.

**[22:01]** Таск – мультипроцессор, третинг – мультипроцессор.

**[22:06]** Также мы имеем таски с первым АПИ или АСИНКЕО.

**[22:11]** Мы имеем даже «ЛОБАФ» и так далее.

**[22:13]** Можно сказать, что мы должны использовать мультипроцессор,

**[22:18]** мультипроцессор, таск и «ЛОБАФ».

**[22:22]** Мультипроцессор и «ЛОБАФ», мы должны использовать

**[22:24]** каждые механизмы в Питоне.
> 📎 **База:** ✅ [[18. Python#GIL в Python]] · threading vs multiprocessing vs asyncio

**[22:31]** Мы имеем мультипроцессор, когда цель будет «СПО-БАУНТ».

**[22:36]** Теплые компетенции или моделл-инференс.

**[22:39]** Потому что транс-сепаритерпроцессор и га-класс-сезон.

**[22:46]** Мы используем мультифредден, когда цель будет «АЕО-БАУНТ».

**[22:53]** Как и «Нетерклз» или «Файл-операциях».

**[22:56]** Серьез, «Шэймэмери» и «Свичим-Счикер».

**[23:05]** Можно мне дать пример?

**[23:13]** Какой-то реальный «ЛОБАФ» для каждого механиза.

**[23:22]** Реальный «ЛОБАФ» для тех, кто хочет работать в мультипроцессор,

**[23:28]** в мультитраде и в «ЛОБАФ».
> 📎 **База:** ✅ [[18. Python#multiprocessing / gunicorn workers]] · use-cases CPU/IO/async

**[23:32]** Для мультипроцессора может быть «Имейш-процессор»

**[23:36]** или «Мотелл-инференс» для многих курсов.

**[23:39]** Для мультифредденов может быть «Доллз-мани-файлз» в параллле.

**[23:48]** И для «Ассинк-АЕО-хэндлин» –

**[23:50]** тысяча веб-эквестов в FastAPI-сервисе.

**[23:54]** Окей.

**[23:59]** Вы имеете опыт с «ФЛАСК» или «ФАСТ-АПИ»?

**[24:06]** Вы имеете опыт с «ФЛАСК» или «ФАСТ-АПИ»?
> 📎 **База:** ✅ [[18. Python#FastAPI (основы)]] · опыт

**[24:11]** Да, я имею опыт с «ФАСТ-АПИ».

**[24:16]** Мы хотели расположить «ААИ» и «РАК-сервисы» на «АВС».

**[24:23]** Например, в банке «Чембот» и «Фин-РАК-процессор»,

**[24:27]** где «Майкл-сервис» был в FastAPI-сервисе с «РАК-процессором»

**[24:32]** с «Ассинк-эндпоинсом» и «ФРАК-процессором».

**[24:37]** Окей. Вы имеете опыт с «ФЛАСК» или «ФАСТ-АПИ»?

**[24:41]** Потому что иногда, когда вы имеете «АЛАМ»,

**[24:44]** вы можете «ФРАК-процессор» стримать.

**[24:46]** Это когда вы используете «УИ» для «ГПТ»

**[24:49]** или любого другого языка.

**[24:51]** Вы можете видеть «Тайпрайд» эффект.

**[24:54]** Это эффект стрима.

**[24:57]** Вы имеете опыт с «Тайпрайдом» эффект?
> 📎 **База:** ❌ LLM streaming / typewriter effect · нет карточки

**[25:00]** Да, я работаю с стримами в «ФРАК-процессором»

**[25:06]** с «Сервис-эндпоинсом» и «ФРАК-процессором»

**[25:10]** с «АЛАМ-эндпоинсом».

**[25:13]** Например, в банке «Чембот»

**[25:16]** мы стримали партизные ответы

**[25:19]** с «Видорик-моделсом» и с «ЧЭТ-УИ».

**[25:23]** Так что, в «Видорик-моделсом»

**[25:25]** вы можете видеть «Масси-ш»

**[25:27]** в реальном времени,

**[25:29]** как и в «ЧЭТ-УИ».

**[25:31]** Да, хорошо.

**[25:33]** Вы имеете опыт с «ФРАК-процессором»,

**[25:35]** да?

**[25:37]** Вы знаете, что я...

**[25:39]** Я думаю, что...

**[25:42]** О, что-то,

**[25:44]** как...

**[25:48]** Что-то, но это не...

**[25:50]** это просто...

**[25:52]** Вы знаете, что это

**[25:54]** «Семантик-чанкин»?
> 📎 **База:** ⚠️ [[17. Data Python ML#RAG: retrieval-augmented generation]] · semantic chunking

**[25:56]** Конечно.

**[25:58]** «Семантик-чанкин»

**[26:00]** means speaking documents

**[26:02]** not by fixed size,

**[26:04]** but by minimum.

**[26:06]** So instead of cutting

**[26:08]** every 500 tokens

**[26:10]** we detect

**[26:12]** sentence or paragraph boundaries

**[26:14]** and...

**[26:16]** so we group text

**[26:18]** that belongs to the same logic

**[26:20]** or semantic unit.

**[26:22]** And it helps retrieval

**[26:24]** because the chunks keep

**[26:26]** full context

**[26:28]** and reduces cases where

**[26:30]** relevant info is split in chunks.

**[26:32]** Okay, okay.

**[26:35]** Now I have more advanced question about...

**[26:41]** when we are building a RAG system,

**[26:43]** we are creating a database,

**[26:45]** the vector of database.

**[26:47]** Where we need to search

**[26:49]** for

**[26:51]** vectors, which are similar

**[26:53]** to user query vector, right?

**[26:55]** Embedding, so in the end vector.

**[26:57]** And we have to the most

**[26:59]** popular way of

**[27:01]** measuring the similarity.

**[27:03]** While it's costing a similarity, right?

**[27:05]** That's the most commonly used

**[27:07]** and also that product.

**[27:09]** Like costing similarity is faster

**[27:11]** and easier to calculate,

**[27:13]** but for some reason we still

**[27:15]** have that product.

**[27:17]** Do you know maybe when and why

**[27:19]** we can use cosine similarity

**[27:21]** if there is any

**[27:23]** any danger?

**[27:27]** Why we need to sometimes

**[27:29]** start product instead of

**[27:31]** costing similarity?
> 📎 **База:** ❌ cosine vs dot product · embedding similarity

**[27:33]** So that product is usually used

**[27:35]** when the embedding model

**[27:37]** isn't

**[27:39]** normalized

**[27:41]** to unit plans.

**[27:45]** Because cosine similarity assumes

**[27:47]** normalized vectors if

**[27:49]** they are

**[27:51]** model outputs

**[27:53]** are normalized embeddings,

**[27:55]** then that product preserves

**[27:57]** magnitude information,

**[27:59]** which can be useful for

**[28:01]** ranking.

**[28:03]** Also some libraries like

**[28:05]** files or open-source

**[28:07]** optimize that progress

**[28:09]** for speed and use it

**[28:11]** internally even when it's

**[28:13]** mathematically related to cosine after

**[28:15]** normalization.

**[28:18]** Okay, yeah, that's really good.

**[28:20]** It's a little bit tricky.

**[28:22]** Do you know maybe example of models

**[28:24]** which are

**[28:26]** normalized and which are not?
> 📎 **База:** ❌ normalized vs unnormalized embeddings · примеры моделей

**[28:33]** Examples.

**[28:35]** So for example, PNEI

**[28:37]** text embedding is very large.

**[28:41]** It's output

**[28:43]** normalized vectors.

**[28:47]** But

**[28:51]** Titan embedding is a bit too

**[28:53]** difficult,

**[28:55]** as far as I know.

**[28:57]** Produce unnormalized vectors,

**[28:59]** so that product is

**[29:01]** preferred unless you manually

**[29:03]** normalize them before indexing.

**[29:05]** Have you ever used this

**[29:07]** unnormalized vectors? Have you ever used

**[29:09]** this dot product measure?

**[29:11]** Maybe I've

**[29:13]** comparison

**[29:15]** about the difference when you are using

**[29:17]** the...

**[29:19]** Because you still can use

**[29:21]** it.

**[29:23]** And there will be

**[29:25]** a missing information because of that.

**[29:27]** Because you measure only the

**[29:29]** angle between the vectors.

**[29:31]** But you're losing the information which is

**[29:33]** coded on a magnitude.

**[29:35]** So on the left.

**[29:37]** Do you have maybe comparison between them?

**[29:39]** Have you ever used this

**[29:41]** unnormalized vector with dot product

**[29:43]** or all these similarity

**[29:45]** vectors?

**[29:47]** Yes.

**[29:49]** We use the Titan embeddings

**[29:51]** V2, which are unnormalized.

**[29:53]** So we use

**[29:55]** dot product in OpenSearch.

**[29:57]** But in earlier projects

**[29:59]** like the automotive knowledge platform

**[30:01]** we used OpenAI embeddings

**[30:03]** which are already normalized.

**[30:05]** So the similarity

**[30:07]** was fine without extra

**[30:09]** preprocessing.

**[30:11]** Okay.

**[30:15]** Okay, that's really good.

**[30:17]** Now I have questions about frameworks.

**[30:19]** You mentioned that you have experience with

**[30:21]** langgraph, right?

**[30:23]** Langchain probably also, right?

**[30:25]** Right.

**[30:27]** Yeah.

**[30:29]** LANA index?

**[30:31]** Also.

**[30:33]** Also, okay. QAI?

**[30:35]** No.

**[30:37]** Okay.

**[30:39]** MCP servers.

**[30:41]** Have you ever created one?
> 📎 **База:** ❌ MCP servers · опыт

**[30:43]** Yes.

**[30:49]** No.

**[30:51]** No.

**[30:54]** And React agents?
> 📎 **База:** ⚠️ [[17. Data Python ML#RAG: retrieval-augmented generation]] · ReAct agents / LangGraph

**[31:00]** React agents.

**[31:04]** I worked with

**[31:06]** both langgraph and langchain

**[31:08]** for orchestration

**[31:10]** and also with

**[31:12]** React style agents.

**[31:14]** Okay.

**[31:16]** So basically

**[31:18]** maybe in langgraph.

**[31:22]** So for example

**[31:24]** we would like to have

**[31:26]** two branches, right?

**[31:28]** Basically we have three nodes.

**[31:30]** One node is starting node,

**[31:32]** right?

**[31:34]** So far in total.

**[31:36]** So we have start node, we have

**[31:38]** node on the left side, node on the right side.

**[31:40]** So let's say A, B.

**[31:42]** And we would like to

**[31:44]** run node A and B

**[31:46]** simultaneously, right?

**[31:48]** And they are going to the node C.

**[31:50]** And

**[31:52]** they will run

**[31:54]** two times, right?

**[31:56]** Because it depends.

**[31:58]** If you will

**[32:00]** use a different approach, you can

**[32:02]** like run start node,

**[32:04]** 8 node, C node,

**[32:06]** start node, B node,

**[32:08]** C node.

**[32:10]** So you will run the C node twice.

**[32:12]** And can you tell me how we need

**[32:14]** to

**[32:16]** code this constraint

**[32:18]** to

**[32:20]** have results of both of them

**[32:22]** to run the node C, right?

**[32:24]** So then the node C is run only once

**[32:26]** after the node B,

**[32:28]** after the node A and B are completed.

**[32:30]** Do you know what we need to do

**[32:32]** in code basically?
> 📎 **База:** ❌ LangGraph · join/barrier A∥B → C once

**[32:36]** Yeah.

**[32:38]** This is called

**[32:40]** join constraint

**[32:42]** or synchronization point

**[32:44]** in langgraph.

**[32:48]** So you can define it so node C

**[32:50]** A and B

**[32:52]** to finish.

**[32:54]** Yeah. And how we can define it?

**[32:56]** Like basically in code.

**[32:58]** Like what do we need to do?

**[33:00]** Like basically we have

**[33:02]** we are creating the

**[33:06]** oh yeah, I forgot the word.

**[33:08]** Edge, right?

**[33:10]** And how we need to create this edge

**[33:12]** to have this effect?

**[33:14]** What exactly?

**[33:16]** Like how do you look like

**[33:19]** should I write a code?

**[33:22]** Yeah, you can write a code.

**[33:24]** You can just tell me

**[33:27]** because it's like a simple thing

**[33:29]** which you need to do to

**[33:31]** tell

**[33:35]** like for langgraph

**[33:37]** to get this

**[33:39]** effect.

**[33:41]** So you define it by creating edges

**[33:43]** from both nodes A and B

**[33:45]** to node C

**[33:47]** depends on parameter

**[33:49]** to

**[33:51]** list of A and B

**[33:53]** or some of the graph nodes to trigger C

**[33:55]** only after both upstream nodes

**[34:01]** complete.

**[34:03]** Okay.

**[34:16]** So right now I have

**[34:18]** the agent

**[34:20]** lifecycle management

**[34:22]** and basically

**[34:24]** can you tell me

**[34:26]** maybe do you have experience

**[34:28]** with langfuse or

**[34:30]** I think it's

**[34:32]** langfuse

**[34:34]** langsmeave

**[34:36]** there's phoenix also

**[34:38]** like the open source library

**[34:40]** and many others libraries which you can use

**[34:42]** to

**[34:44]** monitor agent behaviors, right?

**[34:46]** So this is not like you don't want to create a health check

**[34:48]** for whole application

**[34:50]** but you want to create

**[34:52]** guardrails

**[34:54]** or LLM as a judge

**[34:56]** do you have experience with this area?
> 📎 **База:** ❌ LLM-as-judge / Langfuse / agent observability

**[34:58]** Yeah.

**[35:01]** I've worked with

**[35:03]** langsmeave

**[35:05]** for monitoring and evaluation

**[35:09]** we used them to track

**[35:11]** agent traces token usage

**[35:13]** and latency

**[35:15]** and also to run automated

**[35:17]** devals with LLM as a charge

**[35:19]** for example in

**[35:21]** Finrago.

**[35:23]** Do you know maybe

**[35:25]** examples KPI

**[35:27]** like basically the measures which you can

**[35:29]** use to

**[35:31]** measure different

**[35:33]** different

**[35:35]** qualities of your

**[35:37]** of your rug

**[35:39]** maybe you can explain

**[35:41]** why we are using this

**[35:43]** specific KPI
> 📎 **База:** ⚠️ [[17. Data Python ML#RAG: retrieval-augmented generation]] · KPI: recall@k, faithfulness, latency

**[35:45]** For our system

**[35:54]** we usually track

**[35:56]** human KPI

**[35:58]** it's original record

**[36:00]** okay

**[36:02]** but

**[36:04]** how often the correct document appears

**[36:06]** that appears else

**[36:08]** also

**[36:10]** we track

**[36:12]** coordination rate

**[36:14]** faithfulness

**[36:16]** score

**[36:18]** latency

**[36:20]** P95

**[36:23]** cost per query

**[36:25]** also

**[36:27]** there is metric user satisfaction

**[36:31]** Okay, that's quite good

**[36:33]** Yeah, so basically

**[36:35]** I think from this main scope

**[36:37]** I have everything

**[36:39]** Do you have any questions

**[36:41]** or maybe feedback?
> 📎 **База:** ✅ [[16. Опыт и soft skills#Вопросы к интервьюеру про продукт]] · роль/контракт

**[36:43]** Oh, I can, maybe right now I will be able to

**[36:45]** turn on camera

**[36:47]** Sorry for that, but I just wanted to have

**[36:49]** the better

**[36:51]** voice quality and more stable connection

**[36:55]** Do you have any additional questions for me

**[36:57]** maybe about the project, maybe any feedback

**[36:59]** about how this

**[37:01]** conversation was

**[37:03]** proceed

**[37:05]** So is this my role

**[37:09]** a long-term investment

**[37:11]** or short-term demand?

**[37:13]** Oh, so basically

**[37:15]** it's mostly

**[37:17]** for the client, right?

**[37:19]** So basically the project is

**[37:21]** in most cases long-term project

**[37:23]** but even if the project is closed

**[37:25]** you still are the PwC

**[37:29]** employee

**[37:31]** so basically if they are not able to find

**[37:33]** you a project

**[37:35]** and you don't have anything to do

**[37:37]** but they also can

**[37:39]** involve you in different projects

**[37:41]** for PwC-Polska, not only for

**[37:43]** client, also for PwC-Polska

**[37:45]** so

**[37:47]** there is no problem with that

**[37:49]** that if they will not

**[37:51]** be able to find you in another position

**[37:53]** you will still be on the bench

**[37:55]** and you will still get money

**[37:57]** I'm not sure

**[37:59]** how it will look like for you

**[38:01]** but for me it's like

**[38:03]** I have

**[38:05]** two months

**[38:07]** of this period where I can

**[38:09]** if I would like to leave

**[38:11]** I need to wait two months

**[38:13]** and if they want to fire me

**[38:15]** then they

**[38:17]** will need to pay me

**[38:19]** for two months at least

**[38:21]** so basically you have the safety

**[38:23]** from the side that you have this bench

**[38:25]** it's called hard bench

**[38:27]** basically you are choosing

**[38:29]** that you are on bench and you are

**[38:31]** adding this information

**[38:33]** into your time sheet

**[38:35]** and then they need to pay

**[38:37]** this is what my manager told me

**[38:39]** because I ask about it

**[38:41]** this is quite important

**[38:43]** because you have different

**[38:45]** versions of B2B

**[38:47]** B2B contracts

**[38:49]** sometimes it's like contract really similar to

**[38:51]** normal work contract

**[38:53]** so basically they are going to pay you always the same amount

**[38:55]** no matter how many days you are working this week

**[38:57]** and you have also like vacations

**[38:59]** and so on but it's not the case

**[39:01]** here you have just clean B2B

**[39:03]** so you don't have a vacation

**[39:05]** if there is a free day they are not going to pay you for that

**[39:07]** but from the other hand

**[39:09]** they still provide some level

**[39:11]** of safety by this

**[39:13]** bench and

**[39:15]** that's a good part

**[39:19]** okay

**[39:21]** what level of autonomy will I have

**[39:23]** which is

**[39:25]** this is really up to the client

**[39:27]** this project probably they want to rebuild

**[39:29]** something what they already have

**[39:31]** so in terms of databases

**[39:33]** in terms of data, in terms of web store

**[39:35]** cloud is mostly like what client

**[39:37]** you are going to use the client's cloud

**[39:39]** because they have a whole ecosystem

**[39:41]** there and they are not going to move it

**[39:43]** in most cases

**[39:45]** so like with me I am working with Azure

**[39:47]** and there is no chance

**[39:49]** to move whole infrastructure

**[39:51]** anywhere else but in terms of

**[39:55]** like if I would like to use SQL

**[39:57]** like PostgreSQL

**[39:59]** database or any other or not

**[40:01]** SQL database or blob storage

**[40:03]** it's mostly up to me what I would like to use

**[40:05]** in my project and what I see as the most

**[40:07]** usable and the easiest

**[40:09]** for me and sometimes you can just choose

**[40:11]** what is well known for you

**[40:13]** probably

**[40:23]** I don't have questions

**[40:25]** okay

**[40:28]** any feedback for me

**[40:36]** I am excited to

**[40:38]** about this position

**[40:40]** okay

**[40:42]** yeah yeah feedback is like

**[40:44]** if you are not happy with

**[40:46]** this call right I said something

**[40:48]** what I shouldn't or maybe

**[40:50]** I did something what I should not

**[40:52]** yeah this is the feedback yeah it's like more for me

**[40:54]** as a recruiter not like about the position

**[40:56]** it's completely to

**[40:58]** improve quality of

**[41:00]** my

**[41:02]** recruitment processes in the future

**[41:04]** if I did something wrong you can tell me

**[41:06]** and I should fix this

**[41:08]** in the next calls with other

**[41:10]** candidates

**[41:12]** so calls

**[41:14]** totally fine

**[41:16]** okay

**[41:18]** so thank you very much

**[41:20]** have a nice day and see ya

**[41:22]** bye

## Сопоставление с базой

| Тип | Время | Разметка |
|-----|-------|----------|
| База | 01:41 | ✅ [[16. Опыт и soft skills#Один проект за 2–3 минуты]] |
| База | 04:50 | ⚠️ [[17. Data Python ML#RAG: retrieval-augmented generation]] · vector store |
| База | 07:13 | ❌ LangGraph nodes |
| База | 09:11 | ✅ [[02. БД - Часто#ACID и транзакции]] |
| База | 10:24 | ✅ [[02. БД - Часто#Что такое индексы БД и зачем они нужны?]] |
| База | 11:24 | ✅ [[02. БД - Часто#B-tree и физическое хранение на диске]] |
| Задача | 12:35 | 🔧 Python code review · SQL injection + conn · ✅/⚠️ |
| База | 18:57 | ⚠️ [[20. Теория программирования#Итераторы и ленивые последовательности]] |
| База | 22:24 | ✅ [[18. Python#GIL в Python]] |
| База | 23:28 | ✅ [[18. Python#multiprocessing / gunicorn workers]] |
| База | 24:06 | ✅ [[18. Python#FastAPI (основы)]] |
| База | 24:57 | ❌ streaming / typewriter |
| База | 25:54 | ⚠️ RAG · semantic chunking |
| База | 27:31 | ❌ cosine vs dot product |
| База | 28:26 | ❌ normalized embeddings |
| База | 30:41 | ❌ MCP servers |
| База | 30:54 | ⚠️ ReAct / LangGraph |
| База | 32:32 | ❌ LangGraph join |
| База | 34:56 | ❌ LLM-as-judge / observability |
| База | 35:43 | ⚠️ RAG KPIs |
| База | 36:41 | ✅ [[16. Опыт и soft skills#Вопросы к интервьюеру про продукт]] |
