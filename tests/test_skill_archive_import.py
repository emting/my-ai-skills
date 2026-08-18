import json
import zipfile
from pathlib import Path

import pytest

from scripts.import_skill_archive import classify, parse_backup
from scripts import import_skill_zip


BACKUP = Path(__file__).resolve().parents[1] / "docs" / "sources" / "Skills_Full_Configurations_Backup_20260818.md"


def test_backup_contains_all_66_named_skills() -> None:
    skills = parse_backup(BACKUP)

    assert len(skills) == 66
    assert [skill["number"] for skill in skills] == list(range(1, 67))
    assert all(skill["id"] for skill in skills)
    assert len({skill["id"] for skill in skills}) == 66


def test_parsed_skill_keeps_source_trace_and_removes_frontmatter() -> None:
    skill = parse_backup(BACKUP)[0]

    assert skill["source_start_line"] < skill["source_end_line"]
    assert skill["body"]
    assert "name:" not in skill["body"]
    assert "description:" not in skill["body"]


def test_sensitive_and_external_skill_is_human_gated() -> None:
    skill = next(item for item in parse_backup(BACKUP) if item["id"] == "customer-service-email-routing")
    result = classify(skill)

    assert result["risk"] == "high"
    assert result["handles_sensitive_data"] is True
    assert result["requires_confirmation"] is True
    assert result["permissions"]["network"] is True


def test_low_risk_instruction_skill_does_not_require_external_write() -> None:
    skill = next(item for item in parse_backup(BACKUP) if item["id"] == "agent-task-packaging")
    result = classify(skill)

    assert result["risk"] == "low"
    assert result["permissions"]["mcp_write_tools"] is False
    assert result["permissions"]["google_ads_write"] is False
    assert result["permissions"]["notion_write"] is False


def test_directory_zip_import_preserves_resources_and_skips_existing(tmp_path, monkeypatch) -> None:
    archive = tmp_path / "skills_export.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("existing-skill/SKILL.md", "---\nname: existing-skill\ndescription: existing\n---\n# Existing\n")
        handle.writestr("new-skill/SKILL.md", "---\nname: new-skill\ndescription: new\n---\n# New\n## Extra H1\n")
        handle.writestr("new-skill/references/example.txt", "reference")

    root = tmp_path / "repo"
    skills_root = root / "custom_skills"
    existing_dir = skills_root / "existing-skill"
    existing_dir.mkdir(parents=True)
    (existing_dir / "SKILL.md").write_text("keep", encoding="utf-8")
    (existing_dir / "manifest.json").write_text(json.dumps({"id": "existing-skill"}), encoding="utf-8")
    registry = root / "skills.json"
    root.mkdir(exist_ok=True)
    registry.write_text(json.dumps({"version": "1.0.0", "skills": []}), encoding="utf-8")

    monkeypatch.setattr(import_skill_zip, "ROOT", root)
    monkeypatch.setattr(import_skill_zip, "SKILLS_ROOT", skills_root)
    monkeypatch.setattr(import_skill_zip, "REGISTRY_PATH", registry)
    monkeypatch.setattr(import_skill_zip, "SOURCE_ROOT", root / "docs" / "sources")
    monkeypatch.setattr(import_skill_zip, "CATALOG_PATH", root / "docs" / "catalog.md")

    result = import_skill_zip.import_zip_archive(archive)

    assert result["archive_skill_count"] == 2
    assert result["preserved_count"] == 1
    assert result["imported_count"] == 1
    assert (existing_dir / "SKILL.md").read_text(encoding="utf-8") == "keep"
    new_dir = skills_root / "new-skill"
    assert (new_dir / "references" / "example.txt").read_text(encoding="utf-8") == "reference"
    normalized = (new_dir / "SKILL.md").read_text(encoding="utf-8")
    assert normalized.count("\n# ") == 1
    assert "## 標準執行契約" in normalized
    manifest = json.loads((new_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["runtime"] == "instruction_only"
    assert manifest["source"]["provenance_verified"] is True
    assert manifest["safety"]["dry_run_default"] is True
    assert manifest["external_write"]["allowed"] is False


def test_zip_path_traversal_is_rejected(tmp_path) -> None:
    archive = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("../escape/SKILL.md", "# unsafe")
    with pytest.raises(ValueError, match="unsafe ZIP member path"):
        import_skill_zip.safe_extract(archive, tmp_path / "out")
