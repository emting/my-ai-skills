"""Generate a privacy-conscious Markdown report from CSV or Excel data."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

import pandas as pd


SENSITIVE_COLUMN_TOKENS = (
    "name",
    "姓名",
    "email",
    "mail",
    "電話",
    "phone",
    "mobile",
    "tel",
    "address",
    "addr",
    "地址",
    "身分證",
    "身份證",
    "identity",
    "passport",
    "ssn",
    "social_security",
    "customer_id",
    "student_id",
    "user_id",
    "member_id",
)

EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
PHONE_PATTERN = re.compile(r"^[+()\d][\d\s().-]{6,}$")
IDENTITY_PATTERN = re.compile(r"^[A-Za-z][12]\d{8}$")


def load_data(input_path: Path) -> pd.DataFrame:
    """Load a CSV or Excel file based on its extension."""
    if input_path.suffix.lower() == ".csv":
        return pd.read_csv(input_path)
    if input_path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(input_path)
    raise ValueError(f"Unsupported file type: {input_path.suffix}")


def _is_sensitive_column(column_name: object, extra_columns: Iterable[str]) -> bool:
    """Return whether a column name should be redacted in previews."""
    normalized = str(column_name).strip().lower()
    requested = {str(name).strip().lower() for name in extra_columns}
    return normalized in requested or any(token in normalized for token in SENSITIVE_COLUMN_TOKENS)


def _redact_value(value: object, force: bool = False) -> object:
    """Redact common personal-data values while preserving missing values."""
    if pd.isna(value):
        return value
    if force:
        return "[REDACTED]"

    text = str(value).strip()
    if EMAIL_PATTERN.fullmatch(text):
        return "[REDACTED_EMAIL]"
    if IDENTITY_PATTERN.fullmatch(text):
        return "[REDACTED_ID]"
    if PHONE_PATTERN.fullmatch(text) and sum(char.isdigit() for char in text) >= 7:
        return "[REDACTED_PHONE]"
    return value


def redact_dataframe(df: pd.DataFrame, sensitive_columns: Iterable[str] = ()) -> pd.DataFrame:
    """Return a copy whose previews do not expose common personal data."""
    redacted = df.copy()
    for column in redacted.columns:
        force = _is_sensitive_column(column, sensitive_columns)
        redacted[column] = redacted[column].map(
            lambda value: _redact_value(value, force=force)
        )
    return redacted


def generate_report(
    df: pd.DataFrame,
    *,
    preview_rows: int = 10,
    sensitive_columns: Iterable[str] = (),
) -> str:
    """Generate a Markdown report with a redacted data preview."""
    if preview_rows < 0:
        raise ValueError("preview_rows must be non-negative")

    row_count = len(df)
    column_count = len(df.columns)
    safe_preview = redact_dataframe(df, sensitive_columns).head(preview_rows)

    report: list[str] = []
    report.append("# Data Analysis Report")
    report.append("")
    report.append("## Summary")
    report.append("")
    report.append(f"- Rows: {row_count}")
    report.append(f"- Columns: {column_count}")
    report.append("")
    report.append("## Columns")
    report.append("")

    for col in df.columns:
        report.append(f"- `{col}`: {df[col].dtype}")

    report.append("")
    report.append("## Missing Values")
    report.append("")

    missing = df.isna().sum()

    for col, count in missing.items():
        report.append(f"- `{col}`: {count}")

    report.append("")
    report.append("## Preview")
    report.append("")
    if safe_preview.empty:
        report.append("_Preview omitted or the input contains no rows._")
    else:
        report.append(safe_preview.to_markdown(index=False))

    return "\n".join(report)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze CSV or Excel data safely.")
    parser.add_argument("--input", required=True, help="Input CSV or Excel file.")
    parser.add_argument("--output", required=True, help="Output Markdown report.")
    parser.add_argument(
        "--preview-rows",
        type=int,
        default=10,
        help="Number of redacted preview rows to include (default: 10).",
    )
    parser.add_argument(
        "--sensitive-column",
        action="append",
        default=[],
        dest="sensitive_columns",
        help="Column name to redact; may be provided more than once.",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    df = load_data(input_path)
    report = generate_report(
        df,
        preview_rows=args.preview_rows,
        sensitive_columns=args.sensitive_columns,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()
