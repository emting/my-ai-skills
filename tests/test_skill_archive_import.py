from pathlib import Path

from scripts.import_skill_archive import classify, parse_backup


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
