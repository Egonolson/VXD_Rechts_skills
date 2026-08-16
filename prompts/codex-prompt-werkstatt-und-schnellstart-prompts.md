# Codex-Prompt — Werkstatt- und Schnellstart-Prompts fuer alle Plugins

Du bist Codex und arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht` auf dem `main`-Branch. Dein Auftrag: jedes Plugin im Repo bekommt zwei handgepflegte, plugin-spezifische Markdown-Prompts mit sprechenden Dateinamen, die ueber das jeweilige Plugin-README als echte Datei-Downloads angeboten werden. Ziel sind die Nutzer, die kein Claude-Code-Plugin verwenden koennen und stattdessen einen Markdown-Text in einen beliebigen Chatbot kippen.

## Kontext fuer Codex

Es gibt im Repo zwei Sorten von Prompts pro Plugin:
1. **Werkstatt-Prompt** (frueher intern "Megaprompt" genannt): lang, vollstaendig, kuratiert. Dieser Prompt darf gross sein. Keine harte Obergrenze, Richtwert 150 bis 400 Zeilen.
2. **Schnellstart-Prompt** (frueher intern "Miniprompt" genannt): kompakt. **Hoechstens 7.500 Zeichen inklusive Markdown.**

Beide sind keine Code-Plugins, sondern reine Markdown-Krueckenpfade fuer Nutzer ohne Claude-Code-Setup. Im README erklaert das ein freundlicher Vorspruch, ohne dass die anderen Bedienpfade abgewertet werden.

## Pflichtnamen mit Sprechcharakter

Generische Namen wie `MEGAPROMPT.md`, `MINIPROMPT.md`, `mega.md`, `mini.md`, `<slug>-megaprompt.md` oder `<slug>-miniprompt.md` sind **verboten**. Stattdessen tragen die Dateien einen sprechenden, plugin-individualisierten Namen, in dem der Plugin-Slug oder ein klar erkennbarer Plugin-Begriff enthalten ist, und die Funktion ist im Namen sichtbar.

Vorgesehene Konvention:
- Werkstatt-Prompt: `<slug>-werkstatt.md`
- Schnellstart-Prompt: `<slug>-schnellstart.md`

Beispiele:
- `liquiditaetsplanung/liquiditaetsplaner-werkstatt.md`, `liquiditaetsplanung/liquiditaetsplaner-schnellstart.md`
- `arbeitsrecht/arbeitsrecht-werkstatt.md`, `arbeitsrecht/arbeitsrecht-schnellstart.md`
- `gerichtsplugins/richter-finanzgericht/finanzgericht-werkstatt.md`, `.../finanzgericht-schnellstart.md`
- `staatsanwaltschaft-praxis-einstieg/staatsanwaltschaft-einstieg-werkstatt.md` und `.../staatsanwaltschaft-einstieg-schnellstart.md`

Bestehende `<slug>-megaprompt.md` und `<slug>-miniprompt.md` werden per `git mv` auf die neue Konvention umgezogen. Verweise in READMEs, Skripten und Manifesten ziehst du mit. `CHANGELOG.md` bleibt fuer historische Eintraege unveraendert.

## Direkt-Download als Markdown

Werkstatt und Schnellstart bleiben reine Markdown-Dateien. Sie werden nicht in pluginbezogene Prompt-ZIPs verpackt und nicht als zusätzliche Skills unter `skills/` abgelegt.

1. `scripts/inject-direkt-loslegen-section.py` erzeugt pro Plugin zwei HTML-Links mit `download`-Attribut.
2. Das Ziel liegt unter `raw.githubusercontent.com` und verwendet den tatsächlichen Marketplace-Quellpfad des Plugins.
3. Das Dateischema lautet `<plugin>-werkstatt.md` und `<plugin>-schnellstart.md`.
4. Der Plugin-ZIP bleibt davon getrennt und enthält das installierbare Plugin.

URL-Schema als Text: `https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/<plugin-pfad>/<plugin>-werkstatt.md`; für den Schnellstart entsprechend mit `-schnellstart.md`.

## README-Block (oben, prominent, freundlich)

Erweitere oder ersetze den vorhandenen Sofort-Downloads-Block in jedem Plugin-README so, dass ganz oben — direkt nach der H1 und der bestehenden Sofort-Downloads-Tabelle — folgender Abschnitt steht, mit konkret eingesetzten Plugin-Werten:

```markdown
## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP | ZIP | arbeitsrecht.zip aus dem aktuellen Release |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitsrecht/arbeitsrecht-werkstatt.md" download><code>arbeitsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitsrecht/arbeitsrecht-schnellstart.md" download><code>arbeitsrecht-schnellstart.md</code></a> |
```

Der Block ist idempotent ueber HTML-Marker `<!-- BEGIN direkt-loslegen (autogen) -->` und `<!-- END direkt-loslegen (autogen) -->` gefuehrt. Er steht **vor** dem bestehenden `## Experimentell: dieses Plugin auch ohne Claude Code`-Block. Falls dieser experimentelle Block durch den neuen Block ueberfluessig wird, ersetzt du ihn; sonst laesst du ihn weiter unten stehen.

## Pflicht-Struktur Werkstatt-Prompt

```
# <Sprechender Titel> — Werkstatt-Prompt

Kurzbeschreibung in einem Absatz: Rolle, Rechtsgebiet, Ergebnisformate, Anker.

## Rolle
- Berufsbild, Funktion, typische Auftraggeber, Gegenueber.
- Was diese Rolle NICHT ist.

## Werkstattlogik
- Stationen in Reihenfolge (Triage, Eingang, Arbeit, Anschluss). Mindestens fuenf, hoechstens zwoelf.
- Jede Station: Eingang, Pruefung, Arbeitsprodukt, Anschlussentscheidung.

## Pflicht-Workflow am Anfang
- Zwei oder drei Festlegungen, die der Agent zuerst abfragt (Output-Format, Datenquelle, Rolle, Lage). Mit Default.

## Quellen-Disziplin
- Pflicht-Paragrafen und Schemata, mit dem Wort "Paragraf" statt Zeichen.
- Welche Quellen sind live zu verifizieren, welche tabu.
- Aktualitaetsregel je Plugin.

## Leitentscheidungen
- 2 bis 5 echte, pruefbare Entscheidungen mit Gericht, Datum, Aktenzeichen und Kernaussage in einem Satz.
- Hinweis, dass jede Entscheidung vor Verwendung live nachgezogen wird.

## Pruefraster oder Indizienliste
- Plugin-spezifische Anhaltspunkte oder Pruefraster mit Tatbestandsmerkmalen.

## Antwortform
- Pflichtfelder jeder Antwort (Lagebild, Pruefung, Empfehlung, naechster Schritt, Quellen).
- Stop-Kriterien.

## Eigenheiten dieses Plugins
- 4 bis 8 konkrete Stolpersteine, die nur in dieser Materie auftreten.

## Skelette
- 2 bis 3 vorbereitete Antwort-Skelette fuer typische Faelle.
```

Werkstatt darf lang sein. Richtwert 150 bis 400 Zeilen. Keine harte Obergrenze.

## Pflicht-Struktur Schnellstart-Prompt

```
# <Sprechender Titel> — Schnellstart

Eine bis zwei Saetze: was kann ich, fuer wen.

## Rolle
Ein Absatz.

## Triage
Drei bis fuenf Fragen, die der Agent zuerst stellt.

## Werkstatt-Kurzweg
Vier bis acht nummerierte Schritte.

## Anker
Pflicht-Paragrafen und 1 bis 2 Leitentscheidungen in Stichworten.

## Antwortform
Eine Zeile zu jedem Pflichtfeld.

## Stop
Eine Zeile: wann Uebergabe an Berufstraeger.
```

Harte Obergrenze: **7.500 Zeichen inklusive Markdown**. Wer drueber kommt, kuerzt zuerst Triage, dann Anker, zuletzt Werkstatt-Kurzweg.

## Quelle der Wahrheit fuer den Inhalt

Lies in dieser Reihenfolge und uebernimm die dort verwendete Fachsprache:
1. `<plugin>/.claude-plugin/plugin.json` (Keywords und description).
2. `<plugin>/README.md`.
3. Alle `<plugin>/skills/*/SKILL.md` (Frontmatter description plus Body).
4. Wenn vorhanden: `<plugin>/assets/`, `<plugin>/references/`.

Erfinde keine Inhalte, die in den Skills nicht vorkommen. Im Zweifel: weniger schreiben, aber praezise.

## Verbotene Inhalte

- Keine generischen Skelette ("1. Welche Rolle hat die fragende Person und wer ist Gegenueber? 2. ...") als alleinige Substanz.
- Keine Skill-Konkatenation. Wenn ein Skill genannt wird, fasse seine Logik in zwei Saetzen zusammen.
- Keine BeckRS, juris, Kommentar- oder Aufsatzfundstellen aus Modellwissen.
- Keine Emojis, keine spitzen Klammern in JSON-Description-Feldern, kein Paragrafenzeichen, immer das Wort "Paragraf".
- Keine Erwaehnung von Claude, OpenAI, Codex, Cursor, Aider, Continue oder anderem KI-Hilfsnamen in den Prompts oder in Commit-Messages.
- Keine Marketingsprache, kein "wir freuen uns".

## Zeichen- und Format-Konvention

- Echte Umlaute (ae mit Punkten, oe mit Punkten, ue mit Punkten, ss bzw. ss-Ligatur) in Markdown-Prosa. ae/oe/ue/ss-Form nur in Slugs und in JSON-`description`-Feldern.
- Verwende `Paragraf` statt Paragrafenzeichen.
- Maximal eine H1 pro Datei. Datei endet mit Leerzeile. UTF-8 ohne BOM. Kein YAML-Frontmatter.
- Generisches Maskulinum gilt, ohne es sichtbar zu dokumentieren.

## Algorithmus

1. Sammle alle Plugins (`<plugin>/.claude-plugin/plugin.json`, Wurzel und `gerichtsplugins/`).
2. Bestimme pro Plugin den sprechenden Namens-Stamm (z. B. `liquiditaetsplaner` statt `liquiditaetsplanung`, `finanzgericht` statt `richter-finanzgericht`). Quelle: README-Titel oder plugin.json `description`. Bei Unsicherheit: Slug.
3. Suche im Repo nach `<slug>-megaprompt.md`, `<slug>-miniprompt.md`, `MEGAPROMPT.md`, `MINIPROMPT.md` als plugin-lokale Dateien. Ziehe sie via `git mv` um auf `<sprechender-name>-werkstatt.md` und `<sprechender-name>-schnellstart.md` und ergaenze Verweise in den Plugin-READMEs, im Sammelordner-README und in den Skripten.
4. Pro Plugin:
   a. Wenn `<sprechender-name>-werkstatt.md` fehlt oder offensichtlich generisch ist (Skill-Konkatenat, Vorlage, generisches Triage-Skelett), erzeuge ihn neu nach Pflicht-Struktur Werkstatt.
   b. Wenn `<sprechender-name>-schnellstart.md` fehlt oder offensichtlich generisch ist, erzeuge ihn neu nach Pflicht-Struktur Schnellstart und pruefe die 7.500-Zeichen-Grenze.
   c. Validiere: keine Emojis, kein Paragrafenzeichen, keine spitzen Klammern, kein YAML-Frontmatter, exakt eine H1, Schnellstart hoechstens 7.500 Zeichen, Werkstatt mindestens 150 Zeilen.
5. Aktualisiere `scripts/inject-direkt-loslegen-section.py` und `scripts/inject-megaprompt-section.py` so, dass sie die neuen sprechenden Dateinamen als Werkstatt- und Schnellstart-Einträge in den README-Block aufnehmen. Bestehende Mega-/Mini-Verweise in den READMEs werden zurückgebaut.
6. Prüfe die HTML-Direktdownloads gegen die tatsächlich vorhandenen Markdown-Dateien und halte Werkstatt und Schnellstart aus `skills/` heraus.
7. Pruefe `scripts/generate-megaprompt.py` und `scripts/generate-unified-mini-prompts.py` auf Vorrang-Logik (lokale handgepflegte Datei aus dem Plugin-Ordner gewinnt vor Bundle-Generierung). Falls noetig, ergaenze diese Logik fuer die neuen Dateinamen.
8. Lasse `scripts/generate-werkstatt-und-schnellstart-prompts.py`, `scripts/inject-direkt-loslegen-section.py`, `scripts/generate-skills-overview.py`, `scripts/inject-skills-logic-navigation.py`, `scripts/generate-skills-md.py` und `scripts/generate-asset-index.py` laufen.
9. Validiere repo-weit: Skill-description bis 1024 Zeichen, plugin.json- und marketplace.json-description bis 300 Zeichen, kein `\d,\d` in Descriptions, keine XML-Brackets, keine Emojis, kein Paragrafenzeichen in Pruefdateien, Slugs nur aus Kleinbuchstaben, Ziffern und Bindestrich. Bei Fehlern: nicht pushen, sondern fixen. Ich will auf KEINEN FALL die validation failed.
10. Erzeuge `docs/werkstatt-und-schnellstart-coverage.md` mit einer Tabelle für Plugin, Werkstatt-Datei und Schnellstart-Datei sowie einer Schlusszeile mit Gesamtcoverage in Prozent.

## Workflow und Git

- Author: `Klotzkette` <`39582916+Klotzkette@users.noreply.github.com`>. Keine Erwaehnung von Codex, Claude oder OpenAI in Commit-Messages.
- Pull-Pflicht vor jedem Push: `git fetch origin && git pull --rebase origin main`. Erst dann `git push origin main`.
- Committe in Etappen (zum Beispiel 20 Plugins pro Commit) mit knappen, sachlichen Messages.
- Versions-Bump und Tag macht Codex **nur, wenn ich es ausdruecklich anweise**. Andernfalls bleibt die laufende Repo-Version.
- Vor jedem Commit: `git status` und `git diff --stat` zur Selbstkontrolle. Bei jedem Push: zuerst rebase, dann Push.

## Akzeptanzkriterien

- Jedes Plugin hat zwei sprechend benannte Dateien `<sprechender-name>-werkstatt.md` und `<sprechender-name>-schnellstart.md`.
- Beide sind plugin-spezifisch, nicht generisch, in der Pflicht-Struktur.
- Im Plugin-README steht oben ein klarer Downloadblock mit HTML-Direktlinks auf die beiden Markdown-Dateien.
- Werkstatt und Schnellstart liegen nicht als ZIP und nicht als Wrapper-Skill vor.
- Validator laeuft fehlerfrei.
- `docs/werkstatt-und-schnellstart-coverage.md` existiert.

## Ton im README-Vorspruch

Freundlich, sachlich, kurz. Hier eine Vorlage, die Codex je Plugin anpasst:

> Wer hier landet und kein Claude-Code-Plugin betreiben kann oder will, hat trotzdem zwei volle Werkzeugkisten. Eine Markdown-Datei reicht. Du laedst sie herunter, ziehst sie in deinen Chatbot, formulierst deine Frage. Das war es. Die Werkstatt-Datei ist die ausfuehrliche Variante mit allen Stationen. Die Schnellstart-Datei ist die kompakte Variante fuer schnelle Antworten.

## Letztes

Codex schreibt nuechtern, juristisch, ohne Marketing-Sprache. Wo etwas unklar ist, bleibt der Prompt bei der Skill-Sprache und kennzeichnet Live-Verifikation. Lieber weniger Behauptung als eine erfundene.
