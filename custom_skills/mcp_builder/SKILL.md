# MCP Builder

## Purpose

引導使用者新增 MCP Server，完成 Warp 端設定、必要安裝步驟與驗證流程。

## When to Use

適用於以下情境：

- 使用者要新增 MCP Server
- 需要整合新的外部工具或服務
- 要求提供 MCP 設定 JSON、安裝指令與驗證步驟

## Workflow

1. 確認要整合的服務名稱、授權方式與執行環境。
2. 提供 MCP server 設定 JSON 範本。
3. 提供安裝、啟動與 Warp 設定路徑說明。
4. 指定驗證步驟，確認工具能被 Warp 正常讀取。
5. 若需要 API key、token 或外部服務授權，先提醒風險與注入方式。

## Expected Output

1. MCP Server 設定 JSON
2. 安裝與啟動指令
3. Warp 設定位置
4. 驗證檢查清單

## Safety Notes

- 不要直接輸出真實 API key 或 token。
- 若設定會覆寫既有 MCP 配置，先提醒使用者。
- 對外部服務授權前，先確認是否為付費或高權限操作。
