# my-ai-skills

[![Validate skills library](https://github.com/emting/my-ai-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/emting/my-ai-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

這是一個公開、MIT 授權的 AI Skills Library，用於集中管理可被 AI Agent、Coding Assistant、Automation Agent 讀取與調用的技能、腳本、工作流程與 API 規格。專案目前以本地 Markdown instructions、JSON manifests 與資料分析 CLI 為核心；外部 API 與 MCP 設定採明確標示的 optional contract，不代表 repository 已經內建或啟動任何 production service。

> **目前定位：** 可供個人與社群共同維護的 skills prototype。所有涉及第三方服務寫入、部署、預算、憑證或破壞性操作，仍必須依照 skill manifest 與 `SECURITY.md` 的人工批准規則執行。

本版本已將使用者提供的 `Skills_Full_Configurations_Backup_20260818.md` 中 **66 項 skills** 逐一正規化並納管至 `custom_skills/`。每一項都具備獨立的 `SKILL.md`、`manifest.json`、來源行號、輸入／輸出契約、權限宣告、風險分級、人工核准點與停止條件；完整索引請見 [`docs/skill-archive-catalog.md`](docs/skill-archive-catalog.md)。

本儲存庫目標是支援以下使用情境：

- Warp / Terminal AI 讀取任務說明
- Manus 類自主 Agent 執行工作流程
- Codex / GitHub Copilot 協助開發與維護技能
- AMP Code 類 AI Coding Agent 理解專案結構
- 支援 OpenAPI 的 Agent 調用 HTTP API
- 支援 MCP 的 Agent 連接本地或遠端工具

## Developer Quick Start

本章是給**要新增、修改、驗證或提交自訂 AI skill 的開發者**使用的最短完整路徑。閱讀本章後，你應該能在本地建立一個可被 Agent 發現、可被 validator 驗證、具備安全邊界，並能透過 Pull Request 維護的 skill。

> **核心原則：** `SKILL.md` 負責人類與 Agent 可讀的工作流程；`manifest.json` 是機器可讀的契約來源；`skills.json` 只是快速索引。三者必須保持一致，且任何外部寫入、部署、付費、帳戶或破壞性操作都必須明確停在人工批准點。

### 1. 開始前：安裝與驗證 repository

請先取得完整 repository 與 submodules，並使用隔離的 Python 環境執行工具：

```bash
git clone --recurse-submodules https://github.com/emting/my-ai-skills.git
cd my-ai-skills
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git submodule update --init --recursive
```

先跑一次現況品質閘門，確認問題來自你的變更，而不是工作環境：

```bash
python scripts/validate_repo.py
pytest -q
python -m compileall -q custom_skills tests scripts
python scripts/self_assessment.py
```

完整的契約說明位於 [`docs/manifest-contract.md`](docs/manifest-contract.md)；貢獻規則位於 [`CONTRIBUTING.md`](CONTRIBUTING.md)；安全與漏洞回報規則位於 [`SECURITY.md`](SECURITY.md)。

### 2. 了解一個 skill 的目錄結構

每個本地 skill 至少包含 `SKILL.md` 與 `manifest.json`。可執行 skill 另外需要 entrypoint、依賴與測試：

```text
custom_skills/my-skill/
├── SKILL.md                 # 人類與 Agent 閱讀的流程、邊界與輸出規則
├── manifest.json            # 機器可讀的權威契約
├── run.py                   # 可選；runtime 不是 instruction_only 時的實際入口
├── examples/                # 可選；去識別化且可公開的範例資料
└── tests/                   # 可選；技能專屬測試，敏感資料技能建議必備
```

`entrypoint` 必須是相對於 skill 目錄的有效路徑。只有真正存在且可執行的 adapter 才能宣告 `python`、`node`、`shell` 或 `http` runtime；沒有實際 adapter 的技能應使用 `instruction_only`，不得假裝已連接外部服務。

### 3. 新增一個 instruction-only skill

先建立穩定的 skill ID。ID 只能使用小寫字母、數字、連字號或底線；不要使用日期、個人名稱或會隨意改變的行銷標語。版本採 `MAJOR.MINOR.PATCH`：輸出或契約不相容時提高 major，新增相容能力時提高 minor，純文件或修正錯誤時提高 patch。

```bash
mkdir -p custom_skills/my-skill
touch custom_skills/my-skill/SKILL.md
```

`SKILL.md` 必須只有一個 H1，並具備以下標準段落。標題可依語言調整，但建議直接使用專案標準標題，讓 validator 與 reviewer 容易檢查：

```markdown
# My Skill

一句話說明這個 skill 解決的問題、適用對象與主要邊界。

## 觸發與輸入

說明什麼任務應啟用本 skill、需要哪些輸入、哪些情況不應啟用。

## 標準執行契約

1. 先確認目標、範圍、資料來源、授權與驗收條件。
2. 以最小必要資料執行工作，記錄假設與不確定性。
3. 在輸出前執行自我檢查，不捏造來源、結果或已完成的外部操作。

## 輸出契約

列出輸出格式、必要欄位、引用或證據要求、品質檢查與失敗時的回報方式。

## 安全與人工核准

說明敏感資料、網路、第三方處理、檔案寫入、部署、付費與帳戶操作的限制。

## 停止條件

列出授權不明、資料不完整、來源矛盾、目標漂移、風險升高或無法驗證時必須停止的情況。

## 關聯技能

列出相近技能、優先選擇規則與何時交接給其他 skill；沒有關聯時明確寫出「無」。

## 來源追蹤

說明規則、模板或資料的來源；若為原創，寫明 `original` 與版本。
```

接著建立 `manifest.json`。以下是低風險、無外部連線、instruction-only skill 的最小可用範例；實際專案仍應依資料流與風險調整：

```json
{
  "id": "my-skill",
  "name": "My Skill",
  "version": "0.1.0",
  "description": "A concise description of the skill and its boundary.",
  "entrypoint": "SKILL.md",
  "runtime": "instruction_only",
  "inputs": {
    "request": {"type": "string", "required": true}
  },
  "outputs": {
    "result": {"type": "markdown"}
  },
  "permissions": {
    "filesystem_read": false,
    "filesystem_write": false,
    "network": false
  },
  "safety": {
    "handles_sensitive_data": false,
    "requires_user_confirmation": false,
    "destructive": false,
    "stop_conditions": [
      "授權、資料範圍或驗收條件無法確認時停止。"
    ],
    "approval_scope": [],
    "audit_requirements": ["record_assumptions"],
    "rollback_required": false,
    "dry_run_default": true,
    "data_minimization": "redact_by_default",
    "rules": [
      "不得捏造事實、資料、來源、同意或驗證結果。",
      "任何外部寫入、發佈、部署或不可逆操作前必須取得明確人工批准。"
    ]
  },
  "risk_level": "low",
  "schema_version": "1.1.0",
  "contract_version": "1.1.0",
  "capabilities": {
    "filesystem": "none",
    "network": "none",
    "shell": "none",
    "git": "none",
    "browser": "none"
  },
  "connectors": [],
  "data_egress": {
    "mode": "none",
    "connectors": [],
    "allowed_data_classes": [],
    "approval_required": false,
    "minimize_and_redact": true,
    "retention": "none_by_default"
  },
  "external_write": {
    "allowed": false,
    "mode": "draft_or_read_only",
    "approval_required": false,
    "approval_scope": []
  },
  "execution": {
    "executor": "instruction_only",
    "adapter": "SKILL.md",
    "network_is_not_implied": true
  },
  "activation": {
    "positive_examples": [
      "使用者明確要求此 skill 所描述的任務。"
    ],
    "negative_examples": [
      "任務不涉及本 skill 的核心目的、輸入或輸出。"
    ],
    "exclude_when": [
      "若需要其他技能的專門能力，應交接而不是同時啟用本 skill。"
    ],
    "priority": 50,
    "delegates_to": [],
    "selection_notes": "以最窄任務範圍、最小權限與最少資料處理為優先。"
  },
  "related_skills": []
}
```

完成後執行 validator。若 `skills.json` 尚未有該技能，請依照下一節更新索引；不要先手動複製一份不完整的 registry entry。

### 4. 新增可執行 skill

若 skill 需要真正執行 Python、Node、Shell 或 HTTP adapter，請先說明為何 instruction-only 不足，再補上可重現入口。以 Python 為例：

```text
custom_skills/my-skill/
├── SKILL.md
├── manifest.json
├── run.py
├── requirements.txt       # 只有技能專屬依賴時才新增
├── examples/
│   └── sample_input.json
└── tests/
    └── test_my_skill.py
```

entrypoint 必須處理明確的輸入與錯誤狀態，不得把 API key 寫死在程式碼中，不得預設開啟網路，不得在沒有人工批准時執行寫入、刪除、部署、付費或發佈。請把外部服務整合放在明確 adapter 內，並在 manifest 中分別宣告唯讀權限、資料外送與 external write，而不是用一個模糊的 `network: true` 代表全部能力。

新增資料處理能力時，至少測試以下情境：正常輸入、空輸入、格式錯誤、敏感欄位遮罩、未授權外部操作與可預期的失敗輸出。可參考 [`custom_skills/data_analysis/`](custom_skills/data_analysis/) 與 [`tests/test_data_analysis.py`](tests/test_data_analysis.py)。

### 5. 修改既有 skill 的正確流程

修改前先閱讀該 skill 的 `SKILL.md`、`manifest.json`、entrypoint、測試與 `related_skills`。接著先判斷變更屬於哪一類，再決定版本與相容性處理：

| 變更類型 | 建議處理 |
|---|---|
| 修正文案、拼字或不改變契約的文件 | 增加 patch 版本；同步更新 `SKILL.md` 與必要的 CHANGELOG。 |
| 新增相容的輸入、輸出或流程 | 增加 minor 版本；補上 manifest、文件與測試。 |
| 改變輸出格式、權限、觸發邊界或行為契約 | 增加 major 版本或提供 migration note；不能只改 README。 |
| 新增網路、第三方資料外送、寫入、部署或付費能力 | 重新評估 risk level、permissions、data_egress、external_write、人工核准、停止條件與 rollback。 |
| 移除或重新命名 skill ID | 先提供相容別名或 migration；同步更新 registry、related skills、文件與使用者安裝流程。 |

變更時應讓以下檔案在同一個 commit 或同一個 Pull Request 中保持一致：

```text
custom_skills/<skill-id>/SKILL.md
custom_skills/<skill-id>/manifest.json
skills.json                         # 若 registry metadata 或路徑受到影響
CHANGELOG.md                        # 若是公開契約、功能或安全變更
README.md / docs/                   # 若使用方式或邊界改變
custom_skills/<skill-id>/tests/     # 若有可執行行為或回歸風險
```

### 6. 權限、資料流與人工批准

權限採**最小必要原則**。請使用標準欄位 `filesystem_read`、`filesystem_write`、`network`、`browser_automation`、`third_party_processing`、`shell`、`git` 及服務特定權限；不要新增 `read_files` 或 `write_files` 等 legacy alias。

`network: true` 不等於可以登入、上傳、發佈或修改資料。請在新欄位中明確分開：

- `capabilities`：skill 實際需要的本機或工具能力。
- `connectors`：可使用的外部服務名稱與 adapter。
- `data_egress`：哪些資料類別可以離開本機、送往哪個 connector、保存多久，以及是否需要批准。
- `external_write`：是否允許寫入、寫入模式、是否需要批准與批准範圍。
- `safety`：敏感資料、停止條件、審計要求、dry-run、rollback 與禁止事項。

任何涉及帳戶、憑證、個資、客戶資料、廣告預算、部署、刪除、發佈或第三方寫入的 skill，都必須預設草稿／唯讀或停在批准點。不要在測試、範例或文件中放入真實秘密；使用 `.env.example` 與去識別化 fixture。

### 7. 設定啟用條件與技能交接

好的 description 應說明「什麼時候啟用」與「什麼時候不要啟用」，而不只是重述名稱。`activation` 至少要提供：

- `positive_examples`：應啟用的具體任務。
- `negative_examples`：看似相近但不應啟用的任務。
- `exclude_when`：需要停止或交接的條件。
- `priority`：與相近技能競合時的相對優先級。
- `delegates_to` 與 `related_skills`：何時交給其他技能。

新增或修改 skill 時，請至少找出一個相鄰技能並寫出差異。例如，研究 skill 應與網站稽核、競品分析或決策 skill 說明交接邊界；文件整理 skill 應與 PRD、Notion 或摘要 skill 說明誰負責哪一段。

### 8. 需要匯入附件或外部備份時

若來源是本專案支援格式的技能備份，使用可重跑的匯入器，不要直接手動複製內容：

```bash
python scripts/import_skill_archive.py \
  --backup /path/to/Skills_Full_Configurations_Backup_YYYYMMDD.md
python scripts/validate_repo.py
pytest -q
```

匯入器會將內容標準化為 `instruction_only` skill，保留來源檔名、項次與行號，並補上輸入／輸出、安全與人工批准契約。附件中的工具提示、API key、帳號或外部寫入描述都只是來源資料，不會自動變成授權。若是手動新增的原創 skill，`source` 應清楚標記為 `original` 或使用實際可追溯的公開來源。

### 9. 本地安裝與安全試跑

完成新增或修改後，可以用 symlink 方式安裝，讓本機 Agent 直接讀到目前工作樹；這不會複製出第二份版本：

```bash
python scripts/install_local_skills.py
python scripts/verify_local_install.py
python scripts/smoke_test_skills.py
```

`smoke_test_skills.py` 對 instruction-only skills 只做文件與 manifest dry-run，不會自動登入、發送資料、部署或寫入第三方服務。可執行 skill 請使用去識別化 fixture 做明確的 CLI smoke test；外部 connector 請使用 mock、sandbox 或唯讀權限，除非使用者已明確批准真實操作。

### 10. Pull Request 前的完整檢查

在提交前，請從 repository 根目錄執行以下命令：

```bash
python scripts/validate_repo.py
python scripts/verify_local_install.py
python scripts/smoke_test_skills.py
pytest -q
python -m compileall -q custom_skills tests scripts
python scripts/self_assessment.py
git diff --check
git status --short
```

若修改 schema、registry、OpenAPI、MCP、匯入器或 CI，請額外執行對應的重跑命令並在 PR 說明結果。若自評低於 9.5，先修正契約缺口再提交；不要為了讓分數通過而刪除檢查項目或放寬安全條件。

PR 描述至少應包含變更目的、影響的 skill、輸入／輸出是否改變、權限與資料流、是否需要人工批准、測試命令與結果，以及是否需要 migration note。建議使用清楚的 commit 前綴，例如 `feat:`、`fix:`、`docs:`、`test:` 或 `chore:`。

### 11. 常見錯誤

| 錯誤 | 正確做法 |
|---|---|
| 只新增 `SKILL.md`，沒有 manifest | 補齊 manifest，並讓 registry、manifest 與文件一致。 |
| 把 `skills.json` 當成唯一定義 | 以各 skill 的 `manifest.json` 為權威來源，再更新 registry。 |
| 把所有外部能力寫成 `network: true` | 分開 connectors、data egress、external write 與批准範圍。 |
| 讓 instruction-only skill 宣稱已連接 API | 改為 `instruction_only`，把整合寫成 optional adapter contract。 |
| 只有正向 trigger，沒有排除條件 | 加入 negative examples、exclude_when、priority 與 related skills。 |
| 在文件或 fixture 中放真實個資與 token | 使用去識別化資料、`.env.example` 與秘密掃描。 |
| 修改輸出格式卻不升版 | 依 semver 升版，補 migration note、測試與 CHANGELOG。 |

若你不確定某個變更是否涉及安全或相容性，先停止高影響部分，閱讀 [`SKILL.md`](SKILL.md)、[`AGENTS.md`](AGENTS.md)、[`CONTRIBUTING.md`](CONTRIBUTING.md) 與 [`docs/manifest-contract.md`](docs/manifest-contract.md)，再開一個小範圍 PR 讓 reviewer 先確認方向。

## Core Skills

本節保留原有的核心技能與既有整合入口。附件匯入的 66 項技能以獨立目錄納管，不覆蓋既有技能；若要查看完整清單、類別、風險與關聯技能，請使用 [`docs/skill-archive-catalog.md`](docs/skill-archive-catalog.md)。

### 1. Data Analysis Skill

**用途：**
讀取 CSV / Excel 檔案，進行資料清理、統計分析與 Markdown 報告輸出。

**位置：**

`custom_skills/data_analysis/`

**適用情境：**

- 分析帳單
- 分析學生名單
- 分析行銷數據
- 產生摘要報告

**執行方式：**

```bash
python custom_skills/data_analysis/run.py --input custom_skills/data_analysis/examples/sample_input.csv --output report.md
```

### 2. [Workflow] Email Summary

**用途：**
將 Email 內容整理成摘要、待辦、決策與風險。

**位置：**

`workflows/email_summary.md`

### 3. [Workflow] Research Report

**用途：**
將研究任務整理為可查證、可比較、可決策的 Markdown 報告。

**位置：**

`workflows/research_report.md`

### 4. [Workflow] Website Audit

**用途：**
分析網站首頁訴求、CTA、信任元素、轉換路徑與可改善項。

**位置：**

`workflows/website_audit.md`


### 5. Website Custom Optimizer

**用途：**
依據網站目標與主要受眾，診斷並優化官方網站、Landing Page、產品頁、服務頁、招生頁、活動頁、知識庫與內部入口網，產出網站診斷、資訊架構、文案重寫、SEO、CRO、效能、可近用性、A/B 測試與執行路線圖。

**位置：**

`custom_skills/website-custom-optimizer/`

**適用情境：**

- 網站健檢與改版規劃
- Landing Page 轉換率優化
- 首頁架構設計與網站文案重寫
- SEO、UX/UI、行動版、效能與可近用性檢核
- 上線前檢核與工程／設計需求整理


### 6. Full Sprint

**用途：**
把高層目標轉成可執行、可驗證、可暫停、可恢復、可審計的 Sprint Contract，並在安全邊界、scope、constraints、驗收條件與 budget 內持續推進工程、重構、測試修復、文件或 feature 任務。

**位置：**

`custom_skills/full-sprint/`

**適用情境：**

- 使用者提到 `全力衝刺`、`sprint`、`/sprint`、`/goal`
- 長任務、自主執行、持續推進、跑到完成
- 需要每輪 checkpoint、驗證、log、completion audit 與 final report
- 需要在明確 scope、out_of_scope、constraints 與 validation commands 內交付


### 7. Google Ads AI Copilot

**用途：**
整合 Google Ads、n8n、Notion 與 AI Agent 成為廣告副駕駛，產出 read-only 健康報告、搜尋字詞稽核、否定關鍵字建議、RSA 文案、預算 pacing、行動佇列與自動化規劃；所有會花錢或影響帳戶的操作都需人類批准。

**位置：**

`custom_skills/optimizing-google-ads/`

**適用情境：**

- 慕熙 Moosie 或在地服務的小額廣告投放監控
- 每日／每週 Google Ads 健康報告
- 搜尋字詞稽核、否定關鍵字與高意圖字詞整理
- Google Ads RSA 文案、預算 pacing、30 天行動計畫
- Google Ads API、n8n、MCP Server、Notion 廣告營運資料庫規劃


### 8. 智能文件角色適應器

**用途：**
根據 Notion 文件類型、內容成熟度與使用者意圖，自動切換成文件整理者、策略顧問、SOP 設計師、學習教練或產品／技術 PM，產出可直接貼回 Notion 的摘要、重構、補全、改寫、SOP、PRD、學習筆記或行動方案。

**位置：**

`custom_skills/adapting-notion-docs/`

**適用情境：**

- Notion 筆記、SOP、策略稿、會議紀錄、規格書或學習資料整理
- 判斷文件類型並選擇最適合的助理角色
- 將鬆散筆記整理成可執行文件
- 摘要、重組、補洞、改寫或轉格式


### 9. research-lab — AI 研究實驗室

**用途：**
把市場、產品、競品、技術趨勢、商業模式、教育／AI／補教、廣告投放、SEO／GEO 或成長策略等複雜研究題目，拆成廣度掃描、深度鑽研、交叉驗證與可決策報告。

**位置：**

`custom_skills/research-lab/`

**適用情境：**

- 市場研究、產品研究、競品分析
- 技術趨勢、商業模式、教育／AI／補教主題研究
- 廣告投放、SEO／GEO、成長策略研究
- 壓力測試與需要形成決策報告的複雜問題


### 10. Managing Public Relations／公關品牌與危機處理

**用途：**
協助企業、品牌或個人建立公關策略、品牌訊息、利益關係人管理、媒體應對、PESO 媒體組合與危機處理流程，並產出核心訊息、媒體策略、對外聲明草稿、媒體 Q&A 與危機 SOP。

**位置：**

`custom_skills/managing-public-relations/`

**適用情境：**

- 提升品牌知名度、信任感、投資吸引力或合作機會
- 設計企業公關、B2B 公關、媒體訪談或品牌故事
- 處理負面新聞、客訴、社群炎上或危機事件
- 建立 CIS、CSR、PESO 與利益關係人溝通


### 11. Analyzing Business Models／商業模式九宮格診斷

**用途：**
用商業模式九宮格診斷事業、產品、個人品牌、服務、課程、內容產品或顧問案是否具備可持續性，找出價值主張、客群、通路、關鍵資源、成本與收益之間的斷點，並產出北極星指標與優先修正項。

**位置：**

`custom_skills/analyzing-business-models/`

**適用情境：**

- 盤點新事業、服務、課程、內容產品或顧問案
- 商業模式說不清楚，收入與成本無法對上
- 從價值主張反推客群、通路、活動、資源與夥伴
- 判斷北極星指標是否真的連到營收


### 12. Designing Pricing Systems／定價策略與成交系統

**用途：**
協助設計價格、報價情境、成交流程與回購系統，判斷該採短期高溢價、長期品牌、封閉式報價或公開標準品策略，並產出至少兩種價格方案、一條成交路徑與回購／推薦設計。

**位置：**

`custom_skills/designing-pricing-systems/`

**適用情境：**

- 不知道產品該賣高價還是合理價
- 客戶嫌貴，但可能是不懂價值
- 設計顧問、課程、保健品、餐廳、實體店或社群商品的成交系統
- 用 CRM、回訪、折價券、返利、試用或社群證據提升成交


### 13. Making Decisions／決策類 Skill

**用途：**
協助把模糊問題、候選方案與權衡條件整理成可判斷、可比較、可執行的決策流程，產出決策摘要、方案比較矩陣、不確定性地圖、推薦方案、反方觀點與低成本驗證計畫。

**位置：**

`custom_skills/making-decisions/`

**適用情境：**

- 多方案比較、優先級排序與風險評估
- 創業方向、專案投入、工具或技術選型
- 腦力激盪後收斂成決策
- CLI 工具與 AI 工作流規劃


### 14. [Community] Awesome Agent Skills

**用途：**
引用社群整理的 agent skills 資源，作為新增技能、參考技能格式與擴充能力時的共用來源。

**來源：**

`https://github.com/heilcheng/awesome-agent-skills`

**位置：**

`community_skills/awesome-agent-skills/`


### 15. [Community] Cloudflare Skills

**用途：**
引用 Cloudflare 官方 agent skills，讓 Agent 在處理 Workers、Pages、KV、D1、R2、AI、Tunnel、WAF、Wrangler、Durable Objects、Agents SDK、Email Service 等 Cloudflare 任務時可讀取官方指令包。

**來源：**

`https://github.com/cloudflare/skills`

**位置：**

`community_skills/cloudflare-skills/`

**可用內容：**

- `skills/cloudflare/SKILL.md`
- `skills/agents-sdk/SKILL.md`
- `skills/durable-objects/SKILL.md`
- `skills/cloudflare-email-service/SKILL.md`
- `skills/wrangler/SKILL.md`
- `skills/workers-best-practices/SKILL.md`
- `skills/web-perf/SKILL.md`
- `skills/sandbox-sdk/SKILL.md`
- `.mcp.json` for Cloudflare MCP server references

## Usage Policy

當 AI Agent 使用本技能庫時，請遵守以下原則：

1. 若任務涉及本機檔案分析，優先檢查 `custom_skills/`。
2. 若任務涉及多步驟流程，優先檢查 `workflows/`。
3. 若任務涉及 HTTP API 調用，優先檢查 `openapi.yaml`。
4. 若任務涉及第三方現成技能，檢查 `community_skills/`。
5. 若任務涉及敏感資料，必須先確認資料來源與授權。
6. 不得將 `.env`、API Key、Token、私密檔案上傳至公開 repo。

## Local Skills Inventory

本機已安裝的 agent skills 整理於 `LOCAL_SKILLS_INVENTORY.md`，包含：

- `~/.agents/skills` 與 `~/.skills` 的對應關係
- 目前已安裝 skill 清單
- 是否已能從本機證據確認對應 GitHub repo
- 後續是否建議納入本技能庫正式管理

機器可讀版本整理於 `local_skills_catalog.json`，格式與 `skills.json` 相容，方便後續自動選 skill、比對來源與做批次納管。

目前已優先納管的本機 skills：

- `custom_skills/to_prd/`
- `custom_skills/write_a_skill/`
- `custom_skills/lovable_github_cloudflare_worker/`
- `custom_skills/mcp_builder/`
- `custom_skills/website-custom-optimizer/`
- `custom_skills/full-sprint/`
- `custom_skills/optimizing-google-ads/`
- `custom_skills/adapting-notion-docs/`
- `custom_skills/research-lab/`
- `custom_skills/managing-public-relations/`
- `custom_skills/analyzing-business-models/`
- `custom_skills/designing-pricing-systems/`
- `custom_skills/making-decisions/`

## Repository Structure

```text
my-ai-skills/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── LOCAL_SKILLS_INVENTORY.md
├── SKILL.md
├── AGENTS.md
├── skills.json
├── local_skills_catalog.json
├── openapi.yaml
├── mcp.json
├── custom_skills/
├── community_skills/
├── workflows/
├── prompts/
├── schemas/
├── docs/
├── scripts/
├── .github/
└── tests/
```

## Compatibility

| 格式 | 用途 |
|---|---|
| Markdown | 給人類與大多數 AI Agent 閱讀 |
| skills.json | 給 Agent 快速索引技能 |
| OpenAPI | 給支援 API 調用的 Agent 使用 |
| MCP Config | 給支援 MCP 的工具連接 |
| Python Scripts | 實際執行任務 |

## Installation

```bash
git clone --recurse-submodules https://github.com/emting/my-ai-skills.git
cd my-ai-skills
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git submodule update --init --recursive
```

若要把 repository 內所有契約完整的 skills 安裝到本機 Agent，建議使用 symlink 模式。這樣更新 repository 後，本機載入內容會同步更新；安裝器不會覆蓋既有的非 symlink 目錄。

```bash
python scripts/install_local_skills.py
python scripts/verify_local_install.py
python scripts/smoke_test_skills.py
```

預設安裝位置是 `~/.agents/skills`；若該位置不存在，安裝器會建立它。卸載時只會移除指向本 repository `custom_skills/` 的 symlink，不會刪除其他技能或使用者資料：

```bash
python scripts/install_local_skills.py --uninstall
```

本 repository 目前包含 80 個可安裝套件，其中 79 個是 instruction-only skills，1 個是 Python CLI。`smoke_test_skills.py` 對 instruction-only skills 只做唯讀 dry-run，不會自動登入、發送網路請求、部署、推送或修改第三方服務。

## Safety

請勿提交以下內容：

- API Key
- Token
- 密碼
- 個人身分資料
- 客戶資料
- 未授權文件
- `.env` 檔案

請使用 `.env.example` 作為環境變數範例。

## License

MIT License

## Development and Validation

完成安裝後，可用以下命令驗證 repository 的機器可讀契約、測試與 Python 語法：

```bash
python scripts/validate_repo.py
python scripts/verify_local_install.py
python scripts/smoke_test_skills.py
pytest -q
python -m compileall -q custom_skills tests scripts
python scripts/self_assessment.py
```

`self_assessment.py` 使用 [`docs/self-assessment-rubric.md`](docs/self-assessment-rubric.md) 的 10 維度量表，並以 `evals/skills.json` 的 80 組技能契約案例檢查封裝完整度、來源可重現性、權限資料流、觸發選擇、安全治理、行為評估、可維護性與 CI 品質。GitHub Actions 將 **9.5/10** 設為最低品質閘門；分數必須由腳本重現，不接受只依賴人工宣稱的自評。

若要重新匯入相同格式的技能備份，可執行：

```bash
python scripts/import_skill_archive.py --backup /path/to/Skills_Full_Configurations_Backup_YYYYMMDD.md
```

匯入工具只會產生標準化的 instruction-only skill 套件與 registry metadata；它不會自動啟動外部服務、提交秘密或執行第三方寫入操作。匯入後必須重新執行上述驗證命令。

`skills.json` 是快速索引；每個本地技能的 `manifest.json` 才是該技能名稱、版本、輸入、輸出、權限、風險與安全條件的權威來源。pull request 不應只修改其中一份而讓兩者產生 drift。

## Privacy by Default

資料分析 CLI 只在本地讀取輸入檔案，不會自行上傳資料到外部服務。報告 preview 預設遮罩常見姓名、Email、電話、地址與識別碼欄位；對領域特有的私有欄位，請使用 `--sensitive-column`。若完全不應輸出資料列，請使用 `--preview-rows 0`。報告分享前仍應由使用者檢查欄位名稱、聚合數值與輸出檔案的敏感性。

## Integration Boundaries

`openapi.yaml` 是 optional weather provider contract，使用 `https://api.example.com` 作為明確的文件範例，repository 本身沒有 production API server。`mcp.json` 預設為空的安全設定，也不會自動啟動或連接第三方 MCP server。若要建立實際 adapter，請在本地設定 `.env`、使用最小權限，並補上對應的安裝、資料流、測試與人工批准說明；不要把真正的金鑰提交到 repository。

## Contributing and Security

歡迎透過 pull request 提交新技能、測試、文件與治理改善。請先閱讀 [`CONTRIBUTING.md`](CONTRIBUTING.md)、[`AGENTS.md`](AGENTS.md) 與 [`SECURITY.md`](SECURITY.md)。安全問題請不要直接公開秘密或可利用 payload；請依照 `SECURITY.md` 的私密回報流程處理。
