#!/usr/bin/env python3
"""Findet SKILL.md, in denen der `BEGIN ausformulierungspflicht (autogen)`-
Marker innerhalb eines noch offenen fenced code blocks gelandet ist,
schneidet den Marker-Block heraus und platziert ihn unmittelbar vor dem
oeffnenden ``` der letzten Code-Fence, so dass er Skill-Instruction bleibt
und nicht in das generierte Endprodukt einfliesst.

Idempotent: wer bereits korrekt platziert ist (Marker ausserhalb fenced
block), wird uebersprungen.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

MARKER_BEGIN = "<!-- BEGIN ausformulierungspflicht (autogen) -->"
MARKER_END = "<!-- END ausformulierungspflicht (autogen) -->"

# Erfasst den gesamten Block einschliesslich der umgebenden Leerzeilen,
# damit nach dem Entfernen keine doppelten Leerzeilen entstehen.
BLOCK_RE = re.compile(
    r"\n*" + re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END) + r"\n*",
    re.DOTALL,
)


def marker_in_open_fence(text: str) -> bool:
    """True, wenn der BEGIN-Marker innerhalb eines noch offenen Fences steht."""
    idx = text.find(MARKER_BEGIN)
    if idx < 0:
        return False
    before = text[:idx]
    return before.count("```") % 2 == 1


def find_last_open_fence_before(text: str, idx: int) -> int | None:
    """Suche von idx rueckwaerts die letzte ```-Zeile, die als oeffnender
    Fence steht (also vor der ungerade viele Fences liegen). Liefert die
    Position des Zeilenanfangs des oeffnenden Fences."""
    lines = text.split("\n")
    # Position jeder Zeile berechnen
    offsets = []
    pos = 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    # Finde Zeilenindex von idx
    line_idx_of_marker = 0
    for i, off in enumerate(offsets):
        if off > idx:
            line_idx_of_marker = i - 1
            break
    else:
        line_idx_of_marker = len(lines) - 1
    # Suche rueckwaerts die letzte ```-Zeile vor dem Marker
    fence_count = 0
    last_open_fence_line = None
    for i in range(line_idx_of_marker, -1, -1):
        if lines[i].lstrip().startswith("```"):
            fence_count += 1
            # Ungerade Anzahl ``` vor Marker = der naechste rueckwaerts ist der oeffnende
            if fence_count == 1:
                last_open_fence_line = i
                # Pruefe, ob das wirklich ein oeffnender Fence ist:
                # Zaehle Fences von Dateianfang bis hierhin
                preceding_fences = sum(
                    1
                    for ln in lines[:i]
                    if ln.lstrip().startswith("```")
                )
                if preceding_fences % 2 == 0:
                    # gerade Anzahl davor => DIESER Fence ist oeffnend
                    return offsets[i]
                # sonst weitersuchen
                fence_count = 0
                continue
    return None


def fix_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if MARKER_BEGIN not in text:
        return "no-marker"
    if not marker_in_open_fence(text):
        return "ok-already"

    # Block extrahieren
    block_match = BLOCK_RE.search(text)
    if not block_match:
        return "marker-but-no-block"
    block_text = block_match.group(0).strip("\n")
    # Block entfernen
    without_block = text[: block_match.start()] + "\n" + text[block_match.end():]
    # Doppelte Leerzeilen aufraeumen
    without_block = re.sub(r"\n{3,}", "\n\n", without_block)

    # Position des oeffnenden Fences im bereinigten Text finden:
    # Da der Block jetzt entfernt ist, ist der ehemals "offene" Fence jetzt
    # wieder ein gewoehnlicher oeffnender Fence vor dem (nun leeren oder mit
    # Template-Resten gefuellten) Inhalt. Wir suchen die LETZTE ```-Zeile,
    # vor der eine gerade Anzahl von ``` steht (also ein oeffnender Fence)
    # und die innerhalb des Ausgabeformat-Blocks liegt.
    # Heuristik: nimm einfach das letzte ``` im File, das nach dem Heading
    # "## Ausgabeformat" / "## Endprodukt" / "## Output" steht.
    ausgabe_heading = re.search(
        r"^#{2,6}\s+(Ausgabe|Endprodukt|Output)[^\n]*$",
        without_block,
        re.MULTILINE | re.IGNORECASE,
    )
    if not ausgabe_heading:
        # Block wieder anhaengen, kein Fix moeglich
        return "no-ausgabe-heading"
    search_start = ausgabe_heading.end()
    # Finde alle Fence-Positionen ab search_start
    fence_positions = [
        m.start()
        for m in re.finditer(r"^```", without_block[search_start:], re.MULTILINE)
    ]
    if not fence_positions:
        return "no-fence-in-ausgabe"
    # Der erste Fence ab dem Heading ist der oeffnende Fence des Templates
    first_fence_in_section = search_start + fence_positions[0]

    # Block direkt VOR den oeffnenden Fence platzieren
    before = without_block[:first_fence_in_section].rstrip()
    after = without_block[first_fence_in_section:]
    fixed = before + "\n\n" + block_text + "\n\n" + after

    if fixed == text:
        return "no-change"
    path.write_text(fixed, encoding="utf-8")
    return "fixed"


SKIP_PARTS = {".git", "node_modules", "__pycache__", "testakten", "docs",
              "scripts", "anlagen-zu-schriftsaetzen-archiv"}


def main() -> int:
    counts: dict[str, int] = {}
    fixed_files: list[str] = []
    for skill_md in REPO.rglob("SKILL.md"):
        if any(part in SKIP_PARTS for part in skill_md.parts):
            continue
        result = fix_file(skill_md)
        counts[result] = counts.get(result, 0) + 1
        if result == "fixed":
            fixed_files.append(str(skill_md.relative_to(REPO)))

    for k, v in sorted(counts.items()):
        print(f"{k}: {v}")
    if fixed_files:
        print(f"\nFixed files ({len(fixed_files)}):")
        for f in fixed_files[:50]:
            print(f"  {f}")
        if len(fixed_files) > 50:
            print(f"  ... ({len(fixed_files)-50} weitere)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
