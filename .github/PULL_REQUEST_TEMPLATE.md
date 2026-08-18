## 變更目的

請說明這個 pull request 解決的問題，以及為什麼需要這項變更。

## 變更範圍

- [ ] 新增或修改 skill
- [ ] 修改 manifest、registry 或 schema
- [ ] 修改 CLI、測試或依賴
- [ ] 修改 workflow、prompt 或整合設定
- [ ] 修改文件或開源治理檔案

請列出主要檔案與相容性影響。

## 驗證

請貼上實際執行的命令與結果：

```text
python scripts/validate_repo.py
pytest -q
python -m compileall -q custom_skills tests scripts
```

## 安全與資料流

請確認本次變更是否涉及敏感資料、網路、瀏覽器、自動化、第三方服務、外部帳戶、寫入、部署、預算、刪除或憑證。如果涉及，請說明權限、資料流與人工批准條件；若不涉及，請填寫「不涉及」。

## Checklist

- [ ] 沒有提交秘密、token、個資、客戶資料或未授權文件
- [ ] manifest 與 `skills.json` 的 metadata 保持一致
- [ ] 使用標準 permission keys，沒有新增 legacy alias
- [ ] 新行為有對應測試或文件
- [ ] 變更不會把 read-only 行為默默變成寫入或部署行為
- [ ] 已閱讀 `AGENTS.md`、`CONTRIBUTING.md` 與 `SECURITY.md`
