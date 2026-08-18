# Changelog

本檔案記錄對使用者、技能契約與公開維護流程有影響的變更。版本遵循語意化版本概念；若 manifest、輸出格式或安全邊界改變，應在此說明。

## [1.4.0] - 2026-08-18

### Added

- 新增 `scripts/generate_recommendation_index.py`，依可重現的逐一測試快照生成 108 個完整 skills 的推薦排名與 registry metadata。
- 新增 `docs/recommendation-index.md`，提供 A、A-、B、C 四級分層、完整排序、測試範圍與限制說明。
- 新增 `docs/evaluations/`，保存逐一測試與 inventory 的 JSON／CSV 機器可讀快照，作為排序來源與後續 drift review 的依據。

### Changed

- `skills.json` 版本提升至 1.4.0；108 個完整 skills 依 recommendation rank 排列，並附 `rank`、`score`、`level`、`status`、`test_scope` 與安全邊界摘要。
- OpenAPI、MCP 與 workflow 輔助 entries 保留於 registry 後段，不再被誤當成已完成逐一測試的 skill，也不虛構推薦分數。
- README、manifest contract 與 self-assessment rubric 補充推薦分級的選擇邏輯、人工批准邊界、測試限制與推薦索引重建流程。

### Safety

- 明確標示推薦排序是治理與安全輔助指標，不是專業品質、成功率或 ROI 保證。
- 107 個 `instruction_only` skills 僅以唯讀契約／內容／eval dry-run 驗證；唯一的 `data_analysis` executable test 使用隔離、離線、去識別化 CSV fixture，未執行外部寫入。

## [1.3.0] - 2026-08-18

### Added

- 解析並整併 `skills_export.zip` 的 91 個目錄型 skills；其中 63 個與既有 ID 重疊而保留原版本，新增 28 個獨立 skill packages。
- 新增 `scripts/import_skill_zip.py`，支援安全解壓、ZIP 路徑穿越與 symlink 阻擋、附加資源保留、archive SHA-256、來源追蹤與可重跑匯入。
- 擴充 `scripts/import_skill_archive.py --backup`，現在同時接受原有 Markdown 備份與目錄型 ZIP。
- 新增 `docs/skill-archive-catalog-zip.md`，記錄 ZIP 來源 hash、整併決策、風險、網路能力、敏感資料與關聯技能。
- 擴充 ZIP importer 測試，覆蓋既有技能不覆蓋、附加資源保留、標準契約生成與路徑穿越阻擋。

### Changed

- repository 目前為 108 個可安裝套件、118 個 registry entries 與 108 組技能契約 evals；新增項目均使用 `instruction_only` runtime，外部寫入預設關閉。
- `README.md` 補充雙格式匯入、來源保存與安全重跑說明；`verify_local_install.py` 移除硬編碼的 80 套件數量，改為可選的明確數量閘門。
- 所有新增 skill 均補齊輸入／輸出、permissions、capabilities、connectors、data_egress、external_write、activation、stop conditions、approval scope、rollback 與資料最小化契約。

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

[1.2.0]: https://github.com/emting/my-ai-skills/commit/2710101f41f5d71286fe74e58d44cb9d3d1c6d56
[1.1.0]: https://github.com/emting/my-ai-skills/commit/39851329f9578389274960f57f711e8162843491
