---
name: ui-minimalist-animation-enhancer
description: Refine web/app UI for minimalism, improve information hierarchy, and add fluid entrance and exit animations. Use when the user asks to improve UI, add entrance/exit animations, simplify layout, or make interface aesthetic and clean.
---

# UI Minimalist Animation Enhancer

UI 介面極簡化重構、資訊層級優化與流暢進退場動畫建立。

## When to Use
- 使用者要求改善 App / Web UI 介面視覺與資訊架構。
- 使用者需要為元件加入進場／退場動畫。

## Steps
1. **資訊架構視覺稽核（UI & IA Audit）**：
   - 檢視元件層級、視覺雜訊（Noise）與對比度。
   - 刪除冗餘裝飾元素，落實極簡主義（Minimalist Design）。
2. **動畫系統建立（Animation Design）**：
   - 選擇適合的動畫庫（如 Framer Motion, CSS Keyframes, Tailwind Animate）。
   - 為卡片、彈窗、列表項目加入自然流暢的進場（Ease-in-out, 150-300ms）與退場動畫。
3. **資訊層級優化（Information Hierarchy Refinement）**：
   - 調整字體大小、字重與留白（Padding/Margin），讓使用者一眼能判讀核心資訊。
4. **預覽與驗收（Verification）**：
   - 檢查動畫是否具備可關閉選項（`prefers-reduced-motion` 友善支援）。
   - 提供修改前後的介面範例說明。

## Gotchas
- 動畫時間嚴格控制在 150ms - 300ms 之間，過長動畫會損害使用者體驗。
- 保留資訊層級優先於純粹視覺效果。

## 標準執行契約

### 觸發與輸入

使用者明確要求「ui-minimalist-animation-enhancer」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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

目前風險等級：**high**。需要人工確認。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。
- 本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `design-proposal-portfolio-persuasion` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `ui-minimalist-animation-enhancer/SKILL.md` 正規化而來，來源項目 SHA-256 為 `a23c3a77ee8ca4a9801e267ea5ded6bbcfe480c3cc05f78b71888cb2474dc6c1`，原始行號範圍為 1–28。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
