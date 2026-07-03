# SA-корпус

Модель частот по типу банка:

| Банк | Корпус | D | Скрипт |
|------|--------|---|--------|
| `11. SA.md` | **только SA** | **6** | `update_bank_frequency.py --files "11. SA.md"` |
| `6–9.*.md` | **SA ∪ GO** | **84** | `--files "6. БД.md" "7. HTTP, сети.md" …` |
| `1–5. GO`, `10. Ops` | GO | **84** | `--full-corpus` (только по явной просьбе) |

Реестр SA-файлов: `scripts/bank_registry.py` → `SA_CORPUS_FILES`.

## Шесть файлов SA-корпуса

| # | Файл | Тип |
|---|------|-----|
| 1 | `Транскрипты/Озон SA 300_water.md` | ядро |
| 2 | `Транскрипты/АльфаБанк SA 280_water.md` | ядро |
| 3 | `Транскрипты/0223.md` | ядро (SA, Avangard) |
| 4 | `Транскрипты/2024_07_16_ASTON_тех_собес_online_audio_converter_mp3cut_net.md` | ядро |
| 5 | `Транскрипты/Собеседование Астра ОМ.md` | ядро |
| 6 | `Транскрипты/t1_SystemAnalyst.md` | **гибрид** (~90% backend/интеграции) |

## Критерии включения

- вакансия или блок теории **системного анализа** у интервьюера;
- не HR и не только live coding.

## В GO-корпус (84), но не в SA-корпус (6)

- `onelayer (2)_water_3.md`, `@exbur ч_собес betica_tech_water.md` — backend с единичным NFR; **не** дают +1 к `11. SA`, но учитываются в `6–9`.
- `Сбербанк 250к` — вакансия SA, собес на другую роль.

## Пересчёт

```bash
python scripts/update_bank_frequency.py --write \
  --files "11. SA.md" "6. БД.md" "7. HTTP, сети.md" "8. Интеграции.md" "9. Архитектура.md"
python scripts/sort_bank_by_frequency.py --write   # для 11. SA — sort_cards_in_file или вручную
```

Новый SA-транскрипт → обновить `SA_CORPUS_FILES`, D=6→7, матрицу, wikilink.

Покрытие: [`SA_coverage_matrix.md`](SA_coverage_matrix.md).
