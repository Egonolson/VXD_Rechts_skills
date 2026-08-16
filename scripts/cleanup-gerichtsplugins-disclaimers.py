#!/usr/bin/env python3
"""
Entfernt KI-VO/Aktengeheimnis/DSGVO-Blöcke aus den Prompts und Skills
in gerichtsplugins/. Diese Hinweise gehören nur in die README.md der Plugins,
nicht in den eigentlichen Prompt-Content, weil das System den eigenen Hinweis
nicht "wissen" muss — der Hinweis adressiert den menschlichen Nutzer und
gehört in die Plugin-Dokumentation.

Was entfernt wird:

- Werkstatt-Prompt:
  - Zeile: > **Vorsicht: ... Art. 22 DSGVO und KI-VO beachten.**
  - Sektion: ## Aktengeheimnis (...)
  - Sektion: ## KI-VO-Hinweis
- Schnellstart-Prompt:
  - Sektion: ## Aktengeheimnis
  - Sektion: ## Art. 22 DSGVO und KI-VO
- SKILL.md:
  - Sektion: ## Warnhinweis (immer)
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GERICHTSPLUGINS = ROOT / "gerichtsplugins"


def remove_section(text: str, header_pattern: str) -> str:
    """Entfernt einen ##-Abschnitt inklusive Inhalt bis zum nächsten ##-Header oder Dateiende."""
    pattern = re.compile(
        r"^##\s+" + header_pattern + r"\b[^\n]*\n.*?(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub("", text)


def remove_vorsicht_line(text: str) -> str:
    """Entfernt die Vorsicht-Quote-Zeile mit DSGVO/KI-VO-Hinweis."""
    pattern = re.compile(
        r"^>\s*\*\*Vorsicht:[^\n]*?(?:DSGVO|KI-VO)[^\n]*\*\*\n",
        re.MULTILINE,
    )
    return pattern.sub("", text)


def normalize_blank_lines(text: str) -> str:
    """Mehr als zwei Leerzeilen zu zwei reduzieren."""
    return re.sub(r"\n{3,}", "\n\n", text)


def process_megaprompt(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out = raw
    out = remove_vorsicht_line(out)
    out = remove_section(out, r"Aktengeheimnis")
    out = remove_section(out, r"KI-VO-Hinweis")
    out = normalize_blank_lines(out)
    if out != raw:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def process_miniprompt(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out = raw
    out = remove_section(out, r"Aktengeheimnis")
    out = remove_section(out, r"Art\.\s*22\s*DSGVO\s*und\s*KI-VO")
    out = normalize_blank_lines(out)
    if out != raw:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def process_skill(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    out = raw
    out = remove_section(out, r"Warnhinweis\s*\(immer\)")
    out = remove_section(out, r"Warnhinweis")
    out = normalize_blank_lines(out)
    if out != raw:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main() -> int:
    if not GERICHTSPLUGINS.is_dir():
        print(f"FEHLER: {GERICHTSPLUGINS} fehlt", file=sys.stderr)
        return 1

    changed_mega = changed_mini = changed_skill = 0

    for mega in GERICHTSPLUGINS.glob("*/*-werkstatt.md"):
        if process_megaprompt(mega):
            changed_mega += 1
            print(f"  werkstatt: {mega.relative_to(ROOT)}")

    for mini in GERICHTSPLUGINS.glob("*/*-schnellstart.md"):
        if process_miniprompt(mini):
            changed_mini += 1
            print(f"  schnellstart: {mini.relative_to(ROOT)}")

    for skill in GERICHTSPLUGINS.glob("*/skills/*/SKILL.md"):
        if process_skill(skill):
            changed_skill += 1

    print(f"\nWerkstatt-Prompts geändert: {changed_mega}")
    print(f"Schnellstart-Prompts geändert: {changed_mini}")
    print(f"Skills geändert: {changed_skill}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
