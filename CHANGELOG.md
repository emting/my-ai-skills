# Changelog

本檔案記錄對使用者、技能契約與公開維護流程有影響的變更。版本遵循語意化版本概念；若 manifest、輸出格式或安全邊界改變，應在此說明。

## [1.2.0] - 2026-08-18

### Added

- 匯入並正規化使用者提供的 `Skills_Full_Configurations_Backup_20260818.md` 全部 66 項 skills，每項均有獨立的 `SKILL.md`、`manifest.json` 與來源行號。
- 新增 `scripts/import_skill_archive.py`，可重跑同格式備份的解析、技能封裝、registry 更新與整併目錄生成。
- 新增 `docs/skill-archive-catalog.md`，列出 66 項技能的 ID、類別、描述、風險、網路能力與既有技能關聯。
- 新增匯入器測試，覆蓋 66 項完整性、來源追蹤、ID 唯一性、高風險人工核准與外部能力宣告。

### Changed

- 所有匯入技能統一使用 `instruction_only` runtime、標準輸入／輸出契約、最小權限宣告、敏感資料規則、人工核准點與停止條件。
- `skills.json` 擴充至 90 個已註冊技能，並將 repository 版本提升至 1.2.0。
- README 與 manifest contract 補充附件整併、重新匯入與來源追蹤說明；既有技能不被同名或相近功能的新技能覆蓋。

## [1.1.0] - 2026-08-18

### Added

- 新增可在本地與 CI 執行的 `scripts/validate_repo.py`，批次驗證 manifests、registry、schema、OpenAPI、MCP 與路徑引用。
- 新增 `CONTRIBUTING.md`、`SECURITY.md` 與 `CODE_OF_CONDUCT.md`。
- 資料分析 CLI 新增 `--preview-rows` 與可重複使用的 `--sensitive-column` 選項。

### Changed

- 所有本地 manifest 的檔案權限欄位統一使用 `filesystem_read` 與 `filesystem_write`。
- 資料分析預覽預設遮罩常見姓名、Email、電話、地址與識別碼欄位。
- README、registry 與環境範例改為清楚的公開專案定位，移除尚未填寫的 maintainer placeholder。
- MCP 設定改為空的安全範例，不再指向 repository 內不存在的 `server.py`。
- OpenAPI 文件改為明確標示的 optional provider contract，不再宣稱 repository 內含 production API server。

### Fixed

- 修正 registry 與 data-analysis、To PRD manifest 之間的 metadata drift。
- schema 接受現有技能使用的連字號 ID，並對 inputs、outputs、permissions 與 safety 提供結構驗證。

[1.2.0]: https://github.com/emting/my-ai-skills/commit/d145302
[1.1.0]: https://github.com/emting/my-ai-skills/commit/39851329f9578389274960f57f711e8162843491
