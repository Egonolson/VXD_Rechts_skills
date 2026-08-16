# Berufsrechtliche KI-Debatte 2025 — Arbeitslinien und Fundstellenlogik

Diese Referenz ist eine intern paraphrasierte Arbeitsunterlage. Sie ersetzt nicht Gesetz, Rechtsprechung, Kammerpraxis oder aktuelle Quellenprüfung. Sie soll verhindern, dass die Skills aus bloßem Bauchgefühl antworten.

## Normativer Kern

- § 43e BRAO erlaubt Dienstleisterzugriff auf Berufsgeheimnisse nur, soweit der Zugriff für die beauftragte Dienstleistung erforderlich ist.
- § 43e Abs. 3 BRAO verlangt Textform, Verschwiegenheitsverpflichtung, Belehrung über strafrechtliche Folgen, Zugriff nur nach Need-to-know und kontrollierte Subunternehmer.
- § 43e Abs. 4 BRAO verlangt bei Auslandsdienstleistungen einen vergleichbaren Geheimnisschutz; DSGVO-Transferinstrumente ersetzen diese Berufsrechtsprüfung nicht.
- § 43e Abs. 5 BRAO ist besonders zu prüfen, wenn ein Tool unmittelbar für ein konkretes Einzelmandat eingesetzt wird.
- § 203 StGB ist eigenständig zu prüfen. Berufsrechtliche Pflichtwidrigkeit und Strafbarkeit laufen nicht automatisch deckungsgleich.

## Arbeitslinien für KI-Outsourcing

### Consumer-Tool und gebundener Dienstleister trennen

Öffentlich zugängliche KI-Frontends ohne berufsspezifische Bindung sind für Mandatsgeheimnisse kein normaler Arbeitsort. Dort nur anonymisiert, abstrahiert oder synthetisch arbeiten. Anders kann es bei bewusst beauftragten Fach- oder Enterprise-Dienstleistern sein, wenn die gesamte §-43e-Kette tragfähig dokumentiert ist.

### Erforderlichkeit richtig verstehen

Die Prüfung fragt nicht abstrakt, ob eine Kanzlei KI nutzen darf oder ob die anwaltliche Arbeit auch manuell möglich wäre. Sie fragt, ob der konkrete Zugriff auf die konkreten Geheimnisse für die beauftragte Dienstleistung in dieser Kanzleiorganisation erforderlich und verhältnismäßig begrenzt ist.

### No-Training als harter Vertragsbaustein

Mandatsdaten dürfen nicht in allgemeines Training, Fine-Tuning, Produktverbesserung, Promptdatenbanken oder Benchmarking abfließen, wenn dafür keine eigene tragfähige Grundlage besteht. Gleiches gilt funktional für Telemetrie, Supportzugriffe und Logdaten mit Inhaltsbezug.

### Verschlüsselung praktisch statt symbolisch

Verschlüsselung, Transport- und Speichersicherheit, Zugriffskontrolle und Protokollierung sind zentrale TOM. Eine Architektur, bei der der Anbieter die beauftragte KI-Dienstleistung technisch gar nicht mehr erbringen kann, ist aber nicht automatisch der einzig denkbare Maßstab. Entscheidend ist die risikogerechte, vertraglich und technisch kontrollierte Zugriffsbeschränkung.

### Kanzleiinfrastruktur und Einzelmandats-Tool trennen

Ein allgemein freigegebenes Kanzleitool ist anders zu behandeln als ein für ein bestimmtes Mandat individuell eingesetztes Tool. Bei Mandatsbezug können Aufklärung, Einwilligung oder zumindest eine gesonderte Mandatsentscheidung erforderlich werden.

### Schatten-KI ernst nehmen

Private Accounts, Smartphone-Apps, Übersetzer, Diktattools, PDF-Dienste und Meeting-Transkription sind oft gefährlicher als das offiziell geprüfte Tool. Eine Kanzlei braucht deshalb Toolinventar, Freigabeliste, Schulung, technische Leitplanken und Incident Response.

## KI-VO-Schnittstellen

- Art. 4 KI-VO verlangt eine realistische KI-Kompetenzorganisation für Personen, die im Auftrag der Kanzlei mit KI arbeiten.
- Interne anwaltliche Entwurfsnutzung ist anders zu bewerten als Mandantenchatbot, Website, Newsletter oder Marketinginhalt.
- Art. 50 KI-VO muss für Chatbots und veröffentlichte KI-Inhalte gesondert geprüft werden; menschliche redaktionelle Verantwortung und anwaltliche Endkontrolle sind zu dokumentieren.
- Eine Kanzlei ist nicht automatisch Anbieterin des zugrunde liegenden Modells. Eigene APIs, White-Label-Systeme oder Mandantenportale können aber zusätzliche Rollenfragen auslösen.

## Output-Regel für Skills

Jeder Skill soll am Ende mindestens eines liefern:

- Toolklassifikation
- §-43e-Erforderlichkeitsvermerk
- Vertragslückenliste
- No-Training-/Telemetrie-Prüfung
- Drittstaat- und Subunternehmermatrix
- KI-VO-Rollenvermerk
- Team-Policy gegen Schatten-KI
- anwaltlichen Endkontrollvermerk
