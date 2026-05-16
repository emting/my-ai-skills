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
