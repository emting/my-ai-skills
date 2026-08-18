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

## 標準執行契約

### 觸發與輸入

僅在使用者需求與本技能描述相符時啟用。先確認目標、受眾、上下文、資料來源、限制與輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與外部依賴。
2. 依技能核心流程處理，分開標示事實、推論、假設與建議。
3. 產出可審閱結果，列出來源、未驗證事項、風險與人工決策點。
4. 輸出前檢查範圍、引用、敏感資料與高影響操作。

## 輸出契約

- **report**：依技能規格提供

## 安全與人工核准

目前風險等級：**medium**。

- 不得捏造資料或來源。
- 外部服務採唯讀或草稿模式；寫入、發佈、部署與不可逆操作前須人工批准。

## 停止條件

若授權、來源、範圍、關鍵數字、身份或外部操作權限無法確認，停止高影響部分並回報缺口；若發現矛盾、敏感資料暴露或輸出無法驗證，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 目前沒有經人工確認的直接關聯技能 有功能相近或可互補的關係；選擇時以任務範圍、資料來源與權限邊界為準。

## 來源追蹤

此技能為 repository 內既有技能；來源與維護責任以 manifest 為準。
