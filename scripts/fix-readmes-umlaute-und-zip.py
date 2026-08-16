#!/usr/bin/env python3
"""Reparatur der Plugin-READMEs:
1. Umschriften ae/oe/ue/ss in echte Umlaute aussern Code-Bloecken, URLs und HTML-Attributen.
2. ZIP-Direktdownload in der Direkt-Downloads-Tabelle ergaenzen, falls nicht vorhanden.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MP = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())

REPO_RAW = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"
REPO_REL = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"

# Wort-zu-Umlaut-Mapping. Reihenfolge wichtig (laengere zuerst).
UMLAUT_MAP = [
    # Sonderfaelle / Zusammensetzungen
    ("aussergewoehnlich", "außergewöhnlich"),
    ("regelmaessig", "regelmäßig"),
    ("regelmaessige", "regelmäßige"),
    ("regelmaessigen", "regelmäßigen"),
    ("regelmaessiger", "regelmäßiger"),
    ("Geschaeftsfuehrer", "Geschäftsführer"),
    ("Geschaeftsfuehrerin", "Geschäftsführerin"),
    ("geschaeftsfuehrend", "geschäftsführend"),
    ("staatsanwaltschaftlich", "staatsanwaltschaftlich"),
    ("Staatsanwaltschaft", "Staatsanwaltschaft"),
    ("Empfaengerhorizont", "Empfängerhorizont"),
    ("Empfaenger", "Empfänger"),
    ("Bautraegervertrag", "Bauträgervertrag"),
    ("bautraegervertrag", "bauträgervertrag"),
    ("Bautraeger", "Bauträger"),
    ("bautraeger", "bauträger"),
    ("Maengelhaftung", "Mängelhaftung"),
    ("Maengelrechte", "Mängelrechte"),
    ("Maengelanzeige", "Mängelanzeige"),
    ("Maengelrechten", "Mängelrechten"),
    ("Maengel", "Mängel"),
    ("Maengelruege", "Mängelrüge"),
    ("Erloeschen", "Erlöschen"),
    ("Vermoegenswertabnahme", "Vermögenswertabnahme"),
    ("Vermoegen", "Vermögen"),
    ("Beschluesse", "Beschlüsse"),
    ("Beschluessen", "Beschlüssen"),
    ("Beschluss", "Beschluss"),
    ("Verfuegung", "Verfügung"),
    ("verfuegt", "verfügt"),
    ("verfuegung", "verfügung"),
    ("Belehrungspflicht", "Belehrungspflicht"),
    ("Tatbestandsmerkmal", "Tatbestandsmerkmal"),
    ("Tatbestandsmerkmale", "Tatbestandsmerkmale"),
    ("Voraussetzungen", "Voraussetzungen"),
    ("Stilrichtungen", "Stilrichtungen"),
    ("Eigenschaeft", "Eigenschaft"),
    ("Allgemeingueltig", "Allgemeingültig"),
    ("Maengelruege", "Mängelrüge"),
    ("Maengelansprueche", "Mängelansprüche"),
    ("Maengelanspruch", "Mängelanspruch"),
    ("Wohnflaechenverordnung", "Wohnflächenverordnung"),
    ("Auflassungsvormerkung", "Auflassungsvormerkung"),
    ("Veraeusserung", "Veräußerung"),
    ("veraeussern", "veräußern"),
    ("Ueberzeugung", "Überzeugung"),
    ("Ueberzeugungen", "Überzeugungen"),
    ("Praezisierung", "Präzisierung"),
    ("praezise", "präzise"),
    ("Praezision", "Präzision"),
    ("Auseinandersetzung", "Auseinandersetzung"),
    ("Pruefungsmassstab", "Prüfungsmaßstab"),
    ("Pruefungsmassstaeben", "Prüfungsmaßstäben"),
    ("Pruefraster", "Prüfraster"),
    ("Pruefpunkt", "Prüfpunkt"),
    ("Pruefpunkten", "Prüfpunkten"),
    ("Pruefpunkte", "Prüfpunkte"),
    ("Anhoerung", "Anhörung"),
    ("Anhoerungen", "Anhörungen"),
    ("Erlaeuterung", "Erläuterung"),
    ("erlaeutert", "erläutert"),
    ("erlaeutern", "erläutern"),
    ("erlaeuternd", "erläuternd"),
    ("Antraege", "Anträge"),
    ("Antrag", "Antrag"),
    ("antraege", "anträge"),
    ("Aenderungsantrag", "Änderungsantrag"),
    ("Aenderung", "Änderung"),
    ("Aenderungen", "Änderungen"),
    ("Aufhebungsantrag", "Aufhebungsantrag"),
    ("zulaessig", "zulässig"),
    ("Zulaessig", "Zulässig"),
    ("Unzulaessig", "Unzulässig"),
    ("unzulaessig", "unzulässig"),
    ("Sondereigentum", "Sondereigentum"),
    ("Gemeinschaftseigentum", "Gemeinschaftseigentum"),
    ("Personenmehrheit", "Personenmehrheit"),
    ("Ergaenzung", "Ergänzung"),
    ("ergaenzt", "ergänzt"),
    ("ergaenzen", "ergänzen"),
    ("ergaenzend", "ergänzend"),
    ("Ergaenzungen", "Ergänzungen"),
    ("Begruendung", "Begründung"),
    ("begruendet", "begründet"),
    ("begruenden", "begründen"),
    ("Begruendungen", "Begründungen"),
    ("Beruecksichtigung", "Berücksichtigung"),
    ("beruecksichtigt", "berücksichtigt"),
    ("beruecksichtigen", "berücksichtigen"),
    ("Aussagekraefte", "Aussagekräfte"),
    ("Aussagekraft", "Aussagekraft"),
    ("zustaendig", "zuständig"),
    ("Zustaendig", "Zuständig"),
    ("Zustaendigkeit", "Zuständigkeit"),
    ("Erstattungsfaehig", "Erstattungsfähig"),
    ("erstattungsfaehig", "erstattungsfähig"),
    ("Tagesordnung", "Tagesordnung"),
    ("Verbraucherschutz", "Verbraucherschutz"),
    ("Verbraucher", "Verbraucher"),
    ("Ablaeufe", "Abläufe"),
    ("Pruefablauf", "Prüfablauf"),
    ("rechtmaessig", "rechtmäßig"),
    ("Pruefantrag", "Prüfantrag"),
    ("Auskunftsanspruch", "Auskunftsanspruch"),
    ("Loeschungsanspruch", "Löschungsanspruch"),
    ("Loeschung", "Löschung"),
    ("loeschen", "löschen"),
    ("Vermoegensverlust", "Vermögensverlust"),
    ("Vermoegensschaden", "Vermögensschaden"),
    ("Vermoegensvorteil", "Vermögensvorteil"),
    ("Anschlussliste", "Anschlussliste"),
    ("Streichung", "Streichung"),
    ("Streichungen", "Streichungen"),
    ("Aufforderung", "Aufforderung"),
    ("Aufforderungsschreiben", "Aufforderungsschreiben"),
    # Standard-Wortpaare
    ("oeffnest", "öffnest"),
    ("oeffnet", "öffnet"),
    ("oeffnen", "öffnen"),
    ("Oeffnen", "Öffnen"),
    ("oeffnen", "öffnen"),
    ("ueberlegt", "überlegt"),
    ("ueberlegen", "überlegen"),
    ("Ueberlegung", "Überlegung"),
    ("ueberpruefen", "überprüfen"),
    ("Ueberpruefung", "Überprüfung"),
    ("ueberprueft", "überprüft"),
    ("uebernimmt", "übernimmt"),
    ("uebernehmen", "übernehmen"),
    ("ueblich", "üblich"),
    ("Schluessel", "Schlüssel"),
    ("schluessig", "schlüssig"),
    ("Schluessigkeit", "Schlüssigkeit"),
    ("waehlst", "wählst"),
    ("waehlt", "wählt"),
    ("waehlen", "wählen"),
    ("Waehlen", "Wählen"),
    ("ausgewaehlt", "ausgewählt"),
    ("gewuenscht", "gewünscht"),
    ("Wunschnote", "Wunschnote"),
    ("Wunschzeugnis", "Wunschzeugnis"),
    ("Geschaeft", "Geschäft"),
    ("geschaeftlich", "geschäftlich"),
    ("moechte", "möchte"),
    ("Moechte", "Möchte"),
    ("Taetigkeit", "Tätigkeit"),
    ("Taetigkeiten", "Tätigkeiten"),
    ("taetig", "tätig"),
    ("Taetig", "Tätig"),
    ("gefuehrt", "geführt"),
    ("Gefuehrt", "Geführt"),
    ("Fuehrung", "Führung"),
    ("fuehren", "führen"),
    ("Fuehren", "Führen"),
    ("fuehrt", "führt"),
    ("schlaegt", "schlägt"),
    ("Schlaegt", "Schlägt"),
    ("bestaetigst", "bestätigst"),
    ("bestaetigen", "bestätigen"),
    ("bestaetigt", "bestätigt"),
    ("Bestaetigung", "Bestätigung"),
    ("Schoenschreiben", "Schönschreiben"),
    ("schoen", "schön"),
    ("Schoen", "Schön"),
    ("bemueht", "bemüht"),
    ("Bemueht", "Bemüht"),
    ("doppelten", "doppelten"),
    ("Boeden", "Böden"),
    ("widerspruechlich", "widersprüchlich"),
    ("Aussere", "Äußere"),
    ("aeussere", "äußere"),
    ("Äusser", "Äußer"),
    ("staerker", "stärker"),
    ("Staerker", "Stärker"),
    ("Bewertungssaetze", "Bewertungssätze"),
    ("ausfuehrlich", "ausführlich"),
    ("Ausfuehrlich", "Ausführlich"),
    ("Gewaehr", "Gewähr"),
    ("prueft", "prüft"),
    ("pruefen", "prüfen"),
    ("Pruefung", "Prüfung"),
    ("gepruefte", "geprüfte"),
    ("geprueft", "geprüft"),
    ("Plausibilitaet", "Plausibilität"),
    ("Vollstaendigkeit", "Vollständigkeit"),
    ("vollstaendig", "vollständig"),
    ("Aktualitaet", "Aktualität"),
    ("Faelle", "Fälle"),
    ("Faellen", "Fällen"),
    ("hinzuziehen", "hinzuziehen"),
    ("muessen", "müssen"),
    ("Muessen", "Müssen"),
    ("muesse", "müsse"),
    ("koennen", "können"),
    ("Koennen", "Können"),
    ("koennte", "könnte"),
    ("koennten", "könnten"),
    ("laesst", "lässt"),
    ("Laesst", "Lässt"),
    ("aehnlich", "ähnlich"),
    ("Aehnlich", "Ähnlich"),
    ("naeher", "näher"),
    ("Naeher", "Näher"),
    ("gegenueber", "gegenüber"),
    ("Gegenueber", "Gegenüber"),
    ("Massnahme", "Maßnahme"),
    ("Massnahmen", "Maßnahmen"),
    ("massnahme", "maßnahme"),
    ("grosse", "große"),
    ("grossen", "großen"),
    ("grosser", "großer"),
    ("Grosse", "Große"),
    ("Grossen", "Großen"),
    ("grosser", "großer"),
    ("aufhaelt", "aufhält"),
    ("aufhaelten", "aufhälten"),
    ("Waehrend", "Während"),
    ("waehrend", "während"),
    ("vollstaendiges", "vollständiges"),
    ("klaeren", "klären"),
    ("Klaeren", "Klären"),
    ("schaetzen", "schätzen"),
    ("Schaetzen", "Schätzen"),
    ("schaetzt", "schätzt"),
    ("Schaetzung", "Schätzung"),
    ("Schaetzungen", "Schätzungen"),
    ("erhaeltlich", "erhältlich"),
    ("Verhaeltnis", "Verhältnis"),
    ("Verhaeltnisse", "Verhältnisse"),
    ("Verhaeltnissen", "Verhältnissen"),
    ("verhaeltnismaessig", "verhältnismäßig"),
    ("erhoeht", "erhöht"),
    ("Erhoehung", "Erhöhung"),
    ("erhoehen", "erhöhen"),
    ("Vollstreckung", "Vollstreckung"),
    ("vollstreckbar", "vollstreckbar"),
    ("Vollstreckungstitel", "Vollstreckungstitel"),
    ("nichtige", "nichtige"),
    ("Verguetung", "Vergütung"),
    ("verguetet", "vergütet"),
    ("verguetung", "vergütung"),
    ("Beguenstigung", "Begünstigung"),
    ("beguenstigt", "begünstigt"),
    ("verbindlich", "verbindlich"),
    ("Anschrift", "Anschrift"),
    ("Mandantenanschreiben", "Mandantenanschreiben"),
    ("Schriftsatzgeruest", "Schriftsatzgerüst"),
    ("Verfuegungs", "Verfügungs"),
    ("Geruest", "Gerüst"),
    ("ueblicherweise", "üblicherweise"),
    ("Hinwirkungspflicht", "Hinwirkungspflicht"),
    ("durchschnittlich", "durchschnittlich"),
    ("ueberdurchschnittlich", "überdurchschnittlich"),
    ("Notenstufen", "Notenstufen"),
    ("Notenstufe", "Notenstufe"),
    # Generische Endungen / Suffixe
    ("naehert", "nähert"),
    ("naehe", "nähe"),
    ("zaehlt", "zählt"),
    ("zaehlen", "zählen"),
    ("waehrt", "währt"),
    ("waehrend", "während"),
    ("Faehigkeit", "Fähigkeit"),
    ("faehig", "fähig"),
    ("Maerz", "März"),
    ("maerz", "märz"),
    # Häufige Kurzworte (am Ende, weil sie sonst längere überschreiben)
    ("fuer", "für"),
    ("Fuer", "Für"),
    ("ueber", "über"),
    ("Ueber", "Über"),
    ("ueberall", "überall"),
    ("ueberhaupt", "überhaupt"),
    ("aber", "aber"),  # unverändert
]


def transform_text(text: str) -> str:
    placeholders = {}

    def mask(pattern: str, t: str, label: str) -> str:
        def sub(m):
            key = f"\x00{label}{len(placeholders)}\x00"
            placeholders[key] = m.group(0)
            return key
        return re.sub(pattern, sub, t, flags=re.DOTALL)

    text = mask(r"```.*?```", text, "F")
    text = mask(r"`[^`]+`", text, "I")
    text = mask(r"https?://[^\s)>\"]+", text, "U")
    text = mask(r"<a [^>]+>[^<]+</a>", text, "A")
    text = mask(r"\[[^\]]+\]\([^)]+\)", text, "L")

    for src, dst in UMLAUT_MAP:
        text = re.sub(rf"\b{re.escape(src)}", dst, text)

    # Demaskieren in umgekehrter Reihenfolge, mehrfach durchlaufen,
    # weil Platzhalter ineinander geschachtelt sein koennen (z.B. inline-code in Link).
    for _ in range(5):
        prev = text
        for k, v in reversed(list(placeholders.items())):
            text = text.replace(k, v)
        if text == prev:
            break
    return text


def ensure_zip_link(text: str, plugin: str) -> str:
    if "Direkt-Downloads" not in text:
        return text
    zip_url = f"{REPO_REL}/{plugin}.zip"
    zip_line = f"| Plugin-ZIP (zur Installation) | ZIP | <a href=\"{zip_url}\" download>{plugin}.zip</a> |"
    if zip_url in text:
        return text
    # In die Tabelle ergaenzen: nach der letzten Markdown-Tabellenzeile
    lines = text.splitlines()
    out = []
    inserted = False
    in_table = False
    last_table_end_idx = None
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("|") and "---" not in ln:
            in_table = True
        elif in_table and not ln.lstrip().startswith("|"):
            if not inserted and last_table_end_idx is None:
                last_table_end_idx = i
        if "## Direkt-Downloads" in ln:
            pass
    # Anderer Ansatz: Plugin-ZIP-Zeile nach der zweiten Tabellenzeile mit Schnellstart einfuegen
    output = []
    inserted = False
    for ln in lines:
        output.append(ln)
        if (not inserted and "schnellstart.md" in ln and ln.lstrip().startswith("|")):
            output.append(zip_line)
            inserted = True
    if inserted:
        return "\n".join(output) + ("\n" if text.endswith("\n") else "")
    # Fallback: am Ende der Tabelle einfuegen
    new_lines = []
    appended = False
    table_started = False
    for i, ln in enumerate(lines):
        new_lines.append(ln)
        if ln.lstrip().startswith("|"):
            table_started = True
        elif table_started and not appended and not ln.lstrip().startswith("|"):
            new_lines.insert(-1, zip_line)
            appended = True
    if not appended and table_started:
        new_lines.append(zip_line)
    return "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")


def main():
    changed = 0
    skipped = 0
    for p in MP["plugins"]:
        name = p["name"]
        src = ROOT / (p.get("source") or f"./{name}").lstrip("./")
        readme = src / "README.md"
        if not readme.exists():
            skipped += 1
            continue
        orig = readme.read_text()
        t = transform_text(orig)
        t = ensure_zip_link(t, name)
        if t != orig:
            readme.write_text(t)
            changed += 1
    # Auch Top-Level-README, ASSET_INDEX, SKILLS, CHANGELOG
    for top in ["README.md", "SKILLS.md", "ASSET_INDEX.md", "CHANGELOG.md"]:
        p = ROOT / top
        if p.exists():
            orig = p.read_text()
            t = transform_text(orig)
            if t != orig:
                p.write_text(t)
                changed += 1
    print(f"changed={changed} skipped={skipped}")


if __name__ == "__main__":
    main()
