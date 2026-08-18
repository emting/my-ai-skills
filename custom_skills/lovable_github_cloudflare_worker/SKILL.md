# Lovable GitHub Cloudflare Worker

## Purpose

協助使用者把 Lovable 產出的原型專案，整理成 GitHub 管理、Cloudflare Worker 部署、可驗證、可回滾的正式交付流程。

## When to Use

適用於以下情境：

- 使用者提到 `lovable`
- 想接上 `GitHub`
- 要部署到 `Cloudflare Worker`
- 遇到 `wrangler` 建置、部署或 runtime 問題

## Required Inputs

1. 專案路徑與主要框架
2. GitHub repository 或 branch 規劃
3. Cloudflare Worker 名稱、route、bindings
4. 是否需要 CI/CD 與回滾策略

## Delivery Workflow

1. Preflight：確認 runtime、依賴、build/test 是否正常。
2. Git baseline：整理 `.gitignore`、建立基線 commit、確認可重現啟動步驟。
3. GitHub connection：驗證 remote、push 狀態、必要 CI。
4. Cloudflare target：建立或修正 `wrangler.toml`、確認 `wrangler dev`。
5. Deploy and smoke test：檢查健康路由、核心功能與資產載入。
6. Rollback plan：保留版本識別與回滾指令。

## Reporting Format

- Pipeline Summary
- Stage Gate 結果
- 異常與修復
- 下一步建議

## Safety Notes

- 不要在對話中輸出 secrets。
- 涉及 `git push`、正式 deploy、或雲端資源變更時，先取得使用者確認。
- 不要跳過 smoke test 與 rollback 檢查。

## 標準執行契約

### 觸發與輸入

僅在使用者需求與本技能描述相符時啟用。先確認目標、受眾、上下文、資料來源、限制與輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與外部依賴。
2. 依技能核心流程處理，分開標示事實、推論、假設與建議。
3. 產出可審閱結果，列出來源、未驗證事項、風險與人工決策點。
4. 輸出前檢查範圍、引用、敏感資料與高影響操作。

## 輸出契約

- **delivery_report**：依技能規格提供

## 安全與人工核准

目前風險等級：**high**。

- Do not print, commit, or transmit secrets, tokens, private keys, or account data.
- Require explicit user confirmation before git push, Cloudflare deploy, route/binding changes, or cloud resource changes.
- Run build, test, smoke test, and rollback checks before any deployment recommendation.
- Do not claim a deployment succeeded without observing an explicit provider result.

## 停止條件

若授權、來源、範圍、關鍵數字、身份或外部操作權限無法確認，停止高影響部分並回報缺口；若發現矛盾、敏感資料暴露或輸出無法驗證，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 目前沒有經人工確認的直接關聯技能 有功能相近或可互補的關係；選擇時以任務範圍、資料來源與權限邊界為準。

## 來源追蹤

來源：`未指定`，項次 未指定，原始行號 ?–?。
