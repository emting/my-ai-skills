# Data Analysis Skill

## Purpose

This skill analyzes CSV or Excel files and generates a privacy-conscious Markdown report. It performs local-only processing and redacts common personal-data columns in previews by default.

## When to Use

Use this skill when the user asks to:

- Analyze a CSV file.
- Analyze an Excel file.
- Summarize tabular data.
- Find trends, outliers, or patterns.
- Create a Markdown report from structured data.

## Inputs

| Input | Required | Description |
|---|---|---|
| input file | Yes | CSV or Excel file |
| output file | Yes | Markdown report path |

## Command

```bash
python custom_skills/data_analysis/run.py --input data.csv --output report.md
```

For sensitive or unknown datasets, the default redaction remains enabled. You can add domain-specific fields and suppress the preview entirely:

```bash
python custom_skills/data_analysis/run.py \
  --input data.csv \
  --output report.md \
  --sensitive-column internal_note \
  --preview-rows 0
```

## Output

The skill produces:

- Markdown summary report.
- Column type overview.
- Missing value summary.
- A redacted preview of the first rows, unless `--preview-rows 0` is used.

## Safety Notes

- Do not upload the input file to external services.
- Do not print sensitive personal data in full.
- Common columns such as names, phone numbers, emails, IDs, and addresses are redacted automatically in previews.
- Use `--sensitive-column COLUMN` once per domain-specific private field.
- Use `--preview-rows 0` when no data values should appear in the report.
- Review generated reports before sharing them; column names and aggregate values may still be sensitive.
