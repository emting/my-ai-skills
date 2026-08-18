#!/usr/bin/env python3
"""Verify that the repository skill packages are installed and loadable locally."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_RUNTIME = {"instruction_only", "python", "node", "shell", "http", "unknown"}
REQUIRED_RISK = {"low", "medium", "high"}


def fail(message: str) -> None:
    raise SystemExit(f"local skill installation failed: {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.home() / ".agents" / "skills",
        help="installed skill directory (default: ~/.agents/skills)",
    )
    parser.add_argument(
        "--expected-count",
        type=int,
        default=80,
        help="number of installed skill packages expected",
    )
    args = parser.parse_args()

    root = args.root.expanduser()
    if not root.is_dir():
        fail(f"missing install directory: {root}")

    directories = sorted(path for path in root.iterdir() if path.is_dir())
    if len(directories) != args.expected_count:
        fail(f"expected {args.expected_count} skill directories, found {len(directories)}")

    failures: list[str] = []
    risks: dict[str, int] = {}
    archive_count = 0
    symlink_count = 0
    for directory in directories:
        skill_file = directory / "SKILL.md"
        manifest_file = directory / "manifest.json"
        if not skill_file.is_file() or not manifest_file.is_file():
            failures.append(f"{directory.name}: missing SKILL.md or manifest.json")
            continue
        if directory.is_symlink():
            symlink_count += 1
        try:
            manifest: dict[str, Any] = json.loads(manifest_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{directory.name}: invalid manifest ({exc})")
            continue

        if manifest.get("id") != directory.name:
            failures.append(f"{directory.name}: manifest id mismatch")
        if manifest.get("runtime") not in REQUIRED_RUNTIME:
            failures.append(f"{directory.name}: unsupported runtime")
        risk = manifest.get("risk_level")
        if risk not in REQUIRED_RISK:
            failures.append(f"{directory.name}: invalid risk_level")
        else:
            risks[risk] = risks.get(risk, 0) + 1
        entrypoint = directory / str(manifest.get("entrypoint", "SKILL.md"))
        if not entrypoint.is_file():
            failures.append(f"{directory.name}: missing entrypoint {entrypoint.name}")

        safety = manifest.get("safety", {})
        if not isinstance(safety, dict):
            failures.append(f"{directory.name}: safety must be an object")
        else:
            if risk == "high" and safety.get("requires_user_confirmation") is not True:
                failures.append(f"{directory.name}: high risk skill is not confirmation gated")
            safety_rules = (
                safety.get("rules")
                or safety.get("forbidden_without_explicit_approval")
                or manifest.get("safety_notes")
            )
            if safety.get("handles_sensitive_data") is True and not safety_rules:
                failures.append(f"{directory.name}: sensitive skill has no safety rules")

        source = manifest.get("source", {})
        if isinstance(source, dict) and source.get("type") == "user_provided_backup":
            archive_count += 1
            if not source.get("section_number") or not source.get("start_line") or not source.get("end_line"):
                failures.append(f"{directory.name}: incomplete archive source trace")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print(f"installed_root={root}")
    print(f"packages={len(directories)}")
    print(f"symlinks={symlink_count}")
    print(f"archive_packages={archive_count}")
    print(f"risk_distribution={json.dumps(risks, ensure_ascii=False, sort_keys=True)}")
    print("Local skill installation verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
