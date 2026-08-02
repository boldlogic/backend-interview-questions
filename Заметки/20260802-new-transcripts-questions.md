# Новые транскрипты 2026-08-02 — распознавание вопросов

Бэкап исходников: `Заметки/.backups/20260802-new-transcripts/`  
Банк **не** трогали. Частоты **не** пересчитывали (только разметка).

Агенты разметки: [Markup A](05b5864e-07ee-4e47-911a-34fa768e6324), [Markup B](252da684-7c58-446b-842e-275e9d0e77d9), [Markup C](f5d3764f-4212-4b25-83a6-e1af63dd5c8b).

## Итог (12 файлов из корня `Транскрипты/`)

| Файл (после переноса) | Стек | Меток ≈ | Ключевые темы |
|----------------------|------|--------:|---------------|
| `python/озон.md` | Python + product analytics | 30 | JOIN, window, A/B, MDE |
| `python/lexica_teh.md` | Python backend | 36 | GIL, декораторы, metaclass, context, индексы, REST |
| `python/Yadro.md` | Python | 31 | типы mutable/immutable, декораторы, Singleton, DNS |
| `python/Фабрика решений.md` | Python | 53 | широкий Python/backend опрос |
| `python/IRLIX(тех собес).md` | Python | 19 | ООП, SOLID, list/map, sort, lambda |
| `python/2025-01-16 14-59-37_water.md` | Python/архитектура | 13 | Clean Arch, DI, Docker, ORM, Sentry |
| `python/GRI-Тех.md` | Python + soft | 54 | теория + опыт |
| `python/2024-12-27 14-58-44_water.md` | Python | 16 | память, FP, схема БД |
| `python/Яндекс, алгособес 720.md` | algo | 6 | Big-O + 3 livecoding ❌ |
| `_unsorted/java_…метрополитен.md` | Java | 13 | gRPC, Kafka, REST, ACID, ООП; Spring ❌ |
| `_unsorted/Data Analyst (MagnitTech).md` | DA/SQL | 7 | SQL livecoding |
| `_unsorted/СБЕР_…compact_2.md` | ML search | 8 | ML/поиск — почти всё ❌ |

Все с `размечено: true` и `## Сопоставление с базой`. Корень `Транскрипты/` от этих 12 очищен.

## Главные ❌ (заготовки — только по запросу)

| Источник | Пробелы |
|----------|---------|
| озон | Bonferroni, CUPED, медиана/мода/матожидание |
| Фабрика | Django middleware/signals/DRF Serializer, mixins, docker/git детали |
| lexica | Alembic / Django migrations |
| Yadro | IP/маска, DHCP |
| Яндекс algo | k closest, симметрия точек, float half-integer |
| IRLIX | exceptions, text vs binary files, mock vs stub |
| water 2025-01-16 | Keycloak, NATS vs Kafka, twelve-factor telemetry |
| Java метро | Spring @Transactional/flush, Gradle proto, JPA lifecycle |
| СБЕР ML | L1/L2, bagging/boosting, PR-AUC/ROC, extrapolation — в `17` нет карточек |
| GRI | `__slots__`, free-threading GC, DRF List vs APIView, профилирование |

## Не из этой пачки (по-прежнему без разметки)

- `_unsorted/IMG_4115.md`, `output2 (mp3cut.net) (2).md`, `Ник.md`

## Следующий шаг (по запросу)

1. Хирургический **+1** частот по ✅-wikilink этих 12 файлов  
2. Заготовки ❌ (приоритет: СБЕР ML → `17`, algo Яндекс, Keycloak)  
3. Доразметить старый `_unsorted`
