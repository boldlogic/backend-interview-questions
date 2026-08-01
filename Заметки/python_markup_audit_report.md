# Аудит разметки Python-транскриптов

## Ложные срабатывания (исправлено)

| Файл | Было | Почему FP | Исправление |
|------|------|-----------|-------------|
| Яндекс. Аналитик | индексы БД на livecoding | «SQL» в Whisper = пары дат отеля, не SQL/индексы | убран wikilink; задача без БД |
| Техсобес Озон | Генераторы на `range` | кандидат про `range()` в лайвкоде, не теория generators | метка снята |
| 2025-02-21 | SQL vs NoSQL | интервьюер перечислял стек компании | → soft skills «стек проекта» |
| rtkit | ACID на «транзакция не повторится» | речь про **идемпотентность** / idempotency key | → идемпотентность HTTP; ACID −1 |
| Культура аналитики | REST principles | кандидат в ответе про опыт, не вопрос теории REST | → ⚠️ опыт |
| Культура аналитики | Docker image vs container | спросили опыт Docker/CI, не теорию image/container | → ⚠️ опыт; freq −1 |

## Пропуски (добавлено)

| Файл | Вопрос | Карточка |
|------|--------|----------|
| rtkit | что такое REST | REST principles |
| rtkit | idempotentность | идемпотентность HTTP |
| rtkit | HTTP/1 vs HTTP/2 («Qtp1») | HTTP/1.1 vs HTTP/2 |
| rtkit | контекстные менеджеры (02:15) | Context managers (метка перенесена на вопрос) |
| Yappy | Event loop | asyncio / Event loop |
| Yappy | threading vs processing | threading vs multiprocessing vs asyncio |
| Спортлевел | connect vs session | ❌ нет карточки |
| Спортлевел | dataclass vs Pydantic | ❌ нет карточки |

## Частоты (хирургия после аудита)

- индексы −1; SQL vs NoSQL −1; ACID −1
- Генераторы −1 (Озон)
- Docker image vs container −1
- REST: −1 Культура +1 rtkit → без изменения числителя относительно до-аудита волны… итого сверено: REST=37
- идемпотентность +1; HTTP/2 +1
- asyncio +1; threading/mp +1; стек проекта +1

## Сверка `18. Python` unique hits

Все числители совпали с числом уникальных транскриптов с wikilink (OK).

## Сознательно не трогали / ок

- МОСГАЗ «генераторы» — по ответу кандидата это Python generators (lazy/yield) — TP
- MTS Redis как очередь — ⚠️ ок
- Angie self-assessment → soft — допустимо
- 27_авг «Индексы» (шум Whisper) — контекст про фильтрацию/ORM — оставляем
- asketa двойной декоратор — один вопрос + уточнение cache decorator — ок

## Кандидаты в stubs (пока ❌)

- dataclass vs Pydantic
- DB connection vs session (SQLAlchemy)
- Memcached vs Redis (уже ❌)
