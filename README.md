# My AI Personal Skills Library

這是一個個人 AI Skills Library，用於集中管理可被 AI Agent、Coding Assistant、Automation Agent 讀取與調用的技能、腳本、工作流程與 API 規格。

本儲存庫目標是支援以下使用情境：

- Warp / Terminal AI 讀取任務說明
- Manus 類自主 Agent 執行工作流程
- Codex / GitHub Copilot 協助開發與維護技能
- AMP Code 類 AI Coding Agent 理解專案結構
- 支援 OpenAPI 的 Agent 調用 HTTP API
- 支援 MCP 的 Agent 連接本地或遠端工具

## Core Skills

### 1. [Private] Data Analysis Skill

**用途：**
讀取 CSV / Excel 檔案，進行資料清理、統計分析與 Markdown 報告輸出。

**位置：**

`custom_skills/data_analysis/`

**適用情境：**

- 分析帳單
- 分析學生名單
- 分析行銷數據
- 產生摘要報告

**執行方式：**

```bash
python custom_skills/data_analysis/run.py --input custom_skills/data_analysis/examples/sample_input.csv --output report.md
```

### 2. [Workflow] Email Summary

**用途：**
將 Email 內容整理成摘要、待辦、決策與風險。

**位置：**

`workflows/email_summary.md`

### 3. [Workflow] Research Report

**用途：**
將研究任務整理為可查證、可比較、可決策的 Markdown 報告。

**位置：**

`workflows/research_report.md`

### 4. [Workflow] Website Audit

**用途：**
分析網站首頁訴求、CTA、信任元素、轉換路徑與可改善項。

**位置：**

`workflows/website_audit.md`

## Usage Policy

當 AI Agent 使用本技能庫時，請遵守以下原則：

1. 若任務涉及本機檔案分析，優先檢查 `custom_skills/`。
2. 若任務涉及多步驟流程，優先檢查 `workflows/`。
3. 若任務涉及 HTTP API 調用，優先檢查 `openapi.yaml`。
4. 若任務涉及第三方現成技能，檢查 `community_skills/`。
5. 若任務涉及敏感資料，必須先確認資料來源與授權。
6. 不得將 `.env`、API Key、Token、私密檔案上傳至公開 repo。

## Repository Structure

```text
my-ai-skills/
├── README.md
├── SKILL.md
├── AGENTS.md
├── skills.json
├── openapi.yaml
├── mcp.json
├── custom_skills/
├── community_skills/
├── workflows/
├── prompts/
├── schemas/
└── tests/
```

## Compatibility

| 格式 | 用途 |
|---|---|
| Markdown | 給人類與大多數 AI Agent 閱讀 |
| skills.json | 給 Agent 快速索引技能 |
| OpenAPI | 給支援 API 調用的 Agent 使用 |
| MCP Config | 給支援 MCP 的工具連接 |
| Python Scripts | 實際執行任務 |

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/my-ai-skills.git
cd my-ai-skills
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Safety

請勿提交以下內容：

- API Key
- Token
- 密碼
- 個人身分資料
- 客戶資料
- 未授權文件
- `.env` 檔案

請使用 `.env.example` 作為環境變數範例。

## License

MIT License
