---
name: product-idea-scoring-matrix
description: Generate 100 product or SaaS ideas based on skills/interests and score each across market demand, execution difficulty, differentiation, startup cost, and time-to-first-revenue. Use when the user asks for 100 product ideas, SaaS ideation, or startup idea scoring matrix.
---

# Product Idea Scoring Matrix

基於技能與興趣的 100 個產品點子生成、5 維度定量評分與 MVP 路線圖。

## When to Use
- 使用者要求產生 100 個產品或創業點子。
- 需要依照市場需求、執行難度、差異化、成本與取勝時間進行客觀評分。

## Steps
1. **背景與技能輸入（Skill/Interest Context）**：
   - 提取使用者的核心技能、領域知識與興趣背景。
2. **100 個點子發想（Idea Generation）**：
   - 涵蓋微型 SaaS、AI 工具、自動化服務、數位產品與垂直社群產品。
3. **5 維度定量評分（5-Dimension Matrix Scoring）**：
   - 為每個點子建立 1-10 分評估：
     - 市場需求（Market Demand）
     - 執行難度（Execution Difficulty）
     - 差異化程度（Differentiation）
     - 啟動成本（Startup Cost）
     - 距離首筆收入時間（Time to First Revenue）
4. **Top 5 精選與驗證行動（Top Picks & Action Plan）**：
   - 篩選綜合得分最高的 Top 5 點子，提供最小可行性產品（MVP）驗證步驟與測試頁面文案。

## Gotchas
- 表格必須清晰美觀，支援分組與排序，方便使用者直接篩選決策。

## 標準執行契約

### 觸發與輸入

使用者明確要求「product-idea-scoring-matrix」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與可能的外部依賴，先列出缺口。
2. 依上方技能流程逐步處理，將事實、推論、假設與建議分開。
3. 產出可直接審閱的結果，列出引用、未驗證事項、風險與人工決策節點。
4. 執行輸出前檢查，確認沒有虛構證據、洩漏敏感資料或超出使用者範圍的動作。

## 輸出契約

至少提供：

- **結果或草稿**：依使用者要求產出分析、策略、腳本、內容、清單或計畫。
- **假設與限制**：明確標示資料不足、未驗證推論與適用範圍。
- **驗證紀錄**：列出使用的來源、檢查方式、驗收條件與尚待確認事項。
- **風險與下一步**：指出人工核准點、低成本驗證方式與可恢復的後續行動。

## 安全與人工核准

目前風險等級：**medium**。需要人工確認。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `ai-project-feasibility-assessment` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `product-idea-scoring-matrix/SKILL.md` 正規化而來，來源項目 SHA-256 為 `641d7aed3dfc168933ad00e0f25f20288957972c7f96b1b7aed1ee400d4a6648`，原始行號範圍為 1–29。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
