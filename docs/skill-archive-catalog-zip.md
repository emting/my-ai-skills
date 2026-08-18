# skills_export.zip 整併目錄

> 本目錄由 `scripts/import_skill_zip.py` 產生。附件共含 91 個 skills；其中與既有本地技能精確重疊的項目不覆蓋，本次新增 28 個獨立 ID。

- 來源檔案：`docs/sources/skills_export_20260818.zip`
- 來源 ZIP SHA-256：`9df813fcdec9d0c5948f5d8892a115b859f93a409a6b0b1e080df3c8581ed4e4`
- 匯入器版本：`1.4.0`
- 保留既有技能：63 個
- 新增技能：28 個

## 整併原則

所有新增技能均採 `instruction_only` runtime，不宣稱已具備真實 API、瀏覽器、Shell 或第三方寫入適配器。原始資源保留在對應 skill 目錄；`SKILL.md` 補上標準契約、安全、來源追蹤與停止條件；manifest 補上能力、連接器、資料外流、外部寫入與 activation 契約。高風險技能預設草稿／唯讀並要求人工核准。

| # | ID | 風險 | 網路 | 敏感資料 | 關聯技能 |
|---:|---|---|:---:|:---:|---|
| 1 | `agent-bible-sq3r-fast-guide` | medium | 是 | 否 | `ai-research-lab`, `research-to-insight` |
| 2 | `agent-big-e-life-coach` | low | 否 | 是 | `decision-making-superpowers` |
| 3 | `agent-cyber-bully-lecturer` | high | 是 | 是 | `ai-security-agent-governance` |
| 4 | `agent-senior-prd-architect-sophia` | high | 是 | 否 | `ai-project-feasibility-assessment` |
| 5 | `agent-skills-actions-auditor` | high | 是 | 否 | `ai-security-agent-governance`, `enterprise-sovereign-ai-adoption` |
| 6 | `app-performance-benchmark-optimizer` | high | 是 | 否 | `website-auditing` |
| 7 | `cloudflare-skills` | high | 是 | 是 | `website-auditing`, `website-landing-page-builder` |
| 8 | `daily-devotional-prayer-guide` | medium | 否 | 是 | — |
| 9 | `emil-design-eng` | high | 是 | 是 | `design-proposal-portfolio-persuasion`, `ui-minimalist-animation-enhancer` |
| 10 | `full-sprint-execution` | high | 否 | 否 | `startup-venture-builder`, `agent-task-packaging` |
| 11 | `game-inspiration-world-builder` | high | 是 | 否 | — |
| 12 | `google-ads-audit` | high | 是 | 否 | `marketing-brief-competitor-analyst` |
| 13 | `high-energy-daily-routine-designer` | high | 否 | 是 | — |
| 14 | `interactive-skill-learning-curriculum` | medium | 是 | 否 | `progressive-quiz-generator` |
| 15 | `life-scenario-simulation-matrix` | high | 是 | 否 | `decision-making-superpowers` |
| 16 | `multi-agent-research-workflow` | medium | 是 | 否 | `ai-research-lab`, `research-to-insight` |
| 17 | `naval-backstage-simulator` | high | 是 | 否 | — |
| 18 | `open-slide` | high | 是 | 否 | `presentation-structure-visual-script`, `presentation-yaml-design-architect` |
| 19 | `presentation-yaml-design-architect` | low | 否 | 否 | — |
| 20 | `product-idea-scoring-matrix` | medium | 是 | 是 | `ai-project-feasibility-assessment` |
| 21 | `system-file-audit-organizer` | high | 是 | 否 | — |
| 22 | `threads-api-skill` | high | 是 | 是 | `threads-viral-consultant` |
| 23 | `ui-minimalist-animation-enhancer` | high | 是 | 否 | `design-proposal-portfolio-persuasion` |
| 24 | `veo-short-video-prompt-engineer` | medium | 是 | 否 | `video-editing-preproduction-script-cuts` |
| 25 | `website-auditing` | high | 是 | 否 | `website-landing-page-builder` |
| 26 | `weekly-podcast-script` | high | 是 | 是 | `couple-podcast-hosting` |
| 27 | `workspace-project-cleanup-agent` | high | 否 | 否 | `system-file-audit-organizer` |
| 28 | `youtube-transcript-summarizer` | medium | 是 | 是 | `youtube-learning-summary-exporter` |

## 未覆蓋的既有 ID

本次來源中另有 63 個 ID 已存在於 repository；匯入器不修改這些目錄或 manifests。它們的完整清單保留於本次盤點報告與來源追蹤資料中。
