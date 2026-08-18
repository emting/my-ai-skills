# Manifest Contract

每個 `custom_skills/<skill-id>/manifest.json` 描述一個可以被 Agent 發現或執行的技能。共用 schema 位於 `schemas/skill.schema.json`；它提供結構驗證，但不取代 `SKILL.md` 對流程、安全與人類可讀說明的責任。

## Required fields

| 欄位 | 說明 |
|---|---|
| `id` | 穩定的技能識別碼，只使用小寫字母、數字、`-` 或 `_`。 |
| `name` | 給人類閱讀的技能名稱。 |
| `version` | `MAJOR.MINOR.PATCH` 形式的版本。契約或輸出不相容時應提高 major。 |
| `description` | 一句話說明技能用途與主要邊界。 |
| `entrypoint` | 相對於 skill 目錄的 `SKILL.md` 或可執行入口。 |
| `runtime` | `instruction_only`、`python`、`node`、`shell`、`http` 或 `unknown`。 |
| `inputs` | 命名輸入欄位；每個欄位至少要有 `type`。 |
| `outputs` | 命名輸出欄位；每個欄位至少要有 `type`。 |
| `permissions` | 實際需要的檔案、網路、工具與外部服務能力。 |
| `safety` | 敏感資料、人工核准、禁止用途、停止條件與不可繞過的安全規則。 |
| `source` | 若技能由外部備份或社群來源匯入，記錄來源檔案、項次、行號與正規化狀態。 |

## Permissions

權限應採最小化宣告。`filesystem_read` 與 `filesystem_write` 描述本地檔案能力；`network` 描述外部網路；`browser_automation` 描述瀏覽器操作；`third_party_processing` 描述將資料送到第三方；`shell` 與 `git` 描述命令列與版本控制能力。服務特定權限如 `google_ads_read`、`google_ads_write`、`notion_read`、`notion_write`、`n8n_write` 與 `mcp_write_tools` 也應如實宣告。

不要使用 `read_files` 或 `write_files`。這些舊欄位會使不同 loader 對技能能力產生歧義，validator 會拒絕它們。附件匯入技能另以 `filesystem_read`、`filesystem_write`、`network`、`third_party_processing` 與服務特定能力宣告最小權限；沒有實際執行器的技能不得宣稱已連接外部服務。

## Safety and risk

`risk_level` 使用 `low`、`medium` 或 `high`。若技能處理敏感資料，將 `safety.handles_sensitive_data` 設為 `true`，並在 `safety.rules` 或 `safety_notes` 說明遮罩、保存、傳輸與分享限制。若技能會寫入、部署、刪除、花費預算、修改權限或處理憑證，應將 `requires_user_confirmation` 設為 `true`，並明確列出不可繞過的批准點。

## Imported archive skills

使用 `scripts/import_skill_archive.py` 匯入的技能一律採 `instruction_only` runtime，來源內容只作為核心流程，並由工具補上四段標準契約：觸發與輸入、執行順序、輸出契約、安全與人工核准。每一項都必須保留 `source.section_number`、`source.start_line` 與 `source.end_line`，以便回溯原始備份；相近功能使用 `related_skills` 互相標記，不直接覆蓋既有技能。

匯入器不會自動執行原始內容中的外部工具、不會建立憑證、不會發送或發佈資料，也不會把附件內的工具提示視為授權。任何第三方寫入、部署、預算、權限或不可逆操作，都必須在技能說明與 manifest 中標示為人工核准事項。

## Registry relationship

`skills.json` 是快速搜尋與相容性索引，不應成為另一份獨立的技能定義。具有 `manifest` 路徑的 registry entry 必須與 manifest 的 `id`、`name`、`description`、`runtime` 與 `risk_level` 保持一致。執行 `python scripts/validate_repo.py` 可以檢查這些關係、所有本地 manifest、entrypoint 路徑與整合設定。
