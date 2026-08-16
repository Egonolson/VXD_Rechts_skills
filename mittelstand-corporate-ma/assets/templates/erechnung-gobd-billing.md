# E-Rechnung, GoBD und Billing

## Rechnungsstamm

| Feld | Inhalt | Status |
| --- | --- | --- |
| Rechnungsnummer |  | offen, vor Versand eindeutig vergeben |
| Mandant |  | offen, mit Engagement Letter abgleichen |
| Aktenzeichen |  | offen, Kanzleiakte pruefen |
| Leistungszeitraum |  | offen, Timesheet-Schnitt abgleichen |
| Umsatzsteuerlogik | Inland / EU / Drittland / Reverse Charge / befreit | offen, steuerliche Behandlung freigeben |
| Format | PDF / XRechnung / ZUGFeRD | offen, Empfaengeranforderung pruefen |
| Export | DATEV / CSV / manuell | offen, Buchhaltungsweg festlegen |

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
