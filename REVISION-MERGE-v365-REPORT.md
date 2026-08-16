# Revision und Merge v365.0.0 — Bericht

Stand: v365.0.0. Schwerpunkt: die 13 Gerichts-Plugins unter `gerichtsplugins/`. Die inhaltliche Anreicherung der 140 Skills (Anker-Rechtsprechung, Pruefungsschemata, Fallstricke, Tenor-Bausteine) war in v358 bis v364 vorbereitet; v365 ergaenzt die Korrektheits- und Sprachschicht, vereinheitlicht die Versionierung und verifiziert Struktur und Formalia.

## Was bei den Gerichts-Plugins gehoben wurde (eine Zeile je Plugin)

- `relationstechnik-zivilrecht` — Doppelpunkt-Formen entgendert; Stationenfolge und Tenor-/Urteilsbausteine der 20 Skills verifiziert (Klaeger-, Beklagten-, Beweisstation, Tenor, Tatbestand, Entscheidungsgruende, Nebenentscheidungen).
- `richter-amtsgericht-zivil` — Wertgrenze auf bis 10.000 Euro (Paragraf 23 GVG, Stand 2026) korrigiert; entgendert; Streitwert-, Beweis- und Urteilsskills verifiziert.
- `richter-amtsgericht-straf` — entgendert; Eroeffnung, Beweiswuerdigung, Strafzumessung, Strafbefehl verifiziert.
- `richter-amtsgericht-insolvenz-restrukturierung` — entgendert; InsO- und StaRUG-Skills verifiziert.
- `richter-amtsgericht-handelsregister` — entgendert; Register-, Firmen- und Loeschungsskills verifiziert.
- `richter-landgericht-zivilkammer` — Zustaendigkeit auf ab 10.001 Euro korrigiert; entgendert; grosse Relation und Berufungsskills verifiziert.
- `richter-landgericht-strafkammer` — entgendert; grosse und kleine Strafkammer, Maszregeln, Revision verifiziert.
- `richter-arbeitsgericht` — entgendert; Gueteverhandlung, Kuendigungsschutz, Beschlussverfahren verifiziert.
- `richter-verwaltungsgericht` — entgendert; Klagearten und Eilrechtsschutz verifiziert.
- `richter-finanzgericht` — entgendert; AdV, Schaetzung, Revisionszulassung verifiziert.
- `richter-sozialgericht` — entgendert; Amtsermittlung und einstweiliger Rechtsschutz verifiziert.
- `richter-familiengericht` — entgendert; Scheidung, Versorgungsausgleich, Sorge, Umgang, Unterhalt, Gewaltschutz verifiziert.
- `richter-bverfg-verfassungsbeschwerden` — entgendert; Annahmeverfahren, Subsidiaritaet, Grundrechtspruefung und Votum aus Sicht wissenschaftlicher Mitarbeiter verifiziert.

## Generisches Maskulinum

Die Gerichts-Plugins waren der verbliebene Bestand mit Doppelpunkt-Formen, nachdem das uebrige Repo bereits auf generisches Maskulinum umgestellt war. Vereinheitlicht: 346 Ersetzungen in 180 Dateien ueber 19 Rollenbegriffe (Amtsrichter, Berichterstatter, Einzelrichter, Vorsitzender, Rechtspfleger, wissenschaftlicher Mitarbeiter und weitere). Originalwortlaut zitierter Gerichtsentscheidungen blieb unangetastet. Verbleibende Doppelpunkt-Gender-Formen in `gerichtsplugins/`: keine.

## Was bei den Wertgrenzen gefixt wurde

Das Justizstandort-Staerkungsgesetz hat zum 01.01.2026 die Streitwertgrenze des Paragraf 23 Nummer 1 GVG von 5.000 Euro auf 10.000 Euro angehoben. Die Gerichts-Plugins fuehrten noch die alte Grenze. Korrigiert:

- Amtsgericht: bis 5.000 Euro auf bis 10.000 Euro (15 Stellen).
- Landgericht: ab 5.001 Euro auf ab 10.001 Euro (14 Stellen).
- Insgesamt 29 Ersetzungen in 28 Dateien.

Fallbetraege in Testakten (zum Beispiel Streitwert 3.500 Euro, Vertragssumme 645.000 Euro) blieben als Sachverhaltszahlen unveraendert. Die Berufungsbeschwer des Paragraf 511 Absatz 2 ZPO war in den Gerichts-Plugins nicht mit einem veralteten Wert von 600 Euro hinterlegt.

## Welche Aktenzeichen geprueft wurden

577 Rechtsprechungs-Verweise in `gerichtsplugins/` wurden auf Schema-Plausibilitaet geprueft (BGH "X ZR NNN/JJ" und Senatsschemata, BVerfG "N BvR NNNN/JJ", BAG "N AZR NNN/JJ", BSG "B N KR NN/JJ R", BFH, BVerwG). Alle gepruefften Verweise folgen einem plausiblen Aktenzeichen-Schema; erkennbare Leitentscheidungen sind korrekt zugeordnet (zum Beispiel BVerfG 1 BvR 400/51 Lueth, 1 BvR 536/72 Lebach, 1 BvR 435/68 Mephisto, 1 BvR 596/56 Apotheken-Urteil; BGH GSSt 1/17; BSG B 1 KR 32/18 R). Keine offensichtlich erfundenen Aktenzeichen gefunden. Hinweis nach der Quellenhygiene des Repos: Schema-Plausibilitaet ersetzt nicht die Einzel-Verifikation jedes Zitats an amtlicher oder frei zugaenglicher Quelle vor produktiver Verwendung.

## Verifikation

- Struktur aller 13 Plugins vollstaendig: README, plugin.json, MEGAPROMPT, MINIPROMPT, Skills (140 gesamt), Testakte.
- Pflicht-Disclaimer (KI-VO Artikel 6 Absatz 2 mit Anhang III Nummer 8 Buchstabe a, Artikel 6 Absatz 3, Artikel 49 Absatz 2, Artikel 22 DSGVO, Paragraf 353b StGB, Paragraf 43 DRiG, Schatten-KI-Ablehnung, Revisionssicherheit, eigene Gefahr) in jedem README vorhanden.
- Keine `_GERICHTE_EXPERIMENTAL`-Verweise mehr. Description-Laengen und Zeichenregeln in den Gerichts-Plugins ohne Verstoss. Keine doppelten H1-Ueberschriften.
- Repo-weiter Versions-Bump auf v365.0.0 (228 plugin.json, marketplace.json, README, SKILLS.md neu erzeugt).
