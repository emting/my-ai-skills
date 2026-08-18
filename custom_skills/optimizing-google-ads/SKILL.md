---
name: optimizing-google-ads
description: "Analyzes Google Ads performance and produces read-only reports, search term audits, RSA copy ideas, budget pacing, action queues, and n8n/Notion/MCP integration plans with human approval required before any write or spend-impacting change. Use when working on Google Ads AI copilot, 廣告副駕駛, Google Ads health reports, search terms, negative keyword suggestions, ad copy, budget pacing, or ad operations automation."
license: MIT
metadata:
  version: "1.0.0"
  category: "Marketing / Ads Operations / AI Copilot"
---

# Google Ads AI 廣告副駕駛

## Purpose

將 Google Ads、n8n、Notion 與 AI Agent 整合成「廣告副駕駛」：AI 負責數據分析、建議、文案與行動佇列；所有會花錢、影響帳戶、改變投放狀態或寫入外部系統的操作，都必須先取得人類批准。

## When to Use

使用者提到以下需求時啟用：

- Google Ads AI 廣告副駕駛、Google Ads copilot、廣告投放監控
- 每日／每週 Google Ads 健康報告
- 搜尋字詞稽核、否定關鍵字建議、高意圖字詞整理
- Google Ads RSA 廣告文案、A/B 測試假設、Sitelinks、Callouts、Structured Snippets
- 預算 pacing、CPC/CPA 趨勢、轉換漏斗診斷、30 天行動計畫
- Google Ads API、n8n、MCP Server、Notion 廣告營運資料庫規劃
- 慕熙 Moosie 或在地服務的小額廣告投放分析

## Core Principles

1. **AI 做分析，人做決策**：所有會花錢或影響廣告帳戶的操作需人工批准。
2. **微預算思維**：NT$3,000／月也要每一塊錢有效率。
3. **保守優先**：不確定就先觀察，不直接大幅調整。
4. **先 Read-only，再 Write**：先建立報表與建議，再加入操作工具。
5. **所有操作可追溯**：操作前後狀態、原因、批准者與結果都要記錄。

## Default Mode

預設為 `read-only analysis`：可以分析使用者提供的報表、CSV、截圖摘要或 API 查詢結果；不得直接修改 Google Ads、Notion、n8n workflow 或 MCP 設定。

```yaml
mode: read_only_analysis
write_operations: require_human_approval
budget_change_limit_per_action: 20_percent
allow_campaign_delete: false
allow_campaign_pause: suggest_only
allow_keyword_negative_add: approval_required
allow_budget_change: approval_required
allow_ad_copy_publish: approval_required
default_market: Taiwan
default_currency: TWD
micro_budget_context: NT$3000_per_month
```

## Analysis Modules

### 1. Daily or Weekly Health Report

檢查：

- Campaign 花費、點擊、曝光、CTR、CPC、CPA。
- Keyword 品質分數、花費與轉換。
- Search Terms 浪費字詞與高意圖字詞。
- 異常警報：花費超標、CPA 過高、CTR 過低、0 轉換高花費。

### 2. Search Terms Audit

將搜尋字詞分類為：

- 🟢 **高意圖**：明確找補習班、課程、服務或可轉換需求。
- 🟡 **中意圖**：可能有學習或服務需求，但意圖不明確。
- 🔴 **低意圖／浪費**：免費、翻譯、求職、非目標年齡、非服務地區或無關需求。

輸出時要區分「建議新增關鍵字」與「建議否定關鍵字」，並標記證據與風險。

### 3. Ad Copy Generation

產出 Google Ads RSA 素材：

- 15 個標題。
- 4 個描述。
- A/B 測試假設。
- Sitelinks、Callouts、Structured Snippets。

教育、課程或補習班情境禁止誇大成果、保證錄取、保證進步、虛構見證或暗示不實資格。

### 4. Bidding, Budget, and Funnel Decisions

分析：

- 預算分配與 pacing。
- 競爭與 CPC 趨勢。
- 轉換漏斗診斷。
- 30 天行動計畫。
- If-then 自動化規則。

所有建議都要標示影響、風險、是否需人工批准。

### 5. Automation and Data Stack Planning

可規劃：

- Google Ads API read-only 報表查詢。
- n8n 每日或每週排程、異常警報、Notion 寫入流程。
- Notion 廣告營運資料庫欄位：日期、Campaign、Cost、Clicks、CTR、CPC、Conversions、CPA、Issue、Recommendation、Approval Status、Approver、Result。
- MCP Server 工具邊界：read-only tools 先行，write tools 需 approval gate 與 audit log。

## Fixed Output Format

```markdown
## Google Ads AI 副駕駛報告

## 1. Dashboard
| Campaign | Cost | Clicks | CTR | CPC | Conv. | CPA |
|---|---|---|---|---|---|---|

## 2. 異常警報
| 等級 | 問題 | 證據 | 建議 |
|---|---|---|---|

## 3. Top 5 建議
| 建議 | 影響 | 風險 | 是否需人工批准 |
|---|---|---|---|

## 4. 搜尋字詞洞察
### 建議新增關鍵字
### 建議否定關鍵字

## 5. 行動佇列
- [ ] 待批准：
- [ ] 可直接觀察：
```

## Safety Rules

- 不刪除 Campaign，只能建議 pause。
- 預算調整單次不超過 20%。
- Write 操作需人類確認。
- 不使用誇大教育成果或保證錄取文案。
- 不直接執行 Google Ads API mutate、Notion 寫入、n8n workflow 更新或 MCP write tool，除非使用者明確批准該次具體操作。
- 不把 Google Ads customer ID、OAuth token、API key、n8n credential、Notion token 或私密報表內容寫入公開 repo 或回覆中。
- 若資料不足，標記「需補資料」或「假設」，不要假裝已完成帳戶稽核。

## Approval Gate

任何高風險操作前，輸出 approval request：

```markdown
## Approval Required

### Proposed Action
<例如：將 campaign A 的每日預算從 NT$100 調整為 NT$120>

### Reason
<基於哪些數據與問題>

### Expected Impact
<預期影響>

### Risk
<風險與回滾方式>

### Change Size
<百分比或範圍，預算調整不得超過 20%>

### Audit Fields
- requested_by: AI
- approved_by: pending
- before_state: <摘要>
- after_state: pending

請明確回覆「批准」後才可執行。
```

## Activation Prompt

```markdown
請啟用「Google Ads AI 廣告副駕駛 Skill」。

任務：根據以下廣告數據或目標，產出健康檢查、搜尋字詞洞察、投放建議與待批准行動。

資料來源：
【貼上 Google Ads 報表、CSV 欄位、搜尋字詞、Campaign 摘要、目標或截圖摘要】

限制：
- 先 read-only 分析。
- 所有 write 操作需人工批准。
- 不刪除 campaign。
- 預算單次調整不超過 20%。
- 不使用誇大教育成果或保證錄取文案。
```

## 標準執行契約

### 觸發與輸入

僅在使用者需求與本技能描述相符時啟用。先確認目標、受眾、上下文、資料來源、限制與輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與外部依賴。
2. 依技能核心流程處理，分開標示事實、推論、假設與建議。
3. 產出可審閱結果，列出來源、未驗證事項、風險與人工決策點。
4. 輸出前檢查範圍、引用、敏感資料與高影響操作。

## 輸出契約

- **ads_copilot_report**：依技能規格提供
- **action_queue**：依技能規格提供
- **approval_requests**：依技能規格提供
- **automation_plan**：依技能規格提供

## 安全與人工核准

目前風險等級：**high**。

- 不得捏造資料或來源。
- 外部服務採唯讀或草稿模式；寫入、發佈、部署與不可逆操作前須人工批准。

## 停止條件

若授權、來源、範圍、關鍵數字、身份或外部操作權限無法確認，停止高影響部分並回報缺口；若發現矛盾、敏感資料暴露或輸出無法驗證，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 目前沒有經人工確認的直接關聯技能 有功能相近或可互補的關係；選擇時以任務範圍、資料來源與權限邊界為準。

## 來源追蹤

此技能為 repository 內既有技能；來源與維護責任以 manifest 為準。
