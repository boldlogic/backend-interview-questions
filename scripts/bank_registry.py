#!/usr/bin/env python3
"""Shared bank question registry and wikilink resolution."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS = ROOT / "Транскрипты"
INDEX_FILE = "GO - индекс.md"
BANK_GLOB = "[0-9]*.md"

# SA-корпус (см. Заметки/SA_CORPUS.md) — знаменатель для 15. SA.md
SA_CORPUS_FILES: frozenset[str] = frozenset(
    {
        "Озон SA 300_water.md",
        "АльфаБанк SA 280_water.md",
        "0223.md",
        "2024_07_16_ASTON_тех_собес_online_audio_converter_mp3cut_net.md",
        "Собеседование Астра ОМ.md",
        "t1_SystemAnalyst.md",
        "Сбербанк 250к отказ_water_2.md",
        "ТТК-Связь.md",
        "АльфаБанк_SA_250_water_1.md",
        "ЛадаЦифра_SA_240_water.md",
        "Собес Гнивц_water-1.md",
        "@foreverrwednesday ом_оффер Digital Biz Factory_water.md",
        "СисАналитик_350к_Aston_water.md",
    }
)

SA_ONLY_BANKS: frozenset[str] = frozenset({"15. SA.md"})
SA_GO_BANKS: frozenset[str] = frozenset(
    {
        "2. БД - Часто.md",
        "3. HTTP - Часто.md",
        "4. Интеграции.md",
        "5. Архитектура - Часто.md",
        "11. БД — Реже.md",
        "12. HTTP — Реже.md",
        "13. Архитектура — Реже.md",
        "14. Ops — Реже.md",
        "17. Data Python ML.md",
    }
)

SKIP_H2 = frozenset({"Задают редко", "Задают часто", "Задают средне", "Оглавление"})
SECTION_NUM_H2_RE = re.compile(r"^\d+\.\s")
SUBSECTION_DENY = frozenset(
    {
        "1. читатель",
        "2. писатель",
        "3. если были заблокированные читатели",
        "4.9 comparable types",
    }
)

MANUAL_ALIASES: dict[tuple[str, str], tuple[str, str]] = {
    ("1. GO - Часто", "5. что такое deadlock в бд?"): ("1. GO - Часто", "Что такое дедлок и рейс кондишион, и `-race`"),
    ("1. GO - Часто", "`sync.map`"): ("1. GO - Часто", "`sync.Map`"),
    ("1. GO - Часто", "data race — что это?"): ("1. GO - Часто", "Что такое дедлок и рейс кондишион, и `-race`"),
    ("1. GO - Часто", "escape analysis"): ("1. GO - Часто", "Stack vs heap — зачем и производительность?"),
    ("1. GO - Часто", "stack vs heap в go"): ("1. GO - Часто", "Stack vs heap — зачем и производительность?"),
    ("1. GO - Часто", "sync.map — когда использовать?"): ("1. GO - Часто", "`sync.Map`"),
    ("1. GO - Часто", "waitgroup — зачем?"): ("8. GO - Редко 1", "`sync.waitgroup`"),
    ("1. GO - Часто", "Много горутин на I/O: сеть vs файлы"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("1. GO - Часто", "какая модель gmp и gomaxprocs?"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("1. GO - Часто", "что такое generics?"): ("7. GO - Средне", "Что такое generics?"),
    ("1. GO - Часто", "что такое модель gmp и gomaxprocs?"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("10. GO - Редко 3", "go.mod — зачем нужен?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("10. GO - Редко 3", "go.sum в git?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("10. БД · HTTP · Arch · Ops — Реже", "1. http методы"): ("12. HTTP — Реже", "HTTP методы"),
    ("15. SA", "как определять границы системы?"): ("15. SA", "границы системы и scope фичи"),
    ("15. SA", "какие артефакты создаёт системный аналитик?"): ("15. SA", "виды документации системного аналитика"),
    ("2. БД - Часто", "32. join: inner, left, right"): ("2. БД - Часто", "Виды JOIN запросов: INNER vs LEFT"),
    ("2. БД - Часто", "35. explain / explain analyze"): ("2. БД - Часто", "EXPLAIN и EXPLAIN ANALYZE"),
    ("2. БД - Часто", "38. шардирование — зачем и как?"): ("2. БД - Часто", "Масштабирование БД"),
    ("2. БД - Часто", "39. репликация бд"): ("2. БД - Часто", "Репликация и read replica"),
    ("2. БД - Часто", "5. что такое deadlock в бд?"): ("1. GO - Часто", "Что такое дедлок и рейс кондишион, и `-race`"),
    ("3. HTTP - Часто", "1. http методы"): ("12. HTTP — Реже", "HTTP методы"),
    ("3. HTTP - Часто", "1. rest — что это?"): ("3. HTTP - Часто", "Что такое RESTful принципы?"),
    ("3. HTTP - Часто", "14. Reverse proxy — что это?"): ("3. HTTP - Часто", "Что такое RESTful принципы?"),
    ("3. HTTP - Часто", "16. grpc vs rest?"): ("3. HTTP - Часто", "REST principles / gRPC vs HTTP?"),
    ("4. Интеграции", "1. kafka — зачем и как работает?"): ("4. Интеграции", "Kafka / RabbitMQ?"),
    ("4. Интеграции", "10.3 kafka / rabbitmq?"): ("4. Интеграции", "Kafka / RabbitMQ?"),
    ("4. Интеграции", "2. outbox pattern"): ("5. Архитектура - Часто", "Transactional outbox"),
    ("5. Архитектура - Часто", "1. микросервисы vs монолит"): ("5. Архитектура - Часто", "Монолит vs микросервисы"),
    ("5. Архитектура - Часто", "2. outbox pattern"): ("5. Архитектура - Часто", "Transactional outbox"),
    ("5. Архитектура - Часто", "3. распределённые транзакции"): ("5. Архитектура - Часто", "Saga / 2PC для двух БД?"),
    ("5. Архитектура - Часто", "9.2 saga / 2pc для двух бд?"): ("5. Архитектура - Часто", "Saga / 2PC для двух БД?"),
    ("5. Архитектура - Часто", "9.3 CAP theorem?"): ("13. Архитектура — Реже", "Знаете ли вы CAP-теорему?"),
    ("5. Архитектура - Часто", "9.8 transactional outbox"): ("5. Архитектура - Часто", "Transactional outbox"),
    ("5. Архитектура - Часто", "как определять границы системы?"): ("15. SA", "границы системы и scope фичи"),
    ("7. GO - Средне", "Set через map"): ("8. GO - Редко 1", "Set через map / Есть ли структура set?"),
    ("7. GO - Средне", "defer, panic, recover"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("7. GO - Средне", "generics в go"): ("7. GO - Средне", "Что такое generics?"),
    ("7. GO - Средне", "generics: версия, кодогенерация"): ("7. GO - Средне", "Что такое generics?"),
    ("7. GO - Средне", "gmp — как работает планировщик?"): ("7. GO - Средне", "что такое модель gmp и gomaxprocs?"),
    ("7. GO - Средне", "ipc между процессами"): ("7. GO - Средне", "Процесс / поток / IPC"),
    ("7. GO - Средне", "set через map"): ("8. GO - Редко 1", "Set через map / Есть ли структура set?"),
    ("7. GO - Средне", "sync.map — когда использовать?"): ("1. GO - Часто", "`sync.Map`"),
    ("7. GO - Средне", "sync/atomic — когда использовать?"): ("7. GO - Средне", "`atomic` vs mutex"),
    ("7. GO - Средне", "Когда Mutex, а когда RWMutex?"): ("7. GO - Средне", "Mutex и RWMutex / Когда Mutex, а когда RWMutex?"),
    ("7. GO - Средне", "Паника, recover и парадигма ошибок"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("7. GO - Средне", "Сложность алгоритмов — Big-O"): ("7. GO - Средне", "что такое o нотация, какая сложность бывает"),
    ("7. GO - Средне", "Строки UTF-8 и руны"): ("8. GO - Редко 1", "Что такое string? / строки vs руны"),
    ("7. GO - Средне", "в чем разница между процессом и потоком"): ("7. GO - Средне", "Процесс / поток / IPC"),
    ("7. GO - Средне", "какая модель gmp и gomaxprocs?"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("7. GO - Средне", "когда mutex, а когда rwmutex?"): ("7. GO - Средне", "Mutex и RWMutex / Когда Mutex, а когда RWMutex?"),
    ("7. GO - Средне", "паника, recover и парадигма ошибок"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("7. GO - Средне", "состояния горутины (gmp)"): ("7. GO - Средне", "что такое модель gmp и gomaxprocs?"),
    ("7. GO - Средне", "строки utf-8 и руны"): ("8. GO - Редко 1", "Что такое string? / строки vs руны"),
    ("7. GO - Средне", "указатели в go"): ("7. GO - Средне", "что такое указатель и сколько он весит"),
    ("7. GO - Средне", "утечка горутин — как найти?"): ("7. GO - Средне", "утечка горутин"),
    ("7. GO - Средне", "что такое defer?"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("7. GO - Средне", "что такое generics?"): ("7. GO - Средне", "Что такое generics?"),
    ("7. GO - Средне", "что такое runtime в go?"): ("7. GO - Средне", "Общее: недостатки Go, компиляция, init, reflect"),
    ("7. GO - Средне", "что такое модель gmp и gomaxprocs?"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("8. GO - Редко 1", "Set через map"): ("8. GO - Редко 1", "Set через map / Есть ли структура set?"),
    ("8. GO - Редко 1", "`sync.map`"): ("1. GO - Часто", "`sync.Map`"),
    ("8. GO - Редко 1", "escape analysis"): ("1. GO - Часто", "Stack vs heap — зачем и производительность?"),
    ("8. GO - Редко 1", "generics в go"): ("7. GO - Средне", "Что такое generics?"),
    ("8. GO - Редко 1", "go.mod — зачем нужен?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("8. GO - Редко 1", "go.sum в git?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("8. GO - Редко 1", "set через map"): ("8. GO - Редко 1", "Set через map / Есть ли структура set?"),
    ("8. GO - Редко 1", "stack vs heap в go"): ("1. GO - Часто", "Stack vs heap — зачем и производительность?"),
    ("8. GO - Редко 1", "waitgroup"): ("8. GO - Редко 1", "`sync.waitgroup`"),
    ("8. GO - Редко 1", "waitgroup — зачем?"): ("8. GO - Редко 1", "`sync.waitgroup`"),
    ("8. GO - Редко 1", "Как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("8. GO - Редко 1", "Строки UTF-8 и руны"): ("8. GO - Редко 1", "Что такое string? / строки vs руны"),
    ("8. GO - Редко 1", "как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("8. GO - Редко 1", "когда interface == nil?"): ("8. GO - Редко 1", "Когда interface == nil / `any` / struct{}"),
    ("8. GO - Редко 1", "строки utf-8 и руны"): ("8. GO - Редко 1", "Что такое string? / строки vs руны"),
    ("8. GO - Редко 1", "указатели в go"): ("7. GO - Средне", "что такое указатель и сколько он весит"),
    ("9. GO - Редко 2", "Как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2", "С какой скоростью идет поиск в массиве и почему?"): ("9. GO - Редко 2", "Что такое массив?"),
    ("9. GO - Редко 2", "как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2", "с какой скоростью идет поиск в массиве и почему?"): ("9. GO - Редко 2", "Что такое массив?"),
    ("9. GO - Редко 2", "чем отличается запись/чтение в буферизованном и небуферизованном канале?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "data race — что это?"): ("1. GO - Часто", "Что такое дедлок и рейс кондишион, и `-race`"),
    ("9. GO - Редко 2-3", "gmp — как работает планировщик?"): ("7. GO - Средне", "что такое модель gmp и gomaxprocs?"),
    ("9. GO - Редко 2-3", "go.mod — зачем нужен?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("9. GO - Редко 2-3", "go.sum в git?"): ("10. GO - Редко 3", "go.mod / go.sum в git?"),
    ("9. GO - Редко 2-3", "ipc между процессами"): ("7. GO - Средне", "Процесс / поток / IPC"),
    ("9. GO - Редко 2-3", "Как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "Когда Mutex, а когда RWMutex?"): ("7. GO - Средне", "Mutex и RWMutex / Когда Mutex, а когда RWMutex?"),
    ("9. GO - Редко 2-3", "Много горутин на I/O: сеть vs файлы"): ("1. GO - Часто", "Что такое модель GMP и GOMAXPROCS?"),
    ("9. GO - Редко 2-3", "Паника, recover и парадигма ошибок"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("9. GO - Редко 2-3", "С какой скоростью идет поиск в массиве и почему?"): ("9. GO - Редко 2", "Что такое массив?"),
    ("9. GO - Редко 2-3", "как сделать канал буферизованным?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "какие операции есть с каналами?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "какие параметры могут иметь каналы?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "когда mutex, а когда rwmutex?"): ("7. GO - Средне", "Mutex и RWMutex / Когда Mutex, а когда RWMutex?"),
    ("9. GO - Редко 2-3", "паника, recover и парадигма ошибок"): ("7. GO - Средне", "defer, panic, recover / exceptions в Go"),
    ("9. GO - Редко 2-3", "с какой скоростью идет поиск в массиве и почему?"): ("9. GO - Редко 2", "Что такое массив?"),
    ("9. GO - Редко 2-3", "состояния горутины (gmp)"): ("7. GO - Средне", "что такое модель gmp и gomaxprocs?"),
    ("9. GO - Редко 2-3", "утечка горутин — как найти?"): ("7. GO - Средне", "утечка горутин"),
    ("9. GO - Редко 2-3", "чем отличается запись/чтение в буферизованном и небуферизованном канале?"): ("9. GO - Редко 2", "Операции и параметры канала"),
    ("9. GO - Редко 2-3", "что такое generics?"): ("7. GO - Средне", "Что такое generics?"),
    ("9. GO - Редко 2-3", "эвакуация мапы"): ("9. GO - Редко 2", "Что такое хеш-таблица / коллизии / эвакуация map"),
    ("16. Опыт и soft skills", "4.4 Дедлайн и стресс (STAR)"): ("16. Опыт и soft skills", "Дедлайн и стресс (STAR)"),
    ("16. Опыт и soft skills", "4.2 Дедлайн и стресс (STAR)"): ("16. Опыт и soft skills", "Дедлайн и стресс (STAR)"),
    ("16. Опыт и soft skills", "Опыт с e-commerce"): ("16. Опыт и soft skills", "Опыт с e-commerce"),
    ("16. Опыт и soft skills", "8.2 Опыт с e-commerce"): ("16. Опыт и soft skills", "Опыт с e-commerce"),
    ("16. Опыт и soft skills", "Опыт с payment gateway / платёжными системами"): ("16. Опыт и soft skills", "Опыт с payment gateway / платёжными системами"),
    ("16. Опыт и soft skills", "8.4 Опыт с payment gateway / платёжными системами"): ("16. Опыт и soft skills", "Опыт с payment gateway / платёжными системами"),
    ("16. Опыт и soft skills", "Опыт с Kubernetes (базовый деплой)"): ("16. Опыт и soft skills", "Опыт с Kubernetes (базовый деплой)"),
    ("16. Опыт и soft skills", "8.3 Опыт с Kubernetes (базовый деплой)"): ("16. Опыт и soft skills", "Опыт с Kubernetes (базовый деплой)"),
    ("16. Опыт и soft skills", "Опыт с брокерами сообщений и Kafka"): ("16. Опыт и soft skills", "Опыт с брокерами сообщений и Kafka"),
    ("16. Опыт и soft skills", "8.6 Опыт с брокерами сообщений и Kafka"): ("16. Опыт и soft skills", "Опыт с брокерами сообщений и Kafka"),
    ("16. Опыт и soft skills", "Опыт с ClickHouse"): ("16. Опыт и soft skills", "Опыт с ClickHouse"),
    ("16. Опыт и soft skills", "8.1 Опыт с ClickHouse"): ("16. Опыт и soft skills", "Опыт с ClickHouse"),
    ("16. Опыт и soft skills", "Опыт с PostgreSQL (по резюме)"): ("16. Опыт и soft skills", "Опыт с PostgreSQL (по резюме)"),
    ("16. Опыт и soft skills", "8.5 Опыт с PostgreSQL (по резюме)"): ("16. Опыт и soft skills", "Опыт с PostgreSQL (по резюме)"),
    ("16. Опыт и soft skills", "1.1 Расскажи про себя"): ("16. Опыт и soft skills", "Расскажи про себя"),
    ("16. Опыт и soft skills", "9.5 Расскажи про свой опыт на собесе"): ("16. Опыт и soft skills", "Расскажи про себя"),
    ("16. Опыт и soft skills", "2.4 Команда и процессы на проекте"): ("16. Опыт и soft skills", "Команда и процессы на проекте"),
    ("16. Опыт и soft skills", "6.1 Code review и agile как опыт"): ("16. Опыт и soft skills", "Команда и процессы на проекте"),
    ("16. Опыт и soft skills", "6.2 Релизы и деплой"): ("16. Опыт и soft skills", "Команда и процессы на проекте"),
    ("16. Опыт и soft skills", "2.5 On-call и инциденты"): ("16. Опыт и soft skills", "On-call, инцидент и ошибка в проде"),
    ("16. Опыт и soft skills", "4.3 Ошибка в проде (STAR)"): ("16. Опыт и soft skills", "On-call, инцидент и ошибка в проде"),
    ("16. Опыт и soft skills", "2.6 Как искать проблему в работе системы"): ("16. Опыт и soft skills", "On-call, инцидент и ошибка в проде"),
    ("16. Опыт и soft skills", "5.3 Ожидания от роли"): ("16. Опыт и soft skills", "Ожидания и критерии выбора работы"),
    ("16. Опыт и soft skills", "5.4 Что ищешь в проекте / компании"): ("16. Опыт и soft skills", "Ожидания и критерии выбора работы"),
    ("16. Опыт и soft skills", "4.1 Конфликт в команде (STAR)"): ("16. Опыт и soft skills", "Конфликт и несогласие (STAR)"),
    ("16. Опыт и soft skills", "4.4 Несогласие с техрешением (STAR)"): ("16. Опыт и soft skills", "Конфликт и несогласие (STAR)"),
}

WIKILINK_RE = re.compile(r"\[\[([^#\]]+)(?:#([^\]]+))?\]\]")
HEADING_RE = re.compile(r"^(##|###) (.+)$", re.MULTILINE)
H2_RE = re.compile(r"^## (.+)$")
H3_RE = re.compile(r"^### (.+)$")
NUM_PREFIX_RE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+")
ARCH_NUM_RE = re.compile(r"^(\d+\.\d+)\s+")


def norm_file(name: str) -> str:
    return name.removesuffix(".md").strip()


def strip_heading_prefix(title: str) -> str:
    title = title.strip()
    m = NUM_PREFIX_RE.match(title)
    if m:
        return title[m.end() :].strip()
    m = ARCH_NUM_RE.match(title)
    if m:
        return title[m.end() :].strip()
    return title


def norm_heading(title: str) -> str:
    s = strip_heading_prefix(title).lower()
    s = s.replace(" in go", " в go")
    s = s.replace(" in golang", " в go")
    return s


def heading_equiv_key(title: str) -> str:
    core = norm_heading(title)
    if " vs " in core:
        parts = sorted(p.strip() for p in core.split(" vs "))
        return " vs ".join(parts)
    return core


def heading_prefix_key(title: str) -> str:
    return norm_heading(title).split("—")[0].strip()


def heading_number(title: str) -> str | None:
    m = NUM_PREFIX_RE.match(title.strip())
    if m:
        return m.group(1)
    m = ARCH_NUM_RE.match(title.strip())
    if m:
        return m.group(1)
    return None


def is_experience_section_h2(title: str) -> bool:
    if title.startswith("Топ-25%"):
        return True
    if SECTION_NUM_H2_RE.match(title):
        return True
    return False


def is_architecture_sd_heading(title: str) -> bool:
    return ARCH_NUM_RE.match(title.strip()) is not None


def is_bank_question_heading(level: str, title: str) -> bool:
    if title in SKIP_H2 or is_experience_section_h2(title):
        return False
    nh = norm_heading(title)
    if nh in SUBSECTION_DENY:
        return False
    if level == "##":
        return True
    if level == "###":
        if is_architecture_sd_heading(title):
            return True
        if NUM_PREFIX_RE.match(title) and ("?" in title or "/" in title):
            return True
    return False


def list_transcripts() -> list[Path]:
    return sorted(
        p for p in TRANSCRIPTS.rglob("*.md") if p.name != "INDEX.md"
    )


def corpus_for_bank(bank_name: str) -> str:
    """Return corpus id: sa | sa_go | go."""
    if bank_name in SA_ONLY_BANKS:
        return "sa"
    if bank_name in SA_GO_BANKS:
        return "sa_go"
    return "go"


def corpus_transcript_names(corpus_id: str) -> frozenset[str]:
    """Transcript filenames allowed for frequency numerator/denominator."""
    if corpus_id == "sa":
        return SA_CORPUS_FILES
    if corpus_id in ("sa_go", "go"):
        return frozenset(p.name for p in list_transcripts())
    raise ValueError(f"unknown corpus_id: {corpus_id!r}")


def corpus_denominator(corpus_id: str) -> int:
    return len(corpus_transcript_names(corpus_id))


def count_for_card_in_corpus(
    bank_file: str,
    card_title: str,
    hits: dict[tuple[str, str], set[str]],
    corpus_id: str,
) -> int:
    nf = norm_file(bank_file)
    nh = norm_heading(card_title)
    txs = hits.get((nf, nh), set())
    allowed = corpus_transcript_names(corpus_id)
    return len(txs & allowed)


def list_bank_paths() -> list[Path]:
    return sorted(ROOT.glob(BANK_GLOB))


def parse_wikilinks(line: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for m in WIKILINK_RE.finditer(line):
        file_part = norm_file(m.group(1).strip())
        heading = (m.group(2) or "").strip()
        if file_part and heading:
            out.append((file_part, heading))
    return out


def wikilink_str(file_part: str, heading: str) -> str:
    return f"[[{file_part}#{heading}]]"


def parse_wikilink_ref(ref: str) -> tuple[str, str]:
    """Parse 'file#heading' into (norm_file, heading)."""
    if "#" not in ref:
        raise ValueError(f"Invalid wikilink ref: {ref}")
    file_part, heading = ref.split("#", 1)
    return norm_file(file_part.strip()), heading.strip()


def is_card_h3(lines: list[str], idx: int) -> bool:
    title = H3_RE.match(lines[idx]).group(1).strip()
    if title in SKIP_H2 or norm_heading(title) in SUBSECTION_DENY:
        return False
    for ln in lines[idx + 1 : idx + 10]:
        if ln.startswith("### ") or ln.startswith("## "):
            break
        if (
            ln.startswith("**Частота:**")
            or ln.startswith("**Темы:**")
            or ln.startswith("**Эталон на собесе:**")
            or ln.startswith("**Как формулируют на собесе:**")
        ):
            return True
    return is_bank_question_heading("###", title)


def parse_bank_cards(text: str) -> list[dict]:
    lines = text.splitlines()
    cards: list[dict] = []
    i = 0
    while i < len(lines):
        h2 = H2_RE.match(lines[i])
        h3 = H3_RE.match(lines[i]) if not h2 else None
        if h2:
            title = h2.group(1).strip()
            if title in SKIP_H2 or is_experience_section_h2(title):
                i += 1
                continue
            start = i
            i += 1
            while i < len(lines) and not H2_RE.match(lines[i]):
                if H3_RE.match(lines[i]) and is_card_h3(lines, i):
                    break
                i += 1
            cards.append({"title": title, "start": start, "end": i, "lines": lines[start:i]})
            continue
        if h3 and is_card_h3(lines, i):
            title = h3.group(1).strip()
            start = i
            i += 1
            while i < len(lines):
                if H2_RE.match(lines[i]):
                    break
                if H3_RE.match(lines[i]) and is_card_h3(lines, i):
                    break
                i += 1
            cards.append({"title": title, "start": start, "end": i, "lines": lines[start:i]})
            continue
        i += 1
    return cards


def build_question_registry(
    bank_paths: list[Path] | None = None,
) -> tuple[
    dict[tuple[str, str], tuple[str, str]],
    dict[tuple[str, str], tuple[str, str]],
    dict[tuple[str, str], list[tuple[str, str]]],
    dict[tuple[str, str], str],
]:
    if bank_paths is None:
        bank_paths = list_bank_paths()
    resolver: dict[tuple[str, str], tuple[str, str]] = {}
    number_index: dict[tuple[str, str], tuple[str, str]] = {}
    prefix_index: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    display: dict[tuple[str, str], str] = {}

    for bp in bank_paths:
        nf = norm_file(bp.name)
        text = bp.read_text(encoding="utf-8")
        for card in parse_bank_cards(text):
            title = card["title"]
            nh = norm_heading(title)
            canon = (nf, nh)
            display[canon] = title
            resolver[(nf, nh)] = canon
            resolver[(nf, heading_equiv_key(title))] = canon
            resolver[(nf, title.strip().lower())] = canon
            num = heading_number(title)
            if num:
                number_index[(nf, num)] = canon
            pk = heading_prefix_key(title)
            if pk:
                prefix_index[(nf, pk)].append(canon)

    for (nf, nh), canon in list(MANUAL_ALIASES.items()):
        nf_c, nh_c = canon
        norm_canon = (nf_c, norm_heading(nh_c))
        resolver[(nf, nh)] = norm_canon
        resolver[(nf, norm_heading(nh))] = norm_canon
        if norm_canon in display:
            resolver[(nf, heading_equiv_key(display[norm_canon]))] = norm_canon

    return resolver, number_index, prefix_index, display


def load_index_aliases() -> dict[tuple[str, str], tuple[str, str]]:
    path = ROOT / INDEX_FILE
    if not path.exists():
        return {}
    aliases: dict[tuple[str, str], tuple[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|-"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        new_file = parts[2]
        new_title = parts[3]
        if not new_file.endswith(".md") or new_title in ("новый заголовок", "—"):
            continue
        nf = norm_file(new_file)
        nh = norm_heading(new_title)
        canon = (nf, nh)
        aliases[(nf, nh)] = canon
        aliases[(nf, heading_equiv_key(new_title))] = canon
    return aliases


def finalize_canon(
    canon: tuple[str, str] | None,
    resolver: dict[tuple[str, str], tuple[str, str]],
) -> tuple[str, str] | None:
    """Map alias targets and numbered headings to real bank card keys."""
    if canon is None:
        return None
    nf, nh = canon
    key = (nf, norm_heading(nh))
    return resolver.get(key, key)


def resolve_link(
    file_part: str,
    heading: str,
    resolver: dict[tuple[str, str], tuple[str, str]],
    aliases: dict[tuple[str, str], tuple[str, str]],
    number_index: dict[tuple[str, str], tuple[str, str]],
    prefix_index: dict[tuple[str, str], list[tuple[str, str]]],
) -> tuple[str, str] | None:
    keys = [
        (file_part, norm_heading(heading)),
        (file_part, heading_equiv_key(heading)),
        (file_part, heading.strip().lower()),
    ]
    for key in keys:
        if key in resolver:
            return finalize_canon(resolver[key], resolver)
        if key in aliases:
            return finalize_canon(aliases[key], resolver)

    num = heading_number(heading)
    if num and (file_part, num) in number_index:
        return finalize_canon(number_index[(file_part, num)], resolver)

    pk = heading_prefix_key(heading)
    if pk:
        candidates = prefix_index.get((file_part, pk), [])
        unique = list(dict.fromkeys(candidates))
        if len(unique) == 1:
            return finalize_canon(unique[0], resolver)

    return None


def canon_to_wikilink(canon: tuple[str, str], display: dict[tuple[str, str], str]) -> str:
    nf, nh = canon
    heading = display.get(canon, nh)
    return wikilink_str(nf, heading)
