# Integrations

本 repository 可以保存 API contract 與 MCP client 設定範例，但不會因為文件存在就自動連線、登入或操作任何第三方服務。整合的實作、憑證與批准責任留在使用者自己的環境中。

## OpenAPI

`openapi.yaml` 描述一個 provider-agnostic 的 `/weather/current` contract。`https://api.example.com` 是文件用的 placeholder，代表 repository 沒有內建 production API server。若要實作 adapter，請在部署或本地設定中替換 server URL，並確認 provider 的路徑、回應、rate limit、錯誤格式與 API key header 都符合實際服務。

不要把 provider key 寫進 YAML、README、測試 fixture 或 shell history。建議使用 `.env` 或平台的 secret store，且只授予必要 scope。整合若會送出使用者資料，應先取得資料擁有者授權，並在 manifest 宣告 `network` 與 `third_party_processing`。

## MCP

`mcp.json` 預設為空的 `mcpServers`，這是刻意設計的安全起點。它不會指向不存在的本地 `server.py`，也不會要求未定義的 `${API_KEY}`。使用者可以依照自己的 MCP client 格式加入 server，但應先閱讀上游 server 文件並確認 command、args、環境變數、資料流與權限。

建議每個 MCP server 都採以下順序驗證：

1. 先以唯讀工具確認連線與 server identity。
2. 確認所有輸入資料的來源、目的地、保存時間與第三方處理者。
3. 將 write、delete、deploy、billing、permission 與 credential 工具視為高風險能力。
4. 在技能 manifest 與文件中標示權限，並要求每一次高風險操作前取得明確人工批准。
5. 以最小化、非敏感的 fixture 執行 smoke test，避免使用真實客戶資料。

## Local environment

請從 `.env.example` 建立本地 `.env`，只填入你實際需要的變數。`.env`、`.env.*` 與憑證檔案不應提交到 Git；如果秘密曾經被提交，必須在 provider 端撤銷或輪替，單純刪除檔案不足以修復歷史暴露。

## Adding an integration

新增整合時，至少應同時提供 provider、用途、輸入、輸出、權限、錯誤處理、批准條件、測試方式與撤銷／停用方式。若 repository 沒有可執行 adapter，請明確使用 `optional` 或 `example` 命名，避免把 contract 誤認為已部署服務。
