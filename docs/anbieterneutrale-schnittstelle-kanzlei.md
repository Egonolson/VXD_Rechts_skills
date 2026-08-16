# Anbieterneutrale Schnittstelle für eine Kanzlei-Arbeitsoberfläche

Stand: Juli 2026

Diese Anleitung richtet sich an eine kleine Kanzlei, die die im Repository enthaltenen Arbeitsabläufe über eine andere, vertraglich freigegebene Modellschnittstelle nutzen möchte. Sie beschreibt einen technisch vorsichtigen Einrichtungs- und Abnahmeweg. Sie bestätigt weder einen Anbieter noch die berufs- oder datenschutzrechtliche Zulässigkeit eines konkreten Betriebsmodells.

## 1. Das richtige Anschlussmodell wählen

Vor der Einrichtung ist zu klären, welcher der drei Wege tatsächlich unterstützt wird. Eine Menübezeichnung oder Eingabemaske darf nicht angenommen werden, nur weil sie in einer anderen Programmversion vorhanden war.

### 1.1 Direkte Schnittstellenmaske in der Cowork-Oberfläche

Dieser Weg kommt nur in Betracht, wenn die installierte Oberfläche eine dokumentierte Maske für einen eigenen Endpunkt oder ein verwaltetes Gateway anbietet. Typische Felder sind Endpunktadresse, Authentifizierungsart, Schlüssel, Modellkennung und erlaubte Zieladressen. Die Kanzlei übernimmt die Werte exakt aus der technischen Dokumentation des freigegebenen Anbieters.

Fehlt die Maske, heißt sie anders oder lässt sich der tatsächliche Datenweg nicht nachweisen, wird nicht durch Ausprobieren konfiguriert. Dann ist Weg 1.2 oder 1.3 zu wählen.

### 1.2 Verwaltetes Kanzlei-Gateway

Ein von der Kanzlei oder ihrem IT-Dienstleister verwaltetes Gateway sitzt zwischen Arbeitsoberfläche und Modellanbieter. Es kann Authentifizierung, Nutzerzuordnung, Kostenlimits, Protokollierung, Modellrouting und Sperrlisten zentral umsetzen. Dieser Weg ist für mehrere Mitarbeiter meist kontrollierbarer, setzt aber eine dokumentierte technische Freigabe voraus.

Die Arbeitsoberfläche erhält nur die Gateway-Adresse und einen dafür bestimmten Zugang. Der eigentliche Anbieterschlüssel bleibt im zentralen Geheimnisspeicher und wird nicht auf jedem Arbeitsplatz verteilt.

### 1.3 Markdown-Arbeitsablauf in einer anderen Oberfläche

Wenn die Cowork-Oberfläche keinen freigegebenen eigenen Endpunkt unterstützt, können Werkstatt- und Schnellstart-Prompts als Markdown-Dateien in einer anderen, freigegebenen Oberfläche verwendet werden. Dabei ist vorab zu prüfen, welche Dateizugriffe, Werkzeuge und dauerhaften Konfigurationen dort tatsächlich verfügbar sind. Ein reiner Textimport ersetzt keine Plugin-Funktion, die lokale Dateien lesen, Arbeitsprodukte speichern oder Werkzeuge ausführen muss.

## 2. Freigabeakte vor dem ersten technischen Test

Die Kanzlei legt eine kurze Freigabeakte an. Sie enthält mindestens:

1. Vertragspartner, Leistungsbeschreibung und Laufzeit.
2. Vereinbarung zur Auftragsverarbeitung, technische und organisatorische Maßnahmen und Unterauftragnehmer.
3. Datenstandorte, Supportzugriffe, Aufbewahrung, Löschung und Verwendung von Eingaben oder Ausgaben.
4. Geheimnisschutz, Rollen und Berechtigungen, Austrittsprozess und Schlüsselrotation.
5. Datenflussbild vom Kanzleiarbeitsplatz bis zum Modell und zurück.
6. Freigegebene Nutzergruppen, zulässige Datenklassen und untersagte Inhalte.
7. Verantwortliche Person für Technik, Datenschutz, Berufsrecht und fachliche Abnahme.

Ohne dokumentierte Freigabe wird nur mit vollständig erfundenen Daten getestet.

## 3. Konfigurationsblatt ausfüllen

Die technische Dokumentation des Anbieters wird in ein einheitliches Konfigurationsblatt übertragen. Werte werden nicht aus Beispielen eines anderen Anbieters abgeleitet.

| Feld | Einzutragender Wert | Kontrollfrage |
| --- | --- | --- |
| Anzeigename | interner, eindeutiger Name | Ist er für Mitarbeiter verständlich? |
| Endpunktadresse | vollständige Basisadresse mit Protokoll | Zeigt das Zertifikat auf die erwartete Domain? |
| Authentifizierung | dokumentiertes Header- oder Token-Schema | Wird der Schlüssel ausschließlich im vorgesehenen Feld gespeichert? |
| Modellkennung | freigegebene technische Kennung | Ist sie im Anbieterprotokoll sichtbar? |
| Erlaubte Hosts | nur erforderliche Domains | Sind Platzhalter und Wildcards vermieden? |
| Zeitlimit | vom Anbieter empfohlener Wert | Bricht eine hängende Anfrage kontrolliert ab? |
| Protokollierung | Umfang, Speicherort, Aufbewahrung | Werden Inhalte, Metadaten und Fehler getrennt behandelt? |
| Kostenlimit | Nutzer- oder Teamgrenze | Löst eine Überschreitung eine Sperre statt stiller Mehrkosten aus? |

## 4. Schlüssel sicher einrichten

Ein Schnittstellenschlüssel gehört weder in den Projektordner noch in Prompt-Dateien, Bildschirmfotos, E-Mails oder Support-Tickets. Bei einer grafischen Oberfläche wird ausschließlich der dafür vorgesehene geschützte Schlüsselspeicher verwendet. Bei einem verwalteten Gateway liegt der Hauptschlüssel im zentralen Geheimnisspeicher; Nutzer erhalten nur einen widerrufbaren Kanzleizugang.

Vor Freigabe werden folgende Punkte geprüft:

1. Schlüssel ist auf die erforderliche Schnittstelle und den notwendigen Umfang begrenzt.
2. Schlüssel ist einer Person, Rolle oder Kanzleigruppe zugeordnet.
3. Rotation, Widerruf und Notfallsperre sind dokumentiert.
4. Protokolle zeigen den Nutzer, aber nicht unkontrolliert den vollständigen Mandatsinhalt.
5. Ein ausgeschiedener Mitarbeiter verliert Zugang ohne Änderung an jedem einzelnen Projekt.

## 5. Verbindung mit erfundenen Daten abnehmen

Die Abnahme beginnt mit einem leeren Arbeitsordner und einem kurzen erfundenen Schreiben. Echte Mandatsunterlagen bleiben außerhalb des Tests.

### 5.1 Technischer Basistest

1. Oberfläche neu starten und nur das freigegebene Profil auswählen.
2. Einen neutralen Satz senden, der keine personenbezogenen Angaben enthält.
3. Im Gateway- oder Anbieterprotokoll Zeit, Nutzer, Modellkennung und Status prüfen.
4. Kontrollieren, dass der Aufruf nicht in einem anderen Konto oder an einem anderen Endpunkt erscheint.
5. Fehlerfall auslösen, etwa mit einem gesperrten Profil, und die verständliche Fehlermeldung prüfen.

### 5.2 Datei- und Plugin-Test

1. Ein einzelnes kleines Plugin installieren oder einen Schnellstart-Prompt als Markdown öffnen.
2. Einen Ordner mit zwei erfundenen PDF-Dateien bereitstellen.
3. Die Arbeitsoberfläche anweisen, vorhandene Unterlagen zuerst zu lesen und ein kurzes Fristenblatt zu erstellen.
4. Prüfen, welche Dateien tatsächlich gelesen und welche Ausgabedateien erzeugt wurden.
5. Sicherstellen, dass keine erneute Grundabfrage erfolgt, wenn die benötigten Angaben bereits in den Dateien stehen.
6. Erst nach erfolgreicher Abnahme weitere Plugins oder den vollständigen Marketplace freigeben.

## 6. Fachliche Abnahme eines Arbeitsprodukts

Ein technisch erfolgreicher Aufruf genügt nicht. Für jedes freigegebene Einsatzgebiet wird mindestens ein erfundener Fall mit Soll-Ergebnis bearbeitet. Die fachliche Abnahme prüft:

1. Tatsachen, Annahmen und fehlende Angaben sind getrennt.
2. Fristen, Zuständigkeit, Anträge und Beweislast werden sichtbar behandelt.
3. Normen und Entscheidungen sind mit verifizierbarer Quelle belegt oder ausdrücklich als zu prüfen markiert.
4. Das Arbeitsprodukt folgt der gewählten Rolle, etwa Mandantenschreiben, Vermerk oder Schriftsatzentwurf.
5. Anlagen, Dateinamen und Ausgabepfade sind nachvollziehbar.
6. Bei fehlenden Unterlagen stellt der Ablauf höchstens die entscheidenden Rückfragen und arbeitet ansonsten weiter.

## 7. Betrieb in einer kleinen Kanzlei

Für den Alltag genügt eine klare Rollenverteilung:

| Rolle | Aufgabe |
| --- | --- |
| Kanzleiinhaber | gibt Einsatzgebiete, Datenklassen und Kostenrahmen frei |
| IT-Verantwortlicher | pflegt Endpunkt, Schlüssel, Hosts, Updates und Notfallsperre |
| Datenschutzverantwortlicher | kontrolliert Vertrag, Datenfluss, Löschung und Betroffenenprozesse |
| Fachverantwortlicher | nimmt Arbeitsabläufe und Musterfälle fachlich ab |
| Nutzer | prüft Quellen, Tatsachen, Fristen und Endfassung vor Verwendung |

Mindestens vierteljährlich werden aktive Nutzer, Schlüssel, Anbieteränderungen, Protokolle, Kosten, Fehlermeldungen und neue Programmversionen kontrolliert. Nach einem größeren Update wird der Basistest wiederholt.

## 8. Störungen ohne Datenverlust behandeln

Wenn eine Anfrage hängt, mehrfach gesendet wird oder am falschen Endpunkt erscheint, wird der Vorgang abgebrochen. Der Nutzer startet nicht wiederholt denselben Auftrag mit echten Unterlagen.

Die Fehlerprüfung erfolgt in dieser Reihenfolge:

1. Status des freigegebenen Endpunkts und Internetverbindung.
2. Ablauf oder Sperre des Kanzleizugangs.
3. Schreibweise von Endpunktadresse und Modellkennung.
4. Zertifikat, Proxy und erlaubte Hosts.
5. Größen- oder Zeitlimit der Anfrage.
6. Anbieter- und Gateway-Protokoll anhand einer Vorgangskennung.

Bei unklarem Datenweg, unbekanntem Empfänger, offenem Schlüssel oder nicht erklärbarer Protokollabweichung bleibt das Profil gesperrt, bis die Ursache dokumentiert und der Schlüssel erforderlichenfalls ersetzt wurde.

## 9. Freigabevermerk

Vor der ersten Nutzung mit echten Mandatsdaten wird ein kurzer Vermerk unterzeichnet:

| Prüfschritt | Verantwortlich | Datum | Ergebnis |
| --- | --- | --- | --- |
| Vertrag und Datenfluss geprüft |  |  |  |
| Technischer Basistest bestanden |  |  |  |
| Datei- und Plugin-Test bestanden |  |  |  |
| Fachlicher Musterfall bestanden |  |  |  |
| Rollen und Notfallsperre eingerichtet |  |  |  |
| Einsatzgebiet und Datenklassen freigegeben |  |  |  |

Die Freigabe gilt nur für die dokumentierte Oberfläche, den dokumentierten Endpunkt, die freigegebene Modellkennung und die bezeichneten Arbeitsabläufe. Änderungen daran lösen eine erneute Prüfung aus.
