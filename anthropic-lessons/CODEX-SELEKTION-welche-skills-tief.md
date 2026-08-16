# Codex-Selektion: Welche Skills sollen auf Anthropic-Tiefe gehen — und welche NICHT

Hi Codex — Tom hat Perplexity gebeten, dir vorzubereiten, **welche** Plugins/Skills aus seinem Repo `Klotzkette/claude-fuer-deutsches-recht` du auf die Anthropic-Median-Länge (~11.000 Bytes pro SKILL.md) heben sollst und welche du **bewusst kurz** lassen sollst.

**Lies das vor `CODEX-INSTRUKTION-skill-tiefe-boost.md` — diese Datei hier sagt dir, wo du das Werkzeug aus der Instruktion anwendest und wo nicht.**

---

## 0. Quelle zum Selbst-Nachschauen

Anthropic hat den Maßstab gesetzt, an dem wir uns orientieren. Schau dir das gerne nochmal selbst an, vor allem die langen Skills aus `litigation-discovery`, `transactional-ma` und `legal-research`:

- **Repo:** https://github.com/anthropics/claude-for-legal
- **Empfohlen zum Lesen:**
  - `litigation-discovery/skills/` (z. B. `privilege-log/SKILL.md`, `deposition-prep/SKILL.md`)
  - `transactional-ma/skills/` (z. B. `disclosure-schedules/SKILL.md`, `closing-checklist/SKILL.md`)
  - `legal-research/skills/` (z. B. `westlaw-search/SKILL.md`, `case-brief/SKILL.md`)
  - `cold-start-interview/` (Profil-Aufbau)
  - `customize/` (punktuelle Profil-Updates)
  - `matter-workspace/` (Mandat als Ordner-Workspace)
  - `managed-agent-cookbooks/` (Tool-Scope, Agent-Skeleton)
- **`.mcp.json`** in jedem Plugin-Root (Westlaw, CourtListener, iManage, Slack, Google Drive, Everlaw, Trellis)

**Anthropic-Kontext bewusst halten:** Anthropic schreibt für US-Großkanzleien und Inhouse-Counsel mit IT-Setup, MCP-Server-Anbindung an Westlaw / iManage / Slack und Mandanten, die einen Skill ein ganzes Mandantenleben lang begleiten. Lange Skills lohnen sich dort, weil der Skill viele Wochen lang dieselben Workflows triggert.

**Daraus folgt für uns:** Lange Skills lohnen sich bei uns nur dort, wo der Kontext vergleichbar ist:

1. **Großkanzlei / Inhouse-Counsel (deutsch).** Plugins, die Wirtschaftsanwälte in Großmandaten begleiten — M&A, Kartell, IP, Bank/Kapitalmarkt, Konzern-Compliance.
2. **MCP-anbindbar.** Plugins, bei denen extern eine Datenbank/API mitspielt (juris, beck-online, Lobbyregister, Handelsregister, Markenregister, ESEF/EDGAR-Pendants, Bundesanzeiger).
3. **Mandatsbegleitend.** Plugins, die ein einzelnes Mandat über Wochen/Monate/Jahre tragen — Insolvenzverfahren, Bauprozess, große Compliance-Fälle, Patentstreit, IPO-Prep.
4. **Komplexe Mehr-Schritt-Workflows.** Plugins, bei denen ein Skill viele Sub-Schritte hat (Due Diligence, Disclosure Schedules, Closing Checklist deutscher Lesart).

**Daraus folgt auch: Lange Skills lohnen sich NICHT** bei Verbraucher-Selbsthilfe (Fluggast, Mahnbescheid, Bürgergeld-Widerspruch), kurzen Tool-Skills (PDF-Stempel, Anlagen-Sortierung, Zitierprüfer), Studentenn-Hilfen (Hausarbeit, Methodenlehre) und Berufsrechts-Mikro-Skills (kurze Email-Umformulierung, Schriftform-Check).

---

## 1. Selektions-Logik in einem Satz

> **Wenn ein Skill einen Wirtschaftsanwalt durch ein Mandat führt, das mehrere Wochen läuft, externe Datenbanken nutzt und mehrere Sub-Workflows hat → Anthropic-Tiefe. Sonst NICHT.**

---

## 2. Plugins in 4 Klassen

### Klasse A — VOLLAUSBAU auf Anthropic-Median (~11k Bytes pro Skill, Pflicht-Sektionen aus `CODEX-INSTRUKTION-skill-tiefe-boost.md`)

**Diese Plugins sind genau das, wofür Anthropic-Skills gebaut sind: Großkanzlei, Inhouse, MCP-anbindbar, mandatsbegleitend.**

| Plugin | Warum Klasse A | MCP-Andocken (Beispiele) |
|---|---|---|
| `grosskanzlei-corporate-ma` | M&A-Großmandate, DD-Workflows | Handelsregister, Bundesanzeiger, juris, beck-online |
| `mittelstand-corporate-ma` | Mittelstands-M&A, dieselben Workflows kleiner | wie oben |
| `corporate-kanzlei` | Konzern-Compliance, Gesellschaftsrecht | Handelsregister, Lobbyregister |
| `gesellschaftsrecht` | HGB/AktG/GmbHG-Tiefe, Streit + Beratung | Handelsregister, juris |
| `gesellschaftsrecht-legal-english` | Cross-Border M&A, Englisch-Pflicht | EDGAR-Pendants, EUR-Lex |
| `kartellrecht-marktabgrenzung-pruefung` | Kartellverfahren, Marktabgrenzung, Fusionsanmeldung | Bundeskartellamt, EU-Kommission, EUR-Lex |
| `fachanwalt-handels-gesellschaftsrecht` | Großmandats-Fachanwaltschaft | wie Gesellschaftsrecht |
| `fachanwalt-bank-kapitalmarktrecht` | IPO-Prep, Prospektprüfung, MaRisk | BaFin, EUR-Lex, juris |
| `fachanwalt-internationales-wirtschaftsrecht` | Cross-Border, Schiedsverfahren | EUR-Lex, UNCITRAL, juris |
| `fachanwalt-it-recht` | Großmandats-IT-Verträge, SaaS, Cloud, KI-VO | EUR-Lex, juris, BfDI |
| `fachanwalt-gewerblicher-rechtsschutz` | Marken-/Patent-Streit, einstweilige Verfügung | DPMA, EUIPO, EPA |
| `gewerblicher-rechtsschutz` | Tiefe IP-Verfahren | DPMA, EUIPO, EPA |
| `patentrecht` | Patentstreit, FTO, Verletzungsanalyse | DPMA, EPA, esp@cenet |
| `patentrecherche` | Mehrtägige Recherchen | DPMA, EPA, esp@cenet |
| `markenrecht-fashion-luxus` | Mandatsbegleitende Markenstrategie | DPMA, EUIPO, WIPO |
| `fachanwalt-urheber-medienrecht` | Verlagsverträge, Lizenz, Filmrecht | DPMA, EUIPO |
| `datenschutzrecht` | Konzern-DSGVO, DPIA, Auftragsverarbeiter-Ketten | EDSA, BfDI, juris |
| `dsa-dma-digitalregulierung` | Plattform-Compliance, sehr vielschichtig | EUR-Lex, EU-Kommission |
| `ki-vo-ai-act-pruefer` | KI-VO-Risikoklassifizierung, mandatsbegleitend | EUR-Lex, EU-AI-Office |
| `ki-governance` | Konzern-KI-Strategie, Policies | wie KI-VO |
| `ki-richtlinie-kanzleien` | Kanzlei-interne KI-Compliance | BRAK, BeurkG |
| `regulatorisches-recht` | Multi-regulatorisch | EUR-Lex, juris, BMJ |
| `aussenwirtschaft-zoll-sanktionen` | Embargo-Listen, Dual-Use, lang-laufende Compliance | BAFA, EU-Sanktions-Map, Zoll |
| `geldwaeschepraevention-aml-kyc` | Konzern-AML, sehr lang | BaFin, FIU, EU-Lex |
| `insolvenzrecht` | Mandatsbegleitend (Insolvenzverfahren = Monate/Jahre) | Insolvenz-Portal, Schuldnerverzeichnis |
| `insolvenzverwaltung` | Verwalter-Workflow, jahrelang | wie Insolvenzrecht |
| `insolvenzplan-starug-planwerkstatt` | StaRUG/Insolvenzplan, mandatsbegleitend | wie Insolvenzrecht |
| `krisenfrueherkennung-starug` | Frühphase-Restrukturierung | Bundesanzeiger, juris |
| `fortbestehensprognose` | Mandatsbegleitend, mehrere Wochen | wie oben |
| `fachanwalt-insolvenz-sanierungsrecht` | Fachanwaltschaft auf höchstem Level | wie Insolvenz |
| `fachanwalt-bau-architektenrecht` | Großbauprozess, jahrelang | VHB, juris, OLG-Portal |
| `fachanwalt-medizinrecht` | Großverfahren, Konzern-Compliance, Krankenhauskette | KBV, GBA, juris |
| `fachanwalt-verwaltungsrecht` | Verwaltungsstreit-Großverfahren | juris, Verwaltungsportale |
| `fachanwalt-vergaberecht` | Vergabeverfahren, mandatsbegleitend | TED, VK-Bund, BMI |
| `fachanwalt-steuerrecht` | Konzern-Betriebsprüfung, mandatsbegleitend | juris, BMF, BFH |
| `steuerrecht-anwalt-und-berater` | Mandatsbegleitend, viele Sub-Workflows | wie oben |
| `verfassungsrecht` | Verfassungsbeschwerde, GG-Prüfung | BVerfG, juris |
| `europarecht-kompass` | EU-Verfahren, Vorlageverfahren | EUR-Lex, EuGH |
| `lobbyregister-bundestag` | Compliance-Workflow für Verbände/Kanzleien | Lobbyregister, BT-Drucksachen |
| `legistik-werkstatt` | Gesetzgebungsverfahren-Begleitung | BT-Drucksachen, BR-Drucksachen |
| `energierecht` | Konzern-Energierecht, EnWG, EEG | BNetzA, juris |
| `umweltrecht` | Großverfahren, BImSchG, UVPG | UBA, juris |
| `bav-strategie-konzern` | bAV-Konzern-Mandat, mandatsbegleitend | aba, juris |
| `forschungszulage-antragstellung` | Antrag über Monate | BSFZ, juris |
| `dfg-foerderantrag` | Förderantrag über Monate | DFG, juris |
| `nda-abgleich` | Bei Großmandaten häufig, viele Klausel-Varianten | iManage-Pendant |
| `vertragsrecht` | Großvertrags-DD, Klausel-Bibliothek | iManage-Pendant, beck-online |
| `wandeldarlehen-lebenszyklus` | Wandeldarlehen über Laufzeit begleiten | Handelsregister, BaFin |
| `gesellschaftsgruender` | Gründung über Wochen, mehrstufig | Handelsregister, IHK |
| `prozessrecht` | ZPO-Tiefe, Prozessstrategie | juris, beck-online, OLG-Portale |
| `urteilsbauer-relationsmacher` | Spruchkörper-Methodik, Tiefe gewollt | juris, dejure.org |
| `aktenauszug-gerichtsverfahren` | Großakten, mandatsbegleitend | iManage-Pendant |
| `aktenaufbereiter-strafrecht` | Großverfahren-Strafrecht | wie oben |
| `strafzumessung` | Großverfahren, mehrere Verhandlungstage | juris, BGH |
| `fachanwalt-strafrecht` | Wirtschaftsstrafrecht, Großverfahren | juris, BGH, dejure |
| `fachanwalt-arbeitsrecht` | Konzern-Arbeitsrecht, Tarif, Betriebsverfassung | juris, BAG, dejure |
| `fachanwalt-erbrecht` | Großnachlässe, mandatsbegleitend | Grundbuch, Handelsregister, juris |
| `kindeswohlgefaehrdung-eilantrag` | Vermögensauseinandersetzung Hochvermögen | juris, BGH |
| `fachanwalt-versicherungsrecht` | Großschäden, Konzern-D&O | BaFin, juris |
| `fachanwalt-transport-speditionsrecht` | Großschäden, internationale Verträge | CMR, juris |
| `fachanwalt-miet-wohnungseigentumsrecht` | Großbestand, mandatsbegleitend | juris, OLG-Portale |
| `immobilienrechtspraxis` | Großtransaktionen, Bestandsverwaltung | Grundbuch, juris |
| `verkehr-infrastrukturrecht` | Großprojekte | juris, BVerwG |
| `normenkontrolle-bauleitplanung` | Normenkontrollverfahren, mandatsbegleitend | juris, BVerwG, BauGB-Portal |
| `produktrecht` | Konzern-Produkt-Compliance, ProdHaftG, ProdSG | EUR-Lex, BAuA |
| `kanzlei-builder-hub` | Kanzlei-Setup-Workflow, mehrstufig | iManage-Pendant |
| `kanzlei-allgemein` | Kanzleiverwaltung, mandatsbegleitend | iManage-Pendant |
| `common-law-kompass` | Cross-Border, lange Skills sinnvoll | Westlaw, CourtListener |

**Klasse A = 70 Plugins.**

---

### Klasse B — TEILAUSBAU (Median ~7k Bytes, nur 5 statt 10 Pflicht-Sektionen)

**Plugins, die zwar fachlich tief sind, aber nicht das Großkanzlei-Mandatsleben-Setup haben. Tiefer als heute, aber nicht volles Anthropic-Maß.**

| Plugin | Warum Klasse B |
|---|---|
| `fachanwalt-agrarrecht` | Fach tief, aber kleines Mandantenuniversum |
| `fachanwalt-sportrecht` | Spezialgebiet, mandatsbegleitend nur teils |
| `fachanwalt-migrationsrecht` | Tief, aber meist Einzelfall, nicht "Großkanzlei-Inhouse" |
| `fachanwalt-sozialrecht` | Tief, aber meist Einzelfall — siehe `selbstvertreter-sozialgericht` |
| `fachanwalt-verkehrsrecht` | Meist Einzelfall, aber Wirtschaftsstrafrecht-Schnittmenge |
| `bereicherungs-und-anfechtungsrecht-pruefer` | Eher Tool, aber dogmatisch komplex |
| `betreuungsrecht` | Mandatsbegleitend, aber meist nicht Großkanzlei |
| `mietrecht` | Mandatsbegleitend, aber meist nicht Großkanzlei |
| `weg-hausverwaltung` | Mandatsbegleitend, kleiner Skalen |
| `arbeitsrecht` | Eher Mittelstand, MCP-anbindbar (Konzern-Schnittmenge) |
| `arbeitszeugnis-analyse` | Tool, aber tief |
| `zwangsvollstreckung` | Mandatsbegleitend, mittlere Tiefe |
| `zwangsverwaltung-zvg` | Mandatsbegleitend, mittlere Tiefe |
| `forderungsmanagement-klagewerkstatt` | Workflow-Plugin, mittlere Tiefe |
| `insolvenzforderungsanmeldungspruefung` | Workflow, mittlere Tiefe |
| `liquiditaetsplanung` | Mandatsbegleitend Insolvenz-Vorfeld |
| `tabellenreview-3d` | Tool für Insolvenz, mittlere Tiefe |
| `audit` / `audits` | Workflow, mittlere Tiefe |
| `barrierefreiheit-web-checker` | Tool, mandatsbegleitend nur teils |
| `phishing-vorfall-pruefer` | IR-Workflow, mittlere Tiefe |
| `berufsrecht-ki-vertragspruefung` | KI-VO-nah, aber spezifischer Use-Case |
| `gewerblicher-rechtsschutz` (falls Klasse A schon: ignorieren) | — |
| `subsumtions-pruefer` | Tool, dogmatisch tief |
| `methodenlehre-buergerliches-recht` | Studium/Methodik, eher Klasse C — Grenzfall |

**Klasse B = ~25 Plugins.**

---

### Klasse C — KURZ LASSEN (NICHT aufpumpen, bleibt bei Median ~4k oder weniger)

**Plugins, deren Wert kurz, präzise und tool-artig zu sein, ist. Aufpumpen würde sie schlechter machen, nicht besser.**

#### C1 — Selbstvertreter / Verbraucher / Schnellhilfe
Diese Skills brauchen den **Laien-Lese-Tempo**. Lang ist hier ein Bug, nicht ein Feature.
- `fluggastrechte`
- `selbstvertreter-amtsgericht`
- `selbstvertreter-sozialgericht`
- `nachbarschaftsstreit-pruefer`
- `mandantenanfragen-assistent`
- `rechtsberatungsstelle`
- `strafbefehl-verteidiger` (Grenzfall — wenn Tom es will, Klasse B)
- `verkehrsowi-verteidiger`
- `einfache-leichte-sprache-jura`

#### C2 — Kurze Tool-Skills (Ein-Klick-Werkzeuge)
- `anlagen-zu-schriftsaetzen`
- `zitierweise-deutsches-recht`
- `vertragsausfueller`
- `schriftform-und-textform-bgb`
- `email-umformulierer-berufsrecht`
- `meinungspruefer`
- `nda-abgleich` (Grenzfall — wenn als Großkanzlei-Tool gedacht: Klasse A; wenn Tool: C2) — **siehe Klasse A für Großkanzlei-Variante**
- `word-legal-ai-plugin-and-skill-for-german-lawyers`
- `bgb-at-pruefer`
- `jveg-kostenpruefer`
- `memorandums-ersteller`

#### C3 — Studium / Methodik / Sprachhilfe
- `jurastudium`
- `hausarbeitenmacher`
- `methodenlehre-buergerliches-recht` (Grenzfall, siehe Klasse B)
- `juristische-sprache-deutsch-als-zweitsprache`

#### C4 — Übersichten / Verzeichnisse
- `uebersicht-fachanwaltschaften`
- `verlagsredaktion`

**Klasse C = ~22 Plugins.**

---

### Klasse D — UNKLAR / Tom-Entscheidung

Falls du beim Bearbeiten unsicher bist, **NICHT raten** — leg den Plugin-Namen in `anthropic-lessons/UNCLEAR-SKILLS.md` ab mit kurzer Begründung. Tom entscheidet pro Plugin.

Kandidaten, die du Tom vorlegen solltest:
- `strafbefehl-verteidiger` — Selbsthilfe oder Anwalts-Tool?
- `methodenlehre-buergerliches-recht` — Studium oder Praxis?
- `nda-abgleich` — Großkanzlei-Klausel-Bibliothek oder Schnell-Check?
- `verwaltete-agentenrezepte` — Meta-Plugin, Sonderfall

---

## 3. Was bedeutet "Klasse A" konkret?

Für jeden Klasse-A-Skill gilt der **volle Pflicht-Sektionen-Katalog** aus `CODEX-INSTRUKTION-skill-tiefe-boost.md`:

1. Zweck (mit Großkanzlei-Kontext, nicht generisch)
2. Wann nutzen / wann NICHT
3. Voraussetzungen (welche MCP-Quellen sollten dranhängen — auch wenn noch nicht implementiert)
4. Workflow (mandatsbegleitend, mit Sub-Schritten über Tage/Wochen)
5. Prüfraster (mit konkreten Normen, BGH-/EuGH-Leitentscheidungen)
6. Output (mit Hand-Off-Tags `[juris]`, `[beck-online — verify]`, `[BGH-Urteil — verlinkt]`)
7. Quellen (NUR dejure.org, openjur.de, BGH/BVerfG/BAG/BFH/BVerwG, EUR-Lex, juris — keine BeckRS-Blind, kein anwalt24)
8. Hand-Off (welcher Skill kommt danach, mit konkretem Skill-Namen)
9. Was dieser Skill NICHT macht
10. Berufsrecht (BRAO, FAO, BORA, Verschwiegenheit, Interessenkonflikt — kein Boilerplate, sondern Skill-spezifisch)

**Median-Ziel:** ~11.000 Bytes pro SKILL.md
**Untergrenze:** 8.500 Bytes
**Obergrenze:** 16.000 Bytes (Anthropic-Max ~49k, aber das übertreiben wir nicht)

---

## 4. Was bedeutet "Klasse B" konkret?

Reduzierter Pflicht-Katalog (5 von 10):
1. Zweck
2. Wann / wann NICHT
3. Workflow (mit Sub-Schritten)
4. Prüfraster (Normen + Leitentscheidungen)
5. Hand-Off

**Median-Ziel:** ~7.000 Bytes pro SKILL.md
**Untergrenze:** 5.500 Bytes
**Obergrenze:** 9.000 Bytes

Berufsrecht, Quellen-Tags, "Was NICHT" optional, wenn fachlich passend.

---

## 5. Was bedeutet "Klasse C" konkret?

**Bleib unter 4.500 Bytes pro SKILL.md.**

Wenn ein Skill in einem Klasse-C-Plugin schon heute > 4.500 Bytes hat: **kürzen**, nicht erweitern. Wenn er bei 1.500–4.500 liegt: **lassen**.

Was du in Klasse C nur kurz erwähnst:
- Ein-Satz-Zweck
- 2–3 Bullet-Schritte
- Ein-Satz-Hinweis "ersetzt keine Rechtsberatung"

**NICHT** machen in Klasse C:
- Lange BGH-Zitate
- Berufsrechts-Boilerplate
- 10 Pflicht-Sektionen
- MCP-Quellenlisten

---

## 6. Reihenfolge der Bearbeitung (PR-Plan für Codex)

Tom will **viele kleine PRs auf dem Seitenbranch**, keinen Mammut-PR. Vorgeschlagene Reihenfolge:

### Phase 1 — Klasse A (70 Plugins, ~25 PRs, je 2–4 Plugins)
1. PR-A01: M&A-Kern (`grosskanzlei-corporate-ma`, `mittelstand-corporate-ma`, `corporate-kanzlei`)
2. PR-A02: Gesellschaftsrecht (`gesellschaftsrecht`, `gesellschaftsrecht-legal-english`, `fachanwalt-handels-gesellschaftsrecht`)
3. PR-A03: Kartell & Bank (`kartellrecht-marktabgrenzung-pruefung`, `fachanwalt-bank-kapitalmarktrecht`)
4. PR-A04: IT / KI / Datenschutz (`fachanwalt-it-recht`, `datenschutzrecht`, `dsa-dma-digitalregulierung`)
5. PR-A05: KI-VO-Familie (`ki-vo-ai-act-pruefer`, `ki-governance`, `ki-richtlinie-kanzleien`)
6. PR-A06: IP-Kern (`fachanwalt-gewerblicher-rechtsschutz`, `gewerblicher-rechtsschutz`, `markenrecht-fashion-luxus`)
7. PR-A07: Patent (`patentrecht`, `patentrecherche`)
8. PR-A08: Medien / Urheber (`fachanwalt-urheber-medienrecht`)
9. PR-A09: Außenwirtschaft / AML (`aussenwirtschaft-zoll-sanktionen`, `geldwaeschepraevention-aml-kyc`)
10. PR-A10: Insolvenzkern (`insolvenzrecht`, `insolvenzverwaltung`, `insolvenzplan-starug-planwerkstatt`)
11. PR-A11: Krise / Fortbestehen (`krisenfrueherkennung-starug`, `fortbestehensprognose`, `fachanwalt-insolvenz-sanierungsrecht`)
12. PR-A12: Bau / Medizin / Verwaltung (`fachanwalt-bau-architektenrecht`, `fachanwalt-medizinrecht`, `fachanwalt-verwaltungsrecht`)
13. PR-A13: Vergabe / Steuer (`fachanwalt-vergaberecht`, `fachanwalt-steuerrecht`, `steuerrecht-anwalt-und-berater`)
14. PR-A14: Verfassung / Europa (`verfassungsrecht`, `europarecht-kompass`)
15. PR-A15: Politik-Compliance (`lobbyregister-bundestag`, `legistik-werkstatt`)
16. PR-A16: Energie / Umwelt (`energierecht`, `umweltrecht`)
17. PR-A17: bAV / Förderanträge (`bav-strategie-konzern`, `forschungszulage-antragstellung`, `dfg-foerderantrag`)
18. PR-A18: Vertrag / NDA (`nda-abgleich`, `vertragsrecht`, `wandeldarlehen-lebenszyklus`, `gesellschaftsgruender`)
19. PR-A19: Prozess (`prozessrecht`, `urteilsbauer-relationsmacher`)
20. PR-A20: Strafrecht (`aktenauszug-gerichtsverfahren`, `aktenaufbereiter-strafrecht`, `strafzumessung`, `fachanwalt-strafrecht`)
21. PR-A21: Arbeit / Erb / Familie (`fachanwalt-arbeitsrecht`, `fachanwalt-erbrecht`, `kindeswohlgefaehrdung-eilantrag`)
22. PR-A22: Versicherung / Transport (`fachanwalt-versicherungsrecht`, `fachanwalt-transport-speditionsrecht`)
23. PR-A23: Immobilien (`fachanwalt-miet-wohnungseigentumsrecht`, `immobilienrechtspraxis`)
24. PR-A24: Verkehr / Infrastruktur / Bauleitplanung (`verkehr-infrastrukturrecht`, `normenkontrolle-bauleitplanung`)
25. PR-A25: Rest A (`produktrecht`, `kanzlei-builder-hub`, `kanzlei-allgemein`, `common-law-kompass`, `regulatorisches-recht`)

### Phase 2 — Klasse B (~25 Plugins, ~6 PRs)
26. PR-B01–B06: je 4–5 Plugins

### Phase 3 — Klasse C-Aufräumung (nur wenn Skills > 4.500 Bytes)
27. PR-C01: Kürzungen Selbstvertreter / Verbraucher
28. PR-C02: Kürzungen Tool-Skills

### Phase 4 — Optional
29. PR-OPT-01: Cold-Start-Prototyp (für Klasse-A-Plugins)
30. PR-OPT-02: Matter-Workspace-Konvention (`mandate/<slug>/mandat.md`)
31. PR-OPT-03: Source-Attribution-Tags `[juris]`, `[beck-online — verify]`

---

## 7. Pro PR

- Branch-Name: `anthropic-tiefe-boost-A01-ma-kern`, `…-A02-gesellschaft`, …
- Basis-Branch: `anthropic-patterns-experimente` (NICHT `main`)
- PR-Titel: `[Tiefe-Boost A01] M&A-Kern: grosskanzlei-corporate-ma, mittelstand-corporate-ma, corporate-kanzlei`
- PR-Body: Vorher/Nachher-Statistik (Bytes pro Skill, durchschnittliche Länge), kurz auflisten welche Pflicht-Sektionen ergänzt wurden
- KEIN Merge nach `main` — Tom merged manuell, wenn er fertig ist
- Validatoren müssen grün bleiben — die ASCII-Regeln aus der Haupt-Instruktion strikt einhalten

---

## 8. Fallback / Unklar

Wenn du beim Bearbeiten eines Plugins unsicher bist (z. B. Plugin sieht aus wie Klasse C, hat aber Großkanzlei-Komponenten):

1. Lege den Plugin-Namen mit kurzer Begründung in `anthropic-lessons/UNCLEAR-SKILLS.md` ab
2. Überspringe das Plugin im aktuellen PR
3. Mach mit dem nächsten weiter

Tom geht die UNCLEAR-Liste später durch.

---

## 9. Lies auch das

- **`CODEX-INSTRUKTION-skill-tiefe-boost.md`** — das eigentliche Werkzeug (Pflicht-Sektionen, ASCII-Regeln, Berufsrechts-Pattern, Vorher/Nachher-Beispiel)
- **`00-analyse-anthropic-vs-uns.md`** — was Anthropic anders macht und warum

---

## 10. TL;DR

- **70 Plugins** kriegen Anthropic-Tiefe (Klasse A — Großkanzlei, MCP, mandatsbegleitend)
- **25 Plugins** kriegen mittleren Boost (Klasse B)
- **22 Plugins** bleiben kurz oder werden gekürzt (Klasse C — Verbraucher, Tools, Studium)
- **Schau dir das Anthropic-Repo selbst an:** https://github.com/anthropics/claude-for-legal
- **Alles auf `anthropic-patterns-experimente`-Seitenbranch, NICHT nach `main` mergen**
