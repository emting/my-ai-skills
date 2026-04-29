import argparse
from pathlib import Path

import pandas as pd


def load_data(input_path: Path) -> pd.DataFrame:
    if input_path.suffix.lower() == ".csv":
        return pd.read_csv(input_path)
    if input_path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(input_path)
    raise ValueError(f"Unsupported file type: {input_path.suffix}")


def generate_report(df: pd.DataFrame) -> str:
    row_count = len(df)
    column_count = len(df.columns)

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
    report.append(df.head(10).to_markdown(index=False))

    return "\n".join(report)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze CSV or Excel data.")
    parser.add_argument("--input", required=True, help="Input CSV or Excel file.")
    parser.add_argument("--output", required=True, help="Output Markdown report.")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    df = load_data(input_path)
    report = generate_report(df)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()
