---
name: optimizing-google-ads
description: "Analyzes Google Ads performance and produces read-only reports, search term audits, RSA copy ideas, budget pacing, action queues, and n8n/Notion/MCP integration plans with human approval required before any write or spend-impacting change. Use when working on Google Ads AI copilot, 廣告副駕駛, Google Ads health reports, search terms, negative keyword suggestions, ad copy, budget pacing, or ad operations automation."
license: MIT
metadata:
  version: "1.0.0"
  category: "Marketing / Ads Operations / AI Copilot"
---

# Google Ads AI 廣告副駕駛 Agent Skill

> **定位**：將 Google Ads、n8n、Notion 與 AI Agent 整合成「廣告副駕駛」Skill：AI 做數據分析與建議，人類批准後才執行高風險操作。

## 使用情境
- 慕熙 Moosie 或在地服務需要小額廣告投放監控。
- 需要每日／每週 Google Ads 健康報告。
- 需要搜尋字詞稽核、否定關鍵字建議、廣告文案、預算 pacing 與行動佇列。
- 需要規劃 Google Ads API、n8n、MCP Server 或 Notion 廣告營運資料庫。

## 核心原則
1. **AI 做分析，人做決策**：所有會花錢或影響廣告帳戶的操作需人工批准。
2. **微預算思維**：NT$3,000／月也要每一塊錢有效率。
3. **保守優先**：不確定就先觀察，不直接大幅調整。
4. **先 Read-only，再 Write**：先建立報表與建議，再加入操作工具。
5. **所有操作可追溯**：操作前後狀態、原因、批准者與結果都要記錄。

## 分析模組
### 每日健康報告
- Campaign 花費、點擊、曝光、CTR、CPC、CPA。
- Keyword 品質分數、花費與轉換。
- Search Terms 浪費字詞與高意圖字詞。
- 異常警報：花費超標、CPA 過高、CTR 過低、0 轉換高花費。

### 搜尋字詞稽核
分類為：
- 🟢 高意圖：明確找補習班或課程。
- 🟡 中意圖：可能有學習需求但不明確。
- 🔴 低意圖／浪費：免費、翻譯、求職、非目標年齡或無關需求。

### 廣告文案生成
產出 Google Ads RSA：15 個標題、4 個描述、A/B 測試假設、Sitelinks、Callouts、Structured Snippets。

### 投放決策分析
- 預算分配。
- 競爭與 CPC 趨勢。
- 轉換漏斗診斷。
- 30 天行動計畫。
- If-then 自動化規則。

## 固定輸出格式
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

## 安全規則
- 不刪除 Campaign，只能建議 pause。
- 預算調整單次不超過 20%。
- Write 操作需人類確認。
- 不使用誇大教育成果或保證錄取文案。

## 啟用提示詞
請啟用「Google Ads AI 廣告副駕駛 Skill」。任務：根據以下廣告數據或目標，產出健康檢查、搜尋字詞洞察、投放建議與待批准行動。

---

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

## Notion 同步紀錄

本技能的指令本文同步自 Notion「Skill 頁面整理庫」頁面 https://app.notion.com/p/b88ebb8ac86a83908fca81911ba7ef72（Notion 版本 v1.0，最後編輯 2026-09-24T01:01:07Z）。上方內容以 Notion 為準；標準執行契約為本 repository 的安全治理補充，同步時不會被覆蓋。
