# Skill-Quality-Hardening vom 02.06.2026

## Ziel

Repo-weiter Sweep über Plugins und Skills mit Fokus auf:

- generische oder zu kurze Skillkörper,
- fehlende Quellen- und Livecheck-Regeln,
- riskante Rechtsprechungs-, BeckRS-, juris-, Kommentar- und Aufsatzfundstellen,
- Workflow-Hakeligkeiten bei Start, Output und Anschluss-Skills.

## Vorgehen

- 8.698 `SKILL.md`-Dateien in 128 Plugins maschinell geprüft.
- Skills ohne erkennbares Quellen-/Livecheck-Signal identifiziert und mit einem knappen Qualitäts-Hardening ergänzt.
- Sehr kurze Skills erneut geprüft und fachlich vertieft.
- Zitierweise-Regel von v4.0 auf v4.1 gehoben und in den Plugin-Spiegel synchronisiert.
- Repo-Generatoren für README-/Skill-Übersichten neu ausgeführt.
- Struktur-, Frontmatter-, Gesamt-PDF- und Diff-Checks ausgeführt.

## Änderungen

- 1.093 Skills mit zusätzlichem Qualitäts-Hardening versehen:
  - aktennah arbeiten,
  - keine Rechtsprechung aus Modellwissen,
  - keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate,
  - unsichere Quellen, Fristen und Behördenpraxis sichtbar als Prüfpunkt markieren,
  - Ergebnis mit Kurzbild, Prüfpfad, Risikoampel, Lückenliste und nächsten Schritten ausgeben.
- 76 vormals sehr knappe Skills in `gesellschaftsgruender` und `anlagen-zu-schriftsaetzen` mit konkreten Vertiefungs-Workflows ausgebaut.
- `references/zitierweise.md` auf v4.1 aktualisiert:
  - zusätzliche Sperre gegen Scheinpräzision,
  - klare Trennung zwischen gesichert, plausibel/zu prüfen und nicht verwendbar,
  - aktuelle Palandt-/Pahlen-Fehlerlogik geschärft.
- `scripts/sync-references.py` repariert: alter Methodik-Dateiname und altes Pluginverzeichnis korrigiert.
- Zitierweise-Skills entschärft:
  - Literatur-Skills arbeiten nur noch mit Nutzerquelle oder dokumentiertem Live-Zugriff,
  - BeckRS/juris nur als gelieferte oder live verifizierte Fundspur,
  - v4.0-Reste auf v4.1 nachgezogen.

## Prüfergebnis

- `short_under_180`: 0
- `skills_without_quality_signal`: 0
- `validate-yaml-frontmatter.py`: 0 Fehler, 0 Warnungen
- `validate-plugin-structure.mjs`: OK
- `validate-testakten-gesamt-pdf.py`: OK für 132 Testakten
- `git diff --check`: OK

## Resthinweis

Dieser Sweep ersetzt keine manuelle Volltextprüfung jeder einzelnen Altentscheidung. Er reduziert das Risiko aber strukturell: Skills dürfen Rechtsprechung und Literatur nicht mehr als gesicherte Quelle ausgeben, wenn Gericht, Datum, Aktenzeichen, freie/amtliche Quelle oder Nutzer-/Livequelle fehlen.
