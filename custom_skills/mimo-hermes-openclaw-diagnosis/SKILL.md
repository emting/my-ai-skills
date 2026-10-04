---
name: mimo-hermes-openclaw-diagnosis
description: 協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線，確認 API Key 類型、Base URL、provider 名稱與模型名稱。
---

# MiMo × Hermes × OpenClaw 設定診斷 Skill

> **定位**：協助設定與排錯 Xiaomi MiMo、Hermes Agent、OpenClaw 的模型連線。核心任務是先確認 API Key 類型、Base URL、provider 名稱與模型名稱是否成對正確。

## 使用情境
- Hermes Agent 或 OpenClaw 要接入 Xiaomi MiMo。
- Pay-as-you-go 與 Token Plan 混用導致授權失敗。
- model not found、provider not found、設定不生效、TUI 無法啟動。
- 需要建立安裝、設定、驗收與故障排查清單。

## 核心判斷
| 方案 | API Key | Base URL |
|---|---|---|
| Pay-as-you-go | `sk-xxxxx` | `https://api.xiaomimimo.com/v1` |
| Token Plan | `tp-xxxxx` | `https://token-plan-cn.xiaomimimo.com/v1` |

不要混用 API Key 與 Base URL。

> 固定設定值（endpoint、CLI 版本、設定路徑）具版本敏感性；套用前先核對官方文件與使用者實際版本。未確認版本時先診斷，不直接建議修改。

## Hermes 規則
- 使用 custom provider 時，provider 必須是 `custom`。
- 不要把 Hermes custom provider 命名成 `xiaomi-coding`、`mimo` 或其他名稱。
- 設定檔重點：
  - `~/.hermes/config.yaml`
  - `~/.hermes/.env`
- 驗收順序：
  1. `hermes --version`
  2. `hermes doctor`
  3. `hermes` 或 `hermes --tui`
  4. 測試繁體中文回覆。

## OpenClaw 規則
- 需要 Node.js 22+。
- Pay-as-you-go 可走 onboarding Xiaomi preset。
- Token Plan 建議手動修改 `~/.openclaw/openclaw.json`。
- Token Plan provider 不要叫 `xiaomi`，可命名 `xiaomi-coding`。
- 若存在舊 `auth` 中的 Xiaomi preset，Token Plan 設定時需移除以避免混淆。

## 固定輸出格式
```markdown
## MiMo × Hermes × OpenClaw 設定診斷

## 1. 目前情境
- 工具：
- 使用方案：
- API Key 類型：
- Base URL：
- 錯誤訊息：

## 2. 可能原因
| 原因 | 檢查方式 | 修正 |
|---|---|---|

## 3. 修正步驟
### Hermes
### OpenClaw

## 4. 驗收清單
- [ ] API Key 與 Base URL 成對
- [ ] Provider 名稱正確
- [ ] Model 名稱正確
- [ ] 基礎 CLI／TUI 對話成功
```

## 安全與品質標準
- 不要求使用者貼出完整 API Key。
- 不在公開文件中保存 secret。
- 所有設定變更前先備份設定檔。
- 基礎 CLI／TUI 成功後，才接 gateway、skills、MCP、cron 或自動化。

## Opus 5 世代模型校準
### 安全項一律保留
「不要求貼出完整 API Key」「不在公開文件保存 secret」「變更前先備份」是安全邊界，不是可卸除的品質補強。

### 原因盤點要兩段式
**不要下「只列最可能的原因」「直接給最可能的解法」。** 設定類問題最常見的情況是兩三個原因疊加（Key 類型錯 + provider 命名錯），只給最可能的那一個會讓你反覆試錯。正確做法：第一輪把所有可能原因全部列進第 2 節表格，第二輪再依「檢查成本低到高」排出動手順序。

### 輸出長度
這是排錯型 Skill，輸出應該是**可直接照做的步驟加驗收清單**。不要附送 Hermes 與 OpenClaw 的架構介紹、各家 CLI 的比較，或 API 認證機制的原理說明，除非你問了。

### 驗收清單是給人勾的
第 4 節驗收清單是你在終端機實際跑一遍用的，保留。但不要在提示詞中追加「輸出修正步驟前再自我檢查一次」——真正能驗證設定對不對的是實際執行 `hermes doctor`，不是多一層 AI 講評。

### 範圍鎖定
使用者丟一則錯誤訊息就診斷那則錯誤。修好基礎 CLI／TUI 之前，不要主動把 gateway、skills、MCP、cron 的設定一起寫進來——這一條原本就在安全與品質標準裡，新世代模型更容易「順手多做」，要特別守住。

### 成本用 effort 控，不要關 thinking
設定這些 Agent 時，若想省 token 而在設定檔關閉 thinking，可能造成工具呼叫外洩成純文字與內部 XML 標籤外洩，在 TUI 環境下特別難判讀。要控成本請調 effort 等級。舊模型調好的 effort 預設值換新模型後要重新掃一次，不要直接沿用。

## 啟用提示詞
請啟用「MiMo × Hermes × OpenClaw 設定診斷 Skill」。任務：根據以下環境與錯誤訊息，找出設定問題並給出安全修正步驟。

---

## 標準執行契約

### 觸發與輸入

使用者明確要求此主題，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入與授權，標記缺口、敏感資料與可能的外部依賴。
2. 依本技能的核心流程逐步處理，將事實、推論、假設與建議分開。
3. 產出可直接審閱的結果，並列出引用、未驗證事項、風險與需要人工決策的節點。
4. 執行輸出前檢查，確認沒有虛構證據、洩漏敏感資料或超出使用者範圍的動作。

### 輸出契約

至少提供：

- **結果或草稿**：依使用者要求產出分析、策略、腳本、內容、清單或計畫。
- **假設與限制**：明確標示資料不足、未驗證推論與適用範圍。
- **驗證紀錄**：列出使用的來源、檢查方式或尚待確認的項目。
- **風險與下一步**：指出人工核准點、低成本驗證方式與可恢復的後續行動。

### 安全與人工核准

目前風險等級：**high**。需要人工確認。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。
- 此技能只提供分析、草稿與驗證建議，不代表法律、財務、醫療、投資或營運承諾；高風險決策須由合適的人員覆核。

### 禁止用途

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。
- 不得在沒有明確批准、完整上下文與可回溯驗證的情況下執行高影響外部操作。

### 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，先停止執行高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露或輸出無法驗證，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 無 有功能相近或可互補的既有技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/Skills_Full_Configurations_Backup_20260818.md` 的第 7 項正規化而來（原始行號 167–206）。來源內容已補上本 repository 的輸入、輸出、權限、安全與停止契約。

## Notion 同步紀錄

本技能的指令本文同步自 Notion「Skill 頁面整理庫」頁面 https://app.notion.com/p/790ebb8ac86a82b3874101a86cf26494（Notion 版本 v1.0，最後編輯 2026-09-24T01:52:48Z）。上方內容以 Notion 為準；標準執行契約為本 repository 的安全治理補充，同步時不會被覆蓋。
