---
теория: true
лайвкодинг: true
опыт: true
---

# @exbur ом оффер betica tech water

- **Специальность:** backend (Betica Tech, e-commerce/betting; интервью на английском)
- **Видео:** `@exbur ом_оффер betica_tech_water.mp4`
- **Аудио:** [@exbur ом_оффер betica_tech_water.mp3](../audio/@exbur ом_оффер betica_tech_water.mp3)
- **Длительность:** 1:42:12
- **Язык (детект):** ru
- **Модель:** faster-whisper / small
- **Распознано:** 2026-07-01 18:25 UTC
- **Разметка:** после реплики интервьюера — одна строка:
  - `> 📎 **База:** …` — **теория**; ссылка на `1–12.*.md`
  - `> 📎 **Задача:** …` — **практика** (live coding, SQL, code review)
  - Статусы: ✅ в банке, ⚠️ частично, ❌ нет, 🔧 упражнение

## Транскрипт

**[00:00]** Добро пожаловать.

**[00:02]** Вы можете называть меня Гуан, так что это будет легко для вас.

**[00:07]** Добро пожаловать, и очень добро пожаловать на этот интервью.

**[00:11]** Для этого интервью мы должны быть в 90-м секунду для интервью.

**[00:18]** Я надеюсь, что вы already aware for the long meeting.

**[00:23]** Итак, первая сессия будет кодинг-челлендж.

**[00:26]** Вы будете написать код там, и мы перейдем в два части.

**[00:31]** Первая часть будет 30 минут для написания код.

**[00:35]** И потом мы будем иметь 15 минут для Q&A и нового рекламы.

**[00:41]** И вторая сессия будет 40 минут для системы дизайн-челленджа.

**[00:49]** Для кодинг-челленджа, я вам нужно поделить

**[00:52]** ваша экрана.

**[00:54]** Так что нечувствованы, что нет AI в бакууме.

**[00:59]** Вы можете использовать любые IDE, которые вы удобны.

**[01:05]** Но просто для того, чтобы вы дизабулировали

**[01:08]** колпайлот или любые AI, которые помогут вам для написания код.

**[01:16]** Какие-то вопросы перед этим?

**[01:19]** Да, конечно.

**[01:21]** Позвольте мне создать бакуум для интервью.

**[01:27]** Окей.

**[01:46]** Я вижу вашу экран.

**[01:48]** Позвольте мне поделить эту экрана.

**[01:52]** Это будет реклама.

**[01:54]** Итак, мы имеем рекламу.

**[02:04]** Мы хотим создать SDK.
> 📎 **Задача:** 🔧 live coding: SDK симуляция сущностей (barracuda/shark/human, attack, статусы) · [[2. GO - Средне#Как устроено ООП в Go?]] · [[1. GO - Часто#Для чего используется интерфейс? / что такое / как устроен интерфейс?]]

**[02:06]** Это SDK будет очень похожа на лабораторию.

**[02:10]** Это будет рекламу.

**[02:12]** Думаю, что эти рекламу,

**[02:15]** у нас нет разработчиков в нашей организации,

**[02:18]** которые могут использовать эту.

**[02:21]** Она служит бизнес-сайт.

**[02:24]** Чтобы служить бизнес-сайт,

**[02:26]** у них может быть очень много

**[02:28]** информации.

**[02:30]** Это очень много на их сайтах.

**[02:32]** Но для нашего сайт,

**[02:34]** мы имеем лабораторию,

**[02:36]** которая не может убить лабораторию,

**[02:40]** если они будут выбирать это.

**[02:43]** Поэтому мы называем это SDK.

**[02:46]** Эти рекламы

**[02:48]** имеют,

**[02:50]** в принципе, три креатива.

**[02:52]** Сейчас,

**[02:53]** первая креатива

**[02:54]** это бакуум,

**[02:55]** вторая,

**[02:57]** вторая,

**[02:58]** человек.

**[02:59]** Другое,

**[03:00]** на креативе

**[03:02]** мы имеем,

**[03:04]** большинство них имеют бакуум,

**[03:06]** бакуум,

**[03:08]** но человек не может убить.

**[03:10]** Это requirement,

**[03:12]** который мы хотим использовать.

**[03:14]** После этого,

**[03:16]** мы хотим специфицировать

**[03:18]** тестирование.

**[03:20]** Мы хотим знать,

**[03:22]** что наш SDK

**[03:24]** может позволить эти функционации.

**[03:26]** Мы хотим,

**[03:28]** чтобы вы выживали,

**[03:30]** просто.

**[03:32]** Просто сделайте это просто.

**[03:34]** make sure that we provide

**[03:36]** the barracuda can

**[03:38]** attack the human.

**[03:40]** Shark can attack the human.

**[03:42]** And then we show the human status.

**[03:44]** For each now,

**[03:46]** please make sure you can

**[03:48]** clean the human remaining life.

**[03:50]** So that we understand

**[03:52]** how to call it working.

**[03:54]** For the life point,

**[03:56]** if there is less than zero,

**[03:58]** it should determine

**[04:00]** that the human status

**[04:02]** dead or something.

**[04:04]** That is our expectation.

**[04:06]** There is no need

**[04:08]** to be production grade.

**[04:10]** So just to make sure

**[04:12]** that you have sorted out

**[04:14]** in the way,

**[04:16]** in the correct way.

**[04:18]** And that's

**[04:20]** only expectation.

**[04:22]** Any question before we start?

**[04:24]** Let me see.

**[04:27]** Okay.

**[04:29]** So we have our

**[04:31]** game SDK.

**[04:33]** It's important.

**[04:35]** We have three creatures,

**[04:37]** barracuda shark and human.

**[04:39]** Yeah, that's right.

**[04:41]** And

**[04:43]** barracuda attacks human.

**[04:45]** Shark attacks human.

**[04:47]** Show the human status.

**[04:49]** So I assume

**[04:51]** we can do this in one file

**[04:53]** in just one main.go.

**[04:55]** No need to

**[04:57]** create additional packages.

**[04:59]** Keep it simple for now.

**[05:03]** I see.

**[05:05]** And in the end we should provide

**[05:07]** some sort of deep demo

**[05:09]** that this whole thing works.

**[05:11]** Just to demonstrate this combat flow

**[05:13]** that we can see here.

**[05:15]** Barracuda attacks human.

**[05:17]** Show the human status.

**[05:19]** Simple display.

**[05:21]** Each turn results.

**[05:23]** All right.

**[05:25]** I see.

**[05:27]** I mean the task

**[05:29]** is quite clear to me.

**[05:31]** One thing that

**[05:33]** kind of

**[05:35]** I guess

**[05:37]** needs some attention is the fact

**[05:39]** that this is like a game, you know, SDK.

**[05:41]** And you know, this like, you know,

**[05:45]** word SDK, whenever, you know, I hear

**[05:47]** SDK, it's all about

**[05:49]** making something, you know, that's

**[05:51]** going to be used by, you know,

**[05:53]** other teams.

**[05:55]** So you know, it should be like, you know, portable

**[05:57]** and stuff.

**[05:59]** Like, you know, like it's completely, you know,

**[06:01]** standalone package.

**[06:03]** Like you have the methods

**[06:05]** and

**[06:07]** like SDK

**[06:09]** sounds, you know, like something

**[06:11]** that you just give to other

**[06:13]** people, you know, and they use it

**[06:15]** without, you know, much thinking.

**[06:17]** But I guess in our case, we just

**[06:19]** want to

**[06:21]** I mean, is it going to be like an SDK

**[06:23]** in its strict definition

**[06:25]** because to me this sounds like

**[06:27]** more of

**[06:29]** just some sort of demo,

**[06:31]** not sure that I can SDK, but

**[06:33]** I might go on here.

**[06:35]** So yeah,

**[06:37]** what does it mean

**[06:39]** SDK here, like in this

**[06:41]** context, in this specific one.

**[06:47]** Basically, we would like to have some

**[06:49]** basic rules.

**[06:51]** The requirement is saying that

**[06:53]** human cannot

**[06:55]** cannot fight.

**[06:57]** So that is the rules that we would like

**[06:59]** to simulate, how we're going to

**[07:01]** simulate it.

**[07:03]** And we provide this as like

**[07:05]** SDK or

**[07:07]** the library.

**[07:09]** So that's the requirements.

**[07:11]** I see.

**[07:13]** All right.

**[07:15]** So, you know, let me just start

**[07:17]** like,

**[07:19]** you know,

**[07:21]** doing some preparation work,

**[07:23]** so to speak.

**[07:25]** Yeah, I guess,

**[07:27]** what we need

**[07:29]** that's for now

**[07:31]** tidy

**[07:33]** touch main.go

**[07:35]** and

**[07:37]** let's see,

**[07:39]** let's just create a minimal package

**[07:41]** package main

**[07:43]** and do

**[07:45]** you know the basic thing

**[07:47]** just to make sure

**[07:52]** it works and

**[07:54]** have something to work with.

**[07:56]** All right.

**[08:01]** It works.

**[08:03]** So yeah,

**[08:05]** the idea here is that

**[08:07]** we want to create

**[08:09]** basically like

**[08:11]** an entity, but with

**[08:13]** different

**[08:15]** with different

**[08:17]** how would I call this one

**[08:19]** with different

**[08:21]** properties.

**[08:26]** So we have, you know,

**[08:28]** we have our human, we have our

**[08:30]** shark and barracuda.

**[08:32]** I guess like a barracuda and shark are

**[08:34]** in their nature are the same is

**[08:36]** just the bite force that they

**[08:38]** have.

**[08:40]** But they're pretty much like, you know,

**[08:42]** the same type of entity.

**[08:44]** And

**[08:46]** yeah,

**[08:48]** we have our human who cannot bite.

**[08:50]** The first thing that I would love, I guess to

**[08:52]** you know, to do here is to create

**[08:54]** some sort of, you know, type

**[08:56]** for, like, you know, just a sort

**[08:58]** of general entity, you know, that would

**[09:00]** be applicable for both the human and

**[09:02]** the like this, you know,

**[09:04]** monster, so to speak, you know, shark

**[09:06]** or barracuda.

**[09:08]** So I would do something like

**[09:10]** let's go to like entity for now

**[09:12]** and

**[09:16]** I guess

**[09:18]** what are the minimal, like, what was

**[09:20]** the minimal, what's the minimal

**[09:22]** minimal, you know, array

**[09:24]** of, like, properties,

**[09:26]** I guess it's like name

**[09:28]** that's called string for now

**[09:30]** and it's called

**[09:32]** health or, you know, the health that it

**[09:34]** has.

**[09:36]** All right.

**[09:38]** And let's

**[09:40]** say this is going to be like our basic type,

**[09:42]** you know, the basic entity.

**[09:44]** And from this basic entity we will, you know,

**[09:46]** like an extension,

**[09:48]** you know, of the,

**[09:50]** like, of this entity

**[09:52]** and this one, these ones are actually

**[09:54]** going to be our, like, for example,

**[09:56]** barracuda or like our shark.

**[09:58]** So let's

**[10:00]** say

**[10:02]** if you have, like, our human

**[10:04]** we're just going to, like,

**[10:06]** compose it of the same,

**[10:08]** you know, like entity and if you have

**[10:10]** like our shark, let's say

**[10:12]** it's going to be the same entity,

**[10:14]** but it's also going to have, like,

**[10:16]** you know,

**[10:18]** damage,

**[10:20]** you know, field, that's going to be, like,

**[10:22]** and, you know, the same thing

**[10:24]** the same thing goes, you know, to, like,

**[10:26]** barracuda, yeah,

**[10:28]** barracuda.

**[10:39]** And yeah, it's going to be pretty much the same.

**[10:41]** So, yeah.

**[10:45]** And later, later, later,

**[10:47]** now, you know,

**[10:49]** we want to actually provide some sort of

**[10:51]** behavior for

**[10:53]** these types, you know, not like types,

**[10:55]** but for these, sort of, big entities.

**[10:57]** So

**[10:59]** I guess in our, you know, general

**[11:01]** approach in our, like, task we have,

**[11:03]** you know, globally we have someone

**[11:05]** who can attack and someone who

**[11:07]** can take this damage.

**[11:09]** So I guess, you know, we can reflect

**[11:11]** this sort of behavior, like,

**[11:13]** in interface. So let's say

**[11:15]** attacker is going to be

**[11:17]** an interface

**[11:19]** and when it does it,

**[11:21]** you know, can attack.

**[11:23]** Let's leave it,

**[11:25]** let it leave it, you know,

**[11:27]** this simplified way for now,

**[11:29]** we're going to, you know, type the actually,

**[11:31]** you know, like parameters later.

**[11:33]** And another type,

**[11:35]** another, you know, activity,

**[11:37]** another method, another interface

**[11:39]** is going to be the, like,

**[11:41]** damage taker,

**[11:43]** I would call this one.

**[11:45]** So, and

**[11:47]** this one going to, you know,

**[11:49]** just take damage.

**[11:51]** And

**[11:53]** yeah,

**[11:55]** yeah, I guess.

**[11:57]** This kind, you know,

**[11:59]** describes what we have right now.

**[12:01]** You know, the attacker can attack

**[12:03]** and the damage taker, you know, he can take

**[12:05]** the damage and

**[12:07]** now I guess we should, like, you know,

**[12:09]** implement this sort of interfaces and make

**[12:11]** sure,

**[12:13]** make sure that we don't, you know,

**[12:15]** like mess this whole thing up

**[12:17]** because we want to, you know,

**[12:19]** yeah, as you mentioned, a human,

**[12:21]** he cannot attack.

**[12:23]** So we should, you know, only assign,

**[12:25]** you know, this damage taker

**[12:27]** thing only to

**[12:29]** the entities that, you know, can actually take

**[12:31]** damage, but not attack.

**[12:33]** So

**[12:35]** let me see.

**[12:37]** I guess we can go like two ways.

**[12:39]** We can, like, you know, implement

**[12:41]** like, for example, you know,

**[12:43]** human,

**[12:45]** and

**[12:47]** allow this

**[12:49]** sort of thing, like, to take damage.

**[12:51]** But this way

**[12:53]** we're going to have to, like, repeat ourselves

**[12:55]** and then the same thing, but for, you know,

**[12:57]** shark, barcuda, entity, you know,

**[12:59]** for human.

**[13:01]** But I guess it's going to be too much,

**[13:03]** like, repetition.

**[13:05]** And anyway, you know, barcuda and shark, they also

**[13:07]** can take damage.

**[13:09]** So I would just, you know,

**[13:11]** like, delegated to the actual entity.

**[13:13]** Nice.

**[13:15]** And what's going to be,

**[13:17]** what's going to be, take damage,

**[13:19]** take damage.

**[13:21]** Well,

**[13:23]** I guess it's going to be at least, you know,

**[13:25]** we should at least specify how much damage

**[13:27]** it's going to take, how, you know, how much damage

**[13:29]** it's going to, like, have.

**[13:31]** And the entity,

**[13:33]** the idea, I guess,

**[13:35]** is that, like, you know, we should, like, do

**[13:37]** something like damage.

**[13:39]** But

**[13:41]** one thing that I can, you know,

**[13:43]** think of is that if you

**[13:45]** want to,

**[13:47]** you know,

**[13:49]** impose some sort of damage

**[13:51]** on the entity that's already dead,

**[13:53]** it's going to be, like,

**[13:55]** it's not going to be right.

**[13:57]** So I guess the first thing that we

**[13:59]** should do is to check

**[14:01]** if the entity is actually, like, you know,

**[14:03]** dead or not.

**[14:05]** And I think,

**[14:07]** yeah, we can do something like

**[14:09]** health.

**[14:11]** But I guess it's going to be even better

**[14:13]** if we introduce something,

**[14:15]** like

**[14:18]** like this one.

**[14:20]** And

**[14:22]** we're just going to return

**[14:26]** e.health.

**[14:29]** Yeah.

**[14:33]** And this way,

**[14:35]** we do this sort of

**[14:37]** gore, you know, like what it's called,

**[14:39]** like gore case or something,

**[14:41]** and, like, if it's dead,

**[14:43]** it's actually dead.

**[14:47]** We should return

**[14:49]** some sort of, you know,

**[14:51]** error.

**[14:53]** And this is going to be reflected here.

**[14:55]** And I guess it's, you know,

**[14:57]** a nice thing is to actually have

**[14:59]** some sort of, you know, domain errors.

**[15:01]** So let's call it

**[15:03]** error already

**[15:05]** already dead

**[15:07]** or something.

**[15:09]** Or

**[15:11]** entity

**[15:13]** that

**[15:17]** something of this, yeah.

**[15:19]** Entity

**[15:21]** is already

**[15:23]** dead.

**[15:25]** And we're going to return this, you know,

**[15:27]** this error here

**[15:29]** already

**[15:31]** entity is dead.

**[15:33]** Yeah.

**[15:35]** And this way we can return, you know, the new.

**[15:37]** Yeah, maybe something of this

**[15:39]** for now.

**[15:41]** Yeah.

**[15:43]** Actually, actually

**[15:45]** after this part, you know,

**[15:47]** the entity also could be,

**[15:49]** you know, the help might be less than zero,

**[15:51]** so we, you know, should check that.

**[15:53]** And we do, like, know the same check

**[15:55]** here.

**[15:57]** But this way,

**[16:05]** this way we can just set it to

**[16:07]** zero.

**[16:09]** And, yeah.

**[16:11]** All right, all right.

**[16:13]** That sounds

**[16:15]** that sounds good.

**[16:17]** What else do we have?

**[16:19]** Yeah,

**[16:21]** we have like our attack method and

**[16:25]** I guess human already implements

**[16:27]** the

**[16:31]** you know, the take damage part.

**[16:33]** And now we should move to

**[16:35]** the attack

**[16:37]** to the attack methods.

**[16:39]** You know, the ones that are

**[16:41]** going to be introduced by the shark

**[16:43]** and by, you know,

**[16:45]** we're good.

**[16:47]** Yeah.

**[16:49]** So, yeah, let's think about how we're going to

**[16:51]** approach this one if we want to attack

**[16:53]** what we can do here, what's going to be

**[16:55]** the params.

**[16:57]** I guess there, yeah,

**[16:59]** since we have like our damage, we don't need to

**[17:01]** specify like any sort of, you know, damage here.

**[17:03]** But we want to make sure

**[17:05]** who like to know who are we going to

**[17:07]** attack.

**[17:09]** So I guess we're going to like, you know, attack some sort

**[17:11]** of entity

**[17:13]** and it's going to actually be just the damage

**[17:15]** taker.

**[17:17]** Yeah.

**[17:19]** Yeah.

**[17:21]** And thus,

**[17:23]** we are going to, you know, call the method

**[17:25]** take damage inside this attack.

**[17:27]** So it's probably going to look something like

**[17:29]** let's see.

**[17:31]** So it's going to be

**[17:33]** our attack damage,

**[17:35]** our attack method is going to be

**[17:37]** let's see,

**[17:39]** like our shark.

**[17:41]** Say it's going to be shark

**[17:43]** attack.

**[17:45]** We have our entity.

**[17:47]** But it's not the entity,

**[17:49]** it's the

**[17:52]** damage taker here

**[17:54]** and it's going to return an error

**[17:56]** if anything goes wrong.

**[17:58]** So yeah, once again, I guess we should,

**[18:00]** you know, save some

**[18:02]** some sort of guard

**[18:04]** long closes here. So, you know, we don't get

**[18:06]** like in any corrupt state, so to speak.

**[18:08]** So, for example,

**[18:10]** if entity is new,

**[18:12]** we should return

**[18:14]** something

**[18:16]** like

**[18:18]** a valid

**[18:20]** entity,

**[18:36]** but some other closes that we can

**[18:38]** think of here.

**[18:40]** If our shark also, you know,

**[18:42]** if it's already dead,

**[18:44]** if it's dead,

**[18:46]** then

**[18:48]** we should also, you know,

**[18:50]** address this

**[18:52]** case.

**[18:56]** And what else might go wrong?

**[18:58]** What else might go wrong?

**[19:02]** I mean,

**[19:04]** if our damage

**[19:06]** isn't correct, even though it's a field

**[19:08]** here,

**[19:10]** but still, I guess we would love, you know,

**[19:12]** to make sure that, you know, the damage that we are going to be

**[19:14]** imposing is correct.

**[19:16]** So, let's say,

**[19:18]** if s damage

**[19:20]** is less than zero

**[19:22]** or maybe

**[19:24]** return

**[19:26]** something like a damage

**[19:28]** invalid damage

**[19:30]** or something, yeah, like this.

**[19:34]** And then add it here.

**[19:36]** Valid

**[19:43]** damage isn't valid.

**[19:47]** All right, all right.

**[19:49]** And here,

**[19:51]** here actually we can, you know, do the

**[19:53]** work, you know, do the stuff that we

**[19:55]** actually care about and it's going to be pretty much

**[19:57]** just, you know,

**[19:59]** our target entity to

**[20:01]** take the damage.

**[20:05]** Take damage.

**[20:07]** And the damage value

**[20:09]** is going to be as the damage.

**[20:11]** And it's going to return

**[20:13]** an error.

**[20:15]** Damage taker.

**[20:22]** Take damage.

**[20:24]** It doesn't return anything,

**[20:26]** but it should.

**[20:28]** Damage.

**[20:32]** And here we should specify here

**[20:34]** that it's going to be the

**[20:36]** damage.

**[20:38]** All right.

**[20:40]** And if error is not new,

**[20:46]** we're just going to return

**[20:48]** the fnt.errorf

**[20:50]** and wrap it around here

**[20:52]** and file

**[20:54]** to impose

**[20:56]** damage.

**[20:58]** And unwrap the error if there is any.

**[21:00]** All right.

**[21:03]** So at this point we

**[21:05]** imposed, you know, some damage

**[21:07]** to the entity and

**[21:09]** I guess our operation here

**[21:11]** is successful, so to speak.

**[21:15]** And I guess the same thing should be done

**[21:17]** for the

**[21:19]** for the barcuda

**[21:50]** and

**[21:52]** let me see.

**[21:54]** Okay.

**[22:00]** So probably something along these lines.

**[22:02]** And you know, we have to create

**[22:04]** our like factory methods

**[22:06]** like new

**[22:08]** new human, new

**[22:10]** new shark and new

**[22:12]** barcuda.

**[22:14]** So let me do it.

**[22:16]** Let me do it somewhere here.

**[22:18]** So

**[22:20]** new human

**[22:22]** is going to return

**[22:24]** us.

**[22:26]** Let me see.

**[22:28]** What we should return in this case.

**[22:30]** It should return like the

**[22:32]** human interface

**[22:34]** the other type of

**[22:36]** humanity

**[22:40]** defined here

**[22:50]** and we're going to just create

**[22:52]** a struct here

**[22:54]** and it's going to be entity

**[22:56]** and

**[22:58]** yeah, name is going to be

**[23:00]** string

**[23:02]** and health

**[23:04]** I guess we might, you know, just default

**[23:06]** to some like some default value

**[23:08]** for the

**[23:10]** health

**[23:12]** like people health

**[23:14]** like 100

**[23:16]** or

**[23:18]** 5.5

**[23:20]** Oh, I see, I see.

**[23:22]** So the human should be 10.

**[23:24]** All right.

**[23:26]** I guess we're just going to hard

**[23:28]** core them here for now, but I mean

**[23:30]** in the real production I guess code it's actually

**[23:32]** it's better to move them to another

**[23:34]** value, but here for you know

**[23:36]** simplicity sake

**[23:38]** just

**[23:40]** hard core them here

**[23:46]** and

**[24:11]** yeah, here

**[24:13]** all right

**[24:15]** and let's do the same thing, but for the

**[24:17]** shark

**[24:19]** and for barcuda

**[24:21]** name

**[24:23]** string

**[24:29]** shark returns

**[24:33]** shark entity

**[24:35]** name

**[24:37]** name

**[24:39]** health

**[24:41]** the health for shark is 5.

**[24:43]** and

**[24:45]** this is where we're going to, you know, specify all the damage

**[24:47]** and the damage in this case

**[24:49]** for the shark is 7.

**[24:51]** All right

**[24:53]** and the last one

**[24:55]** for the new

**[24:57]** new barcuda

**[24:59]** string

**[25:04]** barcuda

**[25:06]** entity

**[25:09]** entity

**[25:14]** and

**[25:18]** health

**[25:20]** is going to be

**[25:22]** is going to be

**[25:24]** 5.

**[25:26]** and damage

**[25:28]** is going to be

**[25:30]** is going to be

**[25:32]** also 5.

**[25:44]** I guess the overall like the draft

**[25:46]** is sort of ready

**[25:48]** but you know I might have

**[25:50]** and so I guess this just

**[25:52]** test our

**[25:54]** code.

**[25:56]** yeah let's have this

**[25:58]** simple combat flow.

**[26:00]** so

**[26:02]** let's call our human

**[26:04]** I don't know

**[26:06]** like Alex for example

**[26:08]** new

**[26:10]** human

**[26:12]** Alex in our case

**[26:14]** our shark

**[26:16]** let's call it

**[26:18]** new shark

**[26:22]** some

**[26:24]** and for barcuda

**[26:26]** I don't know what we should call

**[26:28]** barcuda let's call it

**[26:30]** like

**[26:32]** do you have any names

**[26:34]** for the barcuda

**[26:36]** any name

**[26:40]** I love

**[26:42]** that would be I know

**[26:44]** shark

**[26:46]** okay

**[26:49]** and yeah let's

**[26:51]** let's simulate our battle

**[26:53]** so

**[26:55]** what are we going to do

**[26:57]** what are we going to do

**[26:59]** barcuda attack human

**[27:01]** so we want to

**[27:03]** shark

**[27:05]** attack

**[27:07]** Alex

**[27:09]** and

**[27:13]** if there is

**[27:15]** anything

**[27:17]** just gonna

**[27:19]** just print this whole thing

**[27:23]** this

**[27:30]** after that what we should do

**[27:35]** I guess for simplicity let's just add some

**[27:39]** prints here

**[27:41]** like Alex

**[27:43]** Rex

**[27:45]** just for demonstration purposes

**[27:51]** like the initial state

**[27:53]** like after that

**[27:55]** we're gonna

**[27:57]** shark attacks human

**[27:59]** we're gonna do

**[28:01]** Rex attack

**[28:05]** Alex

**[28:07]** and also if anything goes wrong

**[28:09]** we're just gonna print this whole thing out

**[28:13]** and the last one

**[28:23]** the last one show the human stats

**[28:25]** I guess we can just

**[28:27]** I guess put it here

**[28:33]** let me see

**[28:44]** let me see I get

**[28:46]** almost like

**[28:48]** that's pretty complete

**[28:50]** but let's see if it even

**[28:52]** if it even

**[29:00]** runs

**[29:02]** alright what do we see here

**[29:04]** so what do we see here

**[29:06]** we have like our initial state

**[29:08]** Alex 10

**[29:10]** it has like half of 10

**[29:12]** Rex 5

**[29:14]** Jack 5

**[29:16]** then

**[29:18]** Jack attacks Alex

**[29:20]** and

**[29:22]** after that

**[29:24]** Rex attacks human once again

**[29:26]** and

**[29:28]** his health

**[29:31]** becomes zero

**[29:33]** that means he's

**[29:37]** I guess

**[29:39]** this doesn't work but maybe

**[29:41]** I'll address some of the

**[29:43]** edge cases

**[29:45]** but I guess it's gonna require more testing

**[29:47]** like unit testing

**[29:49]** all the combinations

**[29:51]** but

**[29:53]** yeah, this all

**[29:55]** like a solution

**[29:57]** at least the minimum one

**[29:59]** okay

**[30:01]** now could you copy me

**[30:03]** the code

**[30:05]** and then put it in the meeting chat

**[30:07]** yeah

**[30:09]** there's two questions before we

**[30:19]** start the new requirement

**[30:21]** but I will get your code first

**[30:23]** okay thank you

**[30:25]** so

**[30:27]** first of all

**[30:29]** because you have the function

**[30:31]** called is that

**[30:33]** I will see

**[30:35]** you

**[30:37]** call it yet

**[30:39]** do you have

**[30:41]** the reason why you add it
> 📎 **База:** ✅ [[2. GO - Средне#Как устроено ООП в Go?]] · зачем метод isDead() vs проверка health-полей

**[30:43]** I mean it's just

**[30:45]** you know a standard good practice

**[30:47]** like you know

**[30:49]** what would be the other way to

**[30:51]** you know check

**[30:53]** someone is that

**[30:55]** I guess it's gonna be like

**[30:57]** checking the health

**[30:59]** and like doing something like s.health

**[31:01]** here or like b.health

**[31:03]** and it's just gonna be

**[31:05]** repeating the same functionality across

**[31:07]** different methods

**[31:09]** and

**[31:11]** it's actually going back to the whole

**[31:13]** domain driven design

**[31:15]** we want

**[31:17]** I mean this is the reason

**[31:19]** I used here name

**[31:21]** but you know from the you know like

**[31:23]** small letter here because you know

**[31:25]** this way our fields are

**[31:27]** unexported and we only

**[31:29]** you know interact with our like entities

**[31:31]** we are methods that we define

**[31:33]** so I feel like it's you know

**[31:35]** just like you know a good practice and it's like

**[31:37]** safe to do so and

**[31:39]** yeah I mean this is

**[31:41]** how it's done in production

**[31:45]** how about back to the

**[31:47]** requirement saying like

**[31:49]** would you check the requirement again

**[31:51]** let's see

**[31:53]** regarding the

**[32:00]** give me

**[32:06]** the requirement you mean here like the table

**[32:08]** or the

**[32:10]** yeah

**[32:12]** what are you trying to say here exactly

**[32:14]** like the requirement in terms of the table

**[32:16]** or the combat flow

**[32:18]** combat flow

**[32:20]** but you repeat it

**[32:22]** yeah

**[32:24]** let's see

**[32:29]** Berkeley attacks human

**[32:31]** shark attacks

**[32:33]** human

**[32:35]** yeah

**[32:37]** human stats

**[32:44]** I don't know I might be missing something

**[32:46]** but like

**[32:48]** Berkeley attacks human

**[32:50]** yeah this is our junk

**[32:52]** he attacks Alex

**[32:54]** then shark attacks human

**[32:56]** and we show like the stats

**[32:58]** just show

**[33:00]** the human status

**[33:02]** is it dead or still alive

**[33:04]** oh yeah

**[33:06]** yeah

**[33:08]** yeah

**[33:10]** I mean

**[33:12]** let's do something like

**[33:14]** we already have the function

**[33:16]** for checking that

**[33:18]** yeah

**[33:20]** it's Alex

**[33:22]** dead

**[33:24]** something like

**[33:26]** we here

**[33:28]** Alex

**[33:31]** is dead

**[33:33]** okay

**[33:35]** yeah could you learn it

**[33:37]** yep sure

**[33:43]** okay

**[33:45]** then

**[33:47]** the second question is
> 📎 **База:** ✅ [[1. GO - Часто#Для чего используется интерфейс? / что такое / как устроен интерфейс?]] · что будет при добавлении нового attacker (tiger, t-rex)

**[33:49]** if we add more

**[33:51]** attacker what's gonna happen

**[33:53]** to this code

**[33:56]** if we're gonna

**[33:58]** if we're gonna what

**[34:00]** add new attacker

**[34:02]** it's not balacuda it's not char

**[34:04]** maybe it's

**[34:06]** tlex

**[34:08]** or maybe it's

**[34:10]** tiger

**[34:12]** what is gonna happen

**[34:14]** to this code

**[34:18]** I guess we're just gonna have to implement

**[34:20]** a new type

**[34:22]** like type

**[34:24]** type tiger

**[34:26]** defined as a new struct

**[34:28]** and creating a function

**[34:30]** and make it

**[34:32]** implement the attack

**[34:34]** the attack method

**[34:36]** so this is how it's gonna look like

**[34:38]** that's it

**[34:45]** and

**[34:47]** I guess I should like

**[34:49]** send the

**[34:51]** but yeah for

**[34:53]** for the entity

**[34:55]** you use as entity

**[34:57]** you not use as human

**[34:59]** why the attacker you use as the

**[35:01]** for each

**[35:03]** yeah good impression

**[35:05]** repeat that once again

**[35:07]** so for the human

**[35:09]** for the human I use entity

**[35:11]** but for the

**[35:13]** yeah good impression

**[35:15]** repeat that once again

**[35:17]** could you score down to

**[35:19]** get take damage

**[35:21]** function

**[35:23]** take damage function

**[35:25]** take damage

**[35:27]** yeah

**[35:29]** so

**[35:31]** take damage

**[35:33]** you use the entity

**[35:35]** you didn't use human

**[35:37]** isn't it

**[35:39]** what is difference

**[35:41]** between

**[35:43]** for the attack right

**[35:45]** you use

**[35:47]** individual

**[35:49]** each balacuda and char

**[35:53]** what is different

**[35:55]** why we need to create

**[35:57]** the attack function

**[35:59]** what individual

**[36:01]** each of them

**[36:06]** I guess this is by design

**[36:08]** because

**[36:10]** we assume that human cannot attack

**[36:12]** but

**[36:14]** it takes the damage

**[36:16]** and so

**[36:18]** so do all the other entities

**[36:20]** like the char

**[36:22]** they all can take damage

**[36:24]** but the difference is that human cannot

**[36:26]** he cannot attack

**[36:28]** so we just

**[36:30]** not encapsulate

**[36:32]** but since we are talking about

**[36:34]** I mean yeah

**[36:36]** because

**[36:38]** Golang is not really an OP

**[36:40]** strict

**[36:42]** don't really follow the

**[36:44]** old fashioned OP

**[36:46]** practices but still

**[36:48]** we

**[36:50]** use composition here

**[36:52]** and

**[36:54]** we

**[36:56]** so basically

**[36:59]** we put entity

**[37:01]** like inside the human

**[37:03]** so to speak

**[37:05]** but the

**[37:07]** if you go back to the function

**[37:09]** you use entity you didn't use human

**[37:11]** yeah

**[37:13]** I mean

**[37:15]** why human uses this method

**[37:17]** because it implements it

**[37:19]** because

**[37:21]** yeah

**[37:23]** human consists of

**[37:25]** the entity

**[37:27]** and since entity has this method

**[37:29]** it's like you know gets promoted

**[37:31]** to the human and thus

**[37:33]** we can use the human

**[37:35]** human can use all the methods

**[37:37]** that entity

**[37:39]** provides

**[37:41]** so yeah

**[37:43]** Chinese also implement

**[37:45]** on the shark and balacuda

**[37:47]** I mean

**[37:49]** yeah I mean

**[37:53]** yeah I mean yeah shark and balacuda

**[37:55]** they also do have you know these methods because

**[37:57]** yeah they get promoted

**[37:59]** and do you have like another question

**[38:01]** I might interrupt it you there

**[38:03]** so you couldn't please repeat that

**[38:05]** so

**[38:09]** there is an attacker

**[38:11]** right so this shark and balacuda

**[38:13]** is an attacker behavior

**[38:17]** so my question is
> 📎 **База:** ✅ [[2. GO - Средне#Как устроено ООП в Go?]] · общий тип attacker vs отдельные shark/barracuda

**[38:19]** instead of use as individual

**[38:21]** shouldn't we create

**[38:23]** new type of

**[38:25]** stock

**[38:27]** for attacker

**[38:29]** instead of shark has damage

**[38:31]** and instead of type

**[38:33]** balacuda have damage

**[38:37]** so you mean we should have some sort of

**[38:39]** you know like the same approach

**[38:41]** like with entity

**[38:43]** but for the

**[38:45]** so

**[38:47]** yeah I guess I

**[38:49]** I guess I might start to

**[38:51]** understand what I try to say here

**[38:53]** so we don't really want to

**[38:55]** we don't really

**[38:57]** want to

**[38:59]** create

**[39:01]** like new types

**[39:03]** so yeah if we have like you know

**[39:05]** you know in the worst case scenario

**[39:07]** like 100

**[39:09]** you know more like monsters like you know

**[39:11]** tigers like bears

**[39:13]** and in this case we will have to

**[39:15]** implement each of them like separately

**[39:17]** and this is like not the most

**[39:19]** optimal solution here

**[39:21]** uh

**[39:23]** yeah I guess

**[39:25]** I guess that

**[39:27]** that might be

**[39:29]** that might be

**[39:31]** that's viable yeah that's for sure

**[39:33]** but

**[39:38]** okay to understand

**[39:40]** how we would how we would

**[39:42]** implement that

**[39:44]** I guess

**[39:46]** I guess we would define some other

**[39:48]** struct

**[39:50]** like

**[39:54]** like entity

**[39:56]** as well

**[39:58]** it's gonna be like you know some sort of like core entity

**[40:00]** and

**[40:02]** we will still have you know our

**[40:04]** like interfaces like

**[40:06]** here but

**[40:08]** so basically

**[40:10]** we want to combine

**[40:12]** um

**[40:14]** like the attack method

**[40:16]** um

**[40:18]** let me see let me see I mean

**[40:20]** I guess okay yeah that's

**[40:22]** that's probably doable but

**[40:24]** I might be like lost in the details

**[40:26]** right now but I guess

**[40:28]** it's okay

**[40:30]** it's the same way that it did for the

**[40:32]** human and entity so you just

**[40:34]** have another type of struct for the attack

**[40:36]** behavior and then you use

**[40:38]** the interface for the attack behavior

**[40:40]** so

**[40:42]** there's a new requirement coming in

**[40:44]** and saying that you need to implement

**[40:46]** snakes

**[40:48]** this next they have another

**[40:50]** they have here saying that they have

**[40:52]** question so

**[40:54]** you don't need to write a code

**[40:56]** it just give me the idea or

**[40:58]** maybe pseudo code

**[41:00]** how we gonna integrate

**[41:02]** with this SDK

**[41:04]** so yeah the question is

**[41:07]** how to

**[41:09]** how to

**[41:11]** could you please repeat that once again

**[41:13]** so there's a next

**[41:15]** that we would like to implement right

**[41:17]** and snake has a

**[41:19]** question so the question

**[41:21]** um

**[41:23]** the effect is different from just

**[41:25]** only attack right imagine

**[41:27]** that you got snake back to

**[41:29]** what gonna happen to yourself

**[41:31]** let me know if you still follow

**[41:36]** okay

**[41:38]** then

**[41:40]** yeah

**[41:42]** please also repeat before you

**[41:44]** start um so

**[41:46]** we would like to implement this

**[41:48]** in this SDK

**[41:50]** could you give me

**[41:52]** how to

**[41:54]** integrate with this

**[41:58]** integrate

**[42:02]** integrate let me see

**[42:04]** let me see integrate

**[42:08]** well

**[42:12]** in this current version

**[42:14]** how we do how we

**[42:16]** how do we implement this snake

**[42:18]** so yeah I guess

**[42:22]** we're gonna have like our

**[42:24]** our

**[42:28]** poison

**[42:30]** but it should be like a new

**[42:32]** sort of method

**[42:36]** hmm

**[42:38]** we have our snake so yeah

**[42:40]** for sure we're gonna like define our snake

**[42:42]** it's also gonna be like an entity

**[42:44]** it's gonna have

**[42:46]** its own like name, health etc

**[42:48]** but it's gonna have

**[42:50]** I guess some sort of

**[42:52]** other

**[42:54]** I mean

**[42:56]** the attack

**[42:58]** the attack is gonna be pretty much the same

**[43:00]** I guess

**[43:02]** but we should like create

**[43:04]** a new maybe interface

**[43:06]** not for the damage

**[43:08]** not for the damage taker

**[43:10]** but for the maybe like you know poison

**[43:12]** taker because like you know

**[43:14]** poison might have some other effects

**[43:16]** maybe you know it's not like just

**[43:18]** you know one

**[43:20]** like you know one shot of damage

**[43:22]** might be like lasting

**[43:24]** so I guess it's gonna be like another

**[43:26]** another type so to speak

**[43:28]** of the damage so

**[43:30]** maybe like poison taker

**[43:32]** and we might

**[43:34]** and we

**[43:36]** and we

**[43:38]** like take poison

**[43:40]** and we

**[43:42]** I don't know let's say it's gonna be like poison

**[43:44]** of type poison some sort of

**[43:46]** and we're gonna make sure that

**[43:48]** all the other like human for example

**[43:50]** you know it takes poison and you know

**[43:52]** maybe provide some

**[43:54]** effects

**[43:56]** something like this I guess

**[43:58]** yeah that might be viable

**[44:00]** and what happen if snake

**[44:02]** by two different target

**[44:04]** how do you

**[44:06]** attack the poison state

**[44:08]** what happens if

**[44:10]** the if the snake

**[44:12]** poisons two different

**[44:14]** targets

**[44:16]** mm-hmm they bite

**[44:18]** two different target

**[44:20]** let me see

**[44:23]** two different targets

**[44:30]** well

**[44:32]** I guess the most straightforward way is that

**[44:34]** each of the

**[44:36]** targets

**[44:38]** it should like call the

**[44:40]** take poison method

**[44:42]** mm-hmm

**[44:44]** I guess that's

**[44:46]** that's the way it's gonna be

**[44:48]** but

**[44:50]** how do you track them

**[44:54]** how do I track them

**[44:59]** mm-hmm yeah because

**[45:01]** after you apply the poison

**[45:04]** you need to track

**[45:06]** mm-hmm

**[45:08]** mm-hmm

**[45:12]** well

**[45:14]** I guess it gets a bit more complicated

**[45:16]** because now we should have like some sort of

**[45:18]** state that we can you know track

**[45:20]** track and

**[45:22]** we have to store

**[45:24]** this sort of state somewhere

**[45:26]** like

**[45:28]** I mean

**[45:30]** I guess it's

**[45:32]** more to like you know how games work

**[45:34]** I guess from like from my

**[45:36]** from my you know probably like restricted knowledge

**[45:38]** of how you know game

**[45:40]** game works like there is some sort of you know

**[45:42]** like global loop you know that

**[45:44]** you know like does all the

**[45:46]** ticking and like you know there is some sort of you know

**[45:48]** maybe like background processes that you know

**[45:50]** check what's going on you know with

**[45:52]** all the entities and like updates it

**[45:54]** I mean if

**[45:56]** you know linear towers like some sort of you know

**[45:58]** like game design I guess this is how it's done there

**[46:00]** like you know there's some sort of you know background

**[46:02]** process you know the tracks all the

**[46:04]** like states of all the entities

**[46:06]** and thus updates

**[46:08]** them so

**[46:10]** yeah probably something like this yeah

**[46:12]** yeah

**[46:16]** if you

**[46:18]** can imagine

**[46:20]** like real world let's say

**[46:22]** you got pipe from the snake

**[46:24]** what gonna happen

**[46:26]** could you like give me some pose here

**[46:28]** what gonna happen to yours

**[46:30]** what gonna happen to me

**[46:32]** in case of what

**[46:34]** after you got

**[46:36]** bite from this snake

**[46:38]** well I guess you're gonna be

**[46:40]** you're gonna be

**[46:42]** you're gonna be

**[46:44]** under the

**[46:46]** under the effect of the poison

**[46:48]** and

**[46:50]** if you don't act like you know soon

**[46:52]** if you don't act you know in a rapid like fashion

**[46:54]** you probably gonna die

**[46:56]** you have to do with the you know with the poison

**[46:58]** so it's gonna be I guess like in the terms of

**[47:00]** like our current code

**[47:02]** there's gonna be like

**[47:04]** minus one

**[47:06]** point of health every second

**[47:08]** and until you know it becomes zero

**[47:10]** so it's gonna be like like some sort of

**[47:12]** might be potential

**[47:14]** like some sort of you know

**[47:16]** job you know background job

**[47:18]** that like you know decreases your health like you know like

**[47:20]** debuff you know yeah

**[47:22]** so you're gonna like your health is gonna decrease

**[47:24]** like each second for example

**[47:26]** until you know it reaches

**[47:28]** zero or if you like take some

**[47:30]** measure and you know mitigate the effects

**[47:32]** of the poison maybe you know

**[47:34]** like drink some you know poison or

**[47:36]** something like that and yeah

**[47:38]** yeah so yeah I guess

**[47:40]** that's that's how it's how it's gonna look like

**[47:42]** that exactly so

**[47:44]** the developers they can run

**[47:46]** the world by the times

**[47:48]** so we depends on the times and then

**[47:50]** the trigger every time

**[47:52]** that's the world running

**[47:54]** it's ticked up and the poison gonna

**[47:56]** call maybe

**[47:58]** from the buff

**[48:00]** maybe from the buff

**[48:02]** it's depends on how

**[48:04]** we gonna step but that's the

**[48:06]** exactly what I'm expected

**[48:08]** basically

**[48:10]** we're gonna have

**[48:12]** the second session

**[48:14]** let's

**[48:16]** do you have any kind of throwing

**[48:18]** tools that you're familiar with

**[48:20]** I guess

**[48:22]** it's pretty basic

**[48:24]** okay

**[48:26]** could you

**[48:28]** share the screen and open that

**[48:30]** yep yep sure

**[48:32]** give me a sec

**[48:34]** yep

**[48:52]** it should be

**[48:54]** it should be

**[48:58]** with

**[49:00]** okay

**[49:02]** now we're going to

**[49:04]** have system design
> 📎 **Задача:** 🔧 system design: e-commerce (корзина, inventory, promotion, payment gateway), Black Friday 10M concurrent · [[9. Архитектура#Монолит vs микросервисы]] · [[9. Архитектура#CQRS — когда уместен]] · [[12. Опыт и soft skills#Опыт с брокерами сообщений и Kafka]]

**[49:06]** right

**[49:08]** give me a second

**[49:10]** so

**[49:12]** we would like to

**[49:14]** decide for the e-commerce

**[49:16]** I think you already

**[49:18]** familiar with it so your

**[49:20]** resume has mentioned that you

**[49:22]** have worked with e-commerce before
> 📎 **База:** ✅ [[12. Опыт и soft skills#Опыт с e-commerce]]

**[49:24]** so basically

**[49:26]** we would like to

**[49:28]** decide for the e-commerce

**[49:30]** that's going to support it back

**[49:32]** and for this

**[49:34]** coding challenge

**[49:36]** system design challenge

**[49:38]** we

**[49:40]** will

**[49:42]** need to design

**[49:44]** and know the critical part of the system

**[49:48]** to let it more easier

**[49:50]** because we have the limit of time

**[49:52]** so I will scope down

**[49:54]** the e-commerce

**[49:56]** let's say we going to focus on the card

**[49:58]** the card that

**[50:00]** we can add or remove

**[50:02]** the products

**[50:04]** then the second component is

**[50:06]** inventories

**[50:08]** the warehouse that we use for store

**[50:10]** the number of the products

**[50:12]** and the last one is about

**[50:14]** the promotion

**[50:16]** there is the external

**[50:18]** dependency that you will need to mention

**[50:20]** as well as your payment gateway

**[50:22]** you can leave

**[50:24]** it as external service that we

**[50:26]** are going to call and then it's going

**[50:28]** to return as yes or no

**[50:30]** yes mean

**[50:32]** the payment gateway accept that

**[50:34]** time section

**[50:36]** no means it's going to reject

**[50:38]** that time section and I would

**[50:40]** like

**[50:42]** to know the flow

**[50:44]** or interaction

**[50:46]** how we can handle

**[50:48]** don't respond

**[50:52]** now back to our

**[50:54]** e-commerce

**[50:56]** so

**[51:00]** I will let you reorder

**[51:02]** a little bit

**[51:04]** so we would like to have

**[51:06]** support the back Friday

**[51:08]** so it's going to be very crazy

**[51:10]** volumes during that time right

**[51:14]** I will give you some black number

**[51:16]** so you have the idea and you

**[51:18]** can walk me to

**[51:20]** we going to have 10

**[51:22]** million concurrent users

**[51:26]** which users monthly

**[51:28]** daily

**[51:30]** concurrent

**[51:33]** concurrent mean active user

**[51:35]** during that time

**[51:37]** okay

**[51:41]** then

**[51:43]** we have

**[51:45]** 100,000 SKU

**[51:47]** SKU means stop

**[51:49]** cheap unit

**[51:51]** then

**[51:53]** we going to have

**[51:55]** 50,000 check out

**[51:57]** a minute

**[51:59]** at the peak time

**[52:04]** 50,000 check out

**[52:06]** at the

**[52:08]** the same time

**[52:10]** peak time

**[52:12]** but at the same time

**[52:19]** the expectation

**[52:21]** from this design

**[52:23]** I would like to see the diagram of the service

**[52:27]** the database schema

**[52:29]** how you going to decide

**[52:31]** and the solution

**[52:33]** how to prevent the less condition

**[52:35]** any trace of analysis

**[52:37]** for the real times

**[52:41]** once again

**[52:43]** how to prevent

**[52:45]** raise conditions

**[52:47]** yes

**[52:49]** correct

**[52:52]** and trade off

**[52:54]** of the real times because we would like to handle

**[52:56]** its real times

**[53:03]** alright

**[53:05]** we want to design a system

**[53:07]** that's going to have a card

**[53:09]** we already have

**[53:11]** some

**[53:13]** warehouse is going to be an external system

**[53:15]** I guess

**[53:17]** some other service

**[53:19]** internal

**[53:21]** service warehouse

**[53:23]** warehouse is our internal

**[53:25]** internal

**[53:27]** warehouse

**[53:29]** we want to design a card

**[53:31]** warehouse

**[53:33]** and this external service yes for no

**[53:35]** what does it mean exactly

**[53:37]** this elaboration

**[53:39]** yeah

**[53:41]** the payment get very

**[53:45]** the payment

**[53:47]** yeah

**[53:49]** I'm not quite sure

**[53:51]** so I think

**[53:53]** one of the reason is missing here

**[53:55]** so the first one is card

**[53:57]** I'll remove item just that's correct

**[53:59]** the second one is inventory

**[54:01]** of warehouse that you got it here

**[54:05]** the third one is full-motion

**[54:07]** Это репортение, то есть это как какой-то так, как даже дискал, как какой-то, как 50%.

**[54:19]** Это сейчас правильно?

**[54:21]** Телее того, это лампорат ли.

**[54:24]** А, лампорат ли.

**[54:25]** Т items.

**[54:28]** Итак.

**[54:31]** И final one for the external services is payment gateway.

**[54:37]** А, с Ваймэнгейтвей.

**[54:39]** Ваймэнгейтвей.

**[54:43]** Ваймэнгейтвей.

**[54:46]** Ваймэнгейтвей.

**[54:48]** Слышно.

**[54:50]** Слышно.

**[54:52]** Так, это...

**[54:54]** Да, да, да.

**[54:56]** Так, как 30 минут.

**[54:58]** Все, давайте посмотрим, что мы можем делать здесь.

**[55:00]** В нашей таймфрейме, так сказать.

**[55:02]** Да, я думаю, что я бы хотел,

**[55:04]** может быть, разобраться на

**[55:06]** системах,

**[55:08]** на системах.

**[55:10]** Так, это будет как карта.

**[55:12]** Мы хотим, знаете,

**[55:14]** добавить еще

**[55:16]** как-то, как-то, добавить

**[55:18]** элементы к карту, убрать их.

**[55:20]** У нас есть варху.

**[55:22]** Так, да.

**[55:24]** Мы собираем все элементы,

**[55:26]** как в интернете.

**[55:28]** Так что, это будет с целью

**[55:30]** current design, это правильно?

**[55:32]** Да.

**[55:34]** Хорошо.

**[55:36]** И у нас есть, как говорится,

**[55:38]** promotion.

**[55:40]** И external service

**[55:42]** for the payment.

**[55:44]** Все, у нас есть

**[55:46]** non-functional requirements

**[55:50]** for 10 million concurrent users.

**[55:52]** 100 000

**[55:54]** SKUs.

**[55:56]** 50K checkout

**[55:58]** at the same time.

**[56:00]** И мы хотим, как-то,

**[56:02]** видеть,

**[56:04]** по схему и так далее.

**[56:06]** Ну,

**[56:08]** давайте посмотрим.

**[56:10]** Я думаю, что у нас есть

**[56:12]** интернета

**[56:14]** в системе.

**[56:16]** Так что, сервисная

**[56:18]** компонента.

**[56:20]** Не только для DB-схемы,

**[56:22]** но и для сервиса.

**[56:24]** Да,

**[56:26]** конечно.

**[56:28]** Да, конечно.

**[56:30]** Ну, давайте посмотрим.

**[56:32]** И в том числе, которые будут

**[56:34]** быть Web, Mobile

**[56:36]** или как-то так.

**[56:40]** Мы можем специфицировать Web

**[56:42]** первым?

**[56:51]** Да, Web первым.

**[56:53]** Да, да.

**[56:55]** В том числе клиентов, это будет

**[56:57]** Web, Mobile,

**[56:59]** как-то и так далее.

**[57:05]** Я думаю, что,

**[57:07]** как-то и так далее.

**[57:09]** Я думаю, что мы хотим

**[57:11]** в первую очередь designed some sort of MVP.

**[57:13]** И,

**[57:15]** after that, we're going to move

**[57:17]** to our scaling

**[57:19]** stuff, how we're going to

**[57:21]** implement, how we're going to support

**[57:23]** the concurrent users.

**[57:25]** Я думаю, что

**[57:27]** давайте начнем с simplifying

**[57:29]** for now.

**[57:31]** И давайте

**[57:33]** just define our core

**[57:35]** entities,

**[57:37]** core entities.

**[57:39]** This is what they're going to be.

**[57:41]** It's going to be a user,

**[57:43]** for sure.

**[57:45]** It's going to be a car.

**[57:47]** It's going to be an item.

**[57:49]** That's definitely

**[57:51]** solved.

**[57:53]** And probably,

**[57:55]** like a promotion.

**[57:57]** Since there might be different types

**[57:59]** of the promotions.

**[58:01]** It might be Bogo, but

**[58:03]** who knows if in the future we might

**[58:05]** add something else.

**[58:07]** Yeah.

**[58:09]** And

**[58:11]** let me see.

**[58:13]** User card item promotion

**[58:15]** card item

**[58:19]** item should be called item.

**[58:21]** I think actually,

**[58:23]** yeah, the idea

**[58:25]** is that item

**[58:27]** might not necessarily be

**[58:29]** like

**[58:33]** from my like commerce

**[58:35]** experience.

**[58:37]** Item

**[58:39]** could be one product,

**[58:41]** but one product can have

**[58:43]** several,

**[58:45]** I mean, we can add three,

**[58:47]** for example,

**[58:49]** keyboards in our card.

**[58:51]** And this is going to be one product,

**[58:53]** but three items.

**[58:55]** So I would call this one also a separate entity.

**[58:57]** So we're going to have our product

**[58:59]** and the item is going to be the exact one

**[59:01]** that we are going to add

**[59:03]** into the card,

**[59:05]** so to speak.

**[59:07]** So yeah,

**[59:09]** this could be

**[59:11]** our entities.

**[59:13]** And

**[59:15]** what else do we have here?

**[59:17]** And in terms,

**[59:19]** I guess of the system

**[59:21]** as well,

**[59:23]** the general properties

**[59:25]** is that

**[59:27]** we want to prioritize

**[59:29]** the

**[59:31]** correct values,

**[59:33]** because

**[59:35]** people will buy stuff

**[59:37]** and it's all about money

**[59:39]** and we want to make sure

**[59:41]** that we do not mess up.

**[59:43]** And I guess for the most part

**[59:45]** it's going to be like a read heavy system

**[59:47]** because I guess people do

**[59:49]** look in their cards

**[59:51]** much more often

**[59:53]** than they actually buy,

**[59:55]** like they add products,

**[59:57]** but the actual

**[59:59]** payment

**[01:00:01]** will be done later.

**[01:00:03]** And also I guess we would love

**[01:00:05]** to make sure that all the logic

**[01:00:07]** stays on the backend.

**[01:00:09]** We don't actually want to outsource

**[01:00:11]** any sort of things to the front end

**[01:00:13]** because otherwise there's going to be

**[01:00:15]** some duplication of logic.

**[01:00:17]** So yeah, we should

**[01:00:19]** move all our business logic

**[01:00:21]** to the backend

**[01:00:23]** and the front end

**[01:00:25]** will just render whatever

**[01:00:27]** we are providing them.

**[01:00:29]** Okay.

**[01:00:31]** And I guess

**[01:00:33]** about the card,

**[01:00:35]** we want to make sure that our card

**[01:00:37]** like,

**[01:00:39]** as I mentioned before,

**[01:00:41]** the data should be valid.

**[01:00:43]** We don't really want to any card updated there

**[01:00:45]** because your card is the most

**[01:00:47]** probably important thing.

**[01:00:49]** And yeah,

**[01:00:51]** I guess

**[01:00:53]** let's define some sort of rest API

**[01:00:55]** I think in the current case

**[01:00:57]** rested the most straightforward

**[01:00:59]** and we don't really need

**[01:01:01]** to over complicate this for now.

**[01:01:03]** So yeah.

**[01:01:05]** I guess there's going to be

**[01:01:07]** also sort of card API

**[01:01:09]** like we want

**[01:01:11]** card.

**[01:01:13]** When we are going to

**[01:01:15]** like for example post method

**[01:01:17]** if we want to add something to the card

**[01:01:19]** like yet, if we want to see the card.

**[01:01:21]** What is it?

**[01:01:25]** What is it?

**[01:01:27]** And

**[01:01:31]** for the payment

**[01:01:35]** probably something like

**[01:01:37]** one card like

**[01:01:39]** check out or something.

**[01:01:43]** Yeah.

**[01:01:45]** I mean, I guess I'm not going to

**[01:01:47]** spend too much time here on the like exact

**[01:01:49]** like fields and stuff

**[01:01:51]** but this is like the rough idea

**[01:01:53]** what does it look like.

**[01:01:55]** Yeah.

**[01:01:57]** So for the post card

**[01:01:59]** and post card

**[01:02:01]** check out

**[01:02:03]** the first one is

**[01:02:05]** to add new item

**[01:02:07]** or

**[01:02:09]** it's to create

**[01:02:11]** like the card

**[01:02:13]** or

**[01:02:15]** you know

**[01:02:17]** if the user doesn't have

**[01:02:19]** like any items in its card

**[01:02:21]** this is like

**[01:02:23]** how we're going to create a new card

**[01:02:25]** because like cards is going to be like a separate entity

**[01:02:27]** like a collection of items

**[01:02:29]** that the user currently has

**[01:02:31]** so yeah it's going to be like

**[01:02:33]** creates a new card

**[01:02:35]** this one

**[01:02:37]** get card

**[01:02:39]** yeah we should actually

**[01:02:41]** specify which one

**[01:02:45]** because you know

**[01:02:47]** there are going to be a lot of cards and we want to

**[01:02:49]** use the one that the user actually has

**[01:02:51]** and you know we're going to define

**[01:02:53]** what the card ID is

**[01:02:55]** by using the like you know some sort of authentication

**[01:02:57]** key you know get the user ID

**[01:02:59]** from like from the header

**[01:03:01]** and determine what's going to be

**[01:03:03]** the card that you know belongs to this user

**[01:03:05]** but yeah I guess a bit more technical

**[01:03:07]** yeah

**[01:03:11]** I guess here

**[01:03:13]** we can also do something

**[01:03:15]** like

**[01:03:17]** card

**[01:03:20]** ID

**[01:03:22]** because we want to make sure

**[01:03:24]** that we have

**[01:03:26]** how to

**[01:03:28]** how we're going to add the items

**[01:03:30]** as well so probably

**[01:03:32]** it's going to look like card

**[01:03:34]** ID

**[01:03:36]** and

**[01:03:38]** how we're going to send

**[01:03:40]** our like items

**[01:03:42]** yeah I guess

**[01:03:44]** something like this yeah so we're going to basically

**[01:03:46]** like add an item to the

**[01:03:48]** you know existing card

**[01:03:50]** and

**[01:03:53]** something along the lines

**[01:03:55]** you know like delete the same thing

**[01:03:57]** alright

**[01:03:59]** don't depend much on

**[01:04:01]** yeah yeah yeah sure

**[01:04:05]** so yeah about the database

**[01:04:07]** schema

**[01:04:09]** let me see you know I still would have

**[01:04:11]** to

**[01:04:13]** to start with the like

**[01:04:15]** with the overall design

**[01:04:17]** so let's just start

**[01:04:19]** with like our

**[01:04:21]** client here

**[01:04:23]** then we're going to have for now

**[01:04:25]** some sort of like you know

**[01:04:27]** you know

**[01:04:29]** monolith for now

**[01:04:31]** if we you know we're doing MVP

**[01:04:33]** for now it's going to be like

**[01:04:35]** service here

**[01:04:37]** for the

**[01:04:39]** like

**[01:04:41]** how to how to call this one

**[01:04:43]** uh

**[01:04:45]** monolith

**[01:04:47]** it's actually going to be like

**[01:04:49]** card service

**[01:04:53]** so yeah it's going to be our card service

**[01:04:55]** and yeah this is like

**[01:04:57]** this is where we're going to do all the

**[01:04:59]** interactions with like with the card

**[01:05:01]** and there should be some sort of

**[01:05:03]** you know database

**[01:05:05]** and for now

**[01:05:09]** I would call

**[01:05:11]** like postgres for now

**[01:05:13]** you know for the

**[01:05:15]** like for the you know like transactions

**[01:05:17]** you know asset operations and stuff

**[01:05:19]** so yeah for now

**[01:05:21]** let's see

**[01:05:23]** there are going to be like our main components

**[01:05:25]** for now

**[01:05:27]** client, postgres

**[01:05:29]** and the monolithic structure

**[01:05:33]** and

**[01:05:35]** I guess

**[01:05:37]** I mean

**[01:05:39]** we don't really have like a lot of services right now

**[01:05:41]** here but just for you know

**[01:05:43]** good measure you know add some

**[01:05:45]** sort of like you know API gateway

**[01:05:47]** here for the authentication

**[01:05:49]** stuff

**[01:05:51]** because later we will probably you know add some more services

**[01:05:53]** so yeah in the first like

**[01:05:55]** in the first iteration

**[01:05:57]** I think

**[01:05:59]** this might be like

**[01:06:03]** enough for now

**[01:06:05]** and let's talk about

**[01:06:07]** more of the like

**[01:06:09]** postgres

**[01:06:11]** like you know

**[01:06:13]** DB schema

**[01:06:15]** I guess I'm not gonna like you know

**[01:06:17]** write you know the

**[01:06:19]** exact like fields

**[01:06:21]** but you know our

**[01:06:23]** our postgres is gonna

**[01:06:25]** store some sort of you know like

**[01:06:27]** card is gonna store

**[01:06:29]** for example

**[01:06:31]** card items

**[01:06:33]** is gonna store

**[01:06:35]** our

**[01:06:37]** products, promotions

**[01:06:39]** so pretty much the same thing

**[01:06:41]** that as we mentioned before

**[01:06:43]** promotions

**[01:06:45]** and

**[01:06:49]** yeah and we can also

**[01:06:51]** while we are

**[01:06:53]** added we can add some

**[01:06:55]** a bit of optimization

**[01:06:57]** here is to like

**[01:06:59]** in the potency keys here

**[01:07:01]** just to make sure

**[01:07:03]** that our like you know requests

**[01:07:05]** you know if there is like

**[01:07:07]** the same requests

**[01:07:09]** we can like you know return the data

**[01:07:11]** and you know

**[01:07:13]** not to corrupt the data so to speak

**[01:07:15]** so yeah

**[01:07:17]** probably sampling this

**[01:07:19]** in the first iteration

**[01:07:21]** and if we are talking about like

**[01:07:23]** each of the tables

**[01:07:25]** so yeah cards

**[01:07:29]** let's probably mention

**[01:07:31]** like so yeah cards

**[01:07:35]** it's probably gonna be some sort of like you know

**[01:07:37]** ID

**[01:07:39]** probably

**[01:07:41]** what else like

**[01:07:43]** yeah ID

**[01:07:45]** user ID

**[01:07:47]** some you know created but

**[01:07:49]** but it's

**[01:07:53]** updated I mean that's

**[01:07:55]** that's pretty much standard

**[01:07:57]** and let me

**[01:08:02]** let me see let me see

**[01:08:04]** I feel like

**[01:08:06]** if we are gonna

**[01:08:08]** for example let's say we want to create

**[01:08:10]** card we go here here here

**[01:08:12]** and we're gonna create a card

**[01:08:14]** and also I guess

**[01:08:16]** just for the simplicity

**[01:08:18]** we can add some sort of like version here

**[01:08:20]** and thus you know we can

**[01:08:22]** this is like you know

**[01:08:24]** optimistic like logs

**[01:08:26]** so you know we

**[01:08:28]** support you know

**[01:08:30]** so we don't really like log the whole table

**[01:08:32]** or like the whole row

**[01:08:34]** we can like create you know some version

**[01:08:36]** here for like

**[01:08:38]** optimistic logs

**[01:08:40]** so yeah that might be a bit of

**[01:08:44]** optimization here so yeah

**[01:08:46]** our cards is just gonna store the ID, the user

**[01:08:48]** and then you know the card

**[01:08:50]** items is actually

**[01:08:52]** is gonna be the table that

**[01:08:54]** holds all the items

**[01:08:56]** so it's gonna be

**[01:08:58]** it's gonna be referencing

**[01:09:00]** like you know the first table

**[01:09:04]** collection it's also gonna have like its

**[01:09:06]** own ID but it's also

**[01:09:08]** should like have card ID

**[01:09:10]** so we can reference the items that you know go to

**[01:09:12]** this table

**[01:09:14]** and

**[01:09:16]** what else

**[01:09:22]** let me see

**[01:09:24]** talking about like items

**[01:09:26]** I feel like

**[01:09:30]** a bit of optimization here might be

**[01:09:34]** so we're gonna have our SKU

**[01:09:38]** the store keeping

**[01:09:40]** unit and we can like

**[01:09:42]** cash the price here

**[01:09:44]** so we don't

**[01:09:46]** hit like our

**[01:09:48]** probably

**[01:09:50]** the prices I guess the prices are gonna be

**[01:09:52]** like

**[01:09:54]** warehouse

**[01:09:56]** I guess the prices is gonna be like

**[01:09:58]** some other service because

**[01:10:00]** prices

**[01:10:02]** I guess they are not really like

**[01:10:04]** a part of our scope

**[01:10:08]** like is there any specific

**[01:10:10]** requirement regarding the price because from my

**[01:10:12]** from my experience

**[01:10:14]** we get like you know price from some other

**[01:10:16]** service and we don't really like store it

**[01:10:18]** like as a source of truth and like prices

**[01:10:20]** they are coming from other team because

**[01:10:22]** prices they tend to fluctuate and

**[01:10:24]** tend to change so I assume

**[01:10:26]** you know we get like our prices

**[01:10:28]** from some other external service

**[01:10:30]** is that so

**[01:10:38]** I will say make it simple

**[01:10:40]** because

**[01:10:42]** the requirement on your side

**[01:10:44]** on daily job

**[01:10:46]** maybe it's because

**[01:10:48]** we need to fragment

**[01:10:50]** is that correct

**[01:10:52]** and it's going to be

**[01:10:54]** by region is going to be

**[01:10:56]** by the currency or whatever

**[01:10:58]** but for this one

**[01:11:00]** scope down so only one

**[01:11:02]** region or no need for

**[01:11:04]** fragment and easy

**[01:11:06]** to get it from maybe

**[01:11:08]** inventory

**[01:11:12]** I see

**[01:11:14]** all right

**[01:11:18]** yeah

**[01:11:20]** let's say we're gonna have like our price

**[01:11:22]** here and we're gonna have

**[01:11:24]** like our

**[01:11:26]** quantity

**[01:11:28]** basically it's going to be like a row

**[01:11:30]** it's

**[01:11:32]** going to apply to a specific card ID

**[01:11:34]** we're gonna have like SKU

**[01:11:36]** we're gonna have like our price

**[01:11:38]** we're gonna have like our quantity

**[01:11:40]** so yeah there's going to be like

**[01:11:42]** our card items as a separate table

**[01:11:44]** and

**[01:11:46]** like the

**[01:11:50]** the broad is the promotion

**[01:11:52]** let me see

**[01:11:54]** card item

**[01:11:56]** promotion

**[01:11:58]** regarding

**[01:12:00]** I'm just gonna

**[01:12:02]** quickly

**[01:12:04]** mention this whole thing

**[01:12:06]** yeah

**[01:12:08]** we have

**[01:12:10]** 15 minutes

**[01:12:12]** right

**[01:12:14]** so yeah it's going to be like

**[01:12:16]** cashed response

**[01:12:20]** basically like you know

**[01:12:22]** the same response that we get from cards

**[01:12:24]** but cash here

**[01:12:26]** and we're gonna generate

**[01:12:28]** like header

**[01:12:30]** like

**[01:12:32]** key here

**[01:12:34]** so yeah

**[01:12:36]** it's gonna look like this

**[01:12:38]** and regarding the promotions

**[01:12:40]** it's also going to be like

**[01:12:44]** another

**[01:12:46]** another like some sort of ID

**[01:12:48]** maybe like type or something

**[01:12:50]** like and

**[01:12:52]** times times

**[01:12:54]** something like this

**[01:12:56]** all right

**[01:12:58]** so it's gonna look like this

**[01:13:00]** I feel like this is like

**[01:13:02]** the most minimal example of what we might have here

**[01:13:06]** let me see

**[01:13:08]** what we are missing

**[01:13:10]** so I guess

**[01:13:12]** why we use like posters here

**[01:13:14]** is because we want to have like transactions

**[01:13:16]** because

**[01:13:18]** you know we don't really want to have like any sort of like card mutations

**[01:13:20]** so yeah that's the one thing

**[01:13:22]** we are gonna like snapshot our

**[01:13:24]** you know

**[01:13:26]** price here so

**[01:13:28]** we avoid like you know go into

**[01:13:30]** some other external service

**[01:13:32]** we're gonna like use here like our optimistic login

**[01:13:34]** to you know avoid

**[01:13:36]** any sort of you know

**[01:13:38]** locking issues

**[01:13:40]** and

**[01:13:44]** I guess this one this

**[01:13:46]** like this architecture will work

**[01:13:48]** for probably

**[01:13:50]** for some time

**[01:13:52]** but

**[01:13:54]** I guess like our bottleneck

**[01:13:56]** is our like postgresdb

**[01:13:58]** because like we have like

**[01:14:00]** like 10 million users

**[01:14:02]** like

**[01:14:04]** yeah that's quite a lot

**[01:14:06]** and

**[01:14:08]** I guess one of the options

**[01:14:10]** to address this whole thing

**[01:14:12]** is to make like you know replicas

**[01:14:14]** and

**[01:14:16]** for example like shard them by

**[01:14:18]** userID

**[01:14:20]** so

**[01:14:22]** we're gonna shard by userID

**[01:14:24]** introduce

**[01:14:26]** like

**[01:14:28]** you know sharding

**[01:14:30]** and add some

**[01:14:32]** like you know

**[01:14:34]** error like read replicas

**[01:14:36]** yeah

**[01:14:39]** thus we can you know mitigate

**[01:14:41]** some of the

**[01:14:43]** some of the

**[01:14:45]** not like request but the load

**[01:14:47]** yeah so this way we can

**[01:14:49]** you know make

**[01:14:51]** our

**[01:14:53]** our db

**[01:14:55]** less prone to like you know failure

**[01:14:57]** so it's not gonna become like you know the single point of failure

**[01:15:01]** yeah and like why we

**[01:15:03]** why we like why we

**[01:15:05]** I mean why I chose like you know userID

**[01:15:07]** as a

**[01:15:09]** you know sharding key

**[01:15:11]** because you know all our operations

**[01:15:13]** they're actually you know in the scope of one users

**[01:15:15]** so that's safe and we don't

**[01:15:17]** we're not gonna have like you know cross you know shard

**[01:15:19]** request, squares and stuff

**[01:15:21]** so yeah

**[01:15:23]** that's one way to

**[01:15:25]** approach this whole thing

**[01:15:29]** and

**[01:15:31]** in the future

**[01:15:33]** in the future

**[01:15:35]** if you want to address

**[01:15:37]** maybe like higher load

**[01:15:41]** because yeah sharding is nice

**[01:15:43]** but it's still you know

**[01:15:45]** not maybe like you know

**[01:15:47]** might not address

**[01:15:49]** the load that we still have

**[01:15:51]** and I guess

**[01:15:53]** what we could do here

**[01:15:55]** is to

**[01:15:59]** it's called like you know

**[01:16:01]** cqrs pattern

**[01:16:03]** and we can

**[01:16:05]** you know separate like reads from writes

**[01:16:07]** and like you know create

**[01:16:09]** different services for like

**[01:16:11]** reading and writing

**[01:16:13]** so that's you know something

**[01:16:15]** that we might address in the future

**[01:16:17]** and we are gonna like address our high load
> 📎 **База:** ✅ [[12. Опыт и soft skills#2.2 Архитектура и стек проекта]]

**[01:16:19]** that's one option

**[01:16:21]** that I see

**[01:16:23]** so yeah

**[01:16:25]** this is like this is how we're gonna

**[01:16:27]** you know make sure that our load

**[01:16:29]** is distributed

**[01:16:31]** like across you know reading path

**[01:16:33]** and writing path

**[01:16:35]** yeah

**[01:16:37]** and let me see what else we can like address here

**[01:16:39]** besides the

**[01:16:41]** the database

**[01:16:43]** the database

**[01:16:47]** I guess

**[01:16:49]** I guess we should like you know separate

**[01:16:51]** since we have like our you know I mentioned

**[01:16:53]** that there's gonna be like monolith card service

**[01:16:55]** but probably

**[01:16:57]** it's gonna be

**[01:16:59]** it's probably gonna be

**[01:17:01]** a mesh of services like you know

**[01:17:03]** microservice architecture might be useful

**[01:17:05]** you know if we get to you know these high numbers

**[01:17:07]** uh

**[01:17:09]** so let's say

**[01:17:11]** we're gonna have like our

**[01:17:13]** card service here

**[01:17:15]** card service

**[01:17:17]** card service

**[01:17:19]** and uh

**[01:17:28]** and as I mentioned yeah

**[01:17:30]** since I mentioned cqrs

**[01:17:32]** it's also gonna be like

**[01:17:34]** we're gonna you know separate them

**[01:17:36]** so it's gonna be like card read service

**[01:17:38]** and like card write service

**[01:17:40]** so it's gonna be like this

**[01:17:42]** and we're gonna drop this whole thing

**[01:17:48]** yeah

**[01:17:51]** and uh some

**[01:17:53]** yeah some of the optimizations besides you know

**[01:17:55]** providing like you know creating readers here

**[01:17:57]** we can also introduce

**[01:17:59]** some

**[01:18:01]** caching here

**[01:18:03]** this might be helpful

**[01:18:05]** you know to distribute you know the load

**[01:18:07]** so maybe

**[01:18:09]** a pretty basic approach

**[01:18:11]** sort of like read is here

**[01:18:13]** in the front

**[01:18:15]** so

**[01:18:17]** gonna hit you know the read is first

**[01:18:19]** something like this

**[01:18:21]** yeah

**[01:18:23]** that might be an option

**[01:18:25]** and

**[01:18:27]** what else we might

**[01:18:29]** address here

**[01:18:31]** so we support the 15 million users

**[01:18:35]** I would guess

**[01:18:37]** we can you know separate

**[01:18:39]** our

**[01:18:41]** promotions

**[01:18:50]** as a different service also

**[01:18:52]** you know promotion service

**[01:18:54]** this one will be you know

**[01:18:56]** responsible for

**[01:19:02]** for all the promotions

**[01:19:04]** you know if we if we have like

**[01:19:06]** right now we have only like you know

**[01:19:08]** buy one get one but there might be some other

**[01:19:10]** you know different types of you know promotions

**[01:19:12]** and thus

**[01:19:14]** it will also deal

**[01:19:19]** with the card information

**[01:19:21]** so yeah

**[01:19:23]** so yeah but the basic idea is

**[01:19:30]** to you know separate them into

**[01:19:32]** different you know microservices

**[01:19:34]** so you know each of the services handles

**[01:19:36]** each each all like

**[01:19:38]** tasks so to speak

**[01:19:41]** and what else do we have here

**[01:19:43]** what else do we have here

**[01:19:45]** what else do we have here

**[01:19:47]** yeah I guess

**[01:19:50]** one thing is that we want to make

**[01:19:52]** sure that our like card services

**[01:19:54]** are stateless and you know

**[01:19:56]** we don't really want to

**[01:19:58]** stay you know store in any information

**[01:20:00]** you know we don't really want to introduce any

**[01:20:02]** sort of like state here

**[01:20:04]** so yeah that's that's also a must

**[01:20:06]** and

**[01:20:08]** let me see

**[01:20:10]** ideas

**[01:20:16]** I wanted to see more

**[01:20:23]** during the customer

**[01:20:25]** check out the card

**[01:20:27]** what gonna happen

**[01:20:29]** on our system

**[01:20:33]** about the checkout

**[01:20:35]** let me see

**[01:20:37]** let me see

**[01:20:42]** I guess if we're talking about

**[01:20:44]** you know checkouts

**[01:20:46]** and like payments

**[01:20:48]** the most common pattern that I see

**[01:20:50]** is that

**[01:20:52]** probably we're gonna have like

**[01:20:54]** another you know checkout service

**[01:20:56]** you know that does the whole thing

**[01:20:58]** checkout service

**[01:21:00]** and it will also you know like

**[01:21:02]** get like the same data

**[01:21:04]** but

**[01:21:06]** the information about

**[01:21:08]** the

**[01:21:10]** about like the

**[01:21:12]** transaction stuff

**[01:21:14]** I think in this case

**[01:21:16]** you know we're gonna

**[01:21:18]** like write to some sort of you know

**[01:21:20]** message queue

**[01:21:22]** like some sort of

**[01:21:24]** like SKS or like Kafka

**[01:21:26]** here

**[01:21:28]** from my experience you know most of the like

**[01:21:30]** payment platforms and like you know

**[01:21:32]** whenever we deal with the payments

**[01:21:34]** we just like send a message to the

**[01:21:36]** like you know to the Kafka

**[01:21:38]** and the payment team

**[01:21:40]** processes that on their side

**[01:21:42]** so

**[01:21:44]** probably something like this

**[01:21:46]** like we send our

**[01:21:48]** checkout message to the

**[01:21:50]** to the

**[01:21:52]** message queue

**[01:21:54]** and

**[01:21:56]** here something like this

**[01:21:58]** something like this

**[01:22:00]** what else I mean

**[01:22:04]** we check out

**[01:22:06]** do you have

**[01:22:08]** experience with the payment gateway
> 📎 **База:** ✅ [[12. Опыт и soft skills#Опыт с payment gateway / платёжными системами]]

**[01:22:10]** before

**[01:22:12]** experience with what

**[01:22:14]** payment gateway

**[01:22:16]** do you have

**[01:22:19]** experience with the payment gateway

**[01:22:21]** before

**[01:22:23]** you mean like with the payment

**[01:22:25]** systems and like how we like

**[01:22:27]** deal with the payments

**[01:22:29]** in like in general

**[01:22:31]** yeah

**[01:22:33]** yeah I do

**[01:22:35]** I guess like one of the issues

**[01:22:37]** not like issues but things that we should be aware of

**[01:22:39]** is like some sort of like you know keys

**[01:22:41]** like when we are talking about you know

**[01:22:43]** payments

**[01:22:45]** and if we are talking about for example Kafka

**[01:22:47]** we want to you know add some

**[01:22:49]** you know key to the message so the

**[01:22:51]** payment team can

**[01:22:53]** you know do some deduplications

**[01:22:55]** and make sure they only like you know

**[01:22:57]** handle the message once

**[01:22:59]** so yeah

**[01:23:01]** if we're talking about like you know payments

**[01:23:03]** I guess one thing

**[01:23:05]** to be mindful of

**[01:23:07]** is how we're gonna you know deal with the

**[01:23:09]** like keys and how we're gonna make sure

**[01:23:11]** that our messages

**[01:23:13]** aren't like duplicated

**[01:23:15]** I guess yeah

**[01:23:17]** okay how about this

**[01:23:19]** during the checkout you'll say

**[01:23:21]** you're gonna have the checkout service

**[01:23:23]** and

**[01:23:25]** once the checkout service

**[01:23:27]** receive the request

**[01:23:29]** what's gonna be the sequence
> 📎 **База:** ✅ [[9. Архитектура#Saga / 2PC для двух БД?]] · порядок checkout → payment gateway → БД → message queue

**[01:23:31]** between

**[01:23:33]** payment gateway

**[01:23:35]** between database

**[01:23:37]** on our system

**[01:23:39]** between the

**[01:23:41]** message queue that you mentioned

**[01:23:43]** what is the sequence

**[01:23:45]** and how is handle the

**[01:23:47]** respond

**[01:23:51]** let me see so yeah

**[01:23:53]** what's gonna basically happen when we like

**[01:23:55]** hit checkout and

**[01:23:57]** how it's gonna

**[01:23:59]** how we're gonna basically

**[01:24:01]** what's gonna be like the flow of the data

**[01:24:03]** in our case

**[01:24:05]** let me see

**[01:24:07]** let me see

**[01:24:09]** so basically

**[01:24:11]** our client hits

**[01:24:13]** like for example

**[01:24:15]** you know adds you know some items

**[01:24:17]** to the to the to the card

**[01:24:19]** like we

**[01:24:21]** recalculated

**[01:24:23]** the

**[01:24:25]** the user

**[01:24:27]** hits like checkout

**[01:24:29]** and

**[01:24:31]** basically what we need to do

**[01:24:34]** is send the data

**[01:24:36]** to this

**[01:24:38]** messaging queue and

**[01:24:42]** we will you know

**[01:24:46]** basically we're gonna send like the information

**[01:24:48]** about the current

**[01:24:50]** card

**[01:24:52]** but also I think it's a good practice

**[01:24:54]** before we send

**[01:24:56]** the checkout service

**[01:24:58]** it should probably recalculate

**[01:25:00]** the card once again

**[01:25:02]** because you know the prices

**[01:25:04]** might have changed

**[01:25:06]** so probably checkout service

**[01:25:08]** will recalculate

**[01:25:10]** do the whole calculation once again

**[01:25:12]** just to confirm

**[01:25:14]** and after it gathers all the information

**[01:25:16]** it's gonna send

**[01:25:18]** to the queue

**[01:25:20]** to the Kafka for example

**[01:25:22]** only price

**[01:25:26]** sorry what do you mean

**[01:25:28]** only price

**[01:25:30]** because you mentioned only price

**[01:25:32]** is it only price

**[01:25:34]** just for calculation

**[01:25:39]** I didn't quite gauge that

**[01:25:41]** so you mentioned

**[01:25:45]** that checkout service

**[01:25:47]** will recalculate the

**[01:25:49]** price

**[01:25:51]** the total

**[01:25:53]** the total price

**[01:25:55]** of the currency

**[01:25:57]** definitely that price

**[01:25:59]** definitely total price

**[01:26:01]** or anything else

**[01:26:03]** that you can think about

**[01:26:06]** anything else

**[01:26:08]** well yes

**[01:26:10]** this might not be relevant

**[01:26:12]** but maybe currency and stuff

**[01:26:14]** but this might be

**[01:26:16]** because I had to deal with your currencies

**[01:26:18]** and that might be

**[01:26:20]** anything to think about

**[01:26:22]** maybe

**[01:26:24]** let me see

**[01:26:26]** probably

**[01:26:28]** besides price

**[01:26:30]** what we might recalculate here

**[01:26:32]** to avoid any sort of

**[01:26:34]** issues

**[01:26:36]** well maybe we should also

**[01:26:38]** take a look at the warehouse

**[01:26:40]** and see if the item is still

**[01:26:42]** like available

**[01:26:44]** and make sure

**[01:26:46]** that we are not delivering

**[01:26:48]** the product that is already

**[01:26:50]** out of stock

**[01:26:52]** so probably we should take a look at that

**[01:26:54]** ok

**[01:26:56]** we have one more we need

**[01:26:58]** so after that

**[01:27:00]** after we calculate the price

**[01:27:02]** what's gonna happen next

**[01:27:06]** then we could go to the price

**[01:27:08]** price and inventory

**[01:27:10]** and then we say

**[01:27:12]** ok there's all item in inventories

**[01:27:14]** and the price is already correct

**[01:27:16]** so

**[01:27:18]** what's next

**[01:27:22]** well basically just send the message

**[01:27:24]** to the queue

**[01:27:26]** that's I guess the most straightforward way

**[01:27:28]** here we just send

**[01:27:30]** the information that the payment

**[01:27:32]** team requires

**[01:27:34]** probably

**[01:27:36]** as I mentioned

**[01:27:38]** some sort of message key

**[01:27:40]** the total

**[01:27:42]** price like the user idea

**[01:27:44]** after we send that

**[01:27:46]** so after we send that

**[01:27:48]** and they say

**[01:27:50]** yes

**[01:27:52]** the transaction was approved

**[01:27:54]** what gonna happen on our system

**[01:27:56]** let me see

**[01:28:01]** so

**[01:28:04]** after

**[01:28:06]** alright

**[01:28:08]** the team says yes

**[01:28:20]** well we should handle

**[01:28:22]** I mean it depends

**[01:28:24]** whether it's our scope

**[01:28:26]** to

**[01:28:28]** to handle the payments

**[01:28:32]** because for the most part

**[01:28:34]** payments are being done by some other team

**[01:28:36]** but let's say

**[01:28:38]** we get like our

**[01:28:40]** our

**[01:28:42]** so yeah they say like yes

**[01:28:44]** it doesn't mean that the payment was successful

**[01:28:46]** or it's just

**[01:28:48]** payment was successful

**[01:28:50]** alright I guess

**[01:28:52]** we should just notify

**[01:28:54]** our user

**[01:28:56]** maybe

**[01:28:58]** you know

**[01:29:00]** if we extend this whole system

**[01:29:02]** there might be some sort of like

**[01:29:04]** notification service

**[01:29:06]** you know that does like sending

**[01:29:08]** the email sending like the

**[01:29:10]** SMS message to the phone

**[01:29:12]** and we just you know I guess like return

**[01:29:14]** the response to the client on the

**[01:29:16]** like on the web that

**[01:29:18]** your payment was successful like

**[01:29:20]** or something so

**[01:29:22]** yeah I guess we just you know return a

**[01:29:24]** successful response and we also

**[01:29:26]** might

**[01:29:28]** might send maybe like you know a message

**[01:29:30]** to another queue for the notifications

**[01:29:32]** or

**[01:29:34]** yeah probably

**[01:29:36]** probably you know

**[01:29:38]** there should be some sort of you know

**[01:29:40]** notification service somewhere here that

**[01:29:42]** we will trigger when you know the payment

**[01:29:44]** successful so we notify

**[01:29:46]** all the other parts

**[01:29:48]** yeah probably probably

**[01:29:50]** the most straightforward ways to send

**[01:29:52]** other message to some other queue

**[01:29:54]** and let the other teams

**[01:29:56]** send the other parts of our system

**[01:29:58]** to know that the payment

**[01:30:00]** was successful

**[01:30:02]** I guess that's it

**[01:30:04]** and because we have three components

**[01:30:06]** way we have card we have inventory

**[01:30:08]** and we have promotion what

**[01:30:10]** going to affect

**[01:30:12]** after we have received success

**[01:30:14]** respond from the payment

**[01:30:16]** gateway you said that

**[01:30:18]** we gonna send notification

**[01:30:20]** to client and

**[01:30:22]** there's nothing else

**[01:30:24]** we just

**[01:30:26]** copied the message and that's it

**[01:30:28]** well let me see

**[01:30:32]** I guess

**[01:30:36]** well yeah you're right

**[01:30:38]** that we should like have some sort of way to

**[01:30:40]** process this information because probably

**[01:30:42]** we know we want to like update the

**[01:30:44]** like you know the status of our card

**[01:30:46]** and like you know make sure like it's

**[01:30:48]** like closed or like it's done

**[01:30:50]** like you know it's success or something like this

**[01:30:52]** it's like paid so probably

**[01:30:54]** probably we will

**[01:30:56]** the core idea is that we're gonna send

**[01:30:58]** some sort of message to some other queue

**[01:31:00]** and we should allow our

**[01:31:02]** like you know other

**[01:31:04]** parts of the system to handle this message

**[01:31:06]** so what else could

**[01:31:08]** you know listen for this event

**[01:31:10]** maybe

**[01:31:12]** maybe there should be some sort of

**[01:31:14]** maybe like background job

**[01:31:16]** that you know receives

**[01:31:18]** the events

**[01:31:20]** and

**[01:31:22]** like we update

**[01:31:24]** the

**[01:31:26]** status

**[01:31:28]** but also if we're talking about like if we extend

**[01:31:30]** this whole thing you know

**[01:31:32]** if the payment was successful probably some other

**[01:31:34]** teams that you know do like the delivery

**[01:31:36]** and stuff they also want to know about it

**[01:31:38]** so we definitely should like publish

**[01:31:40]** something from our service that like

**[01:31:42]** this this card you know is done

**[01:31:44]** we like created

**[01:31:46]** this order and like you guys

**[01:31:48]** you should like pay not like pay

**[01:31:50]** you should you know take the delivery

**[01:31:52]** and do the remaining part

**[01:31:54]** so probably the main idea

**[01:31:56]** is that here we should like

**[01:31:58]** send some sort of message to a queue

**[01:32:00]** but I guess you're trying to

**[01:32:04]** to understand how our

**[01:32:06]** existing services will

**[01:32:08]** will handle

**[01:32:10]** this like message

**[01:32:12]** and how they're going to react to

**[01:32:14]** the checkout service

**[01:32:16]** like responding that everything is fine

**[01:32:18]** is this like what you're trying to see here

**[01:32:20]** maybe

**[01:32:24]** I can

**[01:32:26]** I can back to them

**[01:32:28]** what is the interaction

**[01:32:34]** after customer

**[01:32:37]** trying to add

**[01:32:39]** the products to the

**[01:32:41]** card

**[01:32:44]** I would like to

**[01:32:46]** could you elaborate

**[01:32:48]** in chat

**[01:32:50]** how it's going to affect

**[01:32:52]** to our inventory

**[01:32:56]** so

**[01:32:58]** once again

**[01:33:00]** how add an item to a card

**[01:33:02]** will affect our inventory

**[01:33:04]** or

**[01:33:08]** how add an item

**[01:33:10]** to a card will affect

**[01:33:12]** our inventory

**[01:33:16]** let me see

**[01:33:18]** so yeah

**[01:33:22]** are you deducting

**[01:33:24]** the amount of the item

**[01:33:26]** on the database directly

**[01:33:28]** well in the first iteration

**[01:33:32]** that might be the solution

**[01:33:34]** but we should do this like

**[01:33:36]** in a transaction

**[01:33:38]** but if there's going to be like a lot of items

**[01:33:40]** this way we're going to like

**[01:33:42]** block the database

**[01:33:44]** so it's not really the best I guess approach

**[01:33:48]** so that I would like to know

**[01:33:52]** because you're saying that you will not

**[01:33:54]** lock the item

**[01:33:56]** during the customer add to the card

**[01:33:58]** is that correct

**[01:34:00]** so back to the checkout

**[01:34:02]** that means you need to lock it here

**[01:34:06]** right

**[01:34:09]** could you

**[01:34:11]** elaborate more

**[01:34:13]** here a little bit like

**[01:34:15]** how you can confirm that

**[01:34:19]** well yeah

**[01:34:21]** let me see

**[01:34:23]** I guess

**[01:34:25]** I guess we might use some sort of like

**[01:34:27]** optimistic locking here

**[01:34:29]** and like

**[01:34:31]** for the item

**[01:34:33]** you know for each of the item in our warehouse

**[01:34:35]** you know in our inventory

**[01:34:37]** to have like you know the version

**[01:34:39]** of

**[01:34:41]** the quantity

**[01:34:43]** so

**[01:34:45]** basically

**[01:34:47]** we're not going to I guess introduce

**[01:34:49]** like you know this

**[01:34:51]** pessimistic locking here

**[01:34:53]** we're just going to let the user

**[01:34:55]** add the items and like you know

**[01:34:59]** update the quantity

**[01:35:01]** by using some sort of like

**[01:35:03]** version and you know version and

**[01:35:05]** row field in the table

**[01:35:07]** but later

**[01:35:09]** you know when we actually do the checkout

**[01:35:11]** we're going to do the like the pessimistic

**[01:35:13]** locking and thus you know we will

**[01:35:15]** make sure that we do not

**[01:35:17]** you know get this sort of

**[01:35:19]** corrupted state and

**[01:35:21]** this might be a bit of

**[01:35:23]** not probably not the best experience

**[01:35:25]** if you know if you wanted to

**[01:35:27]** like order like three keyboards

**[01:35:29]** but they say we only have

**[01:35:31]** one but I guess

**[01:35:33]** that's a sort of

**[01:35:35]** how to call this one

**[01:35:41]** I forgot

**[01:35:43]** the word but yeah this is

**[01:35:48]** not like a workaround but

**[01:35:50]** I guess that's

**[01:35:52]** fine

**[01:35:54]** because yeah

**[01:35:56]** we want to actually want to lock

**[01:35:58]** the table on the user when they

**[01:36:00]** add items to their cart

**[01:36:02]** but you know since the

**[01:36:04]** checkouts are going to be much less frequent

**[01:36:06]** this is where we're going to be doing

**[01:36:08]** the like locking

**[01:36:10]** like the inventory

**[01:36:12]** table so to speak

**[01:36:14]** and this is where we might

**[01:36:16]** you know tell the user

**[01:36:18]** that like sorry

**[01:36:20]** the item that you're requesting isn't

**[01:36:22]** available or like

**[01:36:24]** the quantity isn't the same as you

**[01:36:26]** required it you know you wanted it to be

**[01:36:28]** so yeah probably you know this

**[01:36:30]** sort of two way approach

**[01:36:32]** doing the optimistic locking

**[01:36:34]** first and then

**[01:36:36]** optimistic locking in the end

**[01:36:38]** yeah I hope that answers the question

**[01:36:42]** yeah you know the reason why we need

**[01:36:44]** to

**[01:36:46]** during the checkout why we need to

**[01:36:48]** calculate the inventory right
> 📎 **База:** ✅ [[6. БД#Уровни изоляции транзакций]] · optimistic в корзине vs pessimistic при checkout

**[01:36:50]** so this is the reason

**[01:36:52]** and come back to

**[01:36:54]** the payment gateway

**[01:36:56]** if they say yes we need to

**[01:36:58]** release the lock and

**[01:37:00]** if they say no

**[01:37:02]** we also need to release the lock

**[01:37:04]** and we also

**[01:37:06]** need to reverse

**[01:37:08]** the amount that we have deducted

**[01:37:10]** but yes that's

**[01:37:12]** to prevent it less condition

**[01:37:14]** I think that's

**[01:37:16]** all of the time today

**[01:37:18]** any questions before we

**[01:37:20]** stop the session

**[01:37:22]** Well I guess

**[01:37:26]** a few words about

**[01:37:28]** you know the company if you don't mind

**[01:37:30]** maybe some of

**[01:37:32]** the work you do

**[01:37:34]** if we have a few minutes

**[01:37:36]** yeah I'm just curious

**[01:37:38]** about maybe

**[01:37:40]** what's your position there

**[01:37:42]** what's your daily activities

**[01:37:44]** and what

**[01:37:46]** a day as a developer

**[01:37:48]** in your case

**[01:37:50]** what it looks like

**[01:37:52]** in a few words

**[01:37:54]** nothing to crazy

**[01:37:56]** yeah

**[01:37:58]** so I'm not quite sure

**[01:38:00]** did you understand

**[01:38:02]** the current situation in betica

**[01:38:04]** but I will give you all the context

**[01:38:06]** that I can give

**[01:38:08]** basically we have

**[01:38:10]** we have launched

**[01:38:12]** the products like long time ago

**[01:38:14]** and we didn't expect this

**[01:38:16]** kind of large amount of

**[01:38:18]** volume

**[01:38:20]** because of the bed thing

**[01:38:22]** so we need to handle

**[01:38:24]** the real time money

**[01:38:28]** and it's

**[01:38:30]** 10 million concurrent users

**[01:38:32]** that you have seen is like

**[01:38:34]** exact amount that we need to handle

**[01:38:36]** the consistency

**[01:38:39]** and even worse because

**[01:38:41]** we have

**[01:38:43]** all and very

**[01:38:47]** long architectures

**[01:38:49]** that serve for that

**[01:38:51]** we have a lot of bugs

**[01:38:53]** incident because we not expect that

**[01:38:55]** we gonna have this kind of volume

**[01:38:57]** so that's why there's a lot of less condition

**[01:38:59]** and deadlocks coming afterwards

**[01:39:01]** as well

**[01:39:03]** so that's the name as legacy patch

**[01:39:05]** from

**[01:39:07]** most of them

**[01:39:09]** running with python

**[01:39:11]** and the database

**[01:39:13]** is on the mysql

**[01:39:15]** the deployment is very legacy

**[01:39:17]** we deploy on the

**[01:39:19]** so it's pain

**[01:39:21]** to the future

**[01:39:23]** so we plan for move

**[01:39:25]** to the Google Kubernetes

**[01:39:27]** name project is

**[01:39:29]** one patch from

**[01:39:31]** so

**[01:39:33]** what is going to be

**[01:39:35]** is going to the same things that you have designed here

**[01:39:37]** but even

**[01:39:39]** more because

**[01:39:41]** you're gonna specify to what is the time section

**[01:39:43]** where it's gonna be charting

**[01:39:45]** where is the positioning

**[01:39:47]** where is indexing

**[01:39:49]** need to be optimized because we need to handle

**[01:39:51]** like a 10 million

**[01:39:53]** concurrent write operation

**[01:39:55]** it's not just lead operation

**[01:39:57]** lead operation is more than that

**[01:39:59]** but yeah, you could imagine

**[01:40:01]** so

**[01:40:03]** critical part also need to identify

**[01:40:05]** and

**[01:40:07]** the infrastructure

**[01:40:09]** site is

**[01:40:11]** almost the same

**[01:40:13]** that you have designed like

**[01:40:15]** we use both guests

**[01:40:17]** legacy, we use mysql

**[01:40:19]** but yes

**[01:40:21]** charting, write operation,

**[01:40:23]** lead, lepica, all of them need to be settled

**[01:40:25]** and

**[01:40:27]** all of them need to be in Golan

**[01:40:29]** so that's the reason

**[01:40:34]** I see seems like quite a challenge

**[01:40:36]** yeah

**[01:40:38]** my position

**[01:40:40]** right now

**[01:40:42]** I'm lead position

**[01:40:44]** so I'm lead the communication squad

**[01:40:46]** we handle a lot of revenues

**[01:40:48]** as well

**[01:40:50]** so it's very serious

**[01:40:52]** but yeah

**[01:40:54]** that's all

**[01:40:56]** and if you don't mind

**[01:40:58]** are you currently in Dubai?

**[01:41:00]** yes, I'm in Dubai

**[01:41:02]** how do you like it?

**[01:41:04]** how about you?

**[01:41:06]** I'm currently initially in Europe

**[01:41:08]** okay

**[01:41:10]** so far so good

**[01:41:12]** nothing much, it's very happy

**[01:41:14]** because we don't have to pay tax

**[01:41:16]** for the income

**[01:41:18]** yes

**[01:41:20]** so that's the

**[01:41:22]** most reason

**[01:41:24]** why we are here

**[01:41:26]** in summer it's going to be hot

**[01:41:28]** yes

**[01:41:30]** you can stay in the room

**[01:41:32]** in the winter it's a little bit cold

**[01:41:34]** it's almost like

**[01:41:36]** 13-14

**[01:41:38]** chances

**[01:41:40]** but yes, so far so good

**[01:41:42]** I'm here to

**[01:41:44]** expand

**[01:41:46]** I think it's similar to the Europe

**[01:41:48]** so

**[01:41:50]** yeah

**[01:41:52]** alright

**[01:41:54]** thanks for the insights

**[01:41:56]** yeah

**[01:41:58]** and I guess that's it

**[01:42:00]** sorry that we

**[01:42:02]** over time here

**[01:42:04]** but yeah

**[01:42:06]** thank you so much

**[01:42:08]** bye bye

**[01:42:10]** see you

## Сопоставление с базой

> Разметка по смыслу вопроса интервьюера. ✅ — точная карточка, ⚠️ — частично, ❌ — карточки нет, 🔧 — практика.

### Теоретические вопросы

| Время | Вопрос (кратко) | Статус | Пункт |
|-------|-----------------|--------|-------|
| 30:41 | Зачем метод isDead() | ✅ | [[2. GO - Средне#Как устроено ООП в Go?]] |
| 33:47 | Что будет при добавлении нового attacker | ✅ | [[1. GO - Часто#Для чего используется интерфейс? / что такое / как устроен интерфейс?]] |
| 38:17 | Общий тип attacker vs shark/barracuda | ✅ | [[2. GO - Средне#Как устроено ООП в Go?]] |
| 01:23:29 | Порядок checkout → payment gateway → БД → queue | ✅ | [[9. Архитектура#Saga / 2PC для двух БД?]] |
| 01:36:48 | Зачем пересчитывать inventory при checkout | ✅ | [[6. БД#Уровни изоляции транзакций]] |

### Практические задачи

| Время | Задача (кратко) | Статус | Пункт / контекст |
|-------|-----------------|--------|------------------|
| 02:04 | Live coding: SDK симуляция сущностей | 🔧 | [[2. GO - Средне#Как устроено ООП в Go?]] · [[1. GO - Часто#Для чего используется интерфейс? / что такое / как устроен интерфейс?]] |
| 49:04 | System design: e-commerce Black Friday | 🔧 | [[9. Архитектура#Монолит vs микросервисы]] · [[9. Архитектура#CQRS — когда уместен]] · [[12. Опыт и soft skills#Опыт с брокерами сообщений и Kafka]] |

### Опыт / behavioral

| Время | Тема | Статус | Пункт |
|-------|------|--------|-------|
| 49:22 | Опыт с e-commerce (по резюме) | ✅ | [[12. Опыт и soft skills#Опыт с e-commerce]] |
| 01:22:08 | Опыт с payment gateway | ✅ | [[12. Опыт и soft skills#Опыт с payment gateway / платёжными системами]] |

| 01:16:17 | and we are gonna like address our high load | ✅ | [[12. Опыт и soft skills#2.2 Архитектура и стек проекта]] |
### Без разметки

| Время | Тема | Статус |
|-------|------|--------|
| 01:38:00–01:40:30 | Контекст Betica: legacy, race/deadlock, миграция в GKE | ❌ контекст компании, не вопрос к кандидату |
| 01:40:54–01:42:10 | Small talk (Dubai, налоги) | ❌ |
