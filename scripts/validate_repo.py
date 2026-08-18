"""Validate the repository's machine-readable contracts and referenced files."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "skill.schema.json"
REGISTRY_PATH = ROOT / "skills.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def relative_path(raw_path: str) -> Path:
    candidate = (ROOT / raw_path).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes repository: {raw_path}") from exc
    return candidate


def check_reference(errors: list[str], raw_path: str, description: str) -> None:
    try:
        path = relative_path(raw_path)
    except ValueError as exc:
        errors.append(f"{description}: {exc}")
        return
    if not path.exists():
        errors.append(f"{description} does not exist: {raw_path}")


def main() -> int:
    errors: list[str] = []

    try:
        schema = load_json(SCHEMA_PATH)
        registry = load_json(REGISTRY_PATH)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: unable to load core metadata: {exc}")
        return 1

    validator = Draft202012Validator(schema)
    registry_items = registry.get("skills")
    if not isinstance(registry_items, list):
        errors.append("skills.json.skills must be an array")
        registry_items = []

    registry_ids: set[str] = set()
    registry_manifest_ids: set[str] = set()

    for index, item in enumerate(registry_items):
        if not isinstance(item, dict):
            errors.append(f"skills[{index}] must be an object")
            continue
        skill_id = item.get("id")
        if not isinstance(skill_id, str) or not skill_id:
            errors.append(f"skills[{index}] has no valid id")
            continue
        if skill_id in registry_ids:
            errors.append(f"duplicate registry id: {skill_id}")
        registry_ids.add(skill_id)

        for field in ("location", "instruction_file", "manifest", "entrypoint", "reference_file", "mcp_reference"):
            value = item.get(field)
            if isinstance(value, str):
                check_reference(errors, value, f"{skill_id}.{field}")

        for field in ("instruction_files",):
            values = item.get(field, [])
            if not isinstance(values, list):
                errors.append(f"{skill_id}.{field} must be an array")
            else:
                for value in values:
                    if isinstance(value, str):
                        check_reference(errors, value, f"{skill_id}.{field}")

        manifest_raw = item.get("manifest")
        if not isinstance(manifest_raw, str):
            continue
        try:
            manifest_path = relative_path(manifest_raw)
            manifest = load_json(manifest_path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{skill_id}.manifest: {exc}")
            continue

        registry_manifest_ids.add(skill_id)
        if manifest.get("id") != skill_id:
            errors.append(
                f"manifest id mismatch for {skill_id}: {manifest.get('id')!r}"
            )
        for field in ("name", "description", "runtime", "risk_level"):
            if field in item and field in manifest and item[field] != manifest[field]:
                errors.append(
                    f"metadata drift for {skill_id}.{field}: "
                    f"registry={item[field]!r}, manifest={manifest[field]!r}"
                )

    manifests: dict[str, Path] = {}
    for manifest_path in sorted((ROOT / "custom_skills").glob("*/manifest.json")):
        try:
            manifest = load_json(manifest_path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{manifest_path.relative_to(ROOT)}: {exc}")
            continue

        skill_id = manifest.get("id")
        if not isinstance(skill_id, str):
            errors.append(f"{manifest_path.relative_to(ROOT)} has no valid id")
            continue
        manifests[skill_id] = manifest_path
        for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "$"
            errors.append(
                f"schema error in {skill_id} at {location}: {error.message}"
            )

        permissions = manifest.get("permissions", {})
        for legacy_key in ("read_files", "write_files"):
            if legacy_key in permissions:
                errors.append(f"legacy permission key in {skill_id}: {legacy_key}")

        entrypoint = manifest.get("entrypoint")
        if isinstance(entrypoint, str):
            check_reference(
                errors,
                str(manifest_path.parent.relative_to(ROOT) / entrypoint),
                f"{skill_id}.entrypoint",
            )

    unregistered = sorted(set(manifests) - registry_manifest_ids)
    for skill_id in unregistered:
        errors.append(f"manifest is not registered: {skill_id}")

    try:
        with (ROOT / "openapi.yaml").open(encoding="utf-8") as handle:
            openapi = yaml.safe_load(handle)
        if not isinstance(openapi, dict) or not openapi.get("openapi"):
            errors.append("openapi.yaml has no openapi version")
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"openapi.yaml: {exc}")

    workflow_dir = ROOT / ".github" / "workflows"
    for workflow_path in sorted(workflow_dir.glob("*.y*ml")):
        try:
            with workflow_path.open(encoding="utf-8") as handle:
                workflow = yaml.safe_load(handle)
            if not isinstance(workflow, dict) or not isinstance(workflow.get("jobs"), dict):
                errors.append(
                    f"{workflow_path.relative_to(ROOT)} must contain a jobs object"
                )
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{workflow_path.relative_to(ROOT)}: {exc}")

    try:
        mcp = load_json(ROOT / "mcp.json")
        if not isinstance(mcp.get("mcpServers"), dict):
            errors.append("mcp.json.mcpServers must be an object")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        errors.append(f"mcp.json: {exc}")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository validation passed: "
        f"{len(manifests)} manifests, {len(registry_items)} registry entries, "
        "OpenAPI, MCP, and referenced paths verified."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
