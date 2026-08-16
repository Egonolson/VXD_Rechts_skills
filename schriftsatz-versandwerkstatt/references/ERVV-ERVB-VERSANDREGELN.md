# Form- und Technikregeln für die Versandmappe

Stand: 14. Juli 2026. Vor einem fristgebundenen Versand sind Normtext, aktuelle Bekanntmachung und gerichtliche Sonderhinweise erneut zu prüfen.

## 1. Zweck

Diese Referenz hält ausschließlich formale und technische Versandregeln fest. Sie bewertet weder Anträge noch Sachvortrag, Beweisangebote oder materielles Recht.

## 2. Dokumentformat

ERVV Paragraf 2 verlangt grundsätzlich PDF. TIFF darf zusätzlich übermittelt werden, wenn bildliche Darstellungen in PDF nicht verlustfrei wiedergegeben werden können. Das Versandwerkzeug erzeugt PDF-Dateien und meldet aktive Inhalte, Verschlüsselung, leere Seiten oder kaum auslesbaren Text als Stop- oder Warnbefund.

Amtlicher Normtext: https://www.gesetze-im-internet.de/ervv/__2.html

## 3. ERVB 2025

Die ERVB 2025 vom 16. Juli 2025 begrenzt eine Nachricht auf höchstens 1.000 Dateien und 200 Megabyte. Ein Dateiname darf einschließlich Endung höchstens 90 Zeichen lang sein. Erlaubt sind Buchstaben des deutschen Alphabets einschließlich Umlauten und scharfem S, Ziffern, Unterstrich und Minus sowie der Punkt als Trenner vor der Dateiendung.

Dieses Plugin verwendet bewusst ein strengeres Kanzleiprofil: ausschließlich ASCII, Wörter mit Unterstrich verbunden und höchstens 80 Zeichen einschließlich `.pdf`. Das ist eine interne Robustheitsregel, keine Behauptung über die gesetzliche Höchstgrenze.

Amtliche Bekanntmachung: https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf

## 4. Signaturroute

Für Zivilverfahren bestimmt ZPO Paragraf 130a Absatz 3 zwei alternative Formwege:

1. qualifizierte elektronische Signatur der verantwortenden Person oder
2. Signatur durch die verantwortende Person und Einreichung auf einem sicheren Übermittlungsweg.

Anlagen zu vorbereitenden Schriftsätzen benötigen nach Satz 2 keine eigene Signatur. Entsprechende Vorschriften bestehen insbesondere in ArbGG Paragraf 46c, SGG Paragraf 65a, VwGO Paragraf 55a, FGO Paragraf 52a und StPO Paragraf 32a. Vor der Freigabe muss die für das Verfahren geltende Vorschrift ausgewählt werden.

Amtlicher ZPO-Normtext: https://www.gesetze-im-internet.de/zpo/__130a.html

Das Plugin behandelt den Signaturweg als Stop-Punkt, wenn verantwortende Person, tatsächlicher Versender oder verwendetes Postfach nicht feststehen. Es erzeugt und prüft selbst keine qualifizierte elektronische Signatur.

## 5. Eingang und Störung

ZPO Paragraf 130a Absatz 5 knüpft den Eingang an die Speicherung auf der für den Empfang bestimmten Einrichtung des Gerichts und sieht eine automatisierte Bestätigung vor. ZPO Paragraf 130d regelt die Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit. Das Plugin ersetzt weder die Prüfung der jeweiligen Verfahrensordnung noch die Glaubhaftmachung einer Störung.

Amtlicher Normtext: https://www.gesetze-im-internet.de/zpo/__130d.html

## 6. Nicht automatisierbare Freigaben

1. Verantwortender Anwalt und tatsächlicher Versender bestätigen die gewählte Signaturroute.
2. Jede konvertierte Seite wird visuell mit der Quelle verglichen.
3. Empfänger, Aktenzeichen, Dokumentart und Frist werden im Versanddialog erneut geprüft.
4. Erst die positive automatisierte Eingangsbestätigung beendet die Ausgangskontrolle.
5. Das Werkzeug löst niemals einen Versand aus und löscht niemals eine Frist.
