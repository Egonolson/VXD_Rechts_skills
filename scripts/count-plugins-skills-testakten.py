#!/usr/bin/env python3
"""Zählt Plugins, Skills und Testakten aus einer Repo-Quelle."""

from __future__ import annotations

import json
from pathlib import Path

from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}


def load_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def main() -> int:
    plugins = load_plugins()
    skill_files = []
    pluginlocal_testakten = []
    for plugin in plugins:
        directory = plugin_dir(plugin)
        skill_files.extend(sorted((directory / "skills").glob("*/SKILL.md")))
        testakte = directory / "testakte"
        if testakte.is_dir() and working_dump_flat_pairs(testakte, include_gesamt_pdf=False):
            pluginlocal_testakten.append(testakte)

    central_testakten = []
    root = REPO / "testakten"
    if root.is_dir():
        for child in sorted(root.iterdir()):
            if child.is_dir() and child.name not in SKIP_TESTAKTEN:
                central_testakten.append(child)

    result = {
        "plugins": len(plugins),
        "skills": len(skill_files),
        "testakten": len(central_testakten) + len(pluginlocal_testakten),
        "central_testakten": len(central_testakten),
        "pluginlocal_testakten": len(pluginlocal_testakten),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
