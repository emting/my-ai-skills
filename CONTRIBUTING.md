# Contributing

感謝你協助改善 `my-ai-skills`。本儲存庫是一個以 Markdown、JSON manifest、工作流程與少量本地 CLI 組成的公開技能庫；貢獻內容應優先考慮可讀性、可驗證性、可移植性與安全邊界。

## 開始之前

請先閱讀 `README.md`、`SKILL.md` 與 `AGENTS.md`。若要修改既有技能，請先閱讀該技能的 `SKILL.md` 與 `manifest.json`，並確認修改不會把原本的 read-only 行為變成寫入、部署或花費資源的行為。

## 新增或修改技能

每個本地技能應至少包含以下檔案：

```text
custom_skills/<skill-id>/
├── SKILL.md
└── manifest.json
```

可執行技能還應提供明確的 entrypoint、依賴與測試。`manifest.json` 是該技能的 metadata source of truth，`skills.json` 是索引；兩者的 ID、名稱、說明、runtime 與 risk level 必須一致。技能 ID 使用小寫字母、數字、連字號或底線，並以 semver 形式管理版本。

權限請使用標準鍵名，例如 `filesystem_read`、`filesystem_write`、`network`、`browser_automation`、`third_party_processing`、`shell` 與 `git`。不要新增 `read_files` 或 `write_files` 這類 legacy alias。所有高風險、破壞性、寫入、部署、帳戶、預算或憑證操作，都必須在 manifest 與 `SKILL.md` 中明確寫出人工批准條件。

## 隱私與安全

不要提交 API key、token、密碼、個人身分資料、客戶資料或未授權文件。請使用 `.env.example` 作為空白設定範本。資料分析技能的輸出預覽預設會遮罩常見個資；若新增資料處理能力，請用測試證明敏感值不會被直接輸出或傳送到第三方服務。

社群 submodule 應視為參考來源，而非預設可信任的可執行程式。若貢獻需要網路、瀏覽器、自動化、付費 API 或第三方資料處理，請在 pull request 中說明資料流、權限與批准需求。

## 本地驗證

在提交 pull request 前，請於 repository 根目錄執行：

```bash
python scripts/validate_repo.py
pytest -q
python -m compileall -q custom_skills tests scripts
```

若修改 OpenAPI、MCP、schema 或 registry，請額外確認 JSON/YAML 可解析，並在 pull request 說明是否有 compatibility impact。若修改既有輸出格式，請提供 migration note 或版本變更理由。

## Pull Request

Pull request 描述請包含：變更目的、影響範圍、測試命令與結果、是否涉及敏感資料或外部服務，以及是否需要人工批准。請保持單一主題、避免提交生成物與本地設定檔，並讓 reviewers 能透過文件與測試重現主要行為。

## Commit 訊息

建議使用清楚的祈使句，例如 `feat: add ...`、`fix: redact ...`、`docs: clarify ...`、`test: cover ...` 或 `chore: validate ...`。若變更會影響公開 manifest 或相容性，請在 commit 或 pull request 中明確標示。
