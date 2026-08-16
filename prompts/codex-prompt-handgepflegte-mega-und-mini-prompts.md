# Codex-Prompt — Handgepflegte Mega- und Mini-Prompts fuer alle Plugins

Du bist Codex und arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht`. Dein Auftrag: dafuer sorgen, dass jedes Plugin im Repo einen handgepflegten, plugin-spezifischen Mega-Prompt **und** einen handgepflegten, plugin-spezifischen Mini-Prompt im jeweiligen Plugin-Ordner traegt. Beide Dateien dienen den Nutzern, die kein Claude-Code-Plugin verwenden koennen und stattdessen einen einzelnen Markdown-Text in einen beliebigen LLM-Chat einfuegen.

---

## Ziel und Pflichtnamen

- Pro Plugin entstehen zwei Dateien im Plugin-Ordner:
  - `<slug>/<slug>-megaprompt.md` — vollstaendiger Werkstattprompt, dicht, aber kuratiert.
  - `<slug>/<slug>-miniprompt.md` — kompakter Schnellstartprompt, hoechstens 7.500 Zeichen.
- Die Dateinamen tragen **immer** den Plugin-Slug. **Niemals** generische Namen wie `MEGAPROMPT.md`, `MINIPROMPT.md`, `mega.md` oder `mini.md`. Die Repo-Konvention ist `<slug>-megaprompt.md` und `<slug>-miniprompt.md`.
- Gilt fuer Plugins im Repo-Wurzelverzeichnis **und** im Sammelordner `gerichtsplugins/`.

## Geltungsbereich

Codex bearbeitet alle Plugins, fuer die gilt:

- Es existiert `<plugin>/.claude-plugin/plugin.json`.
- Plugin liegt entweder im Repo-Wurzelverzeichnis oder unter `gerichtsplugins/<slug>/`.

Bereits vorhandene handgepflegte Dateien (`<plugin>/<slug>-megaprompt.md` oder `<plugin>/<slug>-miniprompt.md`) **werden nicht ueberschrieben**, ausser die Datei traegt eine sichtbare Markierung wie `<!-- autogen -->` oder ist offensichtlich nur ein Skill-Konkatenat. Im Zweifel: nicht anfassen, sondern in der Statusliste markieren.

## Qualitaetsziel

Die Prompts sind kein Skill-Konkatenat. Sie sind eine kuratierte, sinnvoll geordnete Werkstattbeschreibung des Plugins, die ein LLM ohne weiteres Setup als System- oder Kontextprompt verwenden kann. Inhalt soll plugin-spezifisch sein, nicht generisch.

Faustregel:

- Wer das Plugin nicht kennt, kopiert die Datei in einen LLM, kippt einen echten Fall drauf und bekommt eine sinnvolle Antwort.
- Wer das Plugin kennt, erkennt es am Inhalt wieder ohne Slug zu lesen.

## Pflicht-Struktur Mega-Prompt

```
# Megaprompt — <Plugin-Titel mit Funktion>

Kurzbeschreibung in einem Absatz: Rolle, Rechtsgebiet, Ergebnisformate, Anker.

## Rolle
- Wer arbeitet hier (Berufsbild, Funktion, typische Auftraggeber, Gegenueber).
- Was diese Rolle NICHT ist.

## Werkstattlogik
- Stationen in Reihenfolge (Triage, Eingang, Arbeit, Anschluss). Mindestens fuenf, hoechstens zwoelf Stationen.
- Jede Station: Eingang, Pruefung, Arbeitsprodukt, Anschlussentscheidung.

## Pflicht-Workflow am Anfang jedes neuen Falls
- Zwei oder drei Festlegungen, die der Agent zuerst abfragt (z. B. Output-Format, Datenquelle, Rolle, Lage). Mit Default.

## Quellen-Disziplin
- Pflicht-Paragrafen und Schemata des Plugins, mit dem Wort "Paragraf" statt Zeichen.
- Welche Quellen sind live zu verifizieren? Welche Quellen sind tabu (Modellwissen, Aufsaetze, Kommentare)?
- Aktualitaetsregel je Plugin (z. B. BGH-Datenbank, BFH, BVerfG, Bundesanzeiger, Bundesnetzagentur, OFD).

## Leitentscheidungen
- 2 bis 5 echte, pruefbare Entscheidungen mit Gericht, Datum, Aktenzeichen und Kernaussage in einem Satz.
- Hinweis, dass jede Entscheidung vor Verwendung live nachgezogen wird.

## Indizienliste oder Pruefraster
- Plugin-spezifische Anhaltspunkte oder ein Pruefraster mit Tatbestandsmerkmalen.

## Antwortform
- Pflichtfelder jeder Antwort des Agenten (Lagebild, Pruefung, Empfehlung, naechster Schritt, Quellen).
- Stop-Kriterien (wann der Agent abbricht und an einen Berufstraeger uebergibt).

## Eigenheiten dieses Plugins
- 4 bis 8 konkrete Stolpersteine, die nur in dieser Materie auftreten.

## Skelette
- 2 bis 3 vorbereitete Antwort-Skelette fuer typische Faelle des Plugins.
```

Laenge Mega: mindestens 150, hoechstens 400 Zeilen. Inhalt zaehlt, nicht die Zeilenzahl.

## Pflicht-Struktur Mini-Prompt

```
# Miniprompt — <Plugin-Titel mit Funktion>

Eine bis zwei Saetze: was kann ich, fuer wen.

## Rolle
Ein Absatz.

## Triage
Drei bis fuenf Fragen, die der Agent zuerst stellt.

## Werkstatt-Kurzweg
Vier bis acht nummerierte Schritte: Eingang, Pruefung, Output.

## Anker
Pflicht-Paragrafen und 1 bis 2 Leitentscheidungen in Stichworten.

## Antwortform
Eine Zeile zu jedem Pflichtfeld.

## Stop
Eine Zeile: wann Uebergabe an Berufstraeger.
```

Laenge Mini: hoechstens 7.500 Zeichen inklusive Markdown. Wer drueber kommt, kuerzt zuerst die Triage und die Werkstatt-Kurzwege.

## Inhaltliche Pflichten

- **Plugin-spezifisch**: Wenn das Plugin `arbeitsrecht` heisst, kommen Kuendigungsschutzgesetz, Klagefrist drei Wochen nach Paragraf 4 KSchG, Aufhebungsvertrag, Sozialauswahl rein. Nicht: generisches Triage-Geschwurbel.
- **Echte Paragrafen** statt Platzhaltern. Wenn unklar, liest Codex die Skills und uebernimmt die dort verwendeten Paragrafen.
- **Workflow-orientiert**: Schritte in Reihenfolge, mit Eingaengen und Arbeitsprodukten. Keine Bullet-Wuesten ohne Reihenfolge.
- **Anker**: Gerichte, Datenbanken, Standards des Faches (z. B. IDW S 6, BGH-Linie, RVG, GNotKG, FamFG, FGO, AO, SGB).
- **Konkrete Antwort-Skelette** im Imperativ ("Du antwortest ...").

## Quelle der Wahrheit fuer den Inhalt

Codex liest in dieser Reihenfolge und uebernimmt die dort verwendete Fachsprache:

1. `<plugin>/.claude-plugin/plugin.json` (Keywords und description).
2. `<plugin>/README.md` (Selbstbeschreibung des Plugins).
3. Alle `<plugin>/skills/*/SKILL.md` (Frontmatter description plus Body).
4. Wenn vorhanden: `<plugin>/assets/...`, `<plugin>/references/...`.

Codex erfindet keine Inhalte, die in den Skills nicht vorkommen. Im Zweifel: weniger schreiben, aber praezise.

## Verbotene Inhalte

- Keine generischen Skelette ("1. Welche Rolle hat die fragende Person und wer ist Gegenueber? 2. ...") als alleinige Substanz. Wenn vorhanden, ersetzen.
- Keine Skill-Konkatenation. Wenn ein Skill genannt wird, fasst Codex seine Werkstatt-Logik in zwei Saetzen zusammen.
- Keine BeckRS, juris, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Bei Unsicherheit schreibt Codex einen Live-Verifikationshinweis statt einer Behauptung.
- Keine Behauptungen ueber Gerichtspraxis ohne Beleg.
- Keine Emojis, keine spitzen Klammern in JSON-Description-Feldern, kein Paragrafenzeichen, immer das Wort "Paragraf".
- Keine Erwaehnung von Claude, OpenAI, Codex, Cursor, Aider, Continue oder anderem KI-Hilfsnamen.

## Zeichen- und Format-Konvention

- Echte Umlaute (ae, oe, ue, ss) **nur** in Slugs und in JSON-`description`-Feldern. In Markdown-Prosa stehen die echten Buchstaben ae mit Punkten, oe mit Punkten, ue mit Punkten, ss bzw. ss-Ligatur.
- Verwende `Paragraf` statt Paragrafenzeichen.
- Maximal eine H1 pro Datei. Danach H2 und H3.
- Datei endet mit einer Leerzeile.
- UTF-8 ohne BOM.
- Kein vorangestellter YAML-Frontmatter (das ist eine Prompt-Datei, kein Skill).

## Algorithmus fuer Codex

1. Sammle alle Plugins mit `<plugin>/.claude-plugin/plugin.json` (Wurzel und `gerichtsplugins/`).
2. Pro Plugin:
   a. Pruefe, ob `<plugin>/<slug>-megaprompt.md` existiert. Wenn ja und kuratiert: weiter zu Mini. Wenn nicht: erzeuge ihn nach Pflicht-Struktur Mega.
   b. Pruefe, ob `<plugin>/<slug>-miniprompt.md` existiert. Wenn ja und kuratiert: weiter zum naechsten Plugin. Wenn nicht: erzeuge ihn nach Pflicht-Struktur Mini.
   c. Validiere: keine Emojis, kein Paragrafenzeichen, keine spitzen Klammern, kein YAML-Frontmatter, exakt eine H1, Mini hoechstens 7.500 Zeichen, Mega mindestens 150 Zeilen.
3. Aktualisiere die Plugin-`README.md` ueber das vorhandene Skript `scripts/inject-megaprompt-section.py`. Das Skript reicht den lokalen handgepflegten Mega automatisch in den README-Block ein, wenn die Datei existiert. Falls eine analoge Logik fuer den Mini noch fehlt, ergaenzt Codex sie im Skript so, dass der lokale Mini ebenfalls im Block verlinkt wird. Idempotent ueber HTML-Marker.
4. Pruefe, ob `scripts/generate-megaprompt.py` und `scripts/generate-unified-mini-prompts.py` lokale handgepflegte Dateien als Vorrang behandeln. Falls nicht, ergaenzt Codex die Vorrang-Logik (lokale Datei aus dem Plugin-Ordner wird bevorzugt, sonst Skill-Konkatenat als Fallback). Bei der Mega-Variante gibt es das schon, der Mini-Generator wird parallel ausgeruestet.
5. Lasse `scripts/generate-megaprompt.py`, `scripts/generate-unified-mini-prompts.py`, `scripts/generate-skills-md.py` und `scripts/inject-megaprompt-section.py` laufen.
6. Pruefe Validator-Regeln repo-weit: Skill-description bis 1024 Zeichen, plugin.json- und marketplace.json-description bis 300 Zeichen, kein `\d,\d` in Descriptions, keine XML-Brackets, keine Emojis, kein Paragrafenzeichen in Pruefdateien, Slugs nur aus Kleinbuchstaben, Ziffern und Bindestrich. Bei Fehlern: nicht pushen, sondern fixen. Ich will auf KEINEN FALL die validation failed.
7. Committe in Etappen (zum Beispiel 20 Plugins pro Commit). Autor: `Klotzkette` <`39582916+Klotzkette@users.noreply.github.com`>. Keine Erwaehnung von Codex, Claude oder anderen KI-Namen in der Commit-Message.
8. Pull-Pflicht vor jedem Push: `git fetch origin && git pull --rebase origin main`. Erst dann `git push origin main`.
9. Versions-Bump und Tag macht Codex **nur, wenn ich es ausdruecklich anweise**. Ohne Anweisung bleibt die laufende Versionsnummer.

## Akzeptanzkriterien

- Jedes Plugin im Repo hat `<plugin>/<slug>-megaprompt.md` und `<plugin>/<slug>-miniprompt.md`.
- Beide Dateien sind plugin-spezifisch, nicht generisch.
- Skill-Namen und Paragrafen darin sind nicht erfunden.
- README jedes Plugins verlinkt den lokalen Mega und Mini prominent.
- Validator laeuft fehlerfrei.
- Bundle in `testakten/megaprompts/<slug>.md` und `unified-mini-prompts/<slug>.md` ist neu erzeugt und uebernimmt die lokalen Dateien, wo vorhanden.

## Aufraeumen am Ende

- Suche im Repo nach Vorkommen alter Dateinamen `MEGAPROMPT.md`, `MINIPROMPT.md`, `mega.md`, `mini.md` als Plugin-lokale Dateien und ersetze sie durch `<slug>-megaprompt.md` und `<slug>-miniprompt.md` via `git mv`.
- Pruefe READMEs, Skripte und `CHANGELOG.md` auf Verweise auf alte Namen und schreibe sie um. Historische Eintraege im `CHANGELOG.md` (Eintraege zu bereits veroeffentlichten Versionen) bleiben unveraendert.

## Reporting

Am Ende des Laufs erzeugt Codex eine kurze Markdown-Tabelle (`docs/mega-und-mini-coverage.md`) mit den Spalten Plugin, Mega vorhanden, Mega-Quelle (lokal/auto), Mini vorhanden, Mini-Quelle (lokal/auto). Zusaetzlich eine Zeile mit der Gesamtcoverage in Prozent.

## Letztes

Codex schreibt nuechtern, juristisch, ohne Marketing-Sprache. Generisches Maskulinum gilt, ohne es sichtbar zu dokumentieren.
