# Übergabeprompt für Claude Opus 4.8: Letzte Gesamtverfeinerung der Legal-Skills

Du arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht` auf Branch `main`.

## Ziel

Führe eine letzte substanzielle Verfeinerung des Repos durch. Schwerpunkt ist nicht Mengenwachstum, sondern juristische Tiefe, Eleganz, Konsistenz und unmittelbare Nutzbarkeit.

Prüfe alle drei Ebenen:

1. Skills.
2. Werkstatt-Prompts.
3. Schnellstart-Prompts.

Alle Artefakte müssen autark bleiben. Keine Cross-Verweise auf andere Skills, keine Floskeln, keine Prüfprotokoll-Sprache, keine Platzhalter ohne Arbeitsnutzen.

## Skills

Prüfe vorhandene Skill-Dateien, ohne Slugs oder Dateinamen zu ändern:

1. Hat der Skill ein präzises Ziel.
2. Enthält er konkrete Pflichtnormen und ein echtes Prüfraster.
3. Enthält er Stolpersteine, Anti-Muster und ein verwendbares Arbeitsprodukt.
4. Ist die Sprache konkret für das Plugin und nicht beliebig übertragbar.
5. Bleibt die Frontmatter-`description` unter 1024 Zeichen.

Wenn ein Skill leer oder dekorativ wirkt, fülle ihn mit konkreter Prüfung, Risiken, Beispielen und Anti-Mustern. Wenn ein Skill überladen ist, verdichte ihn, ohne Wissen zu verlieren.

## Werkstatt-Prompts

Jeder `{slug}-werkstatt.md` bleibt ein autarker Großprompt. Zielgröße: 10 bis 30 Druckseiten, abhängig von der Materie.

Prüfe:

1. Rolle und Auftrag: klare Funktion, keine Allgemeinplätze.
2. Stop-Kriterien: wann Abbruch, Eskalation, Mandatsablehnung oder Vorlage nötig ist.
3. Stationen des Arbeitsflusses: Eingang, Prüfung, Arbeitsprodukt.
4. Pflichtnormen: Gesetz, Paragraf, Stichwort und Kernfunktion.
5. Leitentscheidungen: Gericht, Aktenzeichen, Datum, Fundstelle und Kernsatz.
6. Prüfraster und Schriftsatzgerüst: passend zum Themengebiet.
7. Arbeitsweise: Reihenfolge, Selbstchecks, Quellenhygiene.
8. Qualitätskontrolle und Abschluss.

Werkstatt-Prompts dürfen keine Skill-Verweise, keine internen Entstehungshinweise und keine bloße Inhaltsverzeichnis-Sprache enthalten.

## Schnellstart-Prompts

Jeder `{slug}-schnellstart.md` bleibt maximal 7500 Zeichen inklusive Leerzeichen.

Prüfe:

1. Themengebiet und Rolle in einem Absatz.
2. Drei bis fünf Eingangsfragen.
3. Vier bis acht Arbeitsschritte.
4. Pflichtnormen verdichtet.
5. Zwei bis drei Leitentscheidungen mit Kernsatz, wenn die Materie Rechtsprechungsanker trägt.
6. Antwortform und Stop-Kriterium.

Der Schnellstart muss in einem beliebigen Chat sofort funktionieren.

## Distribution

Werkstatt- und Schnellstart-Prompts werden nur als Markdown ausgeliefert. Links müssen auf raw.githubusercontent.com zeigen:

`https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin-dir}/{slug}-werkstatt.md`

`https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin-dir}/{slug}-schnellstart.md`

Keine Werkstatt- oder Schnellstart-ZIP-Links einführen.

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

Melde im Chat knapp:

1. Was geändert wurde.
2. Welche Rechtsgebiete oder Profile besonders geschärft wurden.
3. Welche Entscheidungen bestätigt, korrigiert oder ersetzt wurden.
4. Ob Werkstatt und Schnellstart weiterhin autark sind.
5. Den letzten Diff-Statusbericht.
