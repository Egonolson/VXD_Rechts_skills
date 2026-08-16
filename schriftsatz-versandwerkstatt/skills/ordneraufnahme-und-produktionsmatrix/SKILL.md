---
name: ordneraufnahme-und-produktionsmatrix
description: "Liest einen vorhandenen Schriftsatz- und Anlagenordner vor jeder Rückfrage, erkennt Hauptdokument, Fassungen, bereits verwendete Anlagenkennungen, Dubletten, fehlende Belege und nicht unterstützte Formate und liefert eine konkrete Produktionsmatrix mit Quelle, Ziel-PDF, Nummer, Status und einzig noch blockierenden Entscheidungen."
---

# Ordneraufnahme und Produktionsmatrix

## 1. Aktivierung

Nutze diesen Skill bei einem Ordner, ZIP-Inhalt oder Dateisatz, dessen Rollen noch nicht vollständig klar sind. Er ist die erste Station von `versandmappe-endfertigen`, kein allgemeines Aktenanalysewerkzeug.

## 2. Aufnahme ohne Vorinterview

1. Originalpfad, Dateiname, Erweiterung, Bytes, Änderungsdatum und Hash erfassen.
2. Verzeichnisse wie `alt`, `entwurf`, `final`, `anlagen`, `versandt` und `intern` als Fassungsindikatoren behandeln.
3. DOCX, ODT, RTF oder PDF mit Schriftsatzkopf, Anträgen und Signaturzeile als Hauptdokument-Kandidaten markieren.
4. Anlagenverweise im Hauptdokument mit Dateinamen abgleichen.
5. inhaltsgleiche Dateien anhand Hash gruppieren; keine Datei löschen.
6. passwortgeschützte Archive, verschlüsselte PDFs, eingebettete Objekte und proprietäre Container als Stop-Befund markieren.

## 3. Fassungsentscheidung

Bei mehreren Schriftsatzfassungen nicht nach jedem Dokument fragen. Lege eine Rangfolge vor:

1. ausdrücklich als final oder unterschriftsreif bezeichnete Fassung,
2. jüngste Fassung mit vollständigem Rubrum und Anträgen,
3. versandte oder signierte Fassung nur als Vergleich, niemals stillschweigend überschreiben.

Frage einmal: `Soll [Dateiname, Stand] als Hauptdokument endgefertigt werden?` Nur bei gleichwertigen Kandidaten ist diese Rückfrage zwingend.

## 4. Produktionsmatrix

| Rolle | Quelle | Fassung | erkannte Kennung | Ziel | Konverter | Kontrolle | Befund |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hauptdokument | Pfad | Datum/Hash | keine | PDF | Office oder direkt | visuell | Status |
| Anlage | Pfad | Datum/Hash | B 3 | PDF | Bild/Office/E-Mail | visuell | Status |

## 5. Lückenlogik

- Im Schriftsatz genannt, aber keine Datei vorhanden: `stop`.
- Datei mit Anlagenkennung, aber nicht im Schriftsatz genannt: `prüfen`, nicht automatisch versenden.
- Nummernlücke: `stop`, bis Fortsetzung oder bewusste Lücke bestätigt ist.
- Dublette: eine Versandfassung vorschlagen, alle Quellen im internen Log behalten.
- Dateityp nicht unterstützt: Quellanwendung und erforderlichen Export nennen.

## 6. Übergabe

Liefere Produktionsmatrix, Konfliktliste und höchstens zwei gebündelte Rückfragen. Übergib anschließend ohne erneute Inventur an `hauptdokument-pdf-endfertigen` und `anlagen-konvertieren-und-sichtpruefen`.
