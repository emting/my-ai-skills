#!/usr/bin/env python3
"""Perform a safe, read-only dry run of every installed instruction-only skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


CONTRACT_HEADINGS = (
    "## Purpose",
    "## 目的",
    "## Safety",
    "## 安全",
    "## 安全規則",
    "## 來源追蹤",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.home() / ".agents" / "skills")
    args = parser.parse_args()

    root = args.root.expanduser()
    checked = 0
    instruction_only = 0
    executable = 0
    failures: list[str] = []
    by_risk: dict[str, int] = {}

    for directory in sorted(path for path in root.iterdir() if path.is_dir()):
        manifest_path = directory / "manifest.json"
        skill_path = directory / "SKILL.md"
        try:
            manifest: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
            content = skill_path.read_text(encoding="utf-8")
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{directory.name}: cannot load package ({exc})")
            continue

        checked += 1
        runtime = manifest.get("runtime")
        risk = manifest.get("risk_level", "unknown")
        by_risk[risk] = by_risk.get(risk, 0) + 1
        if runtime == "instruction_only":
            instruction_only += 1
            if not any(heading in content for heading in CONTRACT_HEADINGS):
                failures.append(f"{directory.name}: no recognizable contract heading")
            if manifest.get("risk_level") == "high":
                safety = manifest.get("safety", {})
                if safety.get("requires_user_confirmation") is not True:
                    failures.append(f"{directory.name}: high-risk dry run is not confirmation gated")
        else:
            executable += 1
            entrypoint = directory / str(manifest.get("entrypoint", ""))
            if not entrypoint.is_file():
                failures.append(f"{directory.name}: executable entrypoint is missing")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print(f"checked_packages={checked}")
    print(f"instruction_only_dry_runs={instruction_only}")
    print(f"executable_packages={executable}")
    print(f"risk_distribution={json.dumps(by_risk, ensure_ascii=False, sort_keys=True)}")
    print("Safe skill dry-run passed; no external actions were executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
