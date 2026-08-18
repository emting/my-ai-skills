---
name: multi-agent-research-workflow
description: An advanced multi-agent research workflow inspired by Claude Research architecture, enhanced with Full Sprint engineering controls. Use when conducting deep multi-perspective research, executing parallel subagent investigation tasks, or synthesizing research into actionable software engineering sprint contracts.
---

# Multi-Agent Research Workflow

A structured framework based on the Claude Research architecture (LeadResearcher, Subagents, CitationAgent, Memory/Checkpoints) and integrated with Full Sprint execution controls for performing deep, rigorous multi-perspective research and engineering delivery.

## When to Use

Use this skill when:
- The user requests deep research on a complex, multi-faceted topic requiring multiple sources.
- The task requires dividing a broad topic into distinct sub-topics researched in parallel.
- High accuracy, comprehensive coverage, and strict inline source citations ([Title](URL)) are required.
- The research leads into software development, code refactoring, or technical implementation (bridging with Full Sprint execution).

## Core Roles & Workflow

### 1. LeadResearcher (Planning & Strategy)
1. **Analyze Query & Classify Complexity**:
   - **Low**: Single-entity lookup. Execute directly without subagent overhead.
   - **Medium**: 2-3 sub-questions. Create 2-3 parallel research sub-tasks.
   - **High**: Multi-faceted or multi-entity investigation. Create 3-5 parallel sub-tasks.
2. **Strategy & Checkpoint Initialization**:
   - Deconstruct the user query into distinct, non-overlapping sub-queries.
   - Initialize a task tracking checklist (e.g. `task.md`) to maintain state and record milestones.

### 2. Subagents (Parallel Research & Tool Execution)
1. **Parallel Execution**:
   - Dispatch up to 3-5 concurrent subagents (`invoke_subagent`) to investigate specific sub-topics.
2. **Iterative Search & Retrieval**:
   - Subagents query web sources, Google Workspace (Drive, Gmail, Docs), or code execution tools.
   - Evaluate results critically for source quality, authority, and freshness.
3. **Synthesis & Refinement**:
   - Subagents summarize key findings, extract direct facts, and retain raw source URLs for grounding.

### 3. CitationAgent (Fact Grounding & Citation)
1. **Map Claims to Concrete Sources**:
   - Verify every factual claim against the returned tool outputs.
   - Every claim derived from external or internal tools MUST include clickable inline markdown citations: `[Title](URL)`.
2. **No Uncited Claims**:
   - Eliminate or rephrase ungrounded claims where no source URL exists.

### 4. Sprint Bridge & Engineering Handoff (Full Sprint Alignment)
When research scope touches technical implementation, refactoring, or code deliverables:
1. **Draft Sprint Contract**:
   - Define **Allowed Scope** and **Do Not Touch** boundaries.
   - Specify **Acceptance Criteria** and **Stop Rules**.
2. **Test Protection & Verification Strategy**:
   - Define expected unit/integration test coverage before executing code changes.
3. **Execution Report Generation**:
   - Produce a change manifest, test validation output, and delta summary for seamless handoff to `full-sprint-execution`.

### 5. Memory & Quality Control
1. **Progress Verification**:
   - Update checklist status upon completing each research milestone.
2. **LLM-as-Judge Evaluation**:
   - Assess research output against key criteria: Factuality, Citation Accuracy, Coverage Completeness, and Source Diversity.
3. **Retry & Fallback**:
   - If a sub-topic has low coverage or failed search, perform a targeted follow-up lookup before finalizing.

## Gotchas & Principles

- **Avoid Over-Engineering**: Do not spawn 3-5 subagents for simple lookups. Match subagent count to query complexity.
- **Strict Citation Rules**: Never use bracketed numeric references like `[1]` or `[1, 2]`. Always use `[Source Title](URL)`.
- **Prevent Duplication**: Ensure subagent queries do not overlap so research context remains efficient and focused.
- **Respect Rate & Execution Limits**: Limit concurrent tool calls and manage subagent payloads cleanly.

## 標準執行契約

### 觸發與輸入

使用者明確要求「multi-agent-research-workflow」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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

目前風險等級：**medium**。預設可先產出分析或草稿，但仍不得代替使用者做外部高影響決策。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

- 先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。
- 不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。
- 只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。
- 外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 `ai-research-lab`、`research-to-insight` 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `docs/sources/skills_export_20260818.zip` 內的 `multi-agent-research-workflow/SKILL.md` 正規化而來，來源項目 SHA-256 為 `0d403e4f3469165a3db2138c9be7b04aabd340b5c1f80baa1cf68baf527e0bc9`，原始行號範圍為 1–67。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
