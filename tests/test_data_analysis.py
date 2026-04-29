import pandas as pd

from custom_skills.data_analysis.run import generate_report


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
