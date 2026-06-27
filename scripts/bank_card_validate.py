#!/usr/bin/env python3
"""Shared validation for bank interview card sections."""
from __future__ import annotations

import re
from dataclasses import dataclass
from difflib import SequenceMatcher

from bank_registry import WIKILINK_RE, parse_bank_cards


def is_ozhidayut_header(line: str) -> bool:
    s = line.strip()
    return s.startswith("**") and "ожидают на собесе" in s and s.endswith(":**")


def is_etalon_header(line: str) -> bool:
    s = line.strip()
    return s == "**Эталon на собесе:**" or (
        s.startswith("**") and "Этал" in s and "на собесе" in s and s.endswith(":**")
    )


def is_section_break(line: str, *, skip: frozenset[str] | None = None) -> bool:
    s = line.strip()
    if s == "---" or line.startswith("## ") or line.startswith("### "):
        return True
    if s.startswith("**") and s.endswith(":**"):
        if skip and s in skip:
            return False
        return True
    return False


BOILERPLATE_PATTERNS: tuple[re.Pattern[str], str] = (
    (re.compile(r"структурированный ответ", re.I), "boilerplate_structured"),
    (re.compile(r"краткий структурированный", re.I), "boilerplate_brief"),
    (re.compile(r"2–3 ключев", re.I), "boilerplate_key_facts"),
    (re.compile(r"ответить по существу", re.I), "boilerplate_on_point"),
    (re.compile(r"прямой структурированный", re.I), "boilerplate_direct"),
    (re.compile(r"^\s*-\s*Знать \*\*.+\*\*[ —\-–:]", re.I), "truncated_etalon_bullet"),
)

MIN_BULLET_LEN = 12
DUPLICATE_RATIO = 0.72
DUPLICATE_MIN_LEN = 30


@dataclass
class ValidationIssue:
    file: str
    card: str
    kind: str
    detail: str
    line_hint: str = ""


# No wikilink or interview timecodes in [0-9]*.md (see normalize_bank_cards.unwrap_wikilinks)
TIMECODE_RE = re.compile(
    r"(?:^|[\s(~])~?\d{1,2}:\d{2}(?:[–\-]\d{1,2}:\d{2})?",
)


def validate_no_bank_links(text: str, *, file: str) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for i, line in enumerate(text.splitlines(), start=1):
        if m := TIMECODE_RE.search(line):
            issues.append(
                ValidationIssue(
                    file,
                    f"line {i}",
                    "bank_timecode",
                    f"Таймкод в банке: {m.group().strip()}",
                    line_hint=line.strip()[:80],
                )
            )
        for m in WIKILINK_RE.finditer(line):
            issues.append(
                ValidationIssue(
                    file,
                    f"line {i}",
                    "bank_wikilink",
                    f"Wikilink в банке: [[{m.group(1)}]]",
                    line_hint=line.strip()[:80],
                )
            )
    return issues


def _norm(s: str) -> str:
    s = re.sub(r"`[^`]+`", " ", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def extract_section(lines: list[str], header_pred) -> tuple[int | None, list[str]]:
    for i, line in enumerate(lines):
        if not header_pred(line):
            continue
        body: list[str] = []
        for j in range(i + 1, len(lines)):
            if is_section_break(lines[j]):
                break
            body.append(lines[j])
        return i, body
    return None, []


def ozh_bullets(body: list[str]) -> list[str]:
    return [ln.strip()[2:].strip() for ln in body if ln.strip().startswith("- ")]


def is_boilerplate(text: str) -> str | None:
    for pat, kind in BOILERPLATE_PATTERNS:
        if pat.search(text):
            return kind
    return None


def duplicates_etalon(bullet: str, etalon: str) -> bool:
    b = _norm(bullet)
    if len(b) < DUPLICATE_MIN_LEN:
        return False
    for line in etalon.splitlines():
        e = _norm(line)
        if len(e) < 15:
            continue
        if b in e or e in b:
            return True
        if SequenceMatcher(None, b, e).ratio() >= DUPLICATE_RATIO:
            return True
        if len(b) >= 40 and b[:40] in e:
            return True
    return False


def validate_card_lines(
    lines: list[str],
    *,
    file: str,
    title: str,
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    _, ozh_body = extract_section(lines, is_ozhidayut_header)
    _, etalon_body = extract_section(lines, is_etalon_header)
    bullets = ozh_bullets(ozh_body) if ozh_body else []
    etalon = "\n".join(etalon_body) if etalon_body else ""

    if not ozh_body and etalon.strip():
        issues.append(
            ValidationIssue(
                file, title, "missing_ozhidayut", "Есть **Эталon**, но нет **Что oжiдают**"
            )
        )
        return issues

    if ozh_body is not None and not bullets:
        issues.append(ValidationIssue(file, title, "empty_ozhidayut", "Секция пустая"))
        return issues

    for bullet in bullets:
        kind = is_boilerplate(bullet)
        if kind:
            issues.append(
                ValidationIssue(file, title, kind, bullet[:100], line_hint=bullet[:60])
            )
        if etalon and duplicates_etalon(bullet, etalon):
            issues.append(
                ValidationIssue(
                    file,
                    title,
                    "duplicates_etalon",
                    f"Повторяет этalon: {bullet[:90]}",
                    line_hint=bullet[:60],
                )
            )
        if len(bullet.strip()) < MIN_BULLET_LEN and not bullet.strip().startswith("(бонус)"):
            issues.append(
                ValidationIssue(file, title, "too_short", bullet, line_hint=bullet)
            )

    return issues


def validate_file(path) -> list[ValidationIssue]:
    text = path.read_text(encoding="utf-8")
    issues: list[ValidationIssue] = list(
        validate_no_bank_links(text, file=path.name)
    )
    for card in parse_bank_cards(text):
        issues.extend(
            validate_card_lines(card["lines"], file=path.name, title=card["title"])
        )
    return issues
