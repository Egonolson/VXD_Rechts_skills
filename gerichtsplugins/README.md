# gerichtsplugins — Legal-AI-Plugins für Gerichte

> **Experimentelle Plugin-Sammlung für den möglichen Einsatz von KI an deutschen Gerichten.**
> Capability-Experiment. Keine Produktivempfehlung.

## Was ist das hier?

Dieser Ordner bündelt 15 Plugins, die typische gerichtliche Rollen abbilden: Amtsrichter in Zivil-, Straf-, Insolvenz- und Registersachen, Landgerichts-, Verwaltungs-, Finanz-, Sozial-, Arbeits- und Familienrichter, ein Plugin für die Verfassungsbeschwerde am BVerfG, zwei Plugins für Staatsanwaltschaft und Amtsanwaltschaft sowie ein Plugin zur Relationstechnik im Zivilrecht. Jedes Plugin enthält einen vollständigen Werkstatt-Prompt, einen kompakten Schnellstart-Prompt, eine fiktive Testakte aus Richtersicht und je nach Plugin 10 bis 28 fachliche Skills. Im Zentrum stehen Vorbereitung und Aufbau einer richterlichen Entscheidung: Tenor, Sachverhalt, Entscheidungsgründe, Beweiswürdigung, Subsumtion. Die Plugins funktionieren auch ohne Plugin-Setup, weil Werkstatt- und Schnellstart-Markdown portabel sind.

Die richterliche Funktion ist eine besonders sensible Anwendung von KI. Deshalb steht dieser Ordner separat. Wir bilden hier die Werkzeuge ab, damit sichtbar wird, was technisch geht; die Frage, ob und wie das im Echtbetrieb rechtssicher genutzt werden kann, ist in jedem Gericht und in jedem Verfahren neu zu prüfen. Eine ausführliche rechtliche Einordnung zu KI-VO, DSGVO, Aktengeheimnis und Revisionssicherheit folgt unter "Wichtiger Hinweis vor Verwendung".

## Plugins in diesem Ordner

| Plugin | Rolle | README |
|---|---|---|
| `richter-amtsgericht-zivil` | Amtsrichter in Zivilsachen (Streitwert bis 10.000 Euro, sonstige Zuständigkeiten nach Paragraf 23 GVG) | [README](./richter-amtsgericht-zivil/README.md) |
| `richter-amtsgericht-straf` | Strafrichter oder Schöffengericht am Amtsgericht (Paragraf 24 GVG, Paragraf 25 GVG, Paragrafen 28-30 GVG) | [README](./richter-amtsgericht-straf/README.md) |
| `richter-amtsgericht-insolvenz-restrukturierung` | Insolvenzrichter oder Restrukturierungsrichter am Amtsgericht (Paragraf 2 InsO, Paragrafen 34 ff. StaRUG) | [README](./richter-amtsgericht-insolvenz-restrukturierung/README.md) |
| `richter-amtsgericht-handelsregister` | Registerrichter oder Rechtspfleger für Handelsregister, Genossenschaftsregister, Partnerschaftsregister, Vereinsregister | [README](./richter-amtsgericht-handelsregister/README.md) |
| `richter-landgericht-zivilkammer` | Vorsitzender oder Berichterstatter einer Zivilkammer (Paragraf 71 GVG, Streitwert ab 10.001 Euro; auch sonstige Zuständigkeiten Paragrafen 71-74 GVG) sowie zweite Instanz Berufung Paragraf 511 ZPO | [README](./richter-landgericht-zivilkammer/README.md) |
| `richter-landgericht-strafkammer` | Vorsitzender oder Berichterstatter einer großen oder kleinen Strafkammer (Paragraf 74 GVG, Paragraf 76 GVG); Schwurgericht Paragraf 74 Abs. 2 GVG | [README](./richter-landgericht-strafkammer/README.md) |
| `richter-verwaltungsgericht` | Verwaltungsrichter als Einzelrichter oder Kammer (Paragrafen 4-6 VwGO) | [README](./richter-verwaltungsgericht/README.md) |
| `richter-finanzgericht` | Finanzrichter als Einzelrichter oder Senat (Paragraf 5 FGO) | [README](./richter-finanzgericht/README.md) |
| `richter-sozialgericht` | Sozialrichter als Einzelrichter oder Kammer (Paragrafen 12, 31 SGG); mit ehrenamtlichen Richtern in mündlicher Verhandlung | [README](./richter-sozialgericht/README.md) |
| `richter-arbeitsgericht` | Arbeitsrichter als Vorsitzender einer Kammer (mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreis) Paragraf 16 ArbGG | [README](./richter-arbeitsgericht/README.md) |
| `richter-familiengericht` | Familienrichter am Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG) für Ehe-, Kindschafts-, Unterhalts-, Versorgungsausgleichs-, Gewaltschutz- und sonstige Familiensachen nach FamFG | [README](./richter-familiengericht/README.md) |
| `richter-bverfg-verfassungsbeschwerden` | Wissenschaftlicher Mitarbeiter oder Berichterstatter in einer Kammer beider Senate des Bundesverfassungsgerichts (Paragrafen 93a-93d BVerfGG) | [README](./richter-bverfg-verfassungsbeschwerden/README.md) |
| `staatsanwaltschaft-amtsanwaltschaft` | Staatsanwalt oder Amtsanwalt (Paragrafen 141 ff. GVG, Paragrafen 152 ff. StPO) mit 28 Skills zu Anklage, Ermittlung, Durchsuchung, Vernehmung, Adhäsion, Opferschutz, Wiederaufnahme und EuHb | [README](./staatsanwaltschaft-amtsanwaltschaft/README.md) |
| `staatsanwaltschaft-praxis-einstieg` | Praxiseinstieg für Staatsanwälte und Amtsanwälte: Aktenführung, Verfügungslehre, tägliche Arbeitsabläufe | [README](./staatsanwaltschaft-praxis-einstieg/README.md) |
| `relationstechnik-zivilrecht` | Jeder Zivilrechtler (Richter, Referendar, Anwalt) der eine große Relation aufbauen will | [README](./relationstechnik-zivilrecht/README.md) |

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehörde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsätzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschläge produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstützung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschläge.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte dürfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewährleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behördlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Sämtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Systeme auf absehbare Zeit nicht produktiv einsetzen können — das wissen wir. Der Wert dieser Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in jedem freigegebenen Werkzeug mit ausreichendem Kontextfenster und Datei-Upload, etwa einem behördlich freigegebenen On-Premise-System. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt- oder Schnellstart-Prompt zusammen mit weiteren Hausinstruktionen dort einsetzen, soweit das jeweilige Hausrecht und die Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Aufbau jedes Plugins

- `.claude-plugin/plugin.json` — Plugin-Manifest
- `README.md` — Plugin-Beschreibung mit vollständigem Vorspruch
- `<sprechender-name>-werkstatt.md` — vollständiger Arbeits-Prompt, portabel (Dateiname trägt den fachlichen Plugin-Begriff)
- `<sprechender-name>-schnellstart.md` — Kompaktversion bis 7.500 Zeichen (Dateiname trägt den fachlichen Plugin-Begriff)
- `skills/` — 10 fachliche Skills in den Richter-Plugins, 20 fachliche Skills in der Relationstechnik, jeweils zusätzlich ein Schnellstart-Skill
- `testakte/README.md` — fiktive Testakte aus Richtersicht

## Warum dieser Ordner separat steht

Die richterliche Funktion ist eine besonders sensible Anwendung von KI. Aktengeheimnis, richterliche Unabhängigkeit, Art. 22 DSGVO und KI-VO setzen einen strengen Rahmen. Wir bilden hier die Werkzeuge ab, **damit wir wissen, was geht**. Die Frage, ob und wie das im Echtbetrieb rechtssicher genutzt werden kann, ist in jedem Gericht und in jedem Verfahren neu zu prüfen.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
