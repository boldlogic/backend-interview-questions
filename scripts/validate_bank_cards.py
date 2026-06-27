#!/usr/bin/env python3
"""Validate bank card **Что oжiдают** vs **Эталon** quality. Exit 1 on issues."""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

from bank_registry import list_bank_paths
from bank_card_validate import ValidationIssue, validate_file

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Validate bank cards: no boilerplate or etalon-duplicating **Что oжiдают**."
    )
    ap.add_argument("--check", action="store_true", help="Exit 1 if any issue (for CI/agents)")
    ap.add_argument("--report", type=str, default="", help="Write TSV report path")
    ap.add_argument("--file", type=str, default="", help="Single bank file name")
    args = ap.parse_args()

    paths = list_bank_paths()
    if args.file:
        paths = [p for p in paths if p.name == args.file or p.stem == args.file]

    all_issues: list[ValidationIssue] = []
    for path in paths:
        all_issues.extend(validate_file(path))

    if args.report:
        out = ROOT / args.report
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["file", "card", "kind", "detail"])
            for iss in all_issues:
                w.writerow([iss.file, iss.card, iss.kind, iss.detail])

    counts = Counter(i.kind for i in all_issues)
    print(f"Issues: {len(all_issues)} across {len(paths)} files")
    for kind, n in counts.most_common():
        print(f"  {kind}: {n}")

    if all_issues and (args.check or not args.report):
        print("\nExamples:")
        for iss in all_issues[:15]:
            print(f"  [{iss.kind}] {iss.file} :: {iss.card[:50]}")
        if len(all_issues) > 15:
            print(f"  ... +{len(all_issues) - 15} more")

    if args.check and all_issues:
        sys.exit(1)


if __name__ == "__main__":
    main()
