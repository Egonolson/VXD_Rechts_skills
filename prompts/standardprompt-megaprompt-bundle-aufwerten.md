# Standard-Prompt — Megaprompt-Bundle aufwerten

Dieser Prompt ist fuer einen beliebigen Coding-Agenten (Codex CLI, Cursor, Aider, Continue, oder ein anderer LLM-Coding-Assistent mit Repo-Zugriff). Aufgabe: pro Plugin im Repository `Klotzkette/claude-fuer-deutsches-recht` einen besseren, plugin-spezifischen Megaprompt in das Bundle-Verzeichnis `testakten/megaprompts/` schreiben — auf Basis der echten Skills des Plugins. Der Megaprompt soll als eigenstaendige Markdown-Datei nutzbar sein, ohne Plugin-Loader und ohne Claude Code.

---

## Geltungsbereich

- Pro Plugin genau eine Datei: `testakten/megaprompts/<slug>.md`.
- Quelle der Wahrheit sind die Skills des Plugins unter `<slug>/skills/*/SKILL.md` und die Plugin-`README.md`.
- Der Bundle-Mega ist die Plain-Markdown-Variante des Plugins fuer Nutzer ohne Claude-Code-Plugin-Loader.

## Welche Plugins?

Der Coding-Agent verarbeitet alle Plugins, fuer die gilt:

- Es existiert `<plugin>/.claude-plugin/plugin.json`.
- Plugin liegt entweder im Repo-Wurzelverzeichnis oder unter `gerichtsplugins/<slug>/`.
- Ausgenommen sind Plugins mit einem handgepflegten lokalen Megaprompt `<plugin>/<slug>-megaprompt.md`. Diese werden nicht ueberschrieben.

Der Generator `scripts/generate-megaprompt.py` reicht den lokalen Mega bereits durch. Der Coding-Agent arbeitet nur an Plugins ohne lokalen Mega.

## Qualitaetsziel

Der Bundle-Mega ist kein Skill-Konkatenat. Er ist eine kuratierte, sinnvoll geordnete Werkstattbeschreibung des Plugins, die ein LLM ohne weiteres Setup als System-/Kontextprompt verwenden kann. Inhalt soll plugin-spezifisch sein, nicht generisch.

## Pflicht-Struktur jeder Megaprompt-Datei

```
# Megaprompt — <Plugin-Titel>

## Rolle
- Wer arbeitet hier (Berufsbild, Funktion, typische Auftraggeber).
- Was diese Rolle NICHT ist.

## Werkstattlogik
- Stationen in Reihenfolge (Triage, Eingang, Arbeit, Anschluss).
- Stop-Kriterien.

## Pflicht-Workflow am Anfang
- Welche zwei oder drei Festlegungen fragt der Agent zuerst (Output-Format, Datenquelle, Rolle/Lage)?
- Default-Antworten benennen.

## Quellen-Disziplin
- Welche Paragrafen, Schemata, Standards sind die Anker (mit Wort 'Paragraf', nicht Zeichen)?
- Welche Quellen sind live zu verifizieren?
- Aktualitaetsregel je Plugin (z. B. BGH-Datenbank, BFH, BVerfG, Bundesnetzagentur).

## Leitentscheidungen
- 2 bis 5 echte, pruefbare Entscheidungen mit Gericht, Datum, Aktenzeichen und Kernaussage.

## Indizienliste oder Pruefraster
- Plugin-spezifische Anhaltspunkte, die der Agent abfragt.

## Antwortform
- Pflichtfelder jeder Antwort des Agenten (Lagebild, Pruefung, Empfehlung, naechster Schritt, Quellen).

## Eigenheiten dieses Plugins
- 4 bis 8 konkrete Stolpersteine, die nur in dieser Gerichtsbarkeit / Materie auftreten.

## Skelette
- 2 bis 3 vorbereitete Antwort-Skelette fuer typische Faelle des Plugins.
```

## Inhaltliche Pflichten

- **Plugin-spezifisch**: Wenn das Plugin `arbeitsrecht` heisst, kommen Kuendigungsschutzgesetz, Klagefrist drei Wochen nach Paragraf 4 KSchG, Aufhebungsvertrag, Sozialauswahl rein. Nicht: generisches Triage-Geschwurbel.
- **Echte Paragrafen** statt Platzhaltern. Wenn unklar, lies die Skills und uebernimm die dort verwendeten Paragrafen.
- **Workflow-orientiert**: Schritte in Reihenfolge, mit Eingaengen und Arbeitsprodukten. Keine Bullet-Wuesten ohne Reihenfolge.
- **Anker**: Gerichte, Datenbanken, Standards des Faches (z. B. IDW S 6, BGH-Linie, RVG, GNotKG, FamFG).
- **Konkrete Antwort-Skelette** im Imperativ ("Du antwortest ...").

## Verbotene Inhalte

- Keine generischen Templates "1. Welche Rolle hat die fragende Person und wer ist Gegenueber?" als alleinige Substanz.
- Keine Skill-Konkatenation. Wenn du einen Skill nennst, fasse seine Werkstatt-Logik in zwei Saetzen zusammen, statt seinen Text einzukleben.
- Keine BeckRS, juris, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Wenn der Coding-Agent unsicher ist, schreibt er einen Live-Verifikationshinweis.
- Keine Behauptungen ueber Gerichtspraxis ohne Beleg.
- Keine Emojis. Keine spitzen Klammern in Descriptions. Kein Paragrafenzeichen, immer das Wort "Paragraf".
- Keine Erwaehnung von Claude, OpenAI, Codex, Cursor, Aider, Continue oder anderem KI-Hilfsnamen.

## Zeichen- und Format-Konvention

- Echte Umlaute (ae, oe, ue, ss werden zu ae, oe, ue, ss nur in Slugs und in JSON-`description`-Feldern; nicht in Markdown-Prosa). In Markdown-Prosa: `Liquiditaet` -> tatsaechlich "Liquiditaet" mit echtem ae als ae, da auch das Beispiel-Plugin so arbeitet.
- Verwende `Paragraf` statt Paragrafenzeichen.
- Maximal eine H1 pro Datei. Danach H2 und H3.
- Datei endet mit Leerzeile.
- UTF-8 ohne BOM.
- Kein vorangestellter YAML-Frontmatter (das ist eine Megaprompt-Datei, kein Skill).

## Generisches Maskulinum

Das Repo arbeitet im generischen Maskulinum. Dokumentiere das nicht sichtbar in CLAUDE.md, aber halte dich im Prosa-Stil daran.

## Algorithmus fuer den Coding-Agenten

1. Liste alle Plugins (`<slug>/.claude-plugin/plugin.json` und `gerichtsplugins/<slug>/.claude-plugin/plugin.json`).
2. Filtere Plugins, fuer die `<slug>/<slug>-megaprompt.md` existiert. Diese ueberspringst du.
3. Fuer jedes verbleibende Plugin:
   a. Lies `<slug>/README.md` und alle `<slug>/skills/*/SKILL.md`.
   b. Bestimme Rechtsgebiet, typische Faelle, Pflicht-Paragrafen, Spruchkoerper.
   c. Schreibe `testakten/megaprompts/<slug>.md` neu in der Pflicht-Struktur. Mindestens 150, hoechstens 400 Zeilen.
   d. Validiere: keine Emojis, kein Paragrafenzeichen, keine spitzen Klammern, kein YAML-Frontmatter, exakt eine H1.
4. Committe in Etappen (z. B. 20 Plugins pro Commit) mit Autor `Klotzkette` <`39582916+Klotzkette@users.noreply.github.com`>.
5. Versions-Bump beim Abschluss auf die naechste vergebene Repo-Version. Tag und Release nur, wenn ausdruecklich gewuenscht.

## Akzeptanzkriterien

- `testakten/megaprompts/<slug>.md` ist eine in sich vollstaendige Werkstattbeschreibung.
- Ein Mensch, der das Plugin nicht kennt, kann den Megaprompt in ein LLM einfuegen, einen echten Fall draufkippen und eine sinnvolle Antwort bekommen.
- Skill-Schlagworte und Paragrafen sind nicht erfunden.
- Stil ist nuechtern, juristisch, ohne Marketing-Sprache.

## Bei Unklarheit

Wenn ein Plugin so duenn besetzt ist, dass keine sinnvolle Werkstatt entsteht, ersetzt du den bisherigen Bundle-Mega durch einen ausdruecklichen Hinweis "Dieses Plugin ist in Aufbau. Bitte Skill-Liste pruefen." plus die Skill-Liste mit Beschreibung. Keine Erfindung.

## Output

Eine Datei pro Plugin in `testakten/megaprompts/<slug>.md`, UTF-8, ohne BOM, ohne Frontmatter. Nichts anderes.
