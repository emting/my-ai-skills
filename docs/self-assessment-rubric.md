# Skills 自評量表

本量表用於對本 repository 的 80 個 skills 進行可重現自評，總分 10.0 分。每個維度 1.0 分，分數由 repository validator 與 `scripts/self_assessment.py` 自動計算；不得以人工主觀分數取代缺失證據。

| 維度 | 滿分條件 | 計分方式 |
|---|---|---|
| 套件完整性 | 每個 skill 都有可解析 manifest、SKILL.md、entrypoint 與唯一 ID | 通過完整性條件得 1.0，否則按通過比例計算 |
| Registry／schema | registry、manifest、路徑與 schema 全數一致 | 通過 validator 得 1.0，否則 0 |
| 來源可重現性 | 附件來源有檔案、項次、行號、SHA-256、normalizer version | 以 66 個附件 skills 的完整比例計算 |
| 文件結構 | 每個 SKILL.md 恰有一個 H1，並具備標準契約段落 | 以 80 個 skills 的結構通過比例計算 |
| 權限與資料流 | 每個 manifest 都能區分能力、connector、資料外送與外部寫入 | 新 schema 欄位完整且與舊權限交叉驗證得 1.0 |
| 觸發與選擇 | 每個 skill 有正向／負向觸發、排除條件、優先級與有效關聯 | activation 契約與重疊群組 eval 全數通過得 1.0 |
| 安全治理 | 高風險、敏感資料與外部寫入都有批准、禁止用途、停止條件 | 全量安全交叉檢查通過得 1.0 |
| 行為評估 | 每個 skill 至少有 positive trigger、negative trigger、output、safety 案例 | 全量 eval registry 通過得 1.0 |
| 可維護性 | 有版本化模板／匯入器、可重建產物與 drift 檢查 | generator、template、rebuild check 全數通過得 1.0 |
| CI／開源治理 | CI 執行 schema、source、activation、eval、pytest、compile 與秘密檢查 | workflow 具備全部品質閘門得 1.0 |

## 達標規則

`9.5/10` 是本次目標。若總分低於 9.5，必須優先修正最低分維度或最高風險缺口，再重新執行相同腳本。若任何 P0 安全或 provenance 檢查失敗，即使總分達標也不得宣稱完成。

## 分數解讀

| 分數 | 定位 |
|---|---|
| 0–5.9 | 內容集合或早期 prototype |
| 6.0–7.9 | 可使用但需人工維護 |
| 8.0–9.4 | 成熟的開源技能庫，仍需持續治理 |
| 9.5–10.0 | 具備可重現契約、選擇評估、安全邊界與持續品質閘門 |
