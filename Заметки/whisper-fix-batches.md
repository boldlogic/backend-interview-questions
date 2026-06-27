# Whisper ASR — план батчей (после пилота)

Пилот (batch 0) выполнен: 8 файлов, 102 AUTO-замены, 7 файлов изменено.
`record_water.md` пропущен (уже правился). `2024-10-29 12-02-32_water.md` — 0 AUTO в пилоте.

Процедура каждого батча:
```bash
python scripts/pre_edit_guard.py --backup --paths "Транскрипты/<файлы...>"
python scripts/apply_whisper_fixes.py --tier review --files ...
python scripts/apply_whisper_fixes.py --tier auto --files ...
python scripts/apply_whisper_fixes.py --tier auto --write --files ...
```

REVIEW-кандидаты пилота — см. `whisper-fix-pilot-report.md` (4 строки, не применены).

## Доработки словаря после пилота

- `на gorшke` → только `review` (убрано из `auto`).
- `от кavки` / `скavки` → `review` (контекст «из Kafka» vs «сквозь Kafka»).
- Дубликаты блока «Гosh/Go» в YAML убраны; `к Гoshке` добавлено в `auto`.
- **Замечание:** короткая замена `дедлок` убрана; используются фразы `в дедлоке`, `дедлоков`.
- **v2 словарь:** +~80 паттернов (`гуртин*`, postgres-опечатки, RabbitMQ, EXPLAIN ANALYZE); сканер `scripts/scan_asr_errors.py`.
- Корпус dry-run: **463** AUTO; непокрытых probe-строк: **273** (`whisper-fix-candidates.md`).
- Не заменяем корректное «микросервис*» / «мьютекс*» — только ASR-опечатки.

## Batch 1 (10 файлов) — ✅ выполнен

**177** AUTO-замен, 10 файлов изменено. REVIEW: 3 кандидата в `whisper-fix-batch1-review.md` (не применены).

- `Транскрипты/t1 tex sobes.md` (24)
- `Транскрипты/Яндекс.md` (29)
- `Транскрипты/Tech-Compressed.md` (27)
- `Транскрипты/IMG_3600.md` (17)
- `Транскрипты/Golang.Middle.amoCRM.md` (27)
- `Транскрипты/ТБанк.md` (18)
- `Транскрипты/Собес Aston 04.12.2024_water.md` (10)
- `Транскрипты/indriver_go_water.md` (10)
- `Транскрипты/Full screen September 24 2024 16_30_59.md` (8)
- `Транскрипты/Employcity Тех.md` (7)

## Batch 2 (10 файлов) — ✅ выполнен

~90 AUTO-замен (10 файлов). REVIEW: 0.

- `Транскрипты/0220.md`
- `Транскрипты/МоторикаАудио_null_null__bpm_null.md`
- `Транскрипты/Гоуланг технологии.md`
- `Транскрипты/STARTRIBELTD Go.md`
- `Транскрипты/ютека.md`
- `Транскрипты/wildberries.md`
- `Транскрипты/wb_(0).md`
- `Транскрипты/interview_f6.md`
- `Транскрипты/2024-08-05 11-59-46 Ozon part 1_water-1.md`
- `Транскрипты/0204.md`

## Batch 3 (10 файлов) — ✅ выполнен

**53** AUTO-замен, 10 файлов. REVIEW: 0.

- `Транскрипты/Собеседование Lamoda 10.04.2025.md` (8)
- `Транскрипты/Собес_на_стажера_в_группу_поискового_движка_вб_ _сделано_в_Clipc.md` (2)
- `Транскрипты/ozon_тех_скрин (1).md` (2)
- `Транскрипты/ozon_ts.md` (3)
- `Транскрипты/Uzum.md` (4)
- `Транскрипты/Orion_soft_go.md` (6)
- `Транскрипты/Kalabi tech Interview Go.md` (13)
- `Транскрипты/Go_middle_wb.md` (10)
- `Транскрипты/cloud_ru.md` (2)
- `Транскрипты/X5_group_go.md` (3)

## Batch 4 (10 файлов) — ✅ выполнен

**65** AUTO-замен, 6 файлов изменено. REVIEW: 1 (`mailru_algo_audio.md` — не применён).

- `Транскрипты/IMG_7454.md` (19)
- `Транскрипты/BrightPattern.md` (5)
- `Транскрипты/Собес в DataGile v2.md` (2)
- `Транскрипты/Ламода техсобес.md` (24)
- `Транскрипты/yandex_final_interview_team_2_main_part.md` (9)
- `Транскрипты/tbank_go.md` (6)

## Batch 5 (7 файлов) — ✅ выполнен

**6** AUTO-замен, 4 файла. REVIEW: 0.

- `Транскрипты/cобес 1_water.md` (1)
- `Транскрипты/VK_one_day_техскрининг.md` (2)
- `Транскрипты/Backend.md` (2)
- `Транскрипты/1217.md` (1)

---

**Итого по всем батчам (0–5):** пилот + batch 1–5 закрыты.

**record_water.md:** +16 AUTO (v2-словарь, 2025-06) — корпус auto dry-run теперь **0**.

REVIEW остаток (1 строка): `whisper-fix-final-review.md` — «спонсор будет готовить» (не применён).

**Pass 2 (2025-06):** +79 AUTO в 25 файлах; probe-пробелы 284→210; auto dry-run **0**.

Исключены: `INDEX.md`.
