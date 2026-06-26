#!/usr/bin/env python3
"""Migrate Go question bank by frequency tier."""
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent

SOURCES = [
    "1. GO - TOP.md",
    "2. GO - Средне.md",
    "3. GO - Редко.md",
]

FILE_CHASTO = "1. GO - Часто.md"
FILE_SREDNE = "2. GO - Средне.md"
FILES_REDKO = [
    "3. GO - Редко 1.md",
    "4. GO - Редко 2.md",
    "5. GO - Редко 3.md",
]

FILE_META = {
    FILE_CHASTO: ("# 1. GO - Часто", "часто (≥20/59)"),
    FILE_SREDNE: ("# 2. GO - Средне", "средне (5–19/59)"),
    FILES_REDKO[0]: ("# 3. GO - Редко 1", "редко (≤4/59, без частоты)"),
    FILES_REDKO[1]: ("# 4. GO - Редко 2", "редко"),
    FILES_REDKO[2]: ("# 5. GO - Редко 3", "редко"),
}


def parse_cards(text: str) -> list[dict]:
    lines = text.splitlines()
    cards = []
    i = 0
    while i < len(lines):
        m = re.match(r"^## (.+)$", lines[i])
        if m:
            start = i
            title = m.group(1)
            i += 1
            while i < len(lines) and not re.match(r"^## ", lines[i]):
                i += 1
            cards.append({"title": title, "body": lines[start + 1 : i]})
        else:
            i += 1
    return cards


def parse_freq(body: list[str]) -> tuple[str | None, int | None]:
    for line in body:
        if line.startswith("**Частота:**"):
            val = line.removeprefix("**Частота:**").strip()
            m = re.search(r"(\d+)/59", val)
            n = int(m.group(1)) if m else None
            return val, n
    return None, None


def tier(chast: str | None, n59: int | None) -> str:
    if n59 is not None:
        if n59 >= 20:
            return "chasto"
        if n59 >= 5:
            return "sredne"
        return "redko"
    if chast:
        c = chast.lower()
        if "очень часто" in c or re.match(r"^часто\b", c):
            return "chasto"
        if "средне" in c:
            return "sredne"
        if "редко" in c:
            return "redko"
    return "redko"


def strip_num(title: str) -> str:
    return re.sub(r"^\d+\.\s*", "", title).strip()


def body_has_prefix(body: list[str], prefix: str) -> bool:
    return any(line.startswith(prefix) for line in body)


def insert_ozhidayut(body: list[str]) -> list[str]:
    if body_has_prefix(body, "**Что ожидают") or body_has_prefix(
        body, "**Как формулируют"
    ):
        return list(body)
    out = list(body)
    insert_at = 0
    i = 0
    while i < len(out):
        line = out[i]
        if line.strip() == "":
            i += 1
            continue
        if (
            line.startswith("**Частота:**")
            or line.startswith("**Темы:**")
            or re.match(r"^- \[[ xX]\]", line)
        ):
            insert_at = i + 1
            i += 1
            continue
        break
    block = ["", "**Что ожидают на собесе:**", ""]
    return out[:insert_at] + block + out[insert_at:]


def insert_podrobnosti(body: list[str]) -> list[str]:
    if body_has_prefix(body, "**Подробности:**"):
        return list(body)
    out = list(body)
    while out and out[-1].strip() == "":
        out.pop()
    out.extend(["", "**Подробности:**", ""])
    return out


def normalize_card(title: str, body: list[str]) -> tuple[str, list[str]]:
    new_title = strip_num(title)
    body = insert_ozhidayut(body)
    body = insert_podrobnosti(body)
    while body and body[-1].strip() == "":
        body.pop()
    return new_title, body


def extract_themes(body: list[str]) -> str:
    for line in body:
        if line.startswith("**Темы:**"):
            return line.removeprefix("**Темы:**").strip()
    return ""


def render_file(header_h1: str, level: str, cards: list[dict]) -> str:
    lines = [
        header_h1,
        f"- **Уровень:** {level}",
        "- **Навигация:** [[GO - индекс]]",
        "",
    ]
    for idx, c in enumerate(cards):
        lines.append(f"## {c['new_title']}")
        lines.extend(c["body"])
        lines.append("")
        if idx < len(cards) - 1:
            lines.append("---")
            lines.append("")
    return "\n".join(lines) + "\n"


def split_redko(cards: list[dict]) -> list[list[dict]]:
    total = sum(len(c["body"]) + 4 for c in cards)
    target = total / 3
    buckets: list[list[dict]] = [[], [], []]
    acc = 0
    bi = 0
    for c in cards:
        buckets[bi].append(c)
        acc += len(c["body"]) + 4
        if bi < 2 and acc >= target:
            bi += 1
            acc = 0
    return buckets


def build_index_rows(cards_meta: list[dict]) -> str:
    lines = [
        "# GO - индекс",
        "",
        "Карта миграции Go-вопросников. Wikilink: `[[файл#заголовок]]` (без номера).",
        "",
        "| старый файл | старый заголовок | новый файл | новый заголовок | частота | теги |",
        "|-------------|------------------|------------|-----------------|---------|------|",
    ]
    for m in cards_meta:
        ch = m["chast"] or "—"
        lines.append(
            f"| {m['source']} | {m['old_title']} | {m['target_file']} | {m['new_title']} | {ch} | {m['themes']} |"
        )
    return "\n".join(lines) + "\n"


def verify_frequency(meta: list[dict]) -> list[str]:
    errors = []
    for m in meta:
        chast, n59 = parse_freq(m["body"])
        t = tier(chast, n59)
        expected = {
            "chasto": FILE_CHASTO,
            "sredne": FILE_SREDNE,
            "redko": None,
        }
        if t == "redko":
            if m["target_file"] not in FILES_REDKO:
                errors.append(f"{m['new_title']}: redko but in {m['target_file']}")
        elif m["target_file"] != expected[t]:
            errors.append(
                f"{m['new_title']}: tier={t} but in {m['target_file']}"
            )
    return errors


def main():
    all_raw = []
    for src in SOURCES:
        text = (ROOT / src).read_text(encoding="utf-8")
        for c in parse_cards(text):
            chast, n59 = parse_freq(c["body"])
            t = tier(chast, n59)
            new_title, body = normalize_card(c["title"], c["body"])
            all_raw.append(
                {
                    "source": src,
                    "old_title": c["title"],
                    "new_title": new_title,
                    "body": body,
                    "chast": chast,
                    "n59": n59 if n59 is not None else -1,
                    "tier": t,
                    "themes": extract_themes(c["body"]),
                }
            )

    sort_key = lambda x: (-x["n59"], x["new_title"].lower())
    chasto = sorted([c for c in all_raw if c["tier"] == "chasto"], key=sort_key)
    sredne = sorted([c for c in all_raw if c["tier"] == "sredne"], key=sort_key)
    redko = sorted([c for c in all_raw if c["tier"] == "redko"], key=sort_key)

    for name, group in [("chasto", chasto), ("sredne", sredne)]:
        seen = defaultdict(list)
        for c in group:
            seen[c["new_title"]].append(c["old_title"])
        dups = {k: v for k, v in seen.items() if len(v) > 1}
        if dups:
            raise SystemExit(f"Duplicate titles in {name}: {dups}")

    redko_buckets = split_redko(redko)
    for i, bucket in enumerate(redko_buckets):
        seen = defaultdict(list)
        for c in bucket:
            seen[c["new_title"]].append(c["old_title"])
        dups = {k: v for k, v in seen.items() if len(v) > 1}
        if dups:
            raise SystemExit(f"Duplicate titles in redko bucket {i+1}: {dups}")

    meta: list[dict] = []
    for c in chasto:
        c["target_file"] = FILE_CHASTO
        meta.append(c)
    for c in sredne:
        c["target_file"] = FILE_SREDNE
        meta.append(c)
    for i, bucket in enumerate(redko_buckets):
        for c in bucket:
            c["target_file"] = FILES_REDKO[i]
            meta.append(c)

    errors = verify_frequency(meta)
    if errors:
        raise SystemExit("Frequency verify failed:\n" + "\n".join(errors))

    h1, lvl = FILE_META[FILE_CHASTO]
    (ROOT / FILE_CHASTO).write_text(render_file(h1, lvl, chasto), encoding="utf-8")
    h1, lvl = FILE_META[FILE_SREDNE]
    (ROOT / FILE_SREDNE).write_text(render_file(h1, lvl, sredne), encoding="utf-8")
    for i, bucket in enumerate(redko_buckets):
        fn = FILES_REDKO[i]
        h1, lvl = FILE_META[fn]
        (ROOT / fn).write_text(render_file(h1, lvl, bucket), encoding="utf-8")

    (ROOT / "GO - индекс.md").write_text(build_index_rows(meta), encoding="utf-8")

    print(f"OK: chasto={len(chasto)} sredne={len(sredne)} redko={len(redko)}")
    for i, b in enumerate(redko_buckets):
        print(f"  redko {i+1}: {len(b)} cards")
    return meta


if __name__ == "__main__":
    main()
