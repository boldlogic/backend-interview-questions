#!/usr/bin/env python3
"""Warn or block edits when git working tree has uncommitted changes under target paths."""
from __future__ import annotations

import argparse
import fnmatch
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUP_DIR = ROOT / "Заметки" / ".backups"


def git_dirty_paths() -> list[str]:
    """Paths with unstaged/staged/untracked changes relative to HEAD."""
    env = {**os.environ, "LC_ALL": "C.UTF-8"}
    paths: set[str] = set()
    for cmd in (
        ["git", "-c", "core.quotepath=false", "diff", "--name-only"],
        ["git", "-c", "core.quotepath=false", "diff", "--cached", "--name-only"],
        ["git", "-c", "core.quotepath=false", "ls-files", "-o", "--exclude-standard"],
    ):
        out = subprocess.check_output(cmd, cwd=ROOT, text=True, encoding="utf-8", env=env)
        for line in out.splitlines():
            p = line.strip().strip('"').replace("\\", "/")
            if p:
                paths.add(p)
    return sorted(paths)


def matches_any(path: str, patterns: list[str]) -> bool:
    norm = path.replace("\\", "/")
    name = Path(norm).name
    for pat in patterns:
        pat = pat.replace("\\", "/")
        if fnmatch.fnmatch(norm, pat) or fnmatch.fnmatch(name, pat):
            return True
        # explicit file path without glob
        if pat == norm or norm.endswith("/" + pat):
            return True
        if "*/" not in pat and pat in norm:
            return True
    return False


def backup_file(rel_path: str) -> Path:
    src = ROOT / rel_path
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe = rel_path.replace("/", "__")
    dest = BACKUP_DIR / f"{stamp}--{safe}"
    dest.write_bytes(src.read_bytes())
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--paths",
        nargs="+",
        default=["Транскрипты/*.md", "[0-9]*.md", "Задачи/*.md"],
        help="Glob patterns (relative to repo root)",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Copy dirty matched files to Заметки/.backups/ before proceeding",
    )
    parser.add_argument(
        "--require-clean",
        action="store_true",
        help="Exit 1 if any matched file is dirty (agent must not overwrite)",
    )
    args = parser.parse_args()

    dirty = [p for p in git_dirty_paths() if matches_any(p, args.paths)]
    if not dirty:
        print("pre_edit_guard: OK — no uncommitted changes under target paths")
        raise SystemExit(0)

    print("pre_edit_guard: WARNING — uncommitted changes:")
    for p in sorted(set(dirty)):
        print(f"  M {p}")

    if args.backup:
        for p in sorted(set(dirty)):
            bp = backup_file(p)
            print(f"  backup: {bp.relative_to(ROOT)}")

    if args.require_clean:
        print("\nBlocked: commit, stash, or explicit user approval before overwrite.")
        raise SystemExit(1)

    print("\nProceed only with surgical edits; never git checkout/restore these files.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
