# Übergabeprompt für Claude Opus 4.8: Städtebauliche Verträge und Festsetzungen

Du arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht` auf Branch `main`.

## Auftrag

Prüfe und verfeinere die neu angelegten und nachgeschärften Inhalte zu städtebaulichen Verträgen und Festsetzungen zu Bebauungsplänen in den Plugins `normenkontrolle-bauleitplanung` und `fachanwalt-bau-architektenrecht`.

Bearbeite konkret:

1. Alle neuen Skills zu BauGB Paragraf 9, Paragraf 11, Paragraf 12, Paragraf 13a, Paragraf 124, Paragraf 214 und Paragraf 215 sowie BauNVO Paragrafen 1 bis 23.
2. Die Abschnitte zu städtebaulichen Verträgen und Festsetzungen in den Werkstatt-Prompts beider Plugins.
3. Die verdichteten Anker und Prüfraster in den Schnellstart-Prompts beider Plugins.
4. Die Schnittstellen zum Bauträgervertrag, zur Baugenehmigungspraxis und zur Architektenhaftung.

## Prüfprogramm

1. Leitentscheidungen prüfen: Gericht, Datum, Aktenzeichen, Fundstelle und Kernsatz müssen belastbar sein. Ersetze unsichere oder thematisch falsche Entscheidungen durch sichere Entscheidungen zum selben Problem.
2. Prüfraster schärfen: Jeder Skill muss mit Eingang, Tatbestandsmerkmalen, Belegen, typischen Fehlern, Anti-Mustern und Arbeitsprodukt arbeiten.
3. Konsistenz prüfen: Skill, Werkstatt-Prompt und Schnellstart-Prompt müssen dieselben Rechtsanker und dieselbe Arbeitslogik tragen.
4. Autarkie sichern: Werkstatt und Schnellstart dürfen ohne andere Plugin-Dateien verwendbar sein.
5. README-Links prüfen: Werkstatt und Schnellstart werden als Markdown über raw.githubusercontent.com verlinkt, nicht als ZIP.

## Klotzkette-Regeln

- Skill-`description` im Frontmatter maximal 1024 Zeichen.
- `plugin.json`- und `marketplace.json`-`description` maximal 300 Zeichen.
- Kein Dezimalkomma-Muster Ziffer Komma Ziffer. Punkt verwenden.
- Statt Paragrafenzeichen immer `Paragraf` oder `Paragrafen` ausschreiben. Nur die Repo-README darf das Symbol enthalten.
- Keine XML-artigen Klammern in Plugin-, Werkstatt-, Schnellstart- und Skill-Dateien.
- Keine Emojis.
- Slug-Schema `[a-z0-9-]`, maximal 64 Zeichen.
- In Slugs und validatorrelevanten JSON-Feldern niemals Umlaute oder Eszett; dort `ae`, `oe`, `ue`, `ss` verwenden.
- In Markdown-Fließtext echte Umlaute und Eszett schreiben.
- Generisches Maskulinum repo-weit, aber nicht in `CLAUDE.md` sichtbar dokumentieren.
- Regulierungsrahmen, Datenschutz-Grundverordnung und Vertraulichkeitsthemen nur in der Repo-README thematisieren, nicht in Plugins, Werkstatt, Schnellstart oder Skills.
- Die vier Web-Harvesting-Begriffe mit den Wortstämmen s c r a p e und c r a w l sind tabu. Verwende `abrufen`, `lesen`, `auslesen`, `einsammeln`, `konsultieren`.
- Keine Floskeln aus Prüfprotokoll-, Platzhalter- oder Skill-Verweis-Sprache verwenden.
- Werkstatt-Prompts bleiben autark und angemessen tief.
- Schnellstart-Prompts bleiben autark und maximal 7500 Zeichen inklusive Leerzeichen.
- Distribution der Werkstatt- und Schnellstart-Prompts nur als Markdown über raw.githubusercontent.com, nicht als ZIP.
- Autor in jedem Commit: Name `Klotzkette`, E-Mail `39582916+Klotzkette@users.noreply.github.com`.
- Keine Erwähnung von Claude, AI, Codex oder Assistant in Commit-Messages.
- Vor jedem Push `git fetch origin`.
- Push mit `api_credentials=["github"]`.

## Abschluss

Lasse am Ende laufen:

```bash
node scripts/validate-plugin-structure.mjs
python3 scripts/validate-yaml-frontmatter.py
```

Melde knapp:

1. Welche Dateien geändert wurden.
2. Welche Aktenzeichen bestätigt, korrigiert oder ersetzt wurden.
3. Ob Skill, Werkstatt und Schnellstart in beiden Bau-Plugins konsistent sind.
4. Den letzten Diff-Statusbericht.

