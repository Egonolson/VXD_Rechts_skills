#!/usr/bin/env python3
"""Verify GitHub Release assets after upload.

The release workflow uploads several hundred ZIPs. A green upload command is not
quite enough: GitHub may throttle, replace assets slowly, or leave stale assets
on an existing release. This script polls the Release API until every expected
local asset exists remotely with uploaded state, matching size and matching
sha256 digest.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from release_asset_common import expected_asset_metadata


def fail(message: str) -> None:
    print(f"validate-release-assets failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def run_gh_api(resource: str) -> Any:
    proc = subprocess.run(
        ["gh", "api", resource],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        fail(f"gh api {resource!r} failed: {proc.stderr.strip()}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        fail(f"gh api {resource!r} returned invalid JSON: {exc}")


def expected_assets(dist: Path) -> dict[str, dict[str, Any]]:
    try:
        expected = expected_asset_metadata(dist)
    except (OSError, ValueError) as exc:
        fail(str(exc))
    if not expected:
        fail(f"{dist}: no release assets found")
    return expected


def release_id(repo: str, tag: str) -> int:
    proc = subprocess.run(
        [
            "gh",
            "release",
            "view",
            tag,
            "--repo",
            repo,
            "--json",
            "databaseId",
        ],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        fail(f"Release {repo}@{tag} konnte nicht gelesen werden: {proc.stderr.strip()}")
    try:
        value = json.loads(proc.stdout).get("databaseId")
    except json.JSONDecodeError as exc:
        fail(f"Release {repo}@{tag} lieferte ungültiges JSON: {exc}")
    if not value:
        fail(f"{repo}@{tag}: release id missing")
    return int(value)


def fetch_assets(repo: str, tag: str) -> dict[str, dict[str, Any]]:
    remote_release_id = release_id(repo, tag)

    assets: dict[str, dict[str, Any]] = {}
    page = 1
    while True:
        batch = run_gh_api(
            f"repos/{repo}/releases/{remote_release_id}/assets?per_page=100&page={page}"
        )
        if not isinstance(batch, list):
            fail(f"{repo}@{tag}: assets response page {page} is not a list")
        for asset in batch:
            name = asset.get("name")
            if not name:
                fail(f"{repo}@{tag}: asset without name on page {page}")
            if name in assets:
                fail(f"{repo}@{tag}: duplicate asset name {name}")
            assets[name] = asset
        if len(batch) < 100:
            break
        page += 1
    return assets


def diff_assets(expected: dict[str, dict[str, Any]], actual: dict[str, dict[str, Any]]) -> list[str]:
    problems: list[str] = []
    expected_names = set(expected)
    actual_names = set(actual)

    missing = sorted(expected_names - actual_names)
    extra = sorted(actual_names - expected_names)
    if missing:
        problems.append(f"missing assets: {missing[:20]}")
    if extra:
        problems.append(f"unexpected stale assets: {extra[:20]}")

    for name in sorted(expected_names & actual_names):
        asset = actual[name]
        want = expected[name]
        if asset.get("state") != "uploaded":
            problems.append(f"{name}: state={asset.get('state')!r}")
        if int(asset.get("size") or 0) != int(want["size"]):
            problems.append(f"{name}: size remote={asset.get('size')} local={want['size']}")
        remote_digest = asset.get("digest")
        if remote_digest != want["digest"]:
            problems.append(f"{name}: digest remote={remote_digest!r} local={want['digest']!r}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path)
    parser.add_argument("tag")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY"))
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--poll-seconds", type=int, default=10)
    args = parser.parse_args()

    if not args.repo:
        fail("--repo or GITHUB_REPOSITORY is required")

    expected = expected_assets(args.dist)
    deadline = time.monotonic() + args.timeout_seconds
    last_problems: list[str] = []

    while True:
        actual = fetch_assets(args.repo, args.tag)
        last_problems = diff_assets(expected, actual)
        if not last_problems:
            print(f"validate-release-assets OK ({len(expected)} assets verified on {args.repo}@{args.tag})")
            return
        if time.monotonic() >= deadline:
            break
        print(
            f"Waiting for release assets ({len(last_problems)} issue(s)); "
            f"first issue: {last_problems[0]}",
            flush=True,
        )
        time.sleep(args.poll_seconds)

    for problem in last_problems[:50]:
        print(problem, file=sys.stderr)
    fail(f"{len(last_problems)} release asset problem(s) after polling")


if __name__ == "__main__":
    main()
