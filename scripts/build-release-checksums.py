#!/usr/bin/env python3
"""Erzeugt streamend SHA-256-Prüfsummen für alle Release-Dateien."""

from __future__ import annotations

import argparse
from pathlib import Path

from release_asset_common import release_assets, sha256_file


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    args = parser.parse_args()
    if not args.dist.is_dir():
        parser.error(f"kein Verzeichnis: {args.dist}")
    assets = release_assets(args.dist, include_checksums=False)
    if not assets:
        parser.error(f"keine Release-Dateien in {args.dist}")
    target = args.dist / "checksums-sha256.txt"
    temporary = target.with_name(f".{target.name}.tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        for path in assets:
            handle.write(f"{sha256_file(path)}  {path.name}\n")
    temporary.replace(target)
    print(f"build-release-checksums OK ({len(assets)} Dateien)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
