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

# SA-корпус (см. Заметки/SA_CORPUS.md) — знаменатель для 11. SA.md
SA_CORPUS_FILES: frozenset[str] = frozenset(
    {
        "Озон SA 300_water.md",
        "АльфаБанк SA 280_water.md",
        "0223.md",
        "2024_07_16_ASTON_тех_собес_online_audio_converter_mp3cut_net.md",
        "Собеседование Астра ОМ.md",
        "t1_SystemAnalyst.md",
    }
)

SA_ONLY_BANKS: frozenset[str] = frozenset({"11. SA.md"})
SA_GO_BANKS: frozenset[str] = frozenset(
    {
        "6. БД.md",
        "7. HTTP, сети.md",
        "8. Интеграции.md",
        "9. Архитектура.md",
    }
)

SKIP_H2 = frozenset({"Задают редко", "Задают часто", "Задают средне"})
SUBSECTION_DENY = frozenset(
    {
        "1. читатель",
        "2. писатель",
        "3. если были заблокированные читатели",
        "4.9 comparable types",
    }
)

MANUAL_ALIASES: dict[tuple[str, str], tuple[str, str]] = {
    ("6. БД", "35. explain / explain analyze"): ("6. БД", "explain и explain analyze"),
    ("6. БД", "38. шардирование — зачем и как?"): ("6. БД", "масштабирование бд"),
    ("6. БД", "39. репликация бд"): ("6. БД", "репликация и read replica"),
    ("6. БД", "5. что такое deadlock в бд?"): (
        "5. GO - Редко 3",
        "что такое дедлок и рейс кондишион",
    ),
    ("7. HTTP, сети", "1. rest — что это?"): ("7. HTTP, сети", "что такое restful принципы?"),
    ("7. HTTP, сети", "16. grpc vs rest?"): ("7. HTTP, сети", "rest principles / grpc vs http?"),
    ("7. HTTP, сети", "10. http/2 — что нового?"): ("7. HTTP, сети", "http/1.1 vs http/2 vs http/3?"),
    ("3. GO - Редко 1", "stack vs heap в go"): (
        "1. GO - Часто",
        "stack vs heap — зачем и производительность?",
    ),
    ("3. GO - Редко 1", "указатели в go"): ("3. GO - Редко 1", "что такое указатель и сколько он весит"),
    ("4. GO - Редко 2", "data race — что это?"): ("2. GO - Средне", "data race и `-race`"),
    ("4. GO - Редко 2", "интерфейсы в go"): ("3. GO - Редко 1", "что такое interface в go?"),
    ("4. GO - Редко 2", "как работает gc в go?"): ("2. GO - Средне", "как работает gc (tri-color)?"),
    ("3. GO - Редко 1", "как работает gc (tri-color)?"): ("2. GO - Средне", "как работает gc (tri-color)?"),
    ("4. GO - Редко 2", "gmp — как работает планировщик?"): (
        "2. GO - Средне",
        "что такое модель gmp и gomaxprocs?",
    ),
    ("4. GO - Редко 2", "состояния горутины (gmp)"): (
        "2. GO - Средне",
        "что такое модель gmp и gomaxprocs?",
    ),
    ("4. GO - Редко 2", "что такое runtime в go?"): (
        "5. GO - Редко 3",
        "общее: недостатки go, компиляция, init, reflect",
    ),
    ("4. GO - Редко 2", "пустой интерфейс, `any` и пустая struct"): (
        "5. GO - Редко 3",
        "пустой интерфейс, `any` и пустая struct",
    ),
    ("4. GO - Редко 2", "утечка горутин — как найти?"): ("2. GO - Средне", "утечка горутин"),
    ("2. GO - Средне", "sync.map — когда использовать?"): ("3. GO - Редко 1", "`sync.map`"),
    ("2. GO - Средне", "sync/atomic — когда использовать?"): ("2. GO - Средне", "`atomic` vs mutex"),
    ("2. GO - Средне", "какая модель gmp и gomaxprocs?"): (
        "1. GO - Часто",
        "что такое модель gmp и gomaxprocs?",
    ),
    ("2. GO - Средне", "что такое модель gmp и gomaxprocs?"): (
        "1. GO - Часто",
        "что такое модель gmp и gomaxprocs?",
    ),
    ("2. GO - Средне", "table-driven tests"): ("3. GO - Редко 1", "unit-тесты и table-driven"),
    ("1. GO - Часто", "waitgroup — зачем?"): ("3. GO - Редко 1", "`sync.waitgroup`"),
    ("1. GO - Часто", "что такое interface?"): ("3. GO - Редко 1", "что такое interface в go?"),
    ("3. GO - Редко 1", "waitgroup"): ("3. GO - Редко 1", "`sync.waitgroup`"),
    ("3. GO - Редко 1", "generics в go"): ("5. GO - Редко 3", "что такое generics?"),
    ("3. GO - Редко 1", "escape analysis"): ("3. GO - Редко 1", "escape analysis — stack vs heap?"),
    ("3. GO - Редко 1", "можно ли взять указатель на элемент map?"): (
        "2. GO - Средне",
        "можем ли взять указатель на элемент мапы",
    ),
    ("6. БД", "32. join: inner, left, right"): ("6. БД", "виды join запросов: inner vs left"),
    ("8. Интеграции", "1. kafka — зачем и как работает?"): ("8. Интеграции", "kafka / rabbitmq?"),
    ("8. Интеграции", "10.3 kafka / rabbitmq?"): ("8. Интеграции", "kafka / rabbitmq?"),
    ("8. Интеграции", "2. outbox pattern"): ("9. Архитектура", "transactional outbox"),
    ("9. Архитектура", "1. микросервисы vs монолит"): ("9. Архитектура", "монолит vs микросервисы"),
    ("9. Архитектура", "3. распределённые транзакции"): ("9. Архитектура", "saga / 2pc для двух бд?"),
    ("9. Архитектура", "9.8 transactional outbox"): ("9. Архитектура", "transactional outbox"),
    ("9. Архитектура", "9.2 saga / 2pc для двух бд?"): ("9. Архитектура", "saga / 2pc для двух бд?"),
    ("7. HTTP, сети", "14. Reverse proxy — что это?"): (
        "7. HTTP, сети",
        "что такое restful принципы?",
    ),
    ("7. HTTP, сети", "23. что такое stateless и stateful сервисы?"): (
        "7. HTTP, сети",
        "что такое stateless и stateful сервисы?",
    ),
    ("7. HTTP, сети", "1. http методы"): ("7. HTTP, сети", "http методы"),
    ("2. GO - Средне", "Сложность алгоритмов — Big-O"): (
        "2. GO - Средне",
        "что такое o нотация, какая сложность бывает",
    ),
    ("2. GO - Средне", "Передача и возврат: значение vs указатель?"): (
        "2. GO - Средне",
        "передача и возврат: значение vs указатель? / value vs pointer receiver",
    ),
    ("9. Архитектура", "9.3 CAP theorem?"): ("9. Архитектура", "знаете ли вы cap-теорему?"),
    ("9. Архитектура", "9.11 **Что такое Хореография и Оркестрация?**"): (
        "9. Архитектура",
        "что такое хореография и оркестрация?",
    ),
    ("9. Архитектура", "9.12 Что класть в кэш?"): (
        "9. Архитектура",
        "что класть в кэш (и что не класть)",
    ),
    ("9. Архитектура", "9.12 Что класть в кэш (и что не класть)"): (
        "9. Архитектура",
        "что класть в кэш (и что не класть)",
    ),
    ("4. GO - Редко 2", "Много горутин на I/O: сеть vs файлы"): (
        "1. GO - Часто",
        "что такое модель gmp и gomaxprocs?",
    ),
    ("9. Архитектура", "чем отличается системный анализ от бизнес-анализа?"): (
        "11. SA",
        "чем отличается бизнес-аналитик от системного аналитика?",
    ),
    ("9. Архитектура", "какие артефакты создаёт системный аналитик?"): (
        "11. SA",
        "виды документации системного аналитика",
    ),
    ("9. Архитектура", "как определять границы системы?"): (
        "11. SA",
        "границы системы и scope фичи",
    ),
    ("9. Архитектура", "как системный аналитик помогает проектировать архитектуру?"): (
        "11. SA",
        "как системный аналитик помогает проектировать архитектуру?",
    ),
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


def is_architecture_sd_heading(title: str) -> bool:
    return ARCH_NUM_RE.match(title.strip()) is not None


def is_bank_question_heading(level: str, title: str) -> bool:
    if title in SKIP_H2:
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
    return sorted(p for p in TRANSCRIPTS.glob("*.md") if p.name != "INDEX.md")


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
            if title in SKIP_H2:
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
        resolver[(nf, nh)] = canon
        resolver[(nf, norm_heading(nh))] = canon
        if canon in display:
            resolver[(nf, heading_equiv_key(display[canon]))] = canon

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
