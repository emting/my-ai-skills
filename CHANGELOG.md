# Changelog

本檔案記錄對使用者、技能契約與公開維護流程有影響的變更。版本遵循語意化版本概念；若 manifest、輸出格式或安全邊界改變，應在此說明。

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

[1.1.0]: https://github.com/emting/my-ai-skills/releases/tag/v1.1.0
