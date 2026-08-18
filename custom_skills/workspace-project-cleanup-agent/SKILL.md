---
name: workspace-project-cleanup-agent
description: Audit workspace projects, identify abandoned or duplicate work, and safely execute cleanup on git-tracked branches. Use when the user asks to clean up workspace, find abandoned or duplicate projects, or organize codebase projects.
---

# Workspace Project Cleanup Agent

工作區專案與程式碼庫的安全自動化稽核與清理流程。

## When to Use
- 使用者要求稽核工作區中的專案、清理廢棄或未完成的工作。
- 使用者希望整合重複程式碼或建立工作區清理計畫。

## Steps
1. **工作區掃描（Workspace Audit）**：
   - 掃描工作區內所有專案目錄，分析 Git 狀態（最後提交時間、未提交變更、未追蹤檔案）。
   - 識別「已放棄」（>6 個月未更新）、「重複」（類似目錄結構）與「未完成」（有 open TODO / Uncommitted changes）專案。
2. **隔離與備份（Branch Containment & Backup）**：
   - 自動切換至全新 Git 清理分支（如 `ai-cleanup-draft`），絕不直接在主分支（main/master）上作業。
3. **分級執行（Classified Execution）**：
   - **低風險（Direct Action）**：自動刪除空目錄、過期建置快取（`node_modules`、`.cache`、`dist` 可重新 install/build 者）、移除過期格式化暫存檔。
   - **高風險（User Proposal）**：涉及程式碼刪除、目錄搬移或專案合併，先寫入 `cleanup_plan.md`，列出刪除原因與恢復方法，等待使用者審核。
4. **輸出清單與彙報（Reporting）**：
   - 產出結構化清理報告，分類列出「已處理項目」與「待使用者確認項目」。

## Gotchas
- 嚴禁直接執行 `rm -rf` 刪除未受 Git 追蹤的原始碼檔案。
- 高風險檔案異動必須產生提案文件（`cleanup_plan.md`），等使用者確認後才可執行。

## 標準執行契約

### 觸發與輸入

使用者明確要求「workspace-project-cleanup-agent」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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
- 本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `system-file-audit-organizer` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `workspace-project-cleanup-agent/SKILL.md` 正規化而來，來源項目 SHA-256 為 `937d6f0753c1c6bc605e8cb43c4bea3e713092cbce958fcd318e43ead3992e82`，原始行號範圍為 1–27。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
