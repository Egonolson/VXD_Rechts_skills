#!/usr/bin/env python3
"""Regressionstests für die zwei datumsabhängigen Rechtsrechner."""

from __future__ import annotations

import importlib.util
import sys
from datetime import date
from decimal import Decimal
from pathlib import Path
from types import ModuleType


REPO = Path(__file__).resolve().parent.parent


def load_module(name: str, relative_path: str) -> ModuleType:
    path = REPO / relative_path
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Modul nicht ladbar: {relative_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def assert_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: erwartet {expected!r}, erhalten {actual!r}")


def test_pfaendungsrechner() -> None:
    module = load_module(
        "pfaendungsrechner",
        "zwangsvollstreckung/werkzeuge/pfaendungsrechner.py",
    )
    cases = (
        ("1589.99", 0, "0.00"),
        ("1590.00", 0, "1.82"),
        ("1600.00", 0, "8.82"),
        ("2200.00", 1, "7.59"),
        ("4866.30", 3, "602.86"),
        ("5000.27", 5, "268.36"),
    )
    for netto, unterhalt, expected in cases:
        result = module.berechne(netto, unterhalt)
        assert_equal(
            result.pfaendbar,
            Decimal(expected),
            f"Pfändung {netto} Euro mit {unterhalt} Unterhaltspflichten",
        )

    assert_equal(module.p_konto_freibetrag(0), Decimal("1590.00"), "P-Konto")
    assert_equal(
        module.p_konto_freibetrag(1),
        Decimal("2187.42"),
        "P-Konto mit erster Erhöhung",
    )
    assert_equal(module.gueltigkeits_warnung(date(2026, 7, 11)), None, "Gültigkeit")

    try:
        module.berechne("2500", 1, privileg_850d=True)
    except ValueError:
        pass
    else:
        raise AssertionError("Paragraf 850d darf ohne Selbstbehalt nicht rechnen")


def test_verzugszinsrechner() -> None:
    module = load_module(
        "verzugszins_rechner",
        "forderungsmanagement-klagewerkstatt/skills/klage-aus-eigenem-skill/"
        "werkzeuge/verzugszins_rechner.py",
    )
    assert_equal(module.basiszins_an(date(2013, 7, 1)), -0.38, "Basiszins 2013")
    assert_equal(module.basiszins_an(date(2026, 7, 1)), 1.52, "Basiszins 2026")

    periods, interest, total = module.berechne(
        5000.0,
        date(2026, 4, 15),
        date(2026, 10, 15),
        "b2b",
    )
    assert_equal(len(periods), 2, "Periodenwechsel Juli 2026")
    assert_equal(periods[0].bis, date(2026, 6, 30), "Ende erste Zinsperiode")
    assert_equal(periods[1].basiszins, 1.52, "Basiszins zweite Periode")
    assert_equal(interest, 262.53, "Verzugszins")
    assert_equal(total, 5262.53, "Gesamtforderung")

    try:
        module.basiszins_an(date(2027, 1, 1))
    except ValueError:
        pass
    else:
        raise AssertionError("Unbekannter Basiszins 2027 darf nicht fortgeschrieben werden")


def main() -> int:
    test_pfaendungsrechner()
    test_verzugszinsrechner()
    print("test-legal-calculators OK (6 Pfändungsfälle, 2 P-Konto-Fälle, Zinsperioden)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
