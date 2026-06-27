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

## Batch 1 (10 файлов, ~95 AUTO)

- `Транскрипты/t1 tex sobes.md` (22)
- `Транскрипты/Яндекс.md` (11)
- `Транскрипты/Tech-Compressed.md` (11)
- `Транскрипты/IMG_3600.md` (9)
- `Транскрипты/Golang.Middle.amoCRM.md` (9)
- `Транскрипты/ТБанк.md` (7)
- `Транскрипты/Собес Aston 04.12.2024_water.md` (7)
- `Транскрипты/indriver_go_water.md` (7)
- `Транскрипты/Full screen September 24 2024 16_30_59.md` (7)
- `Транскрипты/Employcity Тех.md` (5)

## Batch 2 (10 файлов, ~35 AUTO)

- `Транскрипты/0220.md` (5)
- `Транскрипты/МоторикаАудио_null_null__bpm_null.md` (4)
- `Транскрипты/Гоуланг технологии.md` (4)
- `Транскрипты/STARTRIBELTD Go.md` (4)
- `Транскрипты/ютека.md` (3)
- `Транскрипты/wildberries.md` (3)
- `Транскрипты/wb_(0).md` (3)
- `Транскрипты/interview_f6.md` (3)
- `Транскрипты/2024-08-05 11-59-46 Ozon part 1_water-1.md` (3)
- `Транскрипты/0204.md` (3)

## Batch 3 (10 файлов, ~18 AUTO)

- `Транскрипты/Собеседование Lamoda 10.04.2025.md` (2)
- `Транскрипты/Собес_на_стажера_в_группу_поискового_движка_вб_ _сделано_в_Clipc.md` (2)
- `Транскрипты/ozon_тех_скрин (1).md` (2)
- `Транскрипты/ozon_ts.md` (2)
- `Транскрипты/Uzum.md` (2)
- `Транскрипты/Orion_soft_go.md` (2)
- `Транскрипты/Kalabi tech Interview Go.md` (2)
- `Транскрипты/Go_middle_wb.md` (2)
- `Транскрипты/cloud_ru.md` (1)
- `Транскрипты/X5_group_go.md` (1)

## Batch 4 (10 файлов, ~2 AUTO)

- `Транскрипты/IMG_7454.md` (1)
- `Транскрипты/BrightPattern.md` (1)
- `Транскрипты/Собес в DataGile v2.md` (0)
- `Транскрипты/СОБЕС АВИТО_01_E_major__bpm_60.md` (0)
- `Транскрипты/Производственныи_центр_2025_01_15_15_00_18_1_water.md` (0)
- `Транскрипты/Ламода техсобес.md` (0)
- `Транскрипты/yandex_final_interview_team_2_main_part.md` (0)
- `Транскрипты/tbank_go.md` (0)
- `Транскрипты/merge_video_online_com_1741549423_lce_livekod_sfpmca2i_Sw6jNXxu.md` (0)
- `Транскрипты/mailru_algo_audio.md` (0)

## Batch 5 (7 файлов, ~0 AUTO)

- `Транскрипты/cобес 1_water.md` (0)
- `Транскрипты/VK_one_day_техскрининг.md` (0)
- `Транскрипты/Ozon.md` (0)
- `Транскрипты/IMG_8102.md` (0)
- `Транскрипты/Backend.md` (0)
- `Транскрипты/123.md` (0)
- `Транскрипты/1217.md` (0)
