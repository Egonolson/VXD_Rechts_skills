# Regel für Skill-Autoren und Bearbeiter

Diese Regel richtet sich an alle, die in diesem Repository neue Skills anlegen oder bestehende Skills veredeln.

## Prüfroutine bei jedem neuen oder veredelten Skill

Prüfe nach Fertigstellung eines Skills, ob er sich als eigenständiger Werkstatt-Prompt außerhalb des Plugin-Setups einsetzen lässt. Indizien dafür:

- Der Skill enthält einen substanziellen, inhaltlich tragenden Prompt-Korpus, also nicht nur Router-Logik, Kaltstart-Anweisungen oder Verweise auf andere Skills.
- Der Skill ist fachlich spezifisch (z. B. konkrete Klauselprüfung, konkrete Prüfroutine, konkretes Verfahrensschema), nicht generisch.
- Der Skill liefert ein konkretes Output-Schema (Memo, Prüfbericht, Klausel, Schriftsatzteil, Tabelle, Checkliste).
- Der Skill bezieht sich auf eine identifizierbare Fachanwaltschaft oder Praxisrichtung im deutschen Recht.

Wenn diese Indizien zutreffen, trägst du den Skill in `PROMPTLISTE.md` ein, und zwar in die passende Kategorie (Fachanwaltschaft oder Querschnittsrubrik).

## Was NICHT in die Promptliste gehoert

- Reine Eingangs-, Router- oder Kaltstart-Skills (z. B. `*-kaltstart`, `*-eingang`, `*-router`).
- Reine Workflow-Klebeschichten ohne eigenen Prompt-Wert.
- Generische Sprachpolier- und Hilfsskills ohne juristischen Bezug.
- Historisch-exotische Plugins (Preussisches Landrecht, Roemisches Recht, Roemisch-katholisches Kirchenrecht, Weltraumrecht).

## Wo eintragen

Datei: [`PROMPTLISTE.md`](../PROMPTLISTE.md)

Kategorien orientieren sich an den 24 deutschen Fachanwaltschaften (BORA-Reihenfolge) plus Querschnittsrubriken (BGB AT/BT, Prozesspraxis, Berufsrecht/Kanzleimanagement, Sprache/Lehre, Methodenlehre/Rechtstheorie).

## Wann eintragen

- Bei neu erstellten Plugins: direkt mit dem Feature-Commit, der das Plugin einführt.
- Bei neu hinzugefügten Skills in bestehenden Plugins: nur bei substanziellen Werkstatt-Prompts (siehe oben), die Plugin-Zeile selbst bleibt unverändert, da die Promptliste auf Plugin-Ebene verlinkt.
- Bei Versions-Bumps (Minor und Major): einmal durchsehen und neu hinzugekommene Plugins nachpflegen.

## Wie eintragen

Format pro Plugin-Eintrag in `PROMPTLISTE.md`:

```markdown
### [plugin-name](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/plugin-name)

Kurzbeschreibung (200 bis 250 Zeichen), die das fachliche Profil und den Praxisnutzen abbildet.

**Skills:** [skills/](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/plugin-name/skills) — laden, kopieren, in beliebiges Tool einfuegen.
```

## Beispiel-Workflow

1. Du erstellst ein neues Plugin `xyz-recht`.
2. Prüfe: fällt es unter die Praxis-Kriterien oben?
3. Wenn ja: öffne `PROMPTLISTE.md` und ergänze einen Eintrag in der passenden Kategorie (alphabetisch innerhalb der Kategorie).
4. Aktualisiere die Plugin-Zahl in der Inhaltsverzeichnis-Zeile dieser Kategorie um 1.
5. Committe `PROMPTLISTE.md` zusammen mit dem Plugin-Commit oder in einem direkten Folgecommit `chore(promptliste): xyz-recht eingetragen`.

## Disclaimer

Die Promptliste hat einen eigenen, sehr ausführlichen Disclaimer in `PROMPTLISTE.md`. Ändere ihn nicht, kürze ihn nicht und schiebe ihn nicht nach unten. Er gehört an den Anfang der Datei und ist Teil des Praxis-Konzepts dieses Repositories.
