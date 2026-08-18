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

## 標準執行契約

### 觸發與輸入

僅在使用者需求與本技能描述相符時啟用。先確認目標、受眾、上下文、資料來源、限制與輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與外部依賴。
2. 依技能核心流程處理，分開標示事實、推論、假設與建議。
3. 產出可審閱結果，列出來源、未驗證事項、風險與人工決策點。
4. 輸出前檢查範圍、引用、敏感資料與高影響操作。

## 輸出契約

- **mcp_setup_plan**：依技能規格提供

## 安全與人工核准

目前風險等級：**medium**。

- Never output real API keys, tokens, private keys, or credentials.
- Use placeholders and environment-variable references for authentication examples.
- Require explicit user confirmation before overwriting existing MCP configuration or enabling an external service.
- Identify paid, privileged, networked, or third-party data-processing effects before authorization.

## 停止條件

若授權、來源、範圍、關鍵數字、身份或外部操作權限無法確認，停止高影響部分並回報缺口；若發現矛盾、敏感資料暴露或輸出無法驗證，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 目前沒有經人工確認的直接關聯技能 有功能相近或可互補的關係；選擇時以任務範圍、資料來源與權限邊界為準。

## 來源追蹤

來源：`未指定`，項次 未指定，原始行號 ?–?。
