# Benchmark — Klotzkette German Legal Skills vs. Harvey LAB

> Stand v332.0.0. Vergleich, Methodik und Werkzeuge.

## Inspiration

Harvey LAB (https://github.com/harveyai/harvey-labs) ist ein Open-Source-Benchmark zur Bewertung von LLM-Agents auf juristischer Arbeit (24 Practice Areas, 1.251 Tasks, US-Fokus, MIT). Dieses Repository bringt Harveys methodisches Vorbild — Task-Datenraum + Execution Harness + All-Pass-Rubrics — ins deutsche Rechtssegment.

## Was es gibt

| Komponente | Status | Datei |
|---|---|---|
| Task-Datenraum | vorhanden (206 Testakten in 7 Formaten) | `testakten/` |
| Rubrics pro Testakte | implementiert (Pass/Fail-Checks in YAML) | `testakten/<slug>/rubric.yaml` |
| Execution Harness | implementiert | `scripts/run-eval.py` |
| All-Pass-Scoring | implementiert | im Harness |
| Comparison Dashboard | implementiert (Modell-zu-Modell) | `scripts/compare-eval-runs.py` |
| LLM-Judge | Skelett mit Anthropic-Adapter | `scripts/llm-judge-eval.py` |
| Self-Test-Konvention | seit v293 verbindlich | `references/anwalts-dashboard-konvention.md` |

## Schnellstart

```bash
# Alle Rubrics ausfuehren
python3 scripts/run-eval.py --report

# Ausgewaehlte Akten
python3 scripts/run-eval.py insolvenz-asset-deal-chaincortex-ai-berlin

# JSON-Snapshot fuer Vergleich speichern
python3 scripts/run-eval.py --json-out runs/$(date -u +%Y%m%d-%H%M)-opus4-7.json --label "opus-4-7"

# Modelle vergleichen (zwei Snapshots erforderlich)
python3 scripts/compare-eval-runs.py runs/2026-06-11-opus4-7.json runs/2026-06-12-opus4-8.json

# LLM-Judge auf einen einzelnen Skill-Output
python3 scripts/llm-judge-eval.py path/to/skill-output.md path/to/criterion.md
```

## Rubric-Format

```yaml
name: "Beschreibung der Testakte"
plugin: "primary-plugin-name"

checks:
  - id: r01-readme
    check_type: file_exists
    description: "README vorhanden"
    path: "README.md"

  - id: r02-fristhinweis
    check_type: regex_match
    description: "Standardfrist im Mandantenbrief erwaehnt"
    path: "01_mandantenbrief.md"
    pattern: "(3-Wochen|drei.{0,3}Wochen|. 4 KSchG)"

  - id: r03-anlagen-vorhanden
    check_type: file_count
    description: "Mindestens drei Anlagen"
    glob: "anlagen/*.*"
    min: 3

  - id: r04-bag-rspr-zitiert
    check_type: text_contains
    description: "BAG-Linie referenziert"
    path: "memo.md"
    contains: "BAG"

  - id: r05-finale-pruefung-manuell
    check_type: human_review
    description: "Finale Stil- und Schluesselbotschafts-Pruefung"
    note: "vor Mandanten-Versand manuell pruefen"
```

## Check-Typen

| `check_type` | Pruefung |
|---|---|
| `file_exists` | Datei existiert |
| `text_contains` | Substring kommt in Datei vor |
| `regex_match` | Regex matcht in Datei |
| `file_count` | Anzahl Dateien matchen Glob >= min |
| `human_review` | Manuell — Eval-Skript zaehlt als `skipped` |

## All-Pass-Logik

Eine Akte gilt als All-Pass, wenn alle Pass/Fail-Checks bestanden sind (`human_review`-Checks zaehlen als `skipped` und blockieren das All-Pass-Resultat nicht).

## Verhaeltnis zu Harvey LAB

| Dimension | Harvey LAB | Klotzkette-Repo |
|---|---|---|
| Genre | Benchmark / Evaluator | Skill-Library + Evaluator |
| Sprache/Recht | EN / US-Common-Law | DE / deutsches Recht |
| Volumen | 1.251 Tasks, 24 Areas | 25.640 Skills, 213 Plugins, 206 Testakten |
| Realismus | M&A-Datenraum | Mandatsakten in 7 Originalformaten + Gesamt-PDF |
| Scoring | All-Pass-Rubrics + LLM-Judge | All-Pass-Rubrics + LLM-Judge (kompatibel) |
| Lizenz | MIT | Apache-2.0 OR MIT |

Beide Repos folgen demselben Bewertungsparadigma; die Klotzkette-Plattform spezialisiert sich auf das deutsche Recht und betont die Vollstaendigkeit des anwaltlichen Workflows (Mandatsannahme → Anlage → Schriftsatz → Vergleich).

## Was als naechstes kommen koennte

- **Rubrics fuer alle 206 Testakten** (z. Zt. 5 als Proof-of-Concept)
- **Plugin × Akten-Matrix**: pro Plugin Score gegen relevante Testakten
- **CI-Integration**: PR-Run fuehrt Eval auf geaenderten Plugins aus
- **Auto-Bewertung Skill-Outputs**: LLM-Judge auf Skill-MD-Output, nicht nur Testakten

## Quellenhygiene bleibt unangetastet

Auch der Eval-Harness erzwingt keine Aktenzeichen aus Modellwissen. `text_contains` matcht nur, was wirklich im Repo steht; `human_review` haelt Wertungs-Pruefungen offen.
