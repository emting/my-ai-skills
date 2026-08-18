---
name: warp-ai-multi-agent
description: Warp AI Multi-Agent War Room Launch Configuration. Use when the user asks to configure Warp terminal launch configurations, set up multi-pane CLI agent layouts, or troubleshoot Warp terminal AI agent workflows.
---

# Warp Ai Multi Agent

## Warp AI Multi-Agent War Room

A skill for designing and configuring Warp Terminal Launch Configurations to create a multi-pane CLI AI Agent war room layout.

## When to Use

Use this skill when the user asks to:

  - Set up or configure Warp Terminal Launch Configurations

  - Create a multi-pane CLI Agent workspace (e.g., Amp, Codex, Gemini, Warp Agent)

  - Troubleshoot keybindings, terminal layouts, or launch scripts in Warp

## Default Configuration

Four-pane split layout:

  - Top-Left: Amp (large refactoring & multi-file editing)

  - Bottom-Left: Codex CLI (script generation)

  - Top-Right: Gemini CLI (long-context & multimodal analysis)

  - Bottom-Right: Status, logging, or token/cost monitor pane

\`\`\`yaml

name: AI Multi-Agent

windows:

  - tabs:

      - title: AI Command Center

        layout:

          split_direction: horizontal

          children:

            - layout:

                split_direction: vertical

                children:

                  - command: "amp"

                  - command: "codex chat"

            - layout:

                split_direction: vertical

                children:

                  - command: "gemini"

                  - command: "echo '[低風險] Ready — Warp Agent / Log Pane'"

## Workflow & Validation

1. Verify CLI tools are installed and callable in terminal environment.  
2. Generate or update the Warp Launch Configuration YAML block.  
3. Verify panel layout and keybindings to avoid terminal shortcut conflicts.  
4. Save to Warp Drive for cross-device synchronization if required.

## Gotchas

- Multiple terminal panes provide workspace layout, not mandatory simultaneous agent execution.  
- Do not spawn secondary agents solely to review primary agent outputs unless needed for parallel tasks.  
- Ensure the YAML configuration is complete and ready to paste into Warp editor.

---

## 二、 商業策略、創業與定價

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

此技能由 `docs/sources/Skills_Full_Configurations_Backup_20260818.md` 的第 10 項正規化而來（原始行號 257–345）。來源內容已補上本 repository 的輸入、輸出、權限、安全與停止契約。
