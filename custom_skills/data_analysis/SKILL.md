# Data Analysis Skill

## Purpose

This skill analyzes CSV or Excel files and generates a Markdown report.

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

## Output

The skill produces:

- Markdown summary report.
- Column type overview.
- Missing value summary.
- First rows preview.

## Safety Notes

- Do not upload the input file to external services.
- Do not print sensitive personal data in full.
- Mask private fields such as phone numbers, emails, IDs, and addresses when generating summaries.
