#!/usr/bin/env python3
"""Update wikilinks in Эталоны/Ops using GO - индекс.md."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "GO - индекс.md"
TARGETS = [
    ROOT / "Эталоны" / "Скрининг Авито.md",
    ROOT / "Эталоны" / "авито техскрин.md",
    ROOT / "8. Ops и Linux.md",
]

LINK_RE = re.compile(r"\[\[([^\]#|]+)(?:\|([^\]]+))?\#([^\]]+)\]\]")


def strip_num(s: str) -> str:
    return re.sub(r"^\d+\.\s*", "", s).strip()


def load_index() -> dict[tuple[str, str], tuple[str, str]]:
    text = INDEX.read_text(encoding="utf-8")
    mapping: dict[tuple[str, str], tuple[str, str]] = {}
    for line in text.splitlines():
        if not line.startswith("|") or line.startswith("| старый"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 4:
            continue
        old_file = parts[0].removesuffix(".md")
        old_title = parts[1]
        new_file = parts[2].removesuffix(".md")
        new_title = parts[3]
        for key_title in {old_title, strip_num(old_title)}:
            mapping[(old_file, key_title)] = (new_file, new_title)
    return mapping


def fix_link(match: re.Match, mapping: dict) -> str:
    file_part = match.group(1)
    display = match.group(2)
    anchor = match.group(3)
    anchor_stripped = strip_num(anchor)
    key = (file_part, anchor)
    if key not in mapping:
        key = (file_part, anchor_stripped)
    if key not in mapping:
        return match.group(0)
    new_file, new_title = mapping[key]
    if display:
        return f"[[{new_file}|{display}#{new_title}]]"  # wrong format
    return f"[[{new_file}#{new_title}]]"


def main():
    mapping = load_index()
    updated = 0
    for path in TARGETS:
        text = path.read_text(encoding="utf-8")
        new_text = LINK_RE.sub(lambda m: _replace(m, mapping, path), text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            n = len([1 for a, b in zip(text.splitlines(), new_text.splitlines()) if a != b])
            print(f"Updated {path.name}: ~{n} line changes")
            updated += 1
        else:
            print(f"No changes: {path.name}")
    print(f"Done, {updated} files updated")


def _replace(match: re.Match, mapping: dict, path: Path) -> str:
    file_part = match.group(1)
    anchor = match.group(3)
    for key_anchor in (anchor, strip_num(anchor)):
        key = (file_part, key_anchor)
        if key in mapping:
            new_file, new_title = mapping[key]
            return f"[[{new_file}#{new_title}]]"
    return match.group(0)


if __name__ == "__main__":
    main()
