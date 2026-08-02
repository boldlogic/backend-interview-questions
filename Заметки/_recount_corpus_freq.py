# -*- coding: utf-8 -*-
"""Recount bank Frequencies N/D by corpus rules. Only touches **Частота:** lines and file headers."""
from __future__ import annotations

from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(".")
TRANS = ROOT / "Транскрипты"

CORPUS_DIRS = {
    "go": ["go"],
    "python": ["python"],
    "sa": ["sa"],
    "qa": ["qa"],
    "dev": ["go", "python"],
    "all": ["go", "python", "sa", "qa"],
}


def corpus_files(key: str) -> list[Path]:
    out: list[Path] = []
    for d in CORPUS_DIRS[key]:
        out.extend(sorted((TRANS / d).rglob("*.md")))
    return out


def corpus_size(key: str) -> int:
    return len(corpus_files(key))


# bank file name -> corpus key
BANK_CORPUS: dict[str, str] = {
    "1. GO - Часто.md": "go",
    "7. GO - Средне.md": "go",
    "8. GO - Редко 1.md": "go",
    "9. GO - Редко 2.md": "go",
    "10. GO - Редко 3.md": "go",
    "18. Python.md": "python",
    "17. Data Python ML.md": "python",
    "20. Теория программирования.md": "dev",
    "2. БД - Часто.md": "all",
    "11. БД — Реже.md": "all",
    "3. HTTP - Часто.md": "all",
    "12. HTTP — Реже.md": "all",
    "4. Интеграции.md": "all",
    "5. Архитектура - Часто.md": "all",
    "13. Архитектура — Реже.md": "all",
    "6. Ops - Часто.md": "all",
    "14. Ops — Реже.md": "all",
    "16. Опыт и soft skills.md": "all",
    "15. SA.md": "sa",
    "19. QA.md": "qa",
}

HEADERS: dict[str, str] = {
    "1. GO - Часто.md": (
        "> **Частота:** N/{D} — корпус **Go** (`Транскрипты/go/`).\n"
        "> Полноценные Go-карточки здесь. Языконезависимая выжимка пересечений с Python — в `20. Теория программирования.md`.\n"
    ),
    "7. GO - Средне.md": "> **Частота:** N/{D} — корпус **Go** (`Транскрипты/go/`).\n",
    "8. GO - Редко 1.md": "> **Частота:** N/{D} — корпус **Go** (`Транскрипты/go/`).\n",
    "9. GO - Редко 2.md": "> **Частота:** N/{D} — корпус **Go** (`Транскрипты/go/`).\n",
    "10. GO - Редко 3.md": "> **Частота:** N/{D} — корпус **Go** (`Транскрипты/go/`).\n",
    "18. Python.md": (
        "> **Частота:** N/{D} — корпус **Python** (`Транскрипты/python/`).\n"
        "> Ядро Python / runtime / stdlib и экосистема. Общая теория — в `20. Теория программирования.md`. "
        "SQL/HTTP/Redis — в профильных банках.\n"
    ),
    "17. Data Python ML.md": (
        "> **Частота:** N/{D} — корпус **Python** (`Транскрипты/python/`).\n"
        "> DE / ML / analytics-темы с собесов. **Python-core** — в `18. Python.md`. "
        "Не дублировать SQL/Kafka/Docker из `2`/`4`/`6`/`14`.\n"
    ),
    "20. Теория программирования.md": (
        "> **Частота:** N/{D} — корпус **разработка** = Go ∪ Python (`Транскрипты/go/` ∪ `python/`).\n"
        "> Языконезависимая выжимка тем, общих для Go и Python. "
        "**N считается только по wikilink на карточки этого файла** (не суммируется с twin-карточками в `1`/`7`–`10`). "
        "Go-эталоны и runtime — в Go-банках; Python-runtime — в `18`.\n"
        "> SOLID/паттерны архитектуры — в `5`/`13`.\n"
    ),
    "2. БД - Часто.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "11. БД — Реже.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA · ярус 2 (хвост БД).\n"
    ),
    "3. HTTP - Часто.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "12. HTTP — Реже.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA · ярус 2 (хвост HTTP).\n"
    ),
    "4. Интеграции.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "5. Архитектура - Часто.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n\n"
        "> Секция корпуса · блоки `###`\n"
    ),
    "13. Архитектура — Реже.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA · ярус 2 (хвост архитектуры).\n"
    ),
    "6. Ops - Часто.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "14. Ops — Реже.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "16. Опыт и soft skills.md": (
        "> **Частота:** N/{D} — корпус **все собесы** = Go ∪ Python ∪ SA ∪ QA "
        "(без `_unsorted`).\n"
    ),
    "15. SA.md": "> **Частота:** N/{D} — корпус **SA** (`Транскрипты/sa/`).\n",
    "19. QA.md": (
        "> **Частота:** N/{D} — корпус **QA** (`Транскрипты/qa/`).\n"
        "> QA-специфичные вопросы. Общие темы Python, HTTP, БД и архитектуры — в профильных банках.\n"
    ),
}


def load_banks() -> dict[str, set[str]]:
    banks: dict[str, set[str]] = {}
    for f in ROOT.glob("[0-9]*.md"):
        text = f.read_text(encoding="utf-8")
        titles = set(re.findall(r"^#{2,3} (.+)$", text, re.M))
        banks[f.name] = titles
    return banks


def resolve_bank(fpart: str, banks: dict[str, set[str]]) -> str | None:
    fpart = fpart.strip()
    if fpart in banks:
        return fpart
    if fpart + ".md" in banks:
        return fpart + ".md"
    # strip .md already handled
    m = re.match(r"^(\d+)\.\s*(.+?)(?:\.md)?$", fpart)
    if not m:
        # try without number quirks
        for name in banks:
            if name.lower().startswith(fpart.lower()) or fpart.lower() in name.lower():
                return name
        return None
    n, rest = m.group(1), m.group(2).strip().lower()
    cands = [name for name in banks if name.startswith(n + ".")]
    if not cands:
        return None
    # normalize dashes
    rest_n = rest.replace("—", "-").replace("–", "-")
    best = None
    best_score = -1
    for name in cands:
        bare = re.sub(r"^\d+\.\s*", "", name).lower().replace(".md", "")
        bare_n = bare.replace("—", "-").replace("–", "-")
        score = 0
        if rest_n == bare_n:
            return name
        # token overlap
        for tok in re.split(r"[\s\-]+", rest_n):
            if len(tok) >= 3 and tok in bare_n:
                score += len(tok)
        if score > best_score:
            best_score = score
            best = name
    return best if best_score > 0 else (cands[0] if len(cands) == 1 else cands[0])


def _norm_h(s: str) -> str:
    return s.strip().replace("ё", "е").lower()


# (link_bank, alias_norm) -> (canonical_bank, canonical_title)
# Short/legacy headings after merges (`A / B`) and card moves between files.
MANUAL_ALIASES: dict[tuple[str, str], tuple[str, str]] = {
    ("1. GO - Часто.md", "чем горутина отличается от потока?"): (
        "1. GO - Часто.md",
        "Что такое горутины и зачем нужны / отличия от потоков ОС",
    ),
    ("1. GO - Часто.md", "что такое горутины и зачем нужны"): (
        "1. GO - Часто.md",
        "Что такое горутины и зачем нужны / отличия от потоков ОС",
    ),
    ("1. GO - Часто.md", "способы синхронизации горутин"): (
        "1. GO - Часто.md",
        "Способы синхронизации горутин / Какие примитивы синхронизации / как горутины общаются",
    ),
    ("1. GO - Часто.md", "что при записи/чтении из закрытого канала?"): (
        "1. GO - Часто.md",
        "Что при записи/чтении из закрытого канала? / Что произойдет с читателями/писателями если закрыть канал?",
    ),
    ("1. GO - Часто.md", "какие виды каналов бывают?"): (
        "1. GO - Часто.md",
        "Как устроен канал и как он работает под капотом? / Какие виды каналов бывают?",
    ),
    ("1. GO - Часто.md", "как устроен канал и как он работает под капотом?"): (
        "1. GO - Часто.md",
        "Как устроен канал и как он работает под капотом? / Какие виды каналов бывают?",
    ),
    ("1. GO - Часто.md", "расскажи про каналы"): (
        "1. GO - Часто.md",
        "Как устроен канал и как он работает под капотом? / Какие виды каналов бывают?",
    ),
    ("1. GO - Часто.md", "что такое указатель и сколько он весит"): (
        "1. GO - Часто.md",
        "Указатели: зачем, что такое и сколько он весит",
    ),
    ("1. GO - Часто.md", "что такое модель gmp и gomaxprocs?"): (
        "1. GO - Часто.md",
        "Что такое планировщик / GMP и GOMAXPROCS?",
    ),
    ("1. GO - Часто.md", "context - что такое и зачем использовать?"): (
        "7. GO - Средне.md",
        "context - что такое, как устроен и зачем использовать?",
    ),
    ("1. GO - Часто.md", "mutex и rwmutex"): (
        "7. GO - Средне.md",
        "Mutex / RWMutex / Когда Mutex, а когда RWMutex?",
    ),
    ("1. GO - Часто.md", "что такое string?"): (
        "7. GO - Средне.md",
        "Что такое string? / строки vs руны",
    ),
    ("1. GO - Часто.md", "чем конкурентность  отличается от параллелизма?"): (
        "8. GO - Редко 1.md",
        "Чем конкурентность отличается от параллелизма?",
    ),
    ("1. GO - Часто.md", "чем конкурентность отличается от параллелизма?"): (
        "8. GO - Редко 1.md",
        "Чем конкурентность отличается от параллелизма?",
    ),
    ("1. GO - Часто.md", "зачем нужен select"): (
        "1. GO - Часто.md",
        "Зачем нужен select",
    ),
    ("1. GO - Часто.md", "select: псевдослучайный выбор case"): (
        "1. GO - Часто.md",
        "Зачем нужен select",
    ),
    ("2. БД - Часто.md", "уровни изоляции транзакций"): (
        "2. БД - Часто.md",
        "Уровни изоляции транзакций / Default в PostgreSQL?",
    ),
    ("2. БД - Часто.md", "нормализация и денормализация"): (
        "2. БД - Часто.md",
        "Нормализация / Что такое нормальные формы / Когда денормализуют?",
    ),
    ("5. Архитектура - Часто.md", "монолит vs микросервисы"): (
        "5. Архитектура - Часто.md",
        "Монолит vs микросервисы, главные компромиссы?",
    ),
    ("7. GO - Средне.md", "defer, panic, recover"): (
        "7. GO - Средне.md",
        "defer, panic, recover / exceptions в Go",
    ),
}


def build_title_resolver(banks: dict[str, set[str]]) -> dict[str, dict[str, tuple[str, str]]]:
    """bank -> {norm_heading -> (canonical_bank, title)}."""
    out: dict[str, dict[str, tuple[str, str]]] = {}
    for bank, titles in banks.items():
        m: dict[str, tuple[str, str]] = {}
        candidates: dict[str, list[str]] = defaultdict(list)
        for t in titles:
            candidates[_norm_h(t)].append(t)
            for part in t.split(" / "):
                part = part.strip()
                if len(part) >= 8:
                    candidates[_norm_h(part)].append(t)
        for key, lst in candidates.items():
            uniq = list(dict.fromkeys(lst))
            if len(uniq) == 1:
                m[key] = (bank, uniq[0])
        out[bank] = m
    # manuals (incl. cross-bank) win
    for (b, alias), (tb, title) in MANUAL_ALIASES.items():
        if title not in banks.get(tb, set()):
            continue
        out.setdefault(b, {})[_norm_h(alias)] = (tb, title)
    return out


def resolve_heading(
    bank: str,
    heading: str,
    resolvers: dict[str, dict[str, tuple[str, str]]],
    banks: dict[str, set[str]],
) -> tuple[str, str] | None:
    h = heading.split("|", 1)[0].strip()
    if not h:
        return None
    titles = banks.get(bank, set())
    if h in titles:
        return bank, h
    hit = resolvers.get(bank, {}).get(_norm_h(h))
    if hit:
        return hit
    if len(h) >= 12:
        cands = [t for t in titles if _norm_h(t).startswith(_norm_h(h))]
        if len(cands) == 1:
            return bank, cands[0]
        cands = [t for t in titles if _norm_h(t.split(" / ")[0]) == _norm_h(h)]
        if len(cands) == 1:
            return bank, cands[0]
    return None


def collect_hits(banks: dict[str, set[str]]) -> dict[tuple[str, str], set[str]]:
    """(bank_file, title) -> set of transcript paths (posix).

    Counts all wikilinks in transcript (База + таблицы/итоги).
    Resolves short/legacy headings after merges (`A / B`) and cross-file moves.
    """
    hits: dict[tuple[str, str], set[str]] = defaultdict(set)
    resolvers = build_title_resolver(banks)
    wikilink = re.compile(r"\[\[([^\]|#]+)#([^\]|]+)(?:\|[^\]]+)?\]\]")
    for folder in ["go", "python", "sa", "qa"]:
        for p in (TRANS / folder).rglob("*.md"):
            text = p.read_text(encoding="utf-8", errors="replace")
            for m in wikilink.finditer(text):
                bank = resolve_bank(m.group(1), banks)
                if not bank:
                    continue
                resolved = resolve_heading(bank, m.group(2), resolvers, banks)
                if resolved:
                    hits[resolved].add(p.as_posix())
    return hits


def folder_of(path: str) -> str:
    # Транскрипты/go/foo.md -> go
    parts = Path(path).parts
    try:
        i = parts.index("Транскрипты")
        return parts[i + 1]
    except (ValueError, IndexError):
        return ""


def n_for_card(bank: str, title: str, corpus_key: str, hits: dict) -> int:
    allowed = set(CORPUS_DIRS[corpus_key])
    files = hits.get((bank, title), set())
    return len({f for f in files if folder_of(f) in allowed})


# Card start = ##/### title, then optional blank / optional Темы, then **Частота:**
CARD_START = re.compile(
    r"^(#{2,3}) (.+)\n"
    r"(?:"
    r"\n?\*\*Частота:\*\*\s*\d+/\d+"
    r"|"
    r"\*\*Темы:\*\*[^\n]*\n\*\*Частота:\*\*\s*\d+/\d+"
    r")",
    re.M,
)


def update_frequencies_and_sort(bank: str, denom: int, corpus_key: str, hits: dict) -> tuple[int, int]:
    path = ROOT / bank
    text = path.read_text(encoding="utf-8")

    matches = list(CARD_START.finditer(text))
    if not matches:
        # still update header if possible
        _rewrite_header_only(path, text, bank, denom)
        return 0, 0

    header = text[: matches[0].start()]
    blocks: list[tuple[int, str, str]] = []
    updated = 0
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        card = text[start:end]
        title = m.group(2)
        n = min(n_for_card(bank, title, corpus_key, hits), denom)
        new_card, cnt = re.subn(
            r"(\*\*Частота:\*\*\s*)\d+/\d+",
            rf"\g<1>{n}/{denom}",
            card,
            count=1,
        )
        if cnt:
            updated += 1
        blocks.append((n, title.lower(), new_card.rstrip()))

    blocks.sort(key=lambda x: (-x[0], x[1]))

    new_header = _build_header(header, bank, denom)
    out = new_header.rstrip() + "\n\n" + "\n\n".join(b for _, _, b in blocks) + "\n"
    path.write_text(out, encoding="utf-8")
    return updated, len(blocks)


def _build_header(header: str, bank: str, denom: int) -> str:
    lines = header.splitlines(keepends=True)
    title_line = ""
    i = 0
    if lines and lines[0].startswith("# "):
        title_line = lines[0]
        i = 1
    while i < len(lines) and (lines[i].strip() == "" or lines[i].startswith(">")):
        i += 1
    preserved = "".join(lines[i:])
    new_hdr = HEADERS.get(bank)
    hdr_body = new_hdr.format(D=denom) if new_hdr else f"> **Частота:** N/{denom}\n"
    new_header = title_line + "\n" + hdr_body
    if preserved.strip():
        new_header = new_header.rstrip() + "\n\n" + preserved.lstrip()
    return new_header


def _rewrite_header_only(path: Path, text: str, bank: str, denom: int) -> None:
    # if somehow no cards matched, only refresh leading header blockquotes
    m = CARD_START.search(text)
    if m:
        return
    lines = text.splitlines(keepends=True)
    if not lines or not lines[0].startswith("# "):
        return
    i = 1
    while i < len(lines) and (lines[i].strip() == "" or lines[i].startswith(">")):
        i += 1
    rest = "".join(lines[i:])
    new_hdr = HEADERS.get(bank)
    hdr_body = new_hdr.format(D=denom) if new_hdr else f"> **Частота:** N/{denom}\n"
    path.write_text(lines[0] + "\n" + hdr_body + "\n" + rest.lstrip(), encoding="utf-8")


def main():
    import argparse

    ap = argparse.ArgumentParser(
        description=(
            "DANGEROUS: mass-rewrite **Частота:** in all banks from wikilinks. "
            "Links are incomplete/legacy — this resets accumulated counters. "
            "Prefer surgical +1 per transcript (see AGENTS.md)."
        )
    )
    ap.add_argument(
        "--i-accept-data-loss",
        action="store_true",
        help="Required. Confirms you accept overwriting all bank frequencies.",
    )
    args = ap.parse_args()
    if not args.i_accept_data_loss:
        raise SystemExit(
            "Refusing mass recount. Frequencies are maintained surgically (+1 per interview).\n"
            "Wikilinks are incomplete — global recount destroys counters.\n"
            "If you really need it: python Заметки/_recount_corpus_freq.py --i-accept-data-loss\n"
            "See AGENTS.md § Счётчики and Заметки/20260802-freq-reset-fix.md"
        )

    sizes = {k: corpus_size(k) for k in CORPUS_DIRS}
    print("Corpus sizes:", sizes)
    assert sizes["go"] == 94
    assert sizes["python"] == 29
    assert sizes["dev"] == 123
    assert sizes["all"] == 141
    assert sizes["sa"] == 15
    assert sizes["qa"] == 3

    banks = load_banks()
    hits = collect_hits(banks)

    for bank, corpus_key in BANK_CORPUS.items():
        if not (ROOT / bank).exists():
            print("MISSING", bank)
            continue
        D = sizes[corpus_key]
        u, ncards = update_frequencies_and_sort(bank, D, corpus_key, hits)
        print(f"{bank}: corpus={corpus_key} D={D} cards={ncards} freq_lines={u}")

    # verify
    print("\n=== VERIFY ===")
    errors = []
    for bank, corpus_key in BANK_CORPUS.items():
        D = sizes[corpus_key]
        text = (ROOT / bank).read_text(encoding="utf-8")
        for m in re.finditer(r"\*\*Частота:\*\*\s*(\d+)/(\d+)", text):
            n, d = int(m.group(1)), int(m.group(2))
            if d != D:
                errors.append(f"{bank}: denom {d} != {D}")
            if n > d:
                errors.append(f"{bank}: N>D {n}/{d}")
        # sort check for cards with frequency
        freqs = [int(x) for x in re.findall(r"^#{2,3} .+\n\*\*Частота:\*\*\s*(\d+)/", text, re.M)]
        if freqs != sorted(freqs, reverse=True):
            # find break
            for i in range(len(freqs) - 1):
                if freqs[i] < freqs[i + 1]:
                    errors.append(f"{bank}: unsorted at {freqs[i]}->{freqs[i+1]}")
                    break
        if "[[" in text:
            # bank should not have wikilinks - warn only if in card body (obsidian sometimes)
            pass
    if errors:
        print("ERRORS:")
        for e in errors[:40]:
            print(" ", e)
        print(f"total errors: {len(errors)}")
    else:
        print("OK: denoms and N<=D and sort")


if __name__ == "__main__":
    main()
