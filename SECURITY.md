# Security Policy

## Scope

本政策適用於 `my-ai-skills` repository 內的技能、CLI、manifest、workflow、prompt、schema、OpenAPI 設定與 CI 設定。社群 submodule 的漏洞應同時依照其上游 repository 的安全政策回報。

這個 repository 主要保存指令與本地分析工具，不會因為存在 manifest 或 OpenAPI 文件就自動取得外部帳戶權限。實際整合仍需由使用者在自己的環境中設定憑證與批准邊界。

## Supported baseline

目前以 `main` 分支最新版本為主要支援基線。安全修正應包含可重現的測試、文件更新或 validator 規則，並避免把秘密或真實個資加入 issue、pull request、測試 fixture 或範例檔案。

## Reporting a vulnerability

請不要在公開 issue 貼出 API key、token、密碼、個資、客戶資料或可直接利用的完整 payload。請透過 GitHub repository 的私密安全回報管道聯絡維護者；若該管道不可用，先建立不包含敏感細節的 issue，僅說明需要私密聯絡方式，並等待維護者回覆。

回報內容請盡量包含受影響的版本或 commit、受影響檔案、重現步驟、預期與實際行為、可能的資料暴露範圍，以及不包含秘密的最小化證據。維護者會先確認影響範圍，再決定修正、文件澄清或撤回相關版本的方式。

## Secret exposure

若發現秘密已被提交，請立即在提供者端撤銷或輪替該秘密；不要只依賴刪除 Git commit。接著以不含秘密的方式通知維護者，並指出受影響的檔案與 commit。Repository 內的 `.gitignore` 只降低誤提交機率，不能取代憑證輪替或歷史清理。

## Safe contribution rules

任何會寫入第三方服務、改變權限、部署、花費預算、刪除資料、處理非公開資料或傳送資料到第三方的技能，都必須在 manifest 與文件中清楚宣告，並要求明確人工批准。對不確定的資料流，預設採 read-only、local-only 與最小權限。
