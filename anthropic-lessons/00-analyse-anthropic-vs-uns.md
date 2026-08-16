# Analyse: anthropics/claude-for-legal vs. claude-fuer-deutsches-recht

Stand: v52.8.0 (unser Repo) gegen anthropics/claude-for-legal HEAD (Juni 2026).
Dieser Branch ist isoliert (`anthropic-patterns-experimente`). Wir mergen erst
nach Absprache, damit Codex' parallele Arbeit nicht ueberschrieben wird.

**Quelle Anthropic-Repo:** https://github.com/anthropics/claude-for-legal

**Wichtig:** Die Anthropic-Skills sind lang, weil sie für
US-Grosskanzleien/Inhouse-Counsel mit MCP-Anbindung (Westlaw, CourtListener,
iManage, Slack) gebaut sind und ein Mandantenleben begleiten. **Nicht alle unserer
Plugins haben diesen Kontext.** Welche Plugins für Anthropic-Tiefe geeignet sind
und welche kurz bleiben müssen, steht in
`CODEX-SELEKTION-welche-skills-tief.md`. Die Pflicht-Sektionen aus
`CODEX-INSTRUKTION-skill-tiefe-boost.md` gelten nur für Klasse A (Grosskanzlei,
MCP-anbindbar, mandatsbegleitend - rund 70 von 112 Plugins).

## Quantitativer Vergleich

| Kennzahl                  | Anthropic       | Unser Repo (v52.8.0)  |
|---------------------------|-----------------|-----------------------|
| Plugins                   | 13 (12 + 1 ext.)| 112                   |
| Skills gesamt             | 151             | 3670                  |
| SKILL.md Median (Bytes)   | ~11.000         | ~4.500                |
| SKILL.md Max (Bytes)      | ~49.000         | ~60.000               |
| Agents                    | 9               | 0                     |
| MCP-Server pro Plugin     | 5-15            | 0 (keine .mcp.json)   |
| Managed-Agent-Cookbooks   | 5               | 0                     |
| References (shared)       | 2               | 0                     |
| Validierungsskripte       | 3 Python/Bash   | 2 Python+1 Node       |

**Lesart:** Anthropic baut **wenige tiefe** Skills mit reicher Infrastruktur
drumherum. Wir bauen **viele kompakte** Skills mit minimaler Infrastruktur.
Beide Modelle sind valide. Anthropic gewinnt in Workflow-Tiefe und Persistenz,
wir gewinnen in Breite und einzelnem Tooling pro Rechtsgebiet.

## Was Anthropic strukturell anders macht

### 1. Cold-Start-Interview + persistente CLAUDE.md pro Plugin

Jedes Plugin enthaelt einen `cold-start-interview` Skill, der einen
Practice-Profile-Fragebogen mit dem User durchgeht und das Ergebnis nach
`~/.claude/plugins/config/<marketplace>/<plugin>/CLAUDE.md` schreibt. Alle
anderen Skills lesen diese Datei VOR jeder Aktion.

**Effekt:** Skills brauchen keine Kalt-Frage `Wer fragt? Welche Rolle?` -
diese Information ist persistent. Antworten werden konsistent, weil
Risikokalibrierung, Eskalationskette, Standardseite (Kläger/Beklagter),
Erscheinungsort etc. einmal erfasst und immer geladen werden.

Bei uns wird die Rolle in jedem Skill neu abgefragt. Das ist redundant.

### 2. Shared `company-profile.md` über alle Plugins

`references/company-profile-template.md` definiert Mandanten-/Kanzleidaten
auf Marketplace-Ebene. Das **erste** Plugin-Setup schreibt diese Datei
einmal, danach laden sie alle anderen Plugins. So muss man Jurisdiktion,
Branche und Eskalationskette nur einmal eingeben.

### 3. `customize`-Skill pro Plugin

Punktuelles Ändern eines Profil-Feldes ohne Cold-Start neu laufen lassen.
Praktisch und schoen modular.

### 4. `matter-workspace` Konvention

Pro Mandat ein Ordner unter
`~/.claude/plugins/config/<marketplace>/<plugin>/matters/<slug>/` mit
festen Dateien:

- `matter.md` - Narrativ-Intake
- `history.md` - laufendes Logbuch
- `chronology.md` - Zeitstrahl der relevanten Ereignisse
- `_log.yaml` (eine Datei oben drueber) - alle Mandate strukturiert

Diese Konvention verbindet Skills sauber: `matter-intake` legt an,
`chronology` schreibt fort, `matter-update` aktualisiert, `portfolio-status`
liest aggregiert.

Wir haben Testakten, aber **kein Schema für aktive Mandate**. Das ist
für Mandanten weniger nuetzlich.

### 5. Agents (Subagents) mit definierten Tool-Scopes

Jedes Plugin kann `agents/<name>.md`-Dateien enthalten. Beispiel
`docket-watcher`:

```yaml
---
name: docket-watcher
description: Scheduled agent...
model: sonnet
tools: ["Read", "Write", "mcp__trellis__*", "mcp__courtlistener__*", "mcp__*__slack_send_message"]
---
```

Tools werden **explizit aufgelistet**. Das verhindert ueberbreite
Berechtigungen. Wir haben gar keine Agents.

### 6. Managed-Agent-Cookbooks

Unter `managed-agent-cookbooks/<name>/` liegen `agent.yaml`-Konfigurationen
für headless Hintergrund-Agenten. Sie verweisen auf dieselben Skills wie
das interaktive Plugin (`file: ../../litigation-legal/agents/docket-watcher.md`)
- eine **einzige Quelle der Wahrheit**. Wir haben so etwas nicht.

### 7. `.mcp.json` pro Plugin - Connector-Deklaration

Beispiel `litigation-legal/.mcp.json` deklariert: Slack, Google Drive,
Everlaw, TopCounsel, CourtListener, Trellis, Westlaw etc. Das macht
Skills sofort tool-faehig - der Skill kann `mcp__courtlistener__search_opinion`
aufrufen, wenn der User den Connector hat.

Wir nutzen Connectors nur über den `pplx-cli` und haben keine
Plugin-deklarierten MCP-Server. Da liegt erhebliches Potenzial.

### 8. Side-Framing (Kläger/Beklagter) durchgaengig

Jedes Litigation-Skill liest `## Side` aus dem Practice-Profil und passt
Vokabular und Tagging an:

- Kläger: 🔴 "establishes element", "starts SOL clock"
- Beklagter: 🔴 "breaks element", "opens SOL defense"

Wir kennzeichnen das **manchmal**, aber nicht systematisch.

### 9. Disclosed-Document-Restrictions als Pflicht-Check

Skills mit Dokumentenarbeit (chronology, claim-chart, privilege-log)
fragen zuerst: "Sind diese Dokumente aus Disclosure/Discovery?" Dann
Verweis auf CPR 31.22 (UK) / Rule 26(c) (US). Das ist **defensive
Berufsrecht-Architektur**.

Wir haben das gar nicht. Für deutsches Recht äquivalent:

- Akteneinsicht nach § 147 StPO: nur für Verteidigung verwendbar
- Akteneinsicht im Zivilprozess nach § 299 ZPO: zweckgebunden
- DSGVO-Zweckbindung
- Anwaltliche Schweigepflicht § 43a BRAO bei Drittakten

### 10. Source-Attribution-Tags

Jede zitierte Norm/Entscheidung wird mit Tool-Quelle markiert:

```
[Westlaw] [CourtListener] [web search - verify] [model knowledge - verify] [user provided]
```

So sieht der Anwalt sofort, was er nachpruefen muss. Wir haben nur die
Konvention "dejure.org / openjur.de", aber **kein Tag-System** für
Konfidenz.

### 11. "What it does NOT do" Sektion am Skill-Ende

Jeder Anthropic-Skill endet mit einer Liste expliziter Negativ-Abgrenzungen:

> - **Does NOT calendar deadlines.** Computed deadlines are leads...
> - **Does NOT trust its own filing classifications.**
> - **Does NOT replace your docketing system.**

Das ist eine elegante Lager-Schutz-Mechanik. Sie macht Hallu-Risiken
sichtbar. Wir haben "Was dieser Skill nicht macht" bereits in den
Bauleitern, aber kuerzer und weniger pointiert.

### 12. Hand-Off-Pattern

Skills enden oft mit konkreten Anschluss-Aufrufen:

> Hand off: `/legal-hold --issue` if hold not in place; `/matter-intake`
> if materiality warrants; `/matter-briefing [slug]` if party subpoena.

Wir empfehlen Folge-Skills, aber meist als Plug-Kontext-Hinweis, nicht
als konkreten Slash-Befehl.

### 13. Pfad-Konvention `~/.claude/plugins/config/<...>/`

Anthropic nutzt **eine version-stabile** Config-Pfad-Konvention. Plugin-Updates
ueberschreiben keine User-Daten. Sie migrieren bei Bedarf den alten
Cache-Pfad.

Wir versionieren Plugins aber speichern nirgends User-Mandanten-Daten in
einer dedizierten Config-Layer.

### 14. Argument-Hint im Frontmatter

```yaml
argument-hint: "[path-to-subpoena] [--slug=custom-slug]"
```

Das hilft Slash-Command-Autocompletion und dokumentiert die Aufrufart.
Wir hatten das als verbotenes Feld - aber es war wohl vor Claude Code 2.x
nicht offiziell. Heute ist es **standardkonform** und nuetzlich.

### 15. Schritt-1..N als knappe Workflow-Liste oben

Skills beginnen mit einer **kompakten** nummerierten Liste (5-10 Schritte),
dann erst der ausfuehrliche Reference-Text. So sieht das Modell sofort
den Ablauf. Wir geben oft erst die Erklaerung und dann Schritte.

## Was bei UNS besser ist - das wollen wir nicht aufgeben

1. **Breite Abdeckung deutsches Recht.** 112 Plugins gegen 13. Wir
   decken Fachanwaltsfaecher, Verbraucherrecht, Forderungsmanagement,
   Insolvenz, OWi etc. ab. Anthropic ist nur US-Inhouse-Focus.

2. **Kompakte einsteigerfreundliche Skills.** Unser Median ~4.500 Byte ist
   leichter zu lesen. Anthropic-Skills mit 30-49k Byte sind ueberwaeltigend
   für Solo-Anwaelte.

3. **Testakten.** Wir haben echte deutschsprachige Mandantenakten als
   Sandboxes. Anthropic hat nichts vergleichbares.

4. **Plugin-Build-Pipeline mit Release-ZIPs.** Wir produzieren pro Plugin
   ein ZIP, einen Megazip und ein Komplettpaket. Anthropic ueberlaesst das
   `claude plugin` CLI.

5. **Detail-Pages pro Plugin + Markdown- und Raw-Links pro Skill.** Unsere
   skills-index/ erlaubt Browser-Download einzelner SKILL.md. Anthropic
   verlaesst sich auf GitHub-Navigation.

## Empfehlung - Top 5 uebernehmbare Patterns

In Reihenfolge des erwarteten Nutzens:

1. **`cold-start-interview` + Practice-Profile-CLAUDE.md pro Plugin**.
   Reduziert Redundanz massiv. Solo-Anwaelte müssen ihre Daten einmal
   eingeben, danach kennen alle Skills sie.

2. **`matter-workspace` Konvention** mit `matters/<slug>/matter.md`,
   `history.md`, `_log.yaml`. Verbindet unsere bestehenden Skills zu
   echten Mandatsketten.

3. **`agents/` mit Tool-Scope-Deklaration**. Wir koennten Scheduled Agents
   für Frist-Watching, Rechtsprechungs-Monitoring, DSGVO-Beschwerde-Triage
   bauen.

4. **"What this skill does NOT do" als Standardabschnitt**. Klare
   Negativ-Abgrenzung reduziert Halluzinationsrisiko und Berufsrecht-
   Exposure.

5. **Source-Attribution-Tags** `[BGH-Datenbank]`, `[dejure.org]`,
   `[Web-Recherche - pruefen]`, `[Modellwissen - pruefen]`. Schaerft
   die Pflicht zur Primaerquellenpruefung.

## Was NICHT uebernommen werden sollte

- **Skills auf 30-49k Byte aufblasen.** Unser Stil ist absichtlich
  einsteigerfreundlich kurz. Wir gehen den Mittelweg: pro Plugin EIN
  "Bauleiter"-Skill in Anthropic-Tiefe, der Rest bleibt kompakt.

- **Auf 13 Plugins reduzieren.** Unsere Breite ist ein Alleinstellungsmerkmal.

- **`argument-hint` im Frontmatter pauschal einfuehren.** In unserer
  Validator-Regel ist es derzeit verboten. Wir muessten den Validator
  anpassen UND einen guten Default-Stil setzen.

## Konkrete Branch-Inhalte

Diese Branch enthaelt:

- `00-analyse-anthropic-vs-uns.md` (diese Datei)
- `01-vorschlag-cold-start-interview.md` - Prototyp eines Cold-Start-Skills
  für **deutsches Recht** (am Beispiel fachanwalt-strafrecht)
- `02-vorschlag-matter-workspace.md` - Konvention für aktive Mandate
- `03-vorschlag-source-attribution-tags.md` - Tag-System für Quellenherkunft
- `04-vorschlag-agents-skeleton.md` - Skeleton für einen Frist-Watcher-Agent
- `05-vorschlag-not-do-section.md` - Standardabschnitt für Negativ-Abgrenzung

Alle Vorschlaege sind **Skizzen**, nicht produktionsbereit. Sie werden erst
nach Codex' Update-Welle mit dir gemeinsam in `main` ueberfuehrt.
