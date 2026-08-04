# DA+DE+ML → `Транскрипты/data/` + разметка (2026-08-04)

Бэкап до переноса: `Заметки/.backups/20260804-data-move-markup/`  
Доп. бэкапы разметки агентов: `Заметки/.backups/20260804-data-markup/`, `…/20260804-de-markup/`

## Перенос — 15 файлов → `data/`

### DA / продуктовая аналитика
- AliExpress SQL/Python/A-B
- BetCore Data Analyst
- MagnitTech Data Analyst
- X5 Data Analyst
- Т-Банк Data Analyst
- Т-Банк продуктовый аналитик (техничка)
- Яндекс DA
- IMG_4115 (A/B, статистика)

### DE
- Huntit DE 400k
- ИЦ АИ / ТЕКО DE
- Сбер DE Hadoop

### ML / NLP / GenAI / validation
- Тех WB NLP LLM
- СБЕР ML (поиск на умных устройствах)
- output2 GenAI/RAG
- Совкомбанк — руководитель направления валидации

## Осталось в `_unsorted/` (3)
- `java_собес_в_московскии_метрополитен.md` — Java
- `Uzum_ProjectManager_300_water.md` — Tech PM
- `собес.md` — QA

## Разметка (банк и +1 не трогали)

Все 15: `размечено: true` + сводка (где не было — добавлена).

| Трек | Файл | Маркеры (ориентир) |
|------|------|-------------------|
| DA | IMG_4115 | 0→12 |
| GenAI | output2 | 0→21 |
| DA | AliExpress | 8→14 |
| DA | BetCore | 10→19 |
| DA | Т-банк продуктовый | 2→13 |
| DA | X5 / Т-Банк DA / Яндекс / Magnit | добиты / сводки |
| DE | Huntit | ~10→13 |
| DE | ТЕКО | ~14→19 |
| DE | Сбер Hadoop | ~11→21 |
| ML | WB NLP LLM | ~9→31 |
| ML | Сбер compact | ❌→✅ по `17` |
| ML | Совкомбанк валидация | 3→18 |

## Ключевые ❌ (кандидаты в `17`)
- χ², ratio-метрики, one-/two-sided test, условная вероятность
- Transformer / LoRA / MoE / Softmax / overfitting
- SHAP, nested CV, WOE, Optuna
- CDC/Debezium, ETL tooling, Liquibase
- LangGraph, embeddings cosine, MCP, LLM-as-judge

## Корпус
`data/` **15** · `_unsorted/` **3** · `python/` 65 (без изменений)

**D для `17. Data Python ML`:** по AGENTS пока корпус `python/`. Папка `data/` в знаменатель **не** входит, пока отдельно не обновите правило (python ∪ data).
