from pathlib import Path

import pandas as pd
import pytest

from custom_skills.data_analysis.run import generate_report, load_data


def test_generate_report() -> None:
    df = pd.DataFrame({
        "name": ["A", "B"],
        "score": [90, 80],
    })

    report = generate_report(df)

    assert "Data Analysis Report" in report
    assert "Rows: 2" in report
    assert "Columns: 2" in report
    assert "`name`" in report
    assert "`score`" in report


def test_generate_report_redacts_common_personal_data() -> None:
    df = pd.DataFrame({
        "email": ["alice@example.com"],
        "phone": ["0912-345-678"],
        "address": ["台北市信義區"],
        "score": [95],
    })

    report = generate_report(df)

    assert "alice@example.com" not in report
    assert "0912-345-678" not in report
    assert "台北市信義區" not in report
    assert "[REDACTED]" in report
    assert "95" in report


def test_generate_report_redacts_explicit_sensitive_column() -> None:
    df = pd.DataFrame({"internal_note": ["confidential customer note"]})

    report = generate_report(df, sensitive_columns=["internal_note"])

    assert "confidential customer note" not in report
    assert "[REDACTED]" in report


def test_generate_report_can_omit_preview() -> None:
    df = pd.DataFrame({"value": [1, 2]})

    report = generate_report(df, preview_rows=0)

    assert "Preview" in report
    assert "Preview omitted" in report
    assert "| 1 |" not in report


def test_load_data_supports_csv_and_excel(tmp_path: Path) -> None:
    csv_path = tmp_path / "sample.csv"
    csv_path.write_text("name,score\nA,90\n", encoding="utf-8")
    assert list(load_data(csv_path).columns) == ["name", "score"]

    excel_path = tmp_path / "sample.xlsx"
    pd.DataFrame({"name": ["B"], "score": [80]}).to_excel(excel_path, index=False)
    assert list(load_data(excel_path).columns) == ["name", "score"]


def test_load_data_rejects_unsupported_extension(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Unsupported file type"):
        load_data(tmp_path / "sample.json")


def test_generate_report_rejects_negative_preview_rows() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        generate_report(pd.DataFrame({"value": [1]}), preview_rows=-1)
