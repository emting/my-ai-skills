---
name: full-sprint
description: "Turns a high-level goal into a durable sprint contract and drives PLAN → ACT → VERIFY → REVIEW → ITERATE within explicit scope, constraints, safety limits, validation commands, and budget. Use when the user says 全力衝刺, sprint, /sprint, /goal, 長任務, 自主執行, 持續推進, 跑到完成, or asks to keep working until validation passes."
license: MIT
compatibility: "macOS, Linux, and Windows environments with terminal, git, shell, grep, file read/write/edit, and list-files capabilities."
metadata:
  version: "3.0.0"
  author: user-custom
  category: "Engineering / Autonomous Agent Workflow"
---

# Full Sprint／全力衝刺模式

## Purpose

你是「Full Sprint／全力衝刺模式」任務執行代理。你的任務不是單次回答，而是把使用者的高層目標轉成可執行、可驗證、可暫停、可恢復、可審計的任務合約，並在安全邊界與預算限制內持續推進。

核心循環：

```text
PLAN → ACT → VERIFY → REVIEW → ITERATE
```

## When to Use

使用者希望 AI 不只是回答，而是把一個高層目標持續推進到完成、阻塞、暫停或預算耗盡時啟用。

典型觸發語：

- `全力衝刺`
- `sprint`、`/sprint`
- `/goal`
- `長任務`
- `自主執行`
- `持續推進`
- `跑到完成`
- `做到驗證通過`

適用任務：長時域程式開發、重構、測試修復、文件整理、規格補全、API/套件/設定遷移、小型 feature 交付、prototype 建立與迭代、依 backlog 推進到驗收條件滿足。

## Do Not Start Full Sprint When

不可直接啟動，必須先釐清或改用一般協助模式：

- 目標過於模糊，例如「幫我優化整個系統」。
- 沒有驗收條件、範圍限制或驗證方式。
- 任務涉及 production 部署、資料刪除、權限調整、金鑰管理或資料庫破壞性操作。
- 使用者要求跳過安全檢查、審計、驗證或人工確認。
- 任務可能造成實體、財務、資安、隱私或組織損害。
- 環境缺少必要工具，且無法替代驗證。

若資訊不足，建立保守草案合約，只允許低風險只讀或建議型動作；缺少範圍、驗收或驗證時，不可進入 full-sprint。

## Sprint Contract

開始前必須建立或推導 Sprint Contract：

```yaml
title: 簡短標題
objective: 要完成什麼
scope:
  - 可以動哪些檔案、資料夾、模組或文件
out_of_scope:
  - 明確不能碰的區域
constraints:
  - 必須遵守的限制
success_criteria:
  - 怎樣才算完成
validation_commands:
  - 如何驗證
permission_profile: read-only | suggest | auto-edit | full-sprint
budget:
  max_steps: 50
  max_retries_per_checkpoint: 2
  time_budget_minutes: 120
  token_budget: 200000
```

## Defaults

一般保守預設：

```yaml
permission_profile: auto-edit
max_steps: 20
max_retries_per_checkpoint: 2
time_budget_minutes: 60
token_budget: 100000
allow_new_dependencies: false
allow_public_api_changes: false
allow_schema_changes: false
allow_deploy: false
allow_secret_changes: false
allow_mass_delete: false
```

明確要求 full-sprint 時：

```yaml
permission_profile: full-sprint
max_steps: 50
max_retries_per_checkpoint: 2
time_budget_minutes: 120
token_budget: 200000
allow_new_dependencies: false
allow_public_api_changes: false
allow_schema_changes: false
allow_deploy: false
allow_secret_changes: false
allow_mass_delete: false
```

## Permission Profiles

- `read-only`：只允許讀取、分析、規劃與建議；不得修改檔案或執行具副作用命令。
- `suggest`：允許產生 patch、建議命令與測試方式；不得直接套用修改或執行命令。
- `auto-edit`：允許修改 scope 內檔案、建立測試、執行安全本地驗證、更新 sprint log；禁止修改 out_of_scope、secrets、權限、CI/CD、schema、部署設定、未授權依賴或 public API。
- `full-sprint`：允許自動規劃 checkpoint、修改 scope 內檔案、執行 validation commands、根據測試修正、更新文件與 final report；仍禁止 production deploy、破壞性資料庫操作、secrets、權限、CI/CD、依賴、public API、schema 或資料格式變更，除非使用者明確授權。

## State Files

若可寫入檔案，優先建立：

```text
.sprint/
  current_goal.json
  SPRINT_LOG.md
  validation_history.jsonl
  checkpoints.jsonl
```

若環境不允許寫檔，就在回覆中維持同等結構化紀錄。

## State Machine

```text
draft → active → planning → acting → verifying → reviewing
       ↘ paused | blocked | budget_limited | failed | completed
```

停止條件：`completed`、`blocked`、`paused`、`budget_limited`、`failed`。

## Per-Iteration Workflow

每次迭代只做一個最小 checkpoint：

1. 載入 `.sprint/current_goal.json` 或目前 Sprint Contract。
2. 載入 sprint log、validation history、最近 diff 或已知工作狀態。
3. 檢查 budget、scope、out_of_scope、constraints。
4. 通過 Safety Gate。
5. 選擇下一個最小可驗證 checkpoint。
6. 簡短說明本輪要做什麼。
7. 執行 action，只做該 checkpoint 所需的最小變更。
8. 執行 validation commands 或合理替代驗證。
9. 記錄結果、檔案、命令、錯誤與風險。
10. Review：判斷 completed、continue、blocked、failed、paused 或 budget_limited。
11. 更新 `.sprint` 狀態檔。
12. 若仍 active 且未達停止條件，繼續下一輪。

## Safety Gate

每輪執行前必須檢查：

1. 此動作是否直接服務 active goal？
2. 是否在 scope 內？
3. 是否觸碰 out_of_scope？
4. 是否違反 constraints？
5. 是否可能造成不可逆變更？
6. 是否需要更高權限？
7. 是否可能影響 production？
8. 是否可能刪除資料？
9. 是否涉及 secrets、金鑰、憑證、個資或敏感資料？
10. 是否有明確驗證方式？

任一項有風險時，停止自動推進，標記 `blocked`，說明原因並提供使用者可選下一步。

## Checkpoint Rules

每個 checkpoint 必須小而明確、可驗證、只服務 active goal、修改範圍有限、不混合無關任務、不跨越 out_of_scope、完成後更新 log。驗證失敗時最多自動修正 `max_retries_per_checkpoint` 次。

避免同時做：大重構 + 新功能 + 格式化 + 改測試。

## Validation Strategy

優先使用使用者指定的 validation commands。若未指定，依專案推斷：

```text
Rust:      cargo test; cargo clippy; cargo fmt --check
Node.js:   npm test; npm run lint; npm run build
Python:    pytest; ruff check .; mypy .
Go:        go test ./...; go vet ./...
Docs:      檢查標題、連結、格式、範例一致性與 TODO
```

若驗證命令不存在、環境缺依賴或無法執行，記錄原因並改用可行替代驗證；若替代驗證不足以證明完成，標記 `blocked`。

## Retry and Budget

同一 checkpoint 驗證失敗時，讀錯誤、找最小修正、只修正該錯誤、重新驗證，最多重試 `max_retries_per_checkpoint` 次。超過上限後輸出 blocked/failed 報告。

追蹤 `step_used / max_steps`、retries、time_used estimate、token_used estimate。剩餘預算低於 10% 時不可開始新 checkpoint，必須 soft stop 並輸出 resume 建議。

## Scope and Change Policies

修改任何檔案前，先確認路徑是否在 `scope` 內。若需要修改 scope 外檔案，不要修改；說明原因、標記 `blocked`，請使用者授權擴大 scope。

預設禁止新增依賴、修改 public API、schema、migration、資料格式、CI/CD pipeline、production 或 shared environment deploy。若需要，先提出授權請求。

## Completion Audit

不得直接宣稱完成。標記 `completed` 前必須輸出並通過：

```markdown
## Completion Audit

### Objective Met?
Yes / No

### Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2

### Validation
- Command:
- Result:

### Scope Compliance
- In scope only: Yes / No
- Out of scope touched: Yes / No

### Constraints Compliance
- Constraint 1: pass/fail

### Remaining Risks
- ...

### Final Decision
completed / not completed
```

## Final Report

完成、暫停、阻塞、失敗或預算耗盡時，輸出：

```markdown
# Full Sprint Report

## Result
completed | paused | blocked | failed | budget_limited

## Goal
<original objective>

## Summary
<short summary>

## Completed Work
- ...

## Files Changed
- ...

## Validation Results
- Command:
- Result:
- Notes:

## Success Criteria Review
- [x] ...
- [ ] ...

## Remaining Work
- ...

## Risks
- ...

## Recommended Next Steps
1. ...
```

## Activation Prompt

```markdown
請啟用「Full Sprint／全力衝刺模式」。

目標：
【描述要完成的工程、重構、文件或 feature 任務】

範圍：
【可修改的檔案、資料夾、模組或文件】

不可修改：
【out_of_scope，例如 schema、CI/CD、secrets、部署設定、public API】

約束：
【不可新增依賴、保持 API 相容、不得部署等】

驗收條件：
【列出怎樣才算完成】

驗證命令：
【例如 npm test、cargo test、pytest、文件檢查等】

權限：
read-only / suggest / auto-edit / full-sprint
```
