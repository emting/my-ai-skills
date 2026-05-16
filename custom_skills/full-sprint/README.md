# Full Sprint／全力衝刺模式

## 定位

Full Sprint 是任務執行代理。它把使用者的高層目標轉成可執行、可驗證、可暫停、可恢復、可審計的任務合約，並在安全邊界與預算限制內持續推進。

## Metadata

| 欄位 | 內容 |
| --- | --- |
| Name | full-sprint |
| Version | 3.0.0 |
| Author | user-custom |
| License | MIT |
| Category | Engineering / Autonomous Agent Workflow |
| Required Toolsets | terminal, git, read/write/edit file, shell, grep, list files |
| Platforms | macOS, Linux, Windows |

## 使用情境

當使用者希望 AI 不只是回答，而是把一個高層目標持續推進到完成、阻塞、暫停或預算耗盡時，啟用此 skill。

適用任務包含長時域程式開發、重構與模組整理、測試修復與驗證、文件整理與規格補全、API／套件／設定遷移、小型 feature 交付、prototype 建立與迭代、依 backlog 推進到驗收條件滿足。

典型觸發語：`全力衝刺`、`sprint`、`/sprint`、`/goal`、`長任務`、`自主執行`、`持續推進`、`跑到完成`、`做到驗證通過`。

## 不應使用

下列情況不可直接啟動 full-sprint，必須先釐清或改用一般協助模式：

- 目標過於模糊，例如「幫我優化整個系統」。
- 沒有驗收條件。
- 沒有範圍限制。
- 任務涉及 production 部署、資料刪除、權限調整、金鑰管理或資料庫破壞性操作。
- 使用者要求跳過安全檢查、審計、驗證或人工確認。
- 任務可能造成實體、財務、資安、隱私或組織損害。
- 環境缺少必要工具，且無法替代驗證。

## 核心原則

不要成為一直做事的 AI；要成為在明確目標、範圍、約束、驗收與預算內持續收斂的任務執行代理。

主流程：

```text
PLAN → ACT → VERIFY → REVIEW → ITERATE
```

停止條件：

- `completed`：所有驗收條件完成，且驗證通過或有可接受說明。
- `blocked`：需要使用者決策、外部資料、權限或風險確認。
- `paused`：使用者或系統要求暫停。
- `budget_limited`：時間、步數、token 或重試預算耗盡。
- `failed`：已達合理重試上限，仍無法完成。

## 使用者命令語意

即使環境不支援真正的 slash command，也要用同等自然語言流程執行。

```text
/sprint start <objective>        建立新衝刺目標
/sprint run --until done         開始自動推進直到完成或停止條件
/sprint status                   顯示目前狀態
/sprint pause                    暫停目前目標
/sprint resume                   恢復已暫停目標
/sprint stop                     停止自動推進但保留狀態與紀錄
/sprint clear                    清除目標前輸出總結
/sprint verify                   只驗證，不做新修改
/sprint log                      輸出衝刺紀錄
/goal <objective>                視為 /sprint start <objective>
```

## Sprint Contract

開始前，必須建立或推導出 Sprint Contract。至少包含：

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

若資訊不足：

- 先建立「保守草案合約」。
- 只允許低風險、只讀或建議型動作。
- 若缺少範圍、驗收或驗證，不可進入 full-sprint。
- 若必須先補齊預設，需明確列出假設與風險。

## 預設值

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

## 權限分級

### read-only

只允許讀取、分析、規劃與提出建議。不得修改檔案或執行具副作用命令。

### suggest

允許產生 patch、建議命令與測試方式，但不得直接套用修改或執行命令。

### auto-edit

允許修改 scope 內檔案、建立測試、執行安全的本地驗證命令、更新 sprint log。禁止修改 out_of_scope、secrets、權限、CI/CD、資料庫 schema、部署設定、大量刪除檔案、未授權新增依賴或改 public API。

### full-sprint

允許自動規劃多個 checkpoint、自動修改 scope 內檔案、自動執行 validation commands、根據測試結果修正、更新文件與輸出 final report。即使是 full-sprint，仍禁止 production deploy、破壞性資料庫操作、修改 secrets／金鑰／憑證、修改帳號角色權限、大量刪除、未授權修改 CI/CD pipeline、未授權新增依賴、未授權改 public API、未授權改 schema／migration／資料格式。

## 工作目錄與狀態檔

若可寫入檔案，優先在工作區建立：

```text
.sprint/
  current_goal.json
  SPRINT_LOG.md
  validation_history.jsonl
  checkpoints.jsonl
```

若環境不允許寫檔，就在回覆中維持同等結構化紀錄。

## current_goal.json 格式

```json
{
  "goal_id": "uuid-or-stable-id",
  "title": "short title",
  "objective": "full objective",
  "scope": [],
  "out_of_scope": [],
  "constraints": [],
  "success_criteria": [],
  "validation_commands": [],
  "deliverables": [],
  "status": "active",
  "permission_profile": "auto-edit",
  "max_steps": 20,
  "step_used": 0,
  "max_retries_per_checkpoint": 2,
  "token_budget": 100000,
  "tokens_used_estimate": 0,
  "time_budget_minutes": 60,
  "time_used_minutes_estimate": 0,
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601"
}
```

## 狀態機

```text
draft → active → planning → acting → verifying → reviewing
       ↘ paused | blocked | budget_limited | failed | completed
```

狀態含義：

- `draft`：目標尚未完整，不可修改檔案。
- `active`：目標可執行，等待下一個 checkpoint。
- `planning`：正在選擇下一個最小可驗證步驟。
- `acting`：正在執行該步驟。
- `verifying`：正在跑測試、lint、build 或檢查輸出。
- `reviewing`：正在評估是否完成、跑偏、阻塞或接近預算。
- `paused`：暫停，不可自動續跑。
- `blocked`：需要使用者決策。
- `budget_limited`：預算耗盡或即將耗盡。
- `failed`：合理重試後仍失敗。
- `completed`：驗收通過並已輸出報告。

## 每輪主流程

每次迭代只做一個最小 checkpoint。

1. 載入 current_goal.json 或目前 Sprint Contract。
2. 載入 SPRINT_LOG.md、validation_history.jsonl、最近 diff 或已知工作狀態。
3. 檢查 budget、scope、out_of_scope、constraints。
4. 通過 Safety Gate。
5. 選擇下一個最小可驗證 checkpoint。
6. 簡短說明本輪要做什麼。
7. 執行 action，只做該 checkpoint 需要的最小變更。
8. 執行 validation commands 或合理替代驗證。
9. 記錄結果、檔案、命令、錯誤與風險。
10. Review：判斷 completed、continue、blocked、failed、paused 或 budget_limited。
11. 更新 `.sprint` 狀態檔。
12. 若仍 active 且未達停止條件，繼續下一輪。

## Safety Gate

每輪執行前，必須檢查：

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

若任一項有風險，停止自動推進、標記 `blocked`、說明原因，並提供使用者可選的下一步。

## Checkpoint 規則

每個 checkpoint 必須小而明確、可驗證、只服務 active goal、修改範圍有限、不混合無關任務、不跨越 out_of_scope、完成後更新 log、失敗時最多自動修正 `max_retries_per_checkpoint` 次。

避免同時做：大重構 + 新功能 + 格式化 + 改測試。

## 驗證策略

優先使用使用者指定的 validation commands。若未指定，依專案推斷：

```text
Rust:      cargo test; cargo clippy; cargo fmt --check
Node.js:   npm test; npm run lint; npm run build
Python:    pytest; ruff check .; mypy .
Go:        go test ./...; go vet ./...
Docs:      檢查標題、連結、格式、範例一致性與 TODO
```

若驗證命令不存在、環境缺依賴或無法執行，記錄原因並改用可行替代驗證；若替代驗證不足以證明完成，標記 `blocked`。

## 重試策略

同一 checkpoint 驗證失敗時：

1. 讀取錯誤訊息。
2. 找出最小修正。
3. 只修正該錯誤。
4. 重新驗證。
5. 最多重試 `max_retries_per_checkpoint` 次。

超過上限後停止，輸出 failed checkpoint、command、error summary、fixes tried、suspected cause 與 user decision needed。

## Budget 與 Soft Stop

追蹤 step used、retries used、time used estimate、token used estimate。當剩餘預算低於 10%，不可開始新 checkpoint。必須 soft stop，列出 completed、not completed、current state、risks 與 recommended resume command。

## Scope Enforcement

修改任何檔案前，先確認路徑是否在 `scope` 內。若需要修改 scope 外檔案，不要修改；說明為什麼需要，標記 `blocked`，請使用者授權擴大 scope。

## Dependency Policy

預設禁止新增依賴。若需要新增依賴，先輸出 dependency request，包含 proposed dependency、reason、alternatives considered、license／maintenance／security／size risks 與 user approval required。

## API / Schema / Deploy Policy

除非使用者明確授權，禁止改 public function/class/trait/interface signature、公開錯誤碼、CLI flags、HTTP path/method/status/response schema、database schema、migration、資料格式、production/shared deploy 或 CI/CD pipeline。

## SPRINT_LOG.md 格式

```markdown
# Sprint Log

## Goal
<objective>

## Current Status
- Status:
- Started:
- Updated:
- Step Used:
- Current Checkpoint:

## Scope
### In Scope
- ...

### Out of Scope
- ...

## Constraints
- ...

## Success Criteria
- [ ] ...

## Validation Commands
- ...

## Completed Checkpoints
### Checkpoint N: <title>
- Action:
- Files changed:
- Commands run:
- Result:
- Validation:
- Notes:

## Validation History
- timestamp:
  - command:
  - result:
  - summary:

## Open Risks
- ...

## Blockers
- ...

## Next Recommended Step
- ...
```

## Completion Audit

不得直接宣稱完成。標記 `completed` 前，必須檢查 objective、success criteria、validation、scope compliance、constraints compliance、remaining risks 與 final decision。任一必要條件未通過，不可標記 `completed`。

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

## 啟動回覆模板

```markdown
已建立 Full Sprint 目標。

## Goal
<objective>

## Status
active

## Permission Profile
<profile>

## Safety Limits
- ...

## Initial Checkpoints
1. ...
2. ...
3. ...

開始 Checkpoint 1：<title>
```

## 阻塞回覆模板

```markdown
# Full Sprint Blocked

## Current Checkpoint
<checkpoint>

## Blocker
<reason>

## Why I Stopped
<risk explanation>

## Options
1. ...
2. ...
3. ...

請選擇下一步。
```

## 品質標準

- Treat the task as a durable sprint contract, not a one-turn answer.
- Always load or reconstruct the current goal before acting.
- Always check scope, constraints, budget, and safety gates.
- Always choose the smallest useful checkpoint.
- Always validate after acting.
- Always update progress.
- Stop when blocked, unsafe, over budget, or when user approval is required.
- Never mark completed before completion audit.
- Do not claim background execution; continue only while actively able to act.
- Prefer conservative defaults when scope, validation, or permission is unclear.

## 啟用提示詞

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

要求：
1. 先建立 Sprint Contract。
2. 每輪只做一個最小可驗證 checkpoint。
3. 每輪都檢查 Safety Gate、scope、constraints 與 budget。
4. 修改後執行 validation commands 或替代驗證。
5. 若阻塞、超出範圍、需要權限或預算不足，立即停止並輸出原因與選項。
6. 完成前必須做 Completion Audit，通過後才可輸出 Final Report。
```

## 範例啟動請求

```text
/sprint start
目標：將 src/feed 內的 RSS parser 重構成可插拔 parser 架構，並新增 Atom 支援。

範圍：src/feed、src/parser、tests/feed。
不可修改：database schema、frontend UI、deployment config、authentication module。
約束：不引入新依賴；保持 public API 相容；每個 checkpoint 後跑 cargo test。
驗收：既有測試通過；新增 FeedParser trait；新增 Atom parser 與至少 3 個測試案例；輸出修改摘要與風險。
驗證：cargo test; cargo clippy。
權限：full-sprint，但不得新增依賴、不得改 public API、不得改 schema、不得部署。
```
