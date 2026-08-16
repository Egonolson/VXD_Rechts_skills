#!/usr/bin/env python3
"""Pfaendungsrechner nach Tabelle 1.7.2026.

Berechnet den pfaendbaren Anteil des Nettoarbeitseinkommens nach
Pfaendungsfreigrenzenbekanntmachung 2026 (BGBl 2026 I Nr. 80, 26.3.2026).
Gilt vom 1.7.2026 bis 30.6.2027.

Grundlagen:
- Paragraf 850c Abs. 1 ZPO  Grundfreibetrag
- Paragraf 850c Abs. 2 ZPO  Erhoehungsbetraege fuer Unterhaltsberechtigte
- Paragraf 850c Abs. 3 ZPO  Quoten 3/10, 5/10, 7/10 und Vollpfaendungsgrenze
- Paragraf 850c Abs. 5 ZPO  Aufrundung auf naechsten vollen Zehner minus 1 Cent

Quelle: BGBl 2026 I Nr. 80 und amtliche Tabelle im Anhang.

Eckwerte (Tabelle 1.7.2026; BGBl 2026 I Nr. 80 vom 26.3.2026):
- Grundfreibetrag (0 Unterhaltspflichtige): 1.587,40 EUR / Monat
- Erhoehung 1. unterhaltsberechtigte Person: 597,42 EUR
- Erhoehung je weitere Person (bis 5. Person): 332,83 EUR
- Vollpfaendungsgrenze: 4.866,30 EUR (darueber alles pfaendbar)

Die Berechnung folgt der Methode der amtlichen Tabelle: Netto wird auf den
naechsten vollen 10-EUR-Schritt nach unten abgerundet (Paragraf 850c Abs. 5 ZPO);
vom Ueberschuss ueber den nach Tabelle erhoehten Freibetrag wird der pfaendbare
Anteil mit unterhaltsabhaengiger Quote berechnet.

Benutzung:
    python3 pfaendungsrechner.py --netto 2500 --unterhalt 1
    python3 pfaendungsrechner.py --netto 3200 --unterhalt 2 --privileg
    python3 pfaendungsrechner.py --tabelle  (gibt Tabelle 0-4 Unterhalt aus)
"""

from __future__ import annotations

import argparse
import datetime as _dt
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP

# --------------------------------------------------------------------------- #
# Konstanten Tabelle 1.7.2026
# --------------------------------------------------------------------------- #

TABELLE_GUELTIG_AB = _dt.date(2026, 7, 1)
TABELLE_GUELTIG_BIS = _dt.date(2027, 6, 30)

GRUNDFREIBETRAG = Decimal("1587.40")          # Paragraf 850c Abs. 1 ZPO
ERHOEHUNG_ERSTE_PERSON = Decimal("597.42")    # Paragraf 850c Abs. 2 Satz 1 ZPO
ERHOEHUNG_WEITERE_PERSON = Decimal("332.83")  # Paragraf 850c Abs. 2 Satz 2 ZPO
VOLLPFAENDUNGSGRENZE = Decimal("4866.30")     # Paragraf 850c Abs. 3 Satz 3 ZPO

# Quoten gemaess Paragraf 850c Abs. 3 ZPO (auf den den Grundfreibetrag
# uebersteigenden Teil bis zur Vollpfaendungsgrenze):
# - 0 Unterhaltspflichten:  3/10 unpfaendbar -> 7/10 pfaendbar
# - 1 Unterhaltspflicht:    3/10 + 2/10 unpfaendbar -> 5/10 pfaendbar
# - 2 Unterhaltspflichten:  6/10 unpfaendbar -> 4/10 pfaendbar
# - 3 Unterhaltspflichten:  7/10 unpfaendbar -> 3/10 pfaendbar
# - 4 Unterhaltspflichten:  8/10 unpfaendbar -> 2/10 pfaendbar
# - 5 Unterhaltspflichten:  9/10 unpfaendbar -> 1/10 pfaendbar
# Ab der 6. Person erfolgt keine automatische weitere Reduktion mehr;
# Anpassung durch das Vollstreckungsgericht nach Paragraf 850f ZPO.

QUOTE_GLAEUBIGER_NACH_UP: dict[int, Decimal] = {
    0: Decimal("0.7"),
    1: Decimal("0.5"),
    2: Decimal("0.4"),
    3: Decimal("0.3"),
    4: Decimal("0.2"),
    5: Decimal("0.1"),
}

# P-Konto-Sockel nach Paragraf 899 Absatz 1 ZPO: Grundfreibetrag auf den
# naechsten vollen Zehner aufgerundet. Erhoehungen folgen Paragraf 902 ZPO.
P_KONTO_SOCKEL = Decimal("1590.00")
P_KONTO_ERHOEHUNG_ERSTE = Decimal("597.42")
P_KONTO_ERHOEHUNG_WEITERE = Decimal("332.83")


# --------------------------------------------------------------------------- #
# Berechnung
# --------------------------------------------------------------------------- #


@dataclass
class Berechnungsergebnis:
    netto: Decimal
    unterhaltspflichten: int
    freibetrag: Decimal
    ueber_freibetrag: Decimal
    pfaendbar: Decimal
    schuldneranteil: Decimal
    privilegiert: bool
    hinweise: list[str]

    def als_text(self) -> str:
        zeilen = [
            "PFAENDUNGSBERECHNUNG (Tabelle 1.7.2026)",
            "",
            f"Netto:                  {self.netto:>10} EUR / Monat",
            f"Unterhaltspflichten:    {self.unterhaltspflichten:>10}",
            f"Freibetrag:             {self.freibetrag:>10} EUR",
            f"Ueber Freibetrag:       {self.ueber_freibetrag:>10} EUR",
            f"Pfaendbar / Monat:      {self.pfaendbar:>10} EUR",
            f"Schuldneranteil:        {self.schuldneranteil:>10} EUR",
            f"Privileg Paragraf 850d: {'ja' if self.privilegiert else 'nein':>10}",
            "",
            f"Tabelle gueltig bis:    {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')}",
        ]
        if self.hinweise:
            zeilen.append("")
            zeilen.append("Hinweise:")
            for h in self.hinweise:
                zeilen.append(f"- {h}")
        return "\n".join(zeilen)


def _cent(value: Decimal) -> Decimal:
    """Auf Cent runden, wie es die Werte der amtlichen Tabelle ausweisen."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def gueltigkeits_warnung(heute: _dt.date | None = None) -> str | None:
    """Gibt eine Warnung zurueck, wenn die aktuelle Tabelle bald ablaeuft
    oder bereits abgelaufen ist. Pflicht-Selbstcheck nach § 850c Abs. 4 ZPO
    (jaehrliche Anpassung der Pfaendungsfreigrenzen)."""
    today = heute if heute is not None else _dt.date.today()
    # Die jaehrliche Bekanntmachung knuepft an den Tabellenstart an,
    # nicht an das Kalenderjahr des Tagesdatums (sonst wird bei spaeter
    # Aktualisierung auf das falsche Veroeffentlichungsjahr verwiesen).
    fehlendes_jahr = TABELLE_GUELTIG_AB.year + 1
    if today > TABELLE_GUELTIG_BIS:
        return (
            f"WARNUNG: Pfaendungstabelle ist seit {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')} "
            f"abgelaufen. Aktuelles Tagesdatum {today.strftime('%d.%m.%Y')}. "
            f"Die hier hinterlegten Eckwerte (Stand 1.7.2026) duerfen nicht mehr verwendet werden. "
            f"Pflicht: Pfaendungsfreigrenzenbekanntmachung {fehlendes_jahr} (BGBl. I) abrufen "
            f"und Modul aktualisieren. Verwendung alter Werte = Pfaendungsfehler mit Aufhebungsrisiko."
        )
    abstand = (TABELLE_GUELTIG_BIS - today).days
    if 0 <= abstand <= 30:
        return (
            f"HINWEIS: Pfaendungstabelle laeuft am {TABELLE_GUELTIG_BIS.strftime('%d.%m.%Y')} ab "
            f"(in {abstand} Tagen). Naechste Bekanntmachung des BMJ zu § 850c Abs. 4 ZPO "
            f"vorbereiten und Modul aktualisieren."
        )
    return None


def berechne(
    netto: Decimal | float | str,
    unterhaltspflichten: int = 0,
    privileg_850d: bool = False,
    selbstbehalt: Decimal | float | str | None = None,
) -> Berechnungsergebnis:
    """Berechne den pfaendbaren Anteil des Arbeitseinkommens.

    Parameters
    ----------
    netto
        Monatliches Nettoeinkommen in EUR.
    unterhaltspflichten
        Anzahl unterhaltsberechtigter Personen.
    privileg_850d
        True, wenn die Forderung eine privilegierte Unterhaltsforderung
        nach Paragraf 850d ZPO ist. Selbstbehalt wird dann vom Gericht
        festgesetzt; das Werkzeug zeigt nur einen Richtwert.
    selbstbehalt
        Vom Vollstreckungsgericht festgesetzter oder fuer den konkreten Antrag
        belastbar ermittelter Selbstbehalt fuer Paragraf 850d ZPO. Bei einer
        privilegierten Forderung ist die Angabe zwingend.
    """
    netto_d = Decimal(str(netto))
    if netto_d < 0:
        raise ValueError("Netto darf nicht negativ sein")
    if unterhaltspflichten < 0:
        raise ValueError("Unterhaltspflichten darf nicht negativ sein")

    hinweise: list[str] = []

    if privileg_850d:
        if selbstbehalt is None:
            raise ValueError(
                "Bei Paragraf 850d ZPO muss der konkret anzusetzende "
                "Selbstbehalt mit --selbstbehalt angegeben werden."
            )
        selbst = Decimal(str(selbstbehalt))
        if selbst < 0:
            raise ValueError("Selbstbehalt darf nicht negativ sein")
        freibetrag = selbst
        ueber = max(netto_d - freibetrag, Decimal("0"))
        pfaendbar = _cent(ueber)
        schuldneranteil = _cent(netto_d - pfaendbar)
        hinweise.append(
            "Paragraf 850d ZPO: Selbstbehalt wird vom Vollstreckungsgericht "
            "festgesetzt; die Berechnung verwendet den ausdrücklich angegebenen Betrag."
        )
        return Berechnungsergebnis(
            netto=_cent(netto_d),
            unterhaltspflichten=unterhaltspflichten,
            freibetrag=_cent(freibetrag),
            ueber_freibetrag=_cent(ueber),
            pfaendbar=pfaendbar,
            schuldneranteil=schuldneranteil,
            privilegiert=True,
            hinweise=hinweise,
        )

    # Regulaere Berechnung Paragraf 850c ZPO
    # Freibetrag fuer die Anzeige (Sockel + Tabellen-Erhoehungen bis 5 Personen).
    freibetrag = GRUNDFREIBETRAG
    if unterhaltspflichten >= 1:
        freibetrag += ERHOEHUNG_ERSTE_PERSON
    if unterhaltspflichten >= 2:
        bis_fuenf = min(unterhaltspflichten, 5) - 1
        freibetrag += ERHOEHUNG_WEITERE_PERSON * bis_fuenf

    if unterhaltspflichten > 5:
        hinweise.append(
            "Tabelle stuft bis 5 Unterhaltspflichtige; ab der 6. Person erfolgt "
            "Anpassung durch das Vollstreckungsgericht (Paragraf 850f ZPO). "
            "Werkzeug rechnet hier mit Tabellenwerten fuer 5 Personen."
        )

    # Oberhalb der Vollpfaendungsgrenze ist der Mehrbetrag centgenau voll
    # pfaendbar. Nur der verbleibende Tabellenbetrag wird nach Paragraf 850c
    # Absatz 5 ZPO auf volle zehn Euro abgerundet.
    voll_pfaendbar = max(netto_d - VOLLPFAENDUNGSGRENZE, Decimal("0"))
    tabellen_netto = min(netto_d, VOLLPFAENDUNGSGRENZE)
    tabellen_netto_abger = (
        (tabellen_netto / Decimal("10")).to_integral_value(rounding=ROUND_DOWN)
        * Decimal("10")
    )
    ueber_tabelle = max(tabellen_netto_abger - freibetrag, Decimal("0"))
    ueber_gesamt = max(netto_d - freibetrag, Decimal("0"))

    # Pfaendbarkeitsquote im Tabellenbereich nach Unterhaltsstaffel
    # Paragraf 850c Abs. 3 Saetze 1 und 2 ZPO.
    quote_glaeubiger = QUOTE_GLAEUBIGER_NACH_UP[min(unterhaltspflichten, 5)]

    if voll_pfaendbar > 0:
        pfaendbar = _cent(ueber_tabelle * quote_glaeubiger + voll_pfaendbar)
        hinweise.append(
            f"Netto liegt ueber der Vollpfaendungsgrenze {VOLLPFAENDUNGSGRENZE} EUR; "
            "darueber 100 Prozent pfaendbar."
        )
    else:
        pfaendbar = _cent(ueber_tabelle * quote_glaeubiger)

    schuldneranteil = _cent(netto_d - pfaendbar)

    return Berechnungsergebnis(
        netto=_cent(netto_d),
        unterhaltspflichten=unterhaltspflichten,
        freibetrag=_cent(freibetrag),
        ueber_freibetrag=_cent(ueber_gesamt),
        pfaendbar=pfaendbar,
        schuldneranteil=schuldneranteil,
        privilegiert=False,
        hinweise=hinweise,
    )


def p_konto_freibetrag(unterhaltspflichten: int = 0) -> Decimal:
    """Sockelbetrag Paragraf 850k ZPO inkl. Erhoehungen (bis 5 Personen tabelliert;
    ab der 6. Person Anpassung durch das Vollstreckungsgericht)."""
    if unterhaltspflichten < 0:
        raise ValueError("Unterhaltspflichten darf nicht negativ sein")
    betrag = P_KONTO_SOCKEL
    if unterhaltspflichten >= 1:
        betrag += P_KONTO_ERHOEHUNG_ERSTE
    if unterhaltspflichten >= 2:
        bis_fuenf = min(unterhaltspflichten, 5) - 1
        betrag += P_KONTO_ERHOEHUNG_WEITERE * bis_fuenf
    return _cent(betrag)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Pfaendungsrechner nach Tabelle 1.7.2026 (Paragraf 850c ZPO)."
    )
    p.add_argument("--netto", type=str, help="Nettoeinkommen pro Monat in EUR.")
    p.add_argument(
        "--unterhalt",
        type=int,
        default=0,
        help="Anzahl unterhaltsberechtigter Personen (Default 0).",
    )
    p.add_argument(
        "--privileg",
        action="store_true",
        help="Privilegierte Unterhaltsforderung Paragraf 850d ZPO.",
    )
    p.add_argument(
        "--selbstbehalt",
        type=str,
        default=None,
        help="Konkret anzusetzender Selbstbehalt fuer Paragraf 850d ZPO (bei --privileg erforderlich).",
    )
    p.add_argument(
        "--p-konto",
        action="store_true",
        help="Statt Berechnung den P-Konto-Freibetrag ausgeben.",
    )
    p.add_argument(
        "--tabelle",
        action="store_true",
        help="Druckt eine kompakte Tabelle (0-5 Unterhaltspflichten / 1500-5000 EUR).",
    )
    return p


def _print_tabelle() -> None:
    print("Pfaendungstabelle (Auszug) - Tabelle 1.7.2026")
    print()
    kopf = ["Netto"] + [f"U={n}" for n in range(0, 6)]
    print(" | ".join(f"{c:>10}" for c in kopf))
    print("-" * (12 * len(kopf)))
    for netto in range(1500, 5001, 100):
        zeile = [f"{netto:>10}"]
        for n in range(0, 6):
            r = berechne(Decimal(netto), n)
            zeile.append(f"{r.pfaendbar:>10}")
        print(" | ".join(zeile))


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    ns = parser.parse_args(argv)

    # Gueltigkeits-Pruefung vor jeder Ausgabe: Pflicht-Selbstcheck, damit
    # nach Ablauf der Tabelle (30.6.2027) keine alten Werte unbemerkt
    # weiterverwendet werden.
    warn = gueltigkeits_warnung()
    if warn:
        import sys
        print(warn, file=sys.stderr)

    if ns.tabelle:
        _print_tabelle()
        return 0

    if ns.p_konto:
        print(
            f"P-Konto-Freibetrag (Paragraf 850k ZPO) bei "
            f"{ns.unterhalt} Unterhaltspflichtigen: "
            f"{p_konto_freibetrag(ns.unterhalt)} EUR / Monat"
        )
        return 0

    if not ns.netto:
        parser.error("--netto ist erforderlich (oder --tabelle bzw. --p-konto).")

    result = berechne(
        netto=ns.netto,
        unterhaltspflichten=ns.unterhalt,
        privileg_850d=ns.privileg,
        selbstbehalt=ns.selbstbehalt,
    )
    print(result.als_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
