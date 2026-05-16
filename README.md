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


### 5. [Private] Website Custom Optimizer

**用途：**
依據網站目標與主要受眾，診斷並優化官方網站、Landing Page、產品頁、服務頁、招生頁、活動頁、知識庫與內部入口網，產出網站診斷、資訊架構、文案重寫、SEO、CRO、效能、可近用性、A/B 測試與執行路線圖。

**位置：**

`custom_skills/website-custom-optimizer/`

**適用情境：**

- 網站健檢與改版規劃
- Landing Page 轉換率優化
- 首頁架構設計與網站文案重寫
- SEO、UX/UI、行動版、效能與可近用性檢核
- 上線前檢核與工程／設計需求整理


### 6. [Private] Full Sprint

**用途：**
把高層目標轉成可執行、可驗證、可暫停、可恢復、可審計的 Sprint Contract，並在安全邊界、scope、constraints、驗收條件與 budget 內持續推進工程、重構、測試修復、文件或 feature 任務。

**位置：**

`custom_skills/full-sprint/`

**適用情境：**

- 使用者提到 `全力衝刺`、`sprint`、`/sprint`、`/goal`
- 長任務、自主執行、持續推進、跑到完成
- 需要每輪 checkpoint、驗證、log、completion audit 與 final report
- 需要在明確 scope、out_of_scope、constraints 與 validation commands 內交付


### 7. [Community] Awesome Agent Skills

**用途：**
引用社群整理的 agent skills 資源，作為新增技能、參考技能格式與擴充能力時的共用來源。

**來源：**

`https://github.com/heilcheng/awesome-agent-skills`

**位置：**

`community_skills/awesome-agent-skills/`


### 8. [Community] Cloudflare Skills

**用途：**
引用 Cloudflare 官方 agent skills，讓 Agent 在處理 Workers、Pages、KV、D1、R2、AI、Tunnel、WAF、Wrangler、Durable Objects、Agents SDK、Email Service 等 Cloudflare 任務時可讀取官方指令包。

**來源：**

`https://github.com/cloudflare/skills`

**位置：**

`community_skills/cloudflare-skills/`

**可用內容：**

- `skills/cloudflare/SKILL.md`
- `skills/agents-sdk/SKILL.md`
- `skills/durable-objects/SKILL.md`
- `skills/cloudflare-email-service/SKILL.md`
- `skills/wrangler/SKILL.md`
- `skills/workers-best-practices/SKILL.md`
- `skills/web-perf/SKILL.md`
- `skills/sandbox-sdk/SKILL.md`
- `.mcp.json` for Cloudflare MCP server references

## Usage Policy

當 AI Agent 使用本技能庫時，請遵守以下原則：

1. 若任務涉及本機檔案分析，優先檢查 `custom_skills/`。
2. 若任務涉及多步驟流程，優先檢查 `workflows/`。
3. 若任務涉及 HTTP API 調用，優先檢查 `openapi.yaml`。
4. 若任務涉及第三方現成技能，檢查 `community_skills/`。
5. 若任務涉及敏感資料，必須先確認資料來源與授權。
6. 不得將 `.env`、API Key、Token、私密檔案上傳至公開 repo。

## Local Skills Inventory

本機已安裝的 agent skills 整理於 `LOCAL_SKILLS_INVENTORY.md`，包含：

- `~/.agents/skills` 與 `~/.skills` 的對應關係
- 目前已安裝 skill 清單
- 是否已能從本機證據確認對應 GitHub repo
- 後續是否建議納入本技能庫正式管理

機器可讀版本整理於 `local_skills_catalog.json`，格式與 `skills.json` 相容，方便後續自動選 skill、比對來源與做批次納管。

目前已優先納管的本機 skills：

- `custom_skills/to_prd/`
- `custom_skills/write_a_skill/`
- `custom_skills/lovable_github_cloudflare_worker/`
- `custom_skills/mcp_builder/`
- `custom_skills/website-custom-optimizer/`
- `custom_skills/full-sprint/`

## Repository Structure

```text
my-ai-skills/
├── README.md
├── LOCAL_SKILLS_INVENTORY.md
├── SKILL.md
├── AGENTS.md
├── skills.json
├── local_skills_catalog.json
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
git clone --recurse-submodules https://github.com/YOUR_USERNAME/my-ai-skills.git
cd my-ai-skills
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git submodule update --init --recursive
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
