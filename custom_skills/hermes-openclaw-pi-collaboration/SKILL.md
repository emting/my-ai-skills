---
name: hermes-openclaw-pi-collaboration
description: 以 Hermes 規劃與驗收、OpenClaw 負責渠道排程與跨服務執行、Pi 負責程式庫內開發、Human 最終負責的本機三 Agent 協作架構，含任務契約、路由、安全閘門與知識沉澱。
---

# Hermes × OpenClaw × Pi × Obsidian｜本機三 Agent 協作架構與 SOP
> **定位**：以 Hermes 為規劃與驗收核心、OpenClaw 為常駐入口與跨服務執行者、Pi 為程式庫內工程執行者、Human 為最終責任人的本機三 Agent 協作架構。目標不是讓三個 Agent 同時回答，而是把每項工作交給最適合的一個執行者，並留下可追蹤、可驗收、可回滾的紀錄。

## 1. 適用情境與設計原則
適用於：
- 從 WhatsApp、Telegram、Slack 等渠道接收任務並持續處理
- 需要先規劃、再執行、最後客觀驗收的多步任務
- 程式開發、CLI 除錯、檔案整理與跨服務自動化並存的工作流
- 將成功經驗沉澱為 SOP、Skill Candidate 或專案規範
- 以 Obsidian Vault 作為 Agent 之間的共享狀態與稽核紀錄

### 核心原則
1. **預設單 Agent**：能由一個 Agent 完成，就不啟動三 Agent 流程。
2. **角色而非模型分工**：先決定責任與權限，再選模型。
3. **一項任務只有一位執行 Owner**：Pi 與 OpenClaw 不得同時修改同一資源。
4. **共享狀態靠檔案，不靠對話記憶**：Plan、執行證據、diff、錯誤與核准狀態都要落地。
5. **驗收依靠證據**：測試、Schema、diff、檔案雜湊、dry-run 與人工 Gate 優先於「再叫一個 Agent 講評」。
6. **高風險操作不可全自動**：刪除、部署、付款、對外傳送、權限變更與不可逆覆寫一律需 Human 核准。

## 2. 三 Agent 與 Human 的責任邊界
| 角色 | 核心定位 | 主要輸入 | 主要輸出 | 不得執行 |
|---|---|---|---|---|
| Hermes | Planner／Router／Reviewer／Librarian | Task Contract、執行證據、歷史 SOP | 版本化 Plan、路由決策、驗收結果、Skill／SOP 候選 | 無計畫的大量修改；取代客觀測試；自行核准高風險操作 |
| OpenClaw | Gateway／Ops Executor／Scheduler／Reporter | 渠道訊息、Hermes Plan、排程或事件 | 跨服務操作結果、通知、Execution Report | 複雜程式庫重構；擅自改目標；開放未知訊息來源 |
| Pi | Coding Executor／Debugger | Repo、AGENTS.md、Coding Task Contract | 程式碼 diff、測試結果、工程 Execution Report | 當總管或排程器；跨渠道發訊息；未授權部署與祕密操作 |
| Human | Owner／Approver | Agent 輸出、風險與取捨 | 優先順序、核准／拒絕、最終發布決策 | 把責任歸零給 Agent |

- **Hermes**（角色規範見 `hermes-agent-handbook`）：把模糊需求轉成 Task Contract；判定是否需要 Agent、是否拆分及路由；定義可修改範圍、Stop Rules、驗收方式與回滾方案；依證據驗收；將可複用流程整理為 Skill Candidate，未實跑不得升級為正式 Skill。
- **OpenClaw**（角色規範見 `openclaw-agent-handbook`）：常駐訊息入口、cron／事件觸發器與通知器；處理 repo 外的檔案、瀏覽器、訊息與跨服務操作；執行低至中風險、輸入清楚、可快速驗證的工作；coding 任務送交 Pi；以 allowlist、專用帳號、工作區隔離與最小權限限制工具能力。
- **Pi**：repo 內的讀取、修改、重構、測試、build、lint 與 CLI 除錯；先讀 `AGENTS.md`、README、測試與 package scripts；只修改 Task Contract 授權的檔案或模組；回傳 diff、指令、exit code、測試結果與未解問題；規劃、排程與跨服務協作由外層系統處理。

## 3. 任務路由決策
| 任務訊號 | Owner | 是否需要 Hermes Plan |
|---|---|---|
| git repo、程式碼、測試、build、lint、stack trace | Pi | 小修可用簡化契約；跨模組或高風險修改需要 |
| 訊息渠道、提醒、cron、監控、跨 App 搬移資料 | OpenClaw | 重複且低風險可直接依 SOP；其餘需要 |
| 模糊目標、跨領域取捨、多階段任務、風險判斷 | Hermes | 是 |
| 純問答或單次摘要，無工具與寫入 | 當前對話 Agent | 否 |
| 刪除、部署、付款、公開發布、寄信、權限變更 | 對應 Executor + Human Gate | 是，且執行前再次核准 |

```text
if 不需要工具且一次可完成:
    由當前 Agent 回答
elif 涉及不可逆、金額、對外承諾、權限或 production:
    Hermes 產 Plan → Human 核准 → 指定 Executor
elif 主要資源位於 git repository:
    Pi 執行
elif 主要資源位於訊息渠道、瀏覽器、排程或跨服務:
    OpenClaw 執行
else:
    Hermes 先釐清並指定唯一 Owner
```
> 不要依「哪個 Agent 比較聰明」路由。路由依據應是資源位置、工具需求、風險、可驗證性與責任邊界。

## 4. Obsidian Vault 與共享狀態
```text
00_Inbox/
10_Task_Contracts/
20_Hermes_Plans/
30_Execution/
  OpenClaw/
  Pi/
40_Hermes_Reviews/
50_Skills/
  Candidates/
  Validated/
60_SOP/
70_Artifacts/
80_Archives/
90_System/
  Templates/
  Policies/
  Metrics/
```
命名規則：
```text
TASK-YYYYMMDD-NNN_short-name.md
TASK-YYYYMMDD-NNN_plan-v01.md
TASK-YYYYMMDD-NNN_exec-openclaw-v01.md
TASK-YYYYMMDD-NNN_exec-pi-v01.md
TASK-YYYYMMDD-NNN_review-v01.md
```
單一寫入者原則：
- Task Contract：Human 或任務入口建立；Hermes 可補齊但不得隱藏「需確認」欄位。
- Plan：僅 Hermes 建立與改版。
- Execution Report：僅對應 Executor 寫入。
- Review：僅 Hermes 寫入。
- 正式 SOP／Skill：Human 核准後才可由指定 Agent 建立。
- 原始報告不可覆寫；更正一律建立新版本。

## 5. Task Contract：所有委派的共同入口
```yaml
task_id: TASK-20260903-001
title: ""
requester: human
objective: ""
context:
  sources: []
inputs: []
constraints:
  allowed_paths: []
  forbidden_paths: []
  allowed_tools: []
  prohibited_actions: []
risk: low | medium | high
owner: hermes | openclaw | pi | human
acceptance:
  - ""
budgets:
  max_steps: 8
  max_retries_per_step: 2
  max_tool_calls: 20
  deadline: null
human_gates: []
output_path: ""
```
任務尚不可委派的條件：
- 目標或成功標準無法判定
- 必要資料、帳號或路徑不存在
- 要求同時修改多個來源但未指定單一真實來源
- 高風險操作沒有核准人與回滾方案
- Agent 必須猜測使用者未提供的政策、數值或品牌取捨

遇到上述情況時，狀態設為 `needs_human`，不得自行補完假設。

## 6. Hermes Plan 契約
```yaml
plan_version: 1
route:
  owner: pi | openclaw
  reason: ""
preconditions: []
steps:
  - step_id: S01
    purpose: ""
    inputs: []
    tool_or_command: ""
    expected_output: ""
    verification: ""
    stop_rule: ""
    rollback: ""
risks: []
human_gate_before: []
acceptance_tests: []
```
Plan 的每個步驟必須是可獨立驗證的原子操作。若 Pi 與 OpenClaw 都需參與，必須拆成前後相依的階段，指定交接 artifact；禁止同時修改同一檔案或同一外部物件。

## 7. Executor 交接規格
### 給 Pi 的 Coding Task
除 Task Contract 外，至少提供：repository 路徑與目前 branch；必讀的 `AGENTS.md`／README／設計文件；可修改與禁止修改的路徑；啟動、測試、lint、build 指令；是否允許新增 dependency、migration、network access；完成時必須提供的 diff 與測試證據。
### 給 OpenClaw 的 Ops Task
除 Task Contract 外，至少提供：允許使用的渠道、帳號、workspace 與工具；allowFrom／收件人／目標 channel 白名單；可讀、可寫與禁止存取的目錄或服務；dry-run 與 commit 的分界；對外訊息草稿是否需 Human Gate；重試、超時、去重與通知政策。

## 8. Execution Report 統一格式
```json
{
  "task_id": "TASK-20260903-001",
  "executor": "pi | openclaw",
  "plan_version": 1,
  "status": "succeeded | partial | failed | needs_human",
  "completed_steps": [],
  "changes": [],
  "artifacts": [],
  "commands_or_tools": [],
  "tests": [],
  "deviations": [],
  "errors": [],
  "budgets": {"steps": 0, "tool_calls": 0, "retries": 0, "elapsed_ms": 0},
  "rollback_status": "not_needed | available | executed | unavailable",
  "next_action": null
}
```
Executor 不得只回報「已完成」。報告必須能讓 Hermes 和 Human 重現重要步驟，且不得包含 API key、token、cookie、個資或完整敏感 stdout。

## 9. Hermes Review 與客觀驗收
Review 順序：
1. 核對 task ID、Plan 版本與唯一 Executor。
2. 檢查是否越過 allowed paths／tools／recipients。
3. 執行或檢查客觀證據：測試、lint、build、Schema、diff、連結、檔案存在性。
4. 比對 acceptance criteria，不因報告寫得完整就判定通過。
5. 將結果標為：`passed`、`rework`、`needs_human` 或 `rejected`。
6. 判斷是否值得沉澱，但不得在同一步直接升級為正式 Skill。

```yaml
task_id: ""
plan_version: 1
verdict: passed | rework | needs_human | rejected
evidence_checked: []
acceptance_results: []
scope_violations: []
rework_items: []
residual_risks: []
knowledge_capture: none | sop_candidate | skill_candidate
```

## 10. 安全、權限與人工閘門
| 等級 | 例子 | 執行政策 |
|---|---|---|
| 低 | 唯讀查詢、摘要、格式轉換、測試 | 可依既有 SOP 自動執行 |
| 中 | 受限路徑寫檔、建立草稿、批次重新命名 | Plan + allowlist + 可回滾；視範圍抽查 |
| 高 | 刪除、production 部署、付款、寄送、公開發布、權限與祕密變更 | Hermes Plan + Human 明確核准 + dry-run + 執行後驗證 |

必要控制：
- 每個 Agent 使用不同工作目錄、帳號或 token；禁止共用高權限祕密。
- OpenClaw 渠道必須設定 allowlist；個人訊息與公開入口不得共用同一高權限 Agent。
- Pi 預設只能操作指定 repo；部署金鑰與 production credential 不放入 coding session。
- 所有寫入先備份、branch、transaction 或 dry-run；無法回滾須升級風險。
- 設定 max steps、retries、tool calls、token budget 與 deadline。
- 不把關閉 thinking 當作省成本方式；以 effort、模型路由與任務預算控制成本。

## 11. 失敗、阻塞與升級處理
| 狀況 | 處理方式 |
|---|---|
| 同一步驟暫時性錯誤 | 最多依 Plan 重試 2 次，保留錯誤證據 |
| Schema／參數錯誤 | 停止重試，修正契約或工具輸入 |
| 權限不足 | 標記 needs_human，不要求 Agent 繞過權限 |
| Plan 與現況矛盾 | Executor 停止；Hermes 建立新 Plan 版本 |
| 發現需修改額外檔案或收件人 | 不擴張範圍，先請求核准 |
| 測試失敗 | Pi 回報最小重現、錯誤與已嘗試修正；不得隱瞞 |
| 超過預算或 deadline | 輸出部分成果、阻塞與最小下一步，然後停止 |
| 不可回滾變更即將執行 | 強制 Human Gate |

## 12. 模型與成本路由
- Hermes：較強的規劃模型處理高歧義、跨步驟與高風險任務。
- OpenClaw：低延遲、工具呼叫穩定的 Worker 模型處理高頻操作。
- Pi：依程式語言、repository 大小、context 與測試難度選 coding 模型。
- 含圖片、圖表、UI 截圖時，單獨路由至可靠的多模態模型，再把結構化結果交回 Owner。
- 換模型後重新測量 tool-call 正確率、任務成功率、延遲與成本；不要沿用舊模型的 effort 預設值。

## 13. 可觀測性與最低指標
每次任務至少記錄：task ID、Plan 版本、Agent／模型版本、prompt／Skill 版本；開始與結束時間、工具次數、重試次數、token 或估算成本；status、錯誤分類、Human Gate 次數與驗收證據；是否發生範圍違規、重複寫入或回滾。
建議每月檢視：端到端成功率；每個成功任務的成本與工具呼叫數；返工率與人工介入率；越權攔截率（目標 100%）；P50／P95 完成時間；哪些任務應改成固定自動化。

## 14. Skill／SOP 沉澱規則
- **SOP Candidate**：適合固定、可預測、判斷少的操作流程。至少成功實跑一次，並包含輸入、步驟、例外、回滾與驗收。
- **Skill Candidate**：適合需要語意判斷，但觸發條件、輸入契約、輸出格式與品質標準都能寫清楚的重複任務。
- **升級 Gate**：至少一個真實成功案例；至少一個失敗或邊界案例；已移除環境專屬路徑、帳號、個資與祕密；Human 核准；建立版本號與最後驗證日。

固定流程優先改成 script、database automation 或 n8n；不要因為 Agent 能做，就永久保留成 Agent 任務。

## 15. 完整作業流程
1. **Intake**：OpenClaw、Human 或其他入口建立 Task Contract。
2. **Triage**：簡單任務直接處理；需要多步或風險判斷時交 Hermes。
3. **Plan／Route**：Hermes 指定唯一 Owner、驗收與 Stop Rules。
4. **Policy Gate**：低風險自動；中風險限制範圍；高風險等待 Human。
5. **Execute**：Pi 處理 repo 內工程；OpenClaw 處理渠道、排程與跨服務。
6. **Report**：Executor 寫入結構化 Execution Report 與 artifacts。
7. **Verify**：Hermes 依客觀證據驗收；需返工則建立明確 rework list。
8. **Close**：Human 處理殘餘取捨與對外發布。
9. **Capture**：建立 SOP／Skill Candidate 或歸檔。

## 16. 啟用提示詞
```text
請啟用「Hermes × OpenClaw × Pi × Obsidian 本機三 Agent 協作架構」。

任務：
【描述需求】

已知輸入：
【檔案、repo、渠道、連結或資料】

限制：
【可修改範圍、禁止操作、期限與成本】

要求：
1. 先判斷是否真的需要多 Agent；能單 Agent 完成就不要拆分。
2. 建立 Task Contract，未知欄位標記「需確認」，不得自行猜測。
3. 由 Hermes 指定唯一 Executor：repo 內工程交 Pi；渠道、排程與跨服務交 OpenClaw。
4. 列出客觀驗收、Stop Rules、回滾與 Human Gates。
5. 執行後產出統一 Execution Report；Hermes 依證據 Review。
6. 若可複用，只建立 SOP／Skill Candidate；未實跑與未核准不得升級正式版本。
```

## 17. 上線前驗證清單
- [ ] 用一個純 Pi coding 任務跑完整閉環
- [ ] 用一個純 OpenClaw 排程／跨服務任務跑完整閉環
- [ ] 測試 Plan 版本變更後，Executor 是否停止使用舊版
- [ ] 測試 forbidden path／recipient 是否確實被阻擋
- [ ] 測試工具錯誤、權限不足、超過重試與超過預算
- [ ] 測試 high-risk 任務在 Human 核准前不會執行
- [ ] 確認 Execution Report 不含祕密、個資與完整敏感輸出
- [ ] 確認 Pi 與 OpenClaw 不會同時寫入同一資源
- [ ] 確認所有成功判定都有測試、diff 或其他可重現證據
- [ ] 完成首次實跑後，更新「驗證狀態」與「最後驗證日」

## 標準執行契約

### 觸發與輸入

使用者明確要求「Hermes × OpenClaw × Pi × Obsidian｜本機三 Agent 協作架構與 SOP」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

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
- 對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。
- 涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。
- 本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。

- 不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。
- 不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 無 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能同步自 Notion「Skill 頁面整理庫」頁面 https://app.notion.com/p/521ebb8ac86a838bb73881add5fc2dd0（Notion 版本 v1.0，最後編輯 2026-09-03T14:10:31Z），本文 SHA-256 為 `2dcfbdac1bedd8b17f40595a69951e3e6e95f70cba8de0c90156254a17a279ed`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
