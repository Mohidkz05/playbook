#!/usr/bin/env python3
"""Validate the playbook: routes.toml schema, stack file sections, catalog coverage.

Stdlib only (Python 3.11+). Run: python3 scripts/check.py
"""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTE_KEYS = {"name", "group", "skill", "agent", "reason", "words", "files",
              "builtin", "plugin", "project"}
STACK_SECTIONS = ["Pick", "Why", "Setup", "Checks", "Avoid", "Alternatives", "Sources"]


def check_routes(errors: list[str]) -> list[dict]:
    data = tomllib.loads((ROOT / "routes.toml").read_text(encoding="utf-8"))
    routes = data.get("route", [])
    if not routes:
        errors.append("routes.toml: no [[route]] entries")
    seen: set[str] = set()
    for i, r in enumerate(routes):
        where = f"routes.toml route #{i + 1} ({r.get('name', '?')})"
        if unknown := set(r) - ROUTE_KEYS:
            errors.append(f"{where}: unknown keys {sorted(unknown)}")
        if not r.get("name") or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", r["name"]):
            errors.append(f"{where}: name must be kebab-case")
        elif r["name"] in seen:
            errors.append(f"{where}: duplicate name")
        seen.add(r.get("name", ""))
        if ("skill" in r) == ("agent" in r):
            errors.append(f"{where}: set exactly one of skill / agent")
        if not r.get("reason"):
            errors.append(f"{where}: missing reason")
        if not (r.get("words") or r.get("files")):
            errors.append(f"{where}: needs words and/or files to trigger on")
        for key in ("words", "files"):
            value = r.get(key, [])
            if not isinstance(value, list) or not all(isinstance(v, str) and v for v in value):
                errors.append(f"{where}: {key} must be a list of non-empty strings")
        if "plugin" in r and "@" not in r["plugin"]:
            errors.append(f"{where}: plugin must look like name@marketplace")
    return routes


def check_stacks(errors: list[str]) -> None:
    stacks = sorted((ROOT / "stacks").glob("*.md"))
    if not stacks:
        errors.append("stacks/: no stack files")
    for f in stacks:
        text = f.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, re.M)
        missing = [s for s in STACK_SECTIONS if s not in headings]
        if missing:
            errors.append(f"stacks/{f.name}: missing sections {missing}")
        if not re.search(r"^Last reviewed: \d{4}-\d{2}-\d{2}$", text, re.M):
            errors.append(f"stacks/{f.name}: missing 'Last reviewed: YYYY-MM-DD'")
        if not re.search(r"^# .+", text):
            errors.append(f"stacks/{f.name}: missing title")


def check_catalog(errors: list[str], routes: list[dict]) -> None:
    catalog = (ROOT / "skills.md").read_text(encoding="utf-8")
    for r in routes:
        target = r.get("skill") or r.get("agent")
        if target and f"`{target}`" not in catalog and target not in catalog:
            errors.append(f"skills.md: route '{r['name']}' uses '{target}', which isn't listed")


def main() -> int:
    errors: list[str] = []
    routes = check_routes(errors)
    check_stacks(errors)
    check_catalog(errors, routes)
    if errors:
        print("\n".join(f"✗ {e}" for e in errors))
        return 1
    stacks = len(list((ROOT / "stacks").glob("*.md")))
    print(f"✓ playbook OK: {len(routes)} routes, {stacks} stacks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
