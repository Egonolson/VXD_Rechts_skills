# E-Rechnung, GoBD und Billing

## Rechnungsstamm

| Feld | Inhalt | Status |
| --- | --- | --- |
| Rechnungsnummer |  | offen |
| Mandant |  | offen |
| Aktenzeichen |  | offen |
| Leistungszeitraum |  | offen |
| Umsatzsteuerlogik | Inland / EU / Drittland / Reverse Charge / befreit | offen |
| Format | PDF / XRechnung / ZUGFeRD | offen |
| Export | DATEV / CSV / manuell | offen |

## Leistungspositionen

| Datum | Fee Earner | Workstream | Tätigkeit | Dauer | Satz | Betrag | Narrative | Beleg |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
|  |  |  |  |  |  |  |  |  |

## XRechnung-Datenblock

| Pflichtfeld | Wert | Quelle |
| --- | --- | --- |
| Buyer reference |  |  |
| Seller VAT ID |  |  |
| Invoice issue date |  |  |
| Tax point date |  |  |
| Payment terms |  |  |
| Line item net amount |  |  |
| VAT category |  |  |

## GoBD-Protokoll

- Rechnungsnummer fortlaufend und nicht doppelt vergeben.
- Jede Änderung protokolliert.
- Storno und Korrekturrechnung statt Überschreiben.
- Belege und Leistungsnachweise unveränderbar ablegen.
- XML/PDF/A-3 technisch separat validieren, bevor Versand als final gilt.
