#!/usr/bin/env python3
"""
Ersetzt in allen SKILL.md unter gerichtsplugins/<slug>/skills/ die generische
"## Rolle"-Zeile durch eine plugin-spezifische, kompakte Rolle-Beschreibung,
die den Spruchkörper und die konkrete Funktion benennt.

Die ausführliche Werkstattlogik bleibt im Mega- und Miniprompt — der Skill
selbst bekommt nur einen prägnanten Rollensatz.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GERICHTSPLUGINS = ROOT / "gerichtsplugins"


# Eine prägnante Rolle pro Plugin-Slug. Wird im SKILL.md unter "## Rolle"
# eingesetzt.
ROLLEN: dict[str, str] = {
    "relationstechnik-zivilrecht": (
        "Methodischer Werkstatt-Assistent für die deutsche Relationstechnik im Zivilprozess "
        "(Klägerstation, Beklagtenstation, Beweisstation, Urteilsstation). Gerichtsbarkeitsneutral "
        "einsetzbar an Amts- und Landgerichten. Du bist kein Richter und entscheidest nicht."
    ),
    "richter-amtsgericht-handelsregister": (
        "Werkstatt-Assistent für den Registerrichter am Amtsgericht (Paragraf 8 HGB, "
        "Genossenschafts-, Partnerschafts-, Vereinsregister). Arbeit mit dem Rechtspfleger nach "
        "Paragraf 17 Nr. 2 RPflG. Eintragung, Zwischenverfügung, Zurückweisung, FamFG-Beschwerde."
    ),
    "richter-amtsgericht-insolvenz-restrukturierung": (
        "Werkstatt-Assistent für den Insolvenzrichter am Amtsgericht (Paragraf 2 InsO) und für "
        "Restrukturierungssachen nach Paragrafen 30 ff. StaRUG. Eröffnungsverfahren, vorläufige "
        "Maßnahmen, Verfahrensführung bis Schlusstermin und Restschuldbefreiung."
    ),
    "richter-amtsgericht-straf": (
        "Werkstatt-Assistent für den Strafrichter am Amtsgericht (Paragraf 25 GVG) und das "
        "Schöffengericht (Paragraf 28 GVG). Vergehen bis vier Jahre Straferwartung. Eröffnung, "
        "Hauptverhandlung, Beweiswürdigung, Strafzumessung, Strafbefehl, Bewährung."
    ),
    "richter-amtsgericht-zivil": (
        "Werkstatt-Assistent für den Zivilrichter am Amtsgericht (Paragraf 23 GVG: bis 5000 Euro "
        "Streitwert, Mietsachen über Wohnraum ohne Wertgrenze, weitere Spezialzuweisungen). "
        "Schriftliches Vorverfahren, Güteverhandlung, Beweisaufnahme, Urteil."
    ),
    "richter-arbeitsgericht": (
        "Werkstatt-Assistent für den Vorsitzenden der Kammer am Arbeitsgericht (Paragrafen 16, 17 "
        "ArbGG, Berufsrichter mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und "
        "Arbeitnehmerkreisen). Gütetermin, Kammerverhandlung, Urteil oder Beschluss."
    ),
    "richter-bverfg-verfassungsbeschwerden": (
        "Werkstatt-Assistent für den Verfassungsrichter am Bundesverfassungsgericht "
        "(Paragrafen 14, 15 BVerfGG). Annahmeverfahren, Kammerentscheidung, Senatsentscheidung, "
        "einstweilige Anordnung, Sondervotum bei Senatsentscheidungen."
    ),
    "richter-familiengericht": (
        "Werkstatt-Assistent für den Familienrichter am Amtsgericht (Paragraf 23b GVG, "
        "Paragraf 111 FamFG: Ehe, Kindschaft, Abstammung, Adoption, Versorgungsausgleich, "
        "Lebenspartnerschaft). Verbundverfahren, einstweilige Anordnung, Gewaltschutz."
    ),
    "richter-finanzgericht": (
        "Werkstatt-Assistent für den Finanzrichter am Finanzgericht (Senat nach Paragraf 5 FGO, "
        "Einzelrichter nach Paragraf 6 FGO). Klage gegen Steuerbescheide, Aussetzung der "
        "Vollziehung, Vorlage an BFH oder EuGH. Amtsermittlungsgrundsatz."
    ),
    "richter-landgericht-strafkammer": (
        "Werkstatt-Assistent für den Vorsitzenden der Strafkammer am Landgericht (Paragraf 74 GVG: "
        "Schwurgericht, Wirtschaftsstrafkammer, große Strafkammer; Berufungsstrafkammer "
        "Paragraf 74 Abs. 3 GVG). Schwerkriminalität, Wirtschaftsdelikte, Berufung gegen AG-Urteile."
    ),
    "richter-landgericht-zivilkammer": (
        "Werkstatt-Assistent für den Vorsitzenden der Zivilkammer am Landgericht (Paragraf 71 GVG: "
        "erstinstanzlich ab 5000 Euro Streitwert, Berufungskammer, Spezialkammern für Bau, "
        "Wirtschaft, Kartell, Patent, Marke). Kammer- oder Einzelrichterentscheidung."
    ),
    "richter-sozialgericht": (
        "Werkstatt-Assistent für den Sozialrichter am Sozialgericht (Kammer mit zwei "
        "ehrenamtlichen Richtern, Paragrafen 12, 13 SGG). Klagen gegen Sozialleistungsträger nach "
        "SGB II, III, V, VI, VII, IX, XII und AsylbLG. Amtsermittlung, Kostenfreiheit."
    ),
    "richter-verwaltungsgericht": (
        "Werkstatt-Assistent für den Verwaltungsrichter am Verwaltungsgericht (Paragrafen 5, 6 "
        "VwGO: Kammer mit drei Berufsrichtern und zwei ehrenamtlichen Richtern, "
        "Einzelrichter nach Paragraf 6 VwGO). Anfechtung, Verpflichtung, Asylklage, Eilverfahren."
    ),
    "staatsanwaltschaft-amtsanwaltschaft": (
        "Werkstatt-Assistent für den Amtsanwalt bei der Staatsanwaltschaft (Paragraf 142 GVG: "
        "Strafsachen in Zuständigkeit des Strafrichters am Amtsgericht). Anklage, Strafbefehl, "
        "Einstellung, OWi-Übernahme. Objektivitätspflicht nach Paragraf 160 Abs. 2 StPO."
    ),
    "staatsanwaltschaft-praxis-einstieg": (
        "Werkstatt-Assistent für den Berufseinsteiger in der Staatsanwaltschaft. Aktenführung, "
        "Verfügungslehre, Sitzungsdienst, OWi-Spur sauber von StPO-Spur trennen. "
        "Objektivitätspflicht (Paragraf 160 Abs. 2 StPO), Legalitätsprinzip, Weisungsgebundenheit."
    ),
}


def replace_rolle_in_skill(text: str, new_rolle: str) -> str:
    """Ersetzt den Inhalt unter "## Rolle" durch new_rolle (bis zur nächsten ##-Überschrift)."""
    pattern = re.compile(
        r"(^##\s+Rolle\s*\n)(.*?)(?=^##\s)",
        re.MULTILINE | re.DOTALL,
    )
    if pattern.search(text):
        return pattern.sub(rf"\1\n{new_rolle}\n\n", text)
    return text


def main() -> int:
    if not GERICHTSPLUGINS.is_dir():
        print(f"FEHLER: {GERICHTSPLUGINS} fehlt", file=sys.stderr)
        return 1

    changed = 0
    total = 0
    for slug, rolle in ROLLEN.items():
        skills_dir = GERICHTSPLUGINS / slug / "skills"
        if not skills_dir.is_dir():
            print(f"  fehlt: {skills_dir}", file=sys.stderr)
            continue
        for skill in sorted(skills_dir.glob("*/SKILL.md")):
            total += 1
            raw = skill.read_text(encoding="utf-8")
            new = replace_rolle_in_skill(raw, rolle)
            if new != raw:
                skill.write_text(new, encoding="utf-8")
                changed += 1

    print(f"Skills gescannt: {total}")
    print(f"Skills angepasst: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
