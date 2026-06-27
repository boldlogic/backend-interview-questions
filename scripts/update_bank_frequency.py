#!/usr/bin/env python3
"""Recompute **Частота:** N/D in bank cards from transcript inline База markup."""
from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

from bank_registry import (
    BANK_GLOB,
    INDEX_FILE,
    ROOT,
    build_question_registry,
    list_bank_paths,
    list_transcripts,
    load_index_aliases,
    norm_file,
    norm_heading,
    parse_bank_cards,
    parse_wikilinks,
    resolve_link,
)

REPORT_PATH = ROOT / "scripts" / "frequency_report.tsv"
FREQ_LINE_RE = re.compile(r"^\*\*Частота:\*\*\s*(.*)$")


def build_transcript_hits(
    resolver,
    aliases,
    number_index,
    prefix_index,
):
    hits: dict[tuple[str, str], set[str]] = defaultdict(set)
    orphans: list[dict] = []

    for path in list_transcripts():
        seen_in_transcript: set[tuple[str, str]] = set()
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip().startswith("> 📎 **База:**"):
                continue
            for file_part, heading in parse_wikilinks(line):
                canon = resolve_link(
                    file_part, heading, resolver, aliases, number_index, prefix_index
                )
                if canon is None:
                    orphans.append(
                        {"transcript": path.name, "file": file_part, "heading": heading}
                    )
                    continue
                if canon in seen_in_transcript:
                    continue
                seen_in_transcript.add(canon)
                hits[canon].add(path.name)

    return hits, orphans


def count_for_card(bank_file: str, card_title: str, hits) -> int:
    nf = norm_file(bank_file)
    nh = norm_heading(card_title)
    return len(hits.get((nf, nh), set()))


def read_old_freq(body_lines: list[str]) -> str:
    for ln in body_lines[1:]:
        m = FREQ_LINE_RE.match(ln)
        if m:
            return m.group(1).strip()
    return "—"


def freq_line(n: int, d: int) -> str:
    return f"**Частота:** {n}/{d}"


def upsert_freq_in_card(lines: list[str], n: int, d: int) -> list[str]:
    new_line = freq_line(n, d)
    out = list(lines)
    for i, ln in enumerate(out):
        if ln.startswith("**Частота:**"):
            out[i] = new_line
            return out
    insert_at = 1
    while insert_at < len(out) and out[insert_at].strip() == "":
        insert_at += 1
    out.insert(insert_at, new_line)
    return out


def apply_bank_file(path: Path, hits, d: int, dry_run: bool) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    cards = parse_bank_cards(text)
    changes: list[dict] = []

    replacements: list[tuple[int, int, list[str]]] = []
    for card in cards:
        n = count_for_card(path.name, card["title"], hits)
        old = read_old_freq(card["lines"])
        new = f"{n}/{d}"
        updated = upsert_freq_in_card(card["lines"], n, d)
        if old != new:
            changes.append(
                {"file": path.name, "title": card["title"], "old_freq": old, "new_freq": new}
            )
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
    if not dry_run and new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return changes


def update_go_index(hits, d: int, dry_run: bool) -> int:
    path = ROOT / INDEX_FILE
    lines = path.read_text(encoding="utf-8").splitlines()
    updated = 0
    out: list[str] = []
    for line in lines:
        if not line.startswith("|") or line.startswith("|-"):
            out.append(line)
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 6:
            out.append(line)
            continue
        new_file = parts[2]
        new_title = parts[3]
        if not new_file.endswith(".md") or new_title in ("новый заголовок", "—"):
            out.append(line)
            continue
        n = count_for_card(new_file, new_title, hits)
        new_freq = f"{n}/{d}"
        if parts[4] != new_freq:
            parts[4] = new_freq
            updated += 1
        out.append("| " + " | ".join(parts) + " |")
    new_text = "\n".join(out)
    if path.read_text(encoding="utf-8").endswith("\n"):
        new_text += "\n"
    if not dry_run and updated:
        path.write_text(new_text, encoding="utf-8")
    return updated


def write_report(all_changes, orphans, hits, d: int) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["file", "title", "old_freq", "new_freq"])
        for row in sorted(
            all_changes,
            key=lambda r: (-int(r["new_freq"].split("/")[0]), r["file"], r["title"]),
        ):
            w.writerow([row["file"], row["title"], row["old_freq"], row["new_freq"]])
        w.writerow([])
        w.writerow(["orphan_transcript", "orphan_file", "orphan_heading"])
        seen: set[tuple[str, str]] = set()
        for o in orphans:
            key = (o["file"], o["heading"])
            if key in seen:
                continue
            seen.add(key)
            w.writerow([o["transcript"], o["file"], o["heading"]])
        w.writerow([])
        w.writerow(["rank", "file", "heading", "count", "denominator"])
        ranked = sorted(hits.items(), key=lambda x: (-len(x[1]), x[0][0], x[0][1]))
        for i, ((nf, nh), txs) in enumerate(ranked[:20], 1):
            if txs:
                w.writerow([i, nf + ".md", nh, len(txs), d])


def run(dry_run: bool) -> None:
    transcripts = list_transcripts()
    d = len(transcripts)
    bank_paths = list_bank_paths()

    resolver, number_index, prefix_index, _display = build_question_registry(bank_paths)
    aliases = load_index_aliases()
    hits, orphans = build_transcript_hits(resolver, aliases, number_index, prefix_index)

    bank_cards = {bp.name: parse_bank_cards(bp.read_text(encoding="utf-8")) for bp in bank_paths}
    total_cards = sum(len(c) for c in bank_cards.values())
    with_hits = sum(
        1
        for bp in bank_paths
        for card in bank_cards[bp.name]
        if count_for_card(bp.name, card["title"], hits) > 0
    )

    all_changes: list[dict] = []
    for bp in bank_paths:
        all_changes.extend(apply_bank_file(bp, hits, d, dry_run))
    index_updates = update_go_index(hits, d, dry_run)
    write_report(all_changes, orphans, hits, d)

    mode = "DRY-RUN" if dry_run else "WRITE"
    print(f"=== update_bank_frequency ({mode}) ===")
    print(f"Corpus D={d} transcripts")
    print(f"Bank cards: {total_cards}, with N>0: {with_hits}, zero: {total_cards - with_hits}")
    print(f"Unique questions with hits: {sum(1 for s in hits.values() if s)}")
    print(f"Orphan link pairs: {len({(o['file'], o['heading']) for o in orphans})}")
    print(f"Card frequency lines changed: {len(all_changes)}")
    print(f"GO index rows updated: {index_updates}")
    print(f"Report: {REPORT_PATH.relative_to(ROOT)}")

    top = sorted(hits.items(), key=lambda x: -len(x[1]))[:5]
    for (nf, nh), txs in top:
        print(f"  top: {len(txs)}/{d}  {nf}.md | {nh}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Apply changes")
    parser.add_argument(
        "--full-corpus",
        action="store_true",
        help="Required with --write: explicit intent to recompute ALL bank cards",
    )
    parser.add_argument("--check", action="store_true", help="Exit 1 if frequency lines would change")
    args = parser.parse_args()
    if args.write and not args.full_corpus:
        print(
            "ERROR: --write пересчитывает ВЕСЬ банк и затирает ручные частоты.\n"
            "Для одного собеса: scripts/apply_simber_frequency_bump.py --write\n"
            "Для полного пересчёта: --write --full-corpus (только по явной просьбе пользователя)",
            file=sys.stderr,
        )
        raise SystemExit(2)
    dry_run = not args.write
    run(dry_run=dry_run)
    if args.check and dry_run:
        for line in REPORT_PATH.read_text(encoding="utf-8").splitlines():
            if not line or line.startswith("file\t"):
                continue
            if line.startswith("orphan") or line.startswith("rank"):
                break
            raise SystemExit(1)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
