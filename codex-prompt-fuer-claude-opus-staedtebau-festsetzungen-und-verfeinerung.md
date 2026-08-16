# Übergabeprompt für Claude Opus 4.8: Städtebau, Festsetzungen und letzte Verfeinerung

Du arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht` auf Branch `main`.

## Auftrag

Führe eine letzte juristische Feinschleife an den neuen Skills, an den Abschnitten zu städtebaulichen Verträgen und Festsetzungen in den Werkstatt- und Schnellstart-Dateien der Plugins `normenkontrolle-bauleitplanung` und `fachanwalt-bau-architektenrecht` sowie an der allgemeinen Qualitätsschleife durch.

Schwerpunkte:

1. Prüfe Aktenzeichen, Daten, Fundstellen und Kernsätze der neu eingezogenen Leitentscheidungen.
2. Schärfe Prüfraster zu BauGB Paragraf 9, Paragraf 11, Paragraf 12, Paragraf 13a, Paragraf 124, Paragraf 214 und Paragraf 215 sowie BauNVO Paragrafen 1 bis 23.
3. Prüfe Konsistenz zwischen Skill, Werkstatt-Prompt und Schnellstart-Prompt.
4. Entferne generische Sprache, Doppelungen und bloße Überschriften ohne Arbeitsnutzen.
5. Prüfe, ob die README-Links auf Werkstatt und Schnellstart als raw.githubusercontent.com-Markdown-Links korrekt sind.

## Inhaltliche Leitplanken

- Städtebauliche Verträge: Folgekostenvertrag, Erschließungsvertrag, Durchführungsvertrag, Kausalität, Angemessenheit, Schriftform, Nichtigkeit, Rückabwicklung und Rechtsschutz.
- Festsetzungen: BauGB Paragraf 9, BauNVO, Art und Maß der Nutzung, überbaubare Grundstücksfläche, Bauweise, Verkehrsflächen, Grünflächen, Versorgungsflächen, Innenentwicklung, örtliche Bauvorschriften, Bestimmtheit und Erforderlichkeit.
- Verwende keine unsicheren Fundstellen. Wenn ein im Auftrag genanntes Aktenzeichen nicht belastbar auffindbar ist, ersetze es durch eine sicher belegbare Entscheidung zum gleichen Problem.

## Klotzkette-Regeln

- Skill-`description` im Frontmatter maximal 1024 Zeichen.
- `plugin.json`- und `marketplace.json`-`description` maximal 300 Zeichen.
- Keine Komma-Ziffer-Paare der Form Ziffer Komma Ziffer. Punkt verwenden.
- Statt Paragrafenzeichen immer `Paragraf` oder `Paragrafen` ausschreiben. Nur die Repo-README darf das Symbol enthalten.
- Keine XML-artigen Klammern in Plugin-, Werkstatt-, Schnellstart- und Skill-Dateien.
- Keine Emojis.
- Slug-Schema `[a-z0-9-]`, maximal 64 Zeichen.
- In Slugs und validatorrelevanten JSON-Feldern niemals Umlaute oder Eszett; dort `ae`, `oe`, `ue`, `ss` verwenden.
- In Markdown-Fließtext echte Umlaute und Eszett schreiben.
- Generisches Maskulinum repo-weit, aber nicht in `CLAUDE.md` sichtbar dokumentieren.
- Regulierungsrahmen, Datenschutz-Grundverordnung und Vertraulichkeitsthemen nur in der Repo-README thematisieren, nicht in Plugins, Werkstatt, Schnellstart oder Skills.
- Die vier Web-Harvesting-Begriffe mit den Wortstämmen s c r a p e und c r a w l sind tabu. Verwende `abrufen`, `lesen`, `auslesen`, `einsammeln`, `konsultieren`.
- Keine Floskeln aus Prüfprotokoll-, Platzhalter- oder Skill-Verweis-Sprache verwenden; schreibe die Prüfung unmittelbar fachlich aus.
- Werkstatt-Prompts bleiben autark, 10 bis 30 Druckseiten, ohne Skill-Verweise.
- Schnellstart-Prompts bleiben autark und maximal 7500 Zeichen inklusive Leerzeichen.
- Distribution der Werkstatt- und Schnellstart-Prompts nur als Markdown über raw.githubusercontent.com, nicht als ZIP.
- Autor in jedem Commit: Name `Klotzkette`, E-Mail `39582916+Klotzkette@users.noreply.github.com`.
- Keine Erwähnung von Claude, AI, Codex oder Assistant in Commit-Messages.
- Vor jedem Push `git fetch origin`.
- Push mit `api_credentials=["github"]`.

## Abschluss

Lasse die Validatoren laufen:

```bash
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
```

Melde am Ende knapp:

1. Welche Dateien geändert wurden.
2. Welche Aktenzeichen bestätigt, korrigiert oder ersetzt wurden.
3. Ob Werkstatt und Schnellstart in beiden Bau-Plugins konsistent sind.
4. Den letzten Diff-Statusbericht.
