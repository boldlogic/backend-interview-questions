# Новые транскрипты 2026-08-02 batch2 — разметка

Бэкап исходников: `Заметки/.backups/20260802-new-transcripts-batch2/`  
Банк **не** трогали. Частоты **не** +1.

Агенты: [Markup A](30758d96-12a0-44f5-8197-d4b6f59ff7de), [Markup B](0497b5b6-a67a-4c32-99de-950c4bf3c793).  
Wikilink-заголовки сверены с `Заметки/_bank_titles_for_markup.txt` (0 битых `#title`).

## Итог (8 файлов из корня)

| Файл (после переноса) | Стек | База≈ | Задача≈ | Ключевые темы |
|----------------------|------|------:|--------:|---------------|
| `python/язык т-банк python middle+ измененное.md` | Python + livecoding | 20 | 5 | dict/hash, декораторы, индексы |
| `python/praktikaai_python.md` | Python backend | 12 | 2 | asyncio, CAP, индексы |
| `qa/emex (mp3cut.net).md` | QA + SQL | 2 | 8 | тест-дизайн API, SQL JOIN |
| `python/python.md` | Python / CherryPy | 23 | 4 | структуры, code review, partial index |
| `python/2024-10-09 …online-audio….md` | Django / Звук | 11 | 1 | GIL, context, N+1, изоляции |
| `python/2025_07_15_Лаборатория_….md` | Django / infra | 9 | 0 | JOIN, EXPLAIN, опыт |
| `python/ЛигаЦифровойЭкономики.md` | Python / FastAPI / BI | 18 | 4 | ORM, PK/FK, SQL livecoding, Depends |
| `python/СБЕР девайсы 1 й этап.md` | Python | 7 | 1 | GIL, concurrency, Docker, палиндром |

Все с `размечено: true` и `## Сопоставление с базой`. Корень `Транскрипты/` очищен.

## Главные ❌ (заготовки — только по запросу)

| Источник | Пробелы |
|----------|---------|
| т-банк | `object`/`__hash__`; порядок dict 3.7; logging f-string vs `%` |
| praktikaai | exception при «поломке» GIL; FastAPI lifespan; DBMate |
| emex | default args; Scanner vs BufferedReader (Java) |
| python.md | рекурсия / recursion depth; global; WAL; Redis Pub/Sub |
| Звук 2024-10-09 | Django bulk_create; multiprocessing API; RabbitMQ exchange |
| Лаборатория | SQL-тестинг комбинаторика; private PyPI; docker exec; black/white-box |
| Лига | функция vs метод; SQLAlchemy relationship/cascade |
| СБЕР девайсы | multiprocessing/gunicorn workers; native extensions без GIL |

## Следующий шаг (по запросу)

1. Хирургический **+1** частот по ✅-wikilink этих 8  
2. Заготовки ❌  
3. Ручной выборочный реаудит (как с прошлой пачкой) — особенно soft/опыт и mid-question якоря
