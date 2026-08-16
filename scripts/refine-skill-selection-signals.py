#!/usr/bin/env python3
"""Schärft Skill-Beschreibungen als präzise Auswahlsignale."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DUPLICATE_TITLE_RE = re.compile(r"^([^:]{3,90}):\s*\1:", re.IGNORECASE)
COMMA_NUMBER_RE = re.compile(r"\d\s*,\s*\d")

OUTPUT_RULES: tuple[tuple[tuple[str, ...], str], ...] = (
    (("chronologie", "belegmatrix", "timeline"), "eine Chronologie mit Belegmatrix und Widerspruchsliste"),
    (("fristen", "frist", "risikoampel"), "eine Fristen- und Risikoampel mit Sofortschritten"),
    (("red-team", "qualitygate", "qualitaet", "kontrolle"), "eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck"),
    (("mandantenkommunikation", "entscheidungsvorlage"), "eine Mandantennachricht oder Entscheidungsvorlage"),
    (("schriftsatz", "klage", "antrag", "brief", "memo", "textbausteine"), "einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik"),
    (("dokumentenmatrix", "lueckenliste", "unterlagen"), "eine Dokumentenmatrix mit Nachforderungsliste"),
    (("beweislast", "darlegungslast", "substantiierung", "beweis"), "eine Beweislast- und Substantiierungsmatrix"),
    (("zahlen", "schwellen", "berechnung", "betrag", "gebuehr"), "eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen"),
    (("formular", "portal", "einreichung", "register"), "einen Einreichungsplan mit Form-, Portal- und Nachweischeck"),
    (("verhandlung", "vergleich", "eskalation", "strategie"), "eine Verhandlungs- oder Eskalationslinie mit Optionen"),
    (("international", "schnittstellen", "ausland", "eu"), "eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen"),
    (("tatbestand", "subsumtion", "norm", "anspruch", "pruefung"), "eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten"),
)


def yaml_quote(value: str) -> str:
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def frontmatter_bounds(text: str) -> tuple[int, int] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return 4, end


def field_value(frontmatter: str, field: str) -> str:
    match = re.search(rf"^{re.escape(field)}:\s*(.+)$", frontmatter, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] in {"'", '"'} and value[-1] == value[0]:
        value = value[1:-1]
    return value


def set_description(frontmatter: str, description: str) -> str:
    line = f"description: {yaml_quote(description)}"
    if re.search(r"^description:\s*.+$", frontmatter, re.MULTILINE):
        return re.sub(r"^description:\s*.+$", line, frontmatter, count=1, flags=re.MULTILINE)
    return frontmatter.rstrip() + "\n" + line + "\n"


def skill_files() -> list[Path]:
    return sorted(
        p
        for p in REPO.rglob("SKILL.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    )


def plugin_root(path: Path) -> Path:
    rel = path.relative_to(REPO)
    parts = rel.parts
    if "skills" not in parts:
        return path.parent.parent
    return REPO.joinpath(*parts[: parts.index("skills")])


def plugin_meta(root: Path) -> dict[str, str]:
    manifest = root / ".claude-plugin" / "plugin.json"
    if not manifest.is_file():
        return {"name": root.name, "description": ""}
    data = json.loads(manifest.read_text(encoding="utf-8"))
    return {"name": data.get("name", root.name), "description": data.get("description", "")}


def readme_title(root: Path) -> str:
    readme = root / "README.md"
    if not readme.is_file():
        return ""
    for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            title = line[2:].strip(" #")
            title = re.sub(r"\s+", " ", title)
            title = re.sub(r"\s*\([^)]{1,80}\)\s*$", "", title).strip()
            return title
    return ""


def humanize(text: str) -> str:
    text = re.sub(r"^\d+[-_]", "", text)
    text = text.replace("_", "-").replace("/", "-")
    words = [w for w in text.split("-") if w]
    replacements = {
        "ae": "ä",
        "oe": "ö",
        "ue": "ü",
        "ss": "ß",
        "pruefung": "Prüfung",
        "pruefer": "Prüfer",
        "zustaendigkeit": "Zuständigkeit",
        "fuer": "für",
        "ueber": "über",
        "luecken": "Lücken",
        "lueckenliste": "Lückenliste",
        "klaeger": "Kläger",
        "beklagten": "Beklagten",
        "geschaeftsfuehrer": "Geschäftsführer",
        "gesellschaftsrecht": "Gesellschaftsrecht",
        "migrationsrecht": "Migrationsrecht",
        "insolvenzrecht": "Insolvenzrecht",
        "familienrecht": "Familienrecht",
        "mietrecht": "Mietrecht",
        "strafrecht": "Strafrecht",
        "rentenrecht": "Rentenrecht",
        "sozialrecht": "Sozialrecht",
        "bgb": "BGB",
        "hgb": "HGB",
        "zpo": "ZPO",
        "stpo": "StPO",
        "vwg": "VwG",
        "vvg": "VVG",
        "gmbh": "GmbH",
        "ag": "AG",
        "eu": "EU",
        "drv": "DRV",
        "ma": "M&A",
    }
    out: list[str] = []
    for word in words:
        lower = word.lower()
        out.append(replacements.get(lower, lower.capitalize()))
    return " ".join(out)


def heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip(" #")
    return ""


def clean_description(desc: str) -> str:
    desc = desc.replace("<->", "gegenüber").replace("<", "").replace(">", "")
    desc = desc.replace("§§", "Paragrafen").replace("§", "Paragraf")
    desc = desc.replace("ParagrafParagraf", "Paragrafen")
    desc = desc.replace("…", "...")
    desc = re.sub(r"\bKI-VO\b", "europäischer Technikregulierungsrahmen", desc)
    desc = re.sub(r"\bKI\b", "digitale Werkzeuge", desc)
    desc = re.sub(r"\bAI\b", "digitale Werkzeuge", desc)
    desc = re.sub(r"\bim Plugin\s+([^;.,]+)", r"im Bereich \1", desc)
    desc = re.sub(r"\b([A-ZÄÖÜ][A-Za-zÄÖÜäöüß -]+)-Plugin\b", r"\1", desc)
    desc = re.sub(r"\s+", " ", desc).strip()
    while DUPLICATE_TITLE_RE.search(desc):
        desc = DUPLICATE_TITLE_RE.sub(r"\1:", desc)
    desc = re.sub(r"(: [^:]{8,120})\s*:\s*\1\b", r"\1", desc)
    desc = re.sub(r"\s+fachlich vertieftes Modul mit[^.]+", "", desc)
    desc = re.sub(r"\s+Skill vertieft\b", " Vertieft", desc)
    desc = re.sub(r"\bLiefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt\.?", "", desc)
    desc = re.sub(r"\s+prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung\.?", "", desc)
    desc = re.sub(r"\s+", " ", desc).strip(" ;")
    return desc


def first_sentence(text: str, limit: int = 230) -> str:
    text = text.strip()
    if not text:
        return ""
    text = re.split(r"(?<=[.!?])\s+", text)[0]
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        cut = max(text.rfind(";", 0, limit), text.rfind(".", 0, limit), text.rfind(",", 0, limit), text.rfind(" ", 0, limit))
        text = text[: cut if cut > 80 else limit].rstrip(" ,;:.")
    return text.rstrip(".") + "."


def output_for(slug: str, desc: str) -> str:
    haystack = f"{slug} {desc}".lower()
    for needles, output in OUTPUT_RULES:
        if any(needle in haystack for needle in needles):
            return output
    return "ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt"


def domain_for(root: Path, meta: dict[str, str]) -> str:
    special_domains = {
        "berufsrecht-ki-vertragspruefung": "anwaltlichem Berufsrecht und Vertragsprüfung",
        "festlandchina-wirtschaftsverkehr": "China-Wirtschaftsverkehr",
        "grosskanzlei-corporate-ma": "Großkanzlei Corporate/M&A",
        "mittelstand-corporate-ma": "Mittelstands-Corporate/M&A",
        "ki-governance": "Technik-Governance",
        "ki-richtlinie-kanzleien": "Kanzleirichtlinien für digitale Werkzeuge",
        "ki-vo-ai-act-pruefer": "europäischem Technikregulierungsrecht",
        "word-legal-ai-plugin-and-skill-for-german-lawyers": "Word-Workflows für deutsche Juristen",
    }
    if root.name in special_domains:
        return special_domains[root.name]
    name = meta.get("name") or root.name
    slug_tokens = set(re.split(r"[-_]", f"{root.name}-{name}".lower()))
    if {"ki", "ai"} & slug_tokens:
        return "diesem Spezialbereich"
    domain = readme_title(root) or humanize(name)
    if len(domain) > 58:
        domain = domain[:58].rsplit(" ", 1)[0]
    return domain or "diesem Rechtsbereich"


def has_slug_domain(desc: str, root: Path, meta: dict[str, str]) -> bool:
    if not desc.startswith("Wenn es um "):
        return False
    candidates = {
        humanize(root.name),
        humanize(meta.get("name", "")),
        root.name.replace("-", " ").replace("_", " ").title(),
        (meta.get("name", "") or "").replace("-", " ").replace("_", " ").title(),
    }
    candidates.discard("")
    return any(f" in {candidate} geht:" in desc for candidate in candidates)


def topic_for(path: Path, body: str) -> str:
    title = heading(body)
    if title:
        title = re.sub(r"\s+", " ", title).strip()
        title = re.sub(r"\s+im\s+([A-Za-zÄÖÜäöüß -]+)-Plugin\b", r" in \1", title)
        if 8 <= len(title) <= 90:
            return title
    return humanize(path.parent.name)


def action_for(desc: str, slug: str) -> str:
    lower = f"{desc} {slug}".lower()
    if any(word in lower for word in ("erstpruefung", "triage", "kaltstart", "routing", "einstieg")):
        return "klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill"
    if any(word in lower for word in ("schriftsatz", "klage", "antrag", "brief", "memo", "textbaustein")):
        return "erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag"
    if any(word in lower for word in ("red-team", "qualitygate", "kontrolle", "gegenargument")):
        return "zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition"
    if any(word in lower for word in ("fristen", "frist", "zustaendigkeit", "rechtsweg")):
        return "prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen"
    if any(word in lower for word in ("dokument", "unterlage", "akte", "beleg", "luecke")):
        return "ordnet Akteninhalt, Belege, Lücken und Nachforderungen"
    if any(word in lower for word in ("berechnung", "zahlen", "schwellen", "betrag")):
        return "rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch"
    if any(word in lower for word in ("verhandlung", "vergleich", "eskalation")):
        return "entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad"
    return "ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt"


def should_upgrade(desc: str, duplicate_count: int) -> bool:
    return (
        not desc
        or not desc.startswith("Wenn es um ")
        or len(desc) < 140
        or duplicate_count > 1
        or bool(DUPLICATE_TITLE_RE.search(desc))
        or "fachlich vertieftes Modul" in desc
        or "konkretisierter Spezialmodul" in desc
        or "Spezialmodul mit Prüfachsen" in desc
        or "im Plugin" in desc
        or "-Plugin" in desc
        or desc.endswith("...")
        or "..." in desc[:320]
        or " auftaucht:" in desc
        or "prüft konkret die einschlägigen" in desc
        or "Liefert ein belastbares Arbeitsprodukt" in desc
        or desc.startswith(("Hilft ", "Bearbeite ", "Er soll "))
    )


def build_selector(path: Path, body: str, old_desc: str, root: Path, meta: dict[str, str]) -> str:
    topic = topic_for(path, body)
    domain = domain_for(root, meta)
    action = action_for(old_desc, path.parent.name)
    output = output_for(path.parent.name, old_desc)
    if topic.lower().startswith(("führt ", "juristische ", "spezialfall ")):
        topic = humanize(path.parent.name)
    desc = f"Wenn es um {topic} in {domain} geht: {action}; liefert {output}."
    desc = desc.replace("§", "Paragraf")
    desc = re.sub(r"\s+", " ", desc).strip()
    return desc


def add_alias_signal(desc: str, path: Path, duplicate_count: int) -> str:
    if duplicate_count <= 1:
        return desc
    slug_hint = humanize(path.parent.name)
    if slug_hint and slug_hint.lower() not in desc.lower():
        return f"{desc.rstrip('.')}. Stichwort für die Auswahl: {slug_hint}."
    return desc


def normalize(path: Path, old_desc: str, duplicate_count: int, root: Path, meta: dict[str, str], body: str) -> str:
    cleaned = clean_description(old_desc)
    if should_upgrade(old_desc, duplicate_count) or should_upgrade(cleaned, duplicate_count) or has_slug_domain(cleaned, root, meta):
        cleaned = build_selector(path, body, cleaned, root, meta)
    else:
        cleaned = first_sentence(cleaned, 360)
        if len(cleaned) < 140:
            cleaned = build_selector(path, body, cleaned, root, meta)
    cleaned = add_alias_signal(cleaned, path, duplicate_count)
    cleaned = clean_description(cleaned)
    cleaned = re.sub(
        r"Wenn es um (.+?) in ([A-ZÄÖÜ][^:;.]{2,70}) in \2 geht:",
        r"Wenn es um \1 in \2 geht:",
        cleaned,
    )
    cleaned = cleaned.replace("...", "")
    cleaned = cleaned.replace("-Plugin", "")
    cleaned = cleaned.replace("§", "Paragraf")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"\s+([.;,:])", r"\1", cleaned)
    if COMMA_NUMBER_RE.search(cleaned):
        cleaned = COMMA_NUMBER_RE.sub(lambda m: m.group(0).replace(",", "."), cleaned)
    if len(cleaned) > 760:
        cleaned = first_sentence(cleaned, 520)
    if len(cleaned) < 80:
        cleaned = build_selector(path, body, cleaned, root, meta)
    return cleaned


def current_description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    bounds = frontmatter_bounds(text)
    if not bounds:
        return ""
    return field_value(text[bounds[0] : bounds[1]], "description")


def write_description(path: Path, description: str) -> None:
    text = path.read_text(encoding="utf-8")
    bounds = frontmatter_bounds(text)
    if not bounds:
        return
    frontmatter = text[bounds[0] : bounds[1]]
    path.write_text(text[: bounds[0]] + set_description(frontmatter, description) + text[bounds[1] :], encoding="utf-8")


def deduplicate_current_descriptions(files: list[Path]) -> int:
    descriptions: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        desc = current_description(path)
        if desc:
            descriptions[desc].append(path)

    meta_cache: dict[Path, dict[str, str]] = {}
    changed = 0
    for desc, paths in descriptions.items():
        if len(paths) <= 1:
            continue
        for index, path in enumerate(sorted(paths), start=1):
            root = plugin_root(path)
            meta_cache.setdefault(root, plugin_meta(root))
            slug_hint = humanize(path.parent.name)
            domain = domain_for(root, meta_cache[root])
            suffix = f" Auswahlstichwort: {slug_hint}; Arbeitsfeld: {domain}."
            new_desc = desc.rstrip(".")
            if "Auswahlstichwort:" not in new_desc:
                new_desc += "." + suffix
            elif suffix not in new_desc:
                new_desc += f" Variante {index}."
            new_desc = clean_description(new_desc)
            if new_desc != current_description(path):
                write_description(path, new_desc)
                changed += 1
    return changed


def main() -> int:
    files = skill_files()
    original: dict[Path, str] = {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        bounds = frontmatter_bounds(text)
        if not bounds:
            continue
        frontmatter = text[bounds[0] : bounds[1]]
        original[path] = field_value(frontmatter, "description")

    counts = Counter(original.values())
    meta_cache: dict[Path, dict[str, str]] = {}
    changed = 0
    for path, old_desc in original.items():
        text = path.read_text(encoding="utf-8")
        bounds = frontmatter_bounds(text)
        if not bounds:
            continue
        root = plugin_root(path)
        meta_cache.setdefault(root, plugin_meta(root))
        new_desc = normalize(path, old_desc, counts[old_desc], root, meta_cache[root], text[bounds[1] + 5 :])
        if new_desc == old_desc:
            continue
        frontmatter = text[bounds[0] : bounds[1]]
        updated_fm = set_description(frontmatter, new_desc)
        path.write_text(text[: bounds[0]] + updated_fm + text[bounds[1] :], encoding="utf-8")
        changed += 1

    print(f"Skill-Beschreibungen aktualisiert: {changed}/{len(original)}")
    deduped = deduplicate_current_descriptions(files)
    print(f"Exakte Beschreibungsdoppelungen nachgeschärft: {deduped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
