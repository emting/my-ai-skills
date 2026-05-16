# Write a Skill

## Purpose

建立新的 agent skill，並定義清楚的 description、觸發條件、檔案結構與附帶資源。

## When to Use

適用於以下情境：

- 使用者要新建 skill
- 需要重寫或優化既有 skill
- 想把重複任務整理成可重用的 agent workflow

## Workflow

1. 收集 skill 目標、使用情境與觸發關鍵字。
2. 判斷是否真的需要新 skill，而不是一般 prompt 或單次流程。
3. 產出 `SKILL.md` 的最小可用版本。
4. 視需要補 `manifest.json`、`README.md`、範例或 scripts。
5. 檢查 description 是否具體、可觸發、且沒有過度泛化。

## Required Structure

```text
skill-name/
├── SKILL.md
├── manifest.json
├── README.md
└── optional supporting files
```

## Review Checklist

- description 有沒有明確 `Use when` 或對應觸發條件
- skill 範圍是否單一而聚焦
- 是否真的需要 scripts
- 是否有最小範例或輸出格式說明

## Safety Notes

- 不要為單次任務過度抽象化。
- 不要省略觸發條件描述。
- 若 skill 會執行高風險操作，要在 manifest 中標出。
