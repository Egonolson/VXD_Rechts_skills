#!/usr/bin/env python3
"""Prüft CSV-Aktenstücke auf Feldverschiebungen und verräterische Lösungshilfen."""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "testakten"
HEADER_HINTS = {
    "anmerkung",
    "art",
    "betrag",
    "beleg",
    "bemerkung",
    "beschreibung",
    "buchungstag",
    "datum",
    "faelligkeit",
    "fälligkeit",
    "kreditor",
    "monat",
    "name",
    "position",
    "saldo",
    "status",
    "stichtag",
    "vorgang",
    "zeitraum",
}
SOLUTION_HINT = re.compile(
    r"^\s*#\s*(?:Lesehilfe|Ergebnis|Kontrollrechnung|Diskrepanz|Lösung)",
    re.IGNORECASE,
)
DATE_OR_NUMBER = re.compile(r"^(?:\d{1,4}(?:[.,/-]\d{1,4})*|-?\d+(?:[.,]\d+)?)$")


@dataclass(frozen=True)
class ParsedLine:
    number: int
    text: str
    cells: list[str]


def delimiter_for(lines: list[tuple[int, str]]) -> str:
    sample = lines[0][1]
    return ";" if sample.count(";") > sample.count(",") else ","


def header_score(cells: list[str]) -> float:
    score = len(cells) * 0.1
    for cell in cells:
        value = cell.strip().casefold()
        tokens = set(re.findall(r"[a-zäöüß]+", value))
        score += 4 * len(tokens & HEADER_HINTS)
        if "_" in value:
            score += 2
        if value and not DATE_OR_NUMBER.fullmatch(value) and any(ch.isalpha() for ch in value):
            score += 0.5
        if DATE_OR_NUMBER.fullmatch(value):
            score -= 1
    return score


def parse_lines(path: Path) -> tuple[list[ParsedLine], list[str]]:
    raw_lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    findings = [
        f"{path.relative_to(ROOT.parent)}:{number}: lösungsverratender CSV-Kommentar"
        for number, line in enumerate(raw_lines, start=1)
        if SOLUTION_HINT.search(line)
    ]
    content = [
        (number, line)
        for number, line in enumerate(raw_lines, start=1)
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not content:
        return [], findings
    delimiter = delimiter_for(content)
    parsed = [
        ParsedLine(number, line, next(csv.reader([line], delimiter=delimiter)))
        for number, line in content
    ]
    return parsed, findings


def validate_file(path: Path) -> list[str]:
    rows, findings = parse_lines(path)
    if not rows:
        return findings
    candidates = rows[: min(5, len(rows))]
    header = max(candidates, key=lambda row: header_score(row.cells))
    expected = len(header.cells)
    if expected < 2:
        findings.append(
            f"{path.relative_to(ROOT.parent)}:{header.number}: CSV-Kopf hat weniger als zwei Spalten"
        )
        return findings
    header_index = rows.index(header)
    for row in rows[header_index + 1 :]:
        if len(row.cells) != expected:
            findings.append(
                f"{path.relative_to(ROOT.parent)}:{row.number}: "
                f"{len(row.cells)} statt {expected} CSV-Spalten"
            )
    return findings


def main() -> int:
    files = sorted(ROOT.rglob("*.csv"))
    findings = [finding for path in files for finding in validate_file(path)]
    if findings:
        print(f"validate-testakten-csv: {len(findings)} Fehler")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print(f"validate-testakten-csv OK ({len(files)} CSV-Aktenstücke)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
