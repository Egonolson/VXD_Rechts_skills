# Robotik-Rechtsmatrix

## Leitfrage
Ein Roboter ist selten nur eine Maschine. Er kann zugleich Maschine, unvollständige Maschine, Sicherheitsbauteil, Produkt mit digitalen Elementen, KI-System, Hochrisiko-KI, Medizinprodukt, Verbraucherprodukt, Arbeitsmittel, Datenquelle, Cloud-Service und Vertragsbündel sein.

## Prüfblöcke

| Block | Kernfrage | Typische Dokumente | Anschluss-Skills |
| --- | --- | --- | --- |
| Produktrolle | Wer ist Hersteller, Anbieter, Integrator, Importeur, Händler, Betreiber oder Deployer? | Organigramm, Lieferkette, Labels, Verträge | `rollen-hersteller-anbieter-integrator`, `systemintegrator-als-hersteller` |
| Maschinenrecht | Ist es Maschine, unvollständige Maschine, Sicherheitsbauteil oder geänderte Maschine? | Risikobeurteilung, CE-Akte, Anleitung | `maschine-oder-unvollstaendige-maschine`, `wesentliche-veraenderung-digital` |
| KI-VO | Liegt ein KI-System oder Hochrisiko-KI vor? Wer ist Anbieter/Betreiber? | Zweckbestimmung, Modellkarte, Logs, QMS | `ki-vo-artikel-3-ki-system-robotik`, `ki-vo-artikel-6-hochrisiko-robotik` |
| Produkthaftung | War das Produkt im Zeitpunkt des Inverkehrbringens oder durch Updates fehlerhaft? | Incident Logs, Nutzererwartung, Warnhinweise | `produktfehler-verbrauchererwartung-robotik`, `beweislast-und-offenlegung-produkthaftung` |
| Datenschutz | Welche Sensor- und Telemetriedaten werden verarbeitet? | DSFA, TOMs, Löschkonzept, Betroffeneninfo | `datenschutz-kameras-und-sensorik`, `dsfa-fuer-robotik` |
| Cybersecurity | Ist es ein Produkt mit digitalen Elementen? Wie laufen Updates und Schwachstellenmeldungen? | SBOM, Patch-Policy, CVD-Prozess | `cra-produkt-mit-digitalen-elementen`, `vulnerability-disclosure-und-reporting` |
| Betrieb | Welche Pflichten treffen Betreiber und Beschäftigte? | Unterweisung, Wartungsplan, Betriebsanweisung | `arbeitsschutz-betrsichv-robotik`, `betreiber-mitverschulden-und-fehlbedienung` |
| Sektor | Medizin, Pflege, Haushalt, Logistik, Agrar, öffentlicher Raum? | Zweckbestimmung, Zulassung, Verträge | passende Sektor-Skills |

## Output-Standard
Jede belastbare Ausgabe enthält: Sachverhaltsannahmen, Rollenmatrix, Normenlandkarte, Risikoampel, offene Fragen, Belegliste, Quellencheck, empfohlene Anschluss-Skills und einen nächsten konkreten Schritt.
