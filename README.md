# deutsches-recht-proxy

Ein Proxy-Marketplace für Cowork und Claude Code. Er enthält **keine Plugins**,
sondern nur einen Katalog, der auf die 235 Plugins in
[Klotzkette/claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht)
verweist.

## Warum

Das Original-Repo ist ~1,4 GB groß, hauptsächlich wegen `testakten/` (617 MB
Test-PDFs). Cowork akzeptiert Marketplace-Repos aber nur bis 512 MB, deshalb
schlägt "Add marketplace" dort fehl.

Dieser Katalog ist **150 KB** groß. Jeder Plugin-Eintrag nutzt die Quelle
`git-subdir`, sodass beim Installieren nur der jeweilige Unterordner sparse
geklont wird — gemessen ~15 MB pro Plugin statt 1,4 GB.

Updates kommen weiterhin aus dem Original-Repo: die Einträge zeigen auf
`ref: main` ohne Commit-Pin.

## Einrichten

1. Neues **öffentliches** Repo auf GitHub anlegen, z. B. `deutsches-recht-proxy`.
2. Den Inhalt dieses Ordners hineinpushen:

   ```bash
   git init
   git add -A
   git commit -m "Proxy-Marketplace fuer claude-fuer-deutsches-recht"
   git branch -M main
   git remote add origin https://github.com/DEIN-NAME/deutsches-recht-proxy.git
   git push -u origin main
   ```

3. In Cowork: **Customize → Plugins → Add marketplace** →
   `DEIN-NAME/deutsches-recht-proxy`

   In Claude Code: `/plugin marketplace add DEIN-NAME/deutsches-recht-proxy`

Danach erscheinen alle 235 Plugins unter *Browse plugins* und lassen sich
einzeln installieren.

## Aktualisieren

Neue Plugin-Versionen im Original werden beim Installieren bzw. Aktualisieren
automatisch gezogen. Kommen im Original **neue Plugins** dazu, muss dieser
Katalog neu erzeugt werden — dafür liegt `katalog-neu-bauen.sh` bei.

## Struktur

```
.claude-plugin/marketplace.json   Katalog mit 235 git-subdir-Einträgen
katalog-neu-bauen.sh              Erzeugt marketplace.json neu aus dem Original
README.md
```

## Hinweis

Das Original ist ein privates Community-Projekt ohne Prüfung durch Anthropic.
Vor dem Einsatz auf Mandanten- oder Kundendaten lohnt ein Blick in den
jeweiligen Plugin-Ordner. Die Skills ersetzen keine Rechtsberatung.
