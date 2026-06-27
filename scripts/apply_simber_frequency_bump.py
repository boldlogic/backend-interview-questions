#!/usr/bin/env python3
"""Bump **Частота:** only for cards linked from Транскрипты/СимберСофт.md (+1 vs HEAD)."""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from bank_registry import (
    BANK_GLOB,
    build_question_registry,
    list_bank_paths,
    load_index_aliases,
    norm_file,
    norm_heading,
    parse_bank_cards,
    parse_wikilinks,
    resolve_link,
)

SIMBER = ROOT / "Транскрипты" / "СимберСофт.md"
FREQ_RE = re.compile(r"^\*\*Частота:\*\* \d+/\d+$")
NEW_CARDS: dict[str, list[str]] = {
    "8. Интеграции.md": [
        "Kafka: topic, partition, offset, consumer group",
        "Kafka producer: acks и idempotent producer",
    ],
    "4. GO - Редко 2.md": [
        "Много горутин на I/O: сеть vs файлы",
    ],
}


def head_text(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.check_output(
        ["git", "show", f"HEAD:{rel}"],
        cwd=ROOT,
        text=True,
        errors="replace",
    )


def head_frequencies() -> dict[tuple[str, str], int]:
    out: dict[tuple[str, str], int] = {}
    for bp in list_bank_paths():
        nf = norm_file(bp.name)
        for card in parse_bank_cards(head_text(bp)):
            for ln in card["lines"]:
                m = re.match(r"^\*\*Частота:\*\* (\d+)/(\d+)", ln)
                if m:
                    out[(nf, norm_heading(card["title"]))] = int(m.group(1))
                    break
    return out


def simber_canons() -> set[tuple[str, str]]:
    resolver, ni, pi, _ = build_question_registry(list_bank_paths())
    aliases = load_index_aliases()
    canons: set[tuple[str, str]] = set()
    for line in SIMBER.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("> 📎 **База:**"):
            continue
        for file_part, heading in parse_wikilinks(line):
            c = resolve_link(file_part, heading, resolver, aliases, ni, pi)
            if c:
                canons.add(c)
    for nf, titles in NEW_CARDS.items():
        for title in titles:
            canons.add((norm_file(nf), norm_heading(title)))
    return canons


def upsert_freq(lines: list[str], n: int, d: int) -> list[str]:
    new_line = f"**Частота:** {n}/{d}"
    out = list(lines)
    for i, ln in enumerate(out):
        if ln.startswith("**Частота:**"):
            out[i] = new_line
            return out
    insert = 1
    while insert < len(out) and out[insert].strip() == "":
        insert += 1
    out.insert(insert, new_line)
    return out


def main() -> None:
    d = 56
    head_freq = head_frequencies()
    bump = simber_canons()
    changed = 0

    for bp in list_bank_paths():
        text = bp.read_text(encoding="utf-8")
        lines = text.splitlines()
        cards = parse_bank_cards(text)
        replacements: list[tuple[int, int, list[str]]] = []
        for card in cards:
            nf = norm_file(bp.name)
            nh = norm_heading(card["title"])
            canon = (nf, nh)
            if canon not in bump and card["title"] not in NEW_CARDS.get(bp.name, []):
                continue
            old_n = head_freq.get(canon, 0)
            new_n = old_n + 1 if canon in bump else 1
            old_line = next((ln for ln in card["lines"] if ln.startswith("**Частота:**")), "")
            updated = upsert_freq(card["lines"], new_n, d)
            if old_line != f"**Частота:** {new_n}/{d}":
                changed += 1
            replacements.append((card["start"], card["end"], updated))

        new_lines: list[str] = []
        pos = 0
        for start, end, updated in replacements:
            new_lines.extend(lines[pos:start])
            new_lines.extend(updated)
            pos = end
        new_lines.extend(lines[pos:])
        new_text = "\n".join(new_lines)
        if text.endswith("\n"):
            new_text += "\n"
        if new_text != text:
            bp.write_text(new_text, encoding="utf-8")

    print(f"Bumped {len(bump)} canon keys; cards updated: {changed}")


if __name__ == "__main__":
    main()
