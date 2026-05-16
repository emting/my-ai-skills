# Local Skills Inventory

這份文件整合目前本機已安裝的 local skills，作為後續納管、補 GitHub 來源、或移入 `my-ai-skills` 的單一索引。

## Discovery Notes

- `~/.agents/skills` 目前是 symlink，實際指向 `~/.skills`
- 本次盤點對象是 `~/.skills/` 下的 skill 目錄
- 目前實際數量是 18 個，不是 15 個

## GitHub Status Rules

- `confirmed`: 本機 skill 目錄本身是 Git repo，且有明確 `origin` 指向 GitHub
- `referenced`: skill 文件內提到 GitHub repo，但本機目錄不是可直接追溯的 Git clone
- `unknown`: 目前只看到本機 skill，沒有從本機檔案找到可驗證的 GitHub repo

## Inventory

| Skill | Category | Path | GitHub Status | Evidence | Suggested Handling |
|---|---|---|---|---|---|
| `awesome-design-md` | Design system / UI | `~/.skills/awesome-design-md` | referenced | `SKILL.md` 提到 `https://github.com/VoltAgent/awesome-design-md` | 保留為 local skill，若要納管可補 source metadata |
| `build-fix-local` | Engineering workflow | `~/.skills/build-fix-local` | unknown | 僅看到本機 `SKILL.md` | 若常用可納入 shared workflow 索引 |
| `code-review-local` | Engineering workflow | `~/.skills/code-review-local` | unknown | 僅看到本機 `SKILL.md` | 可視為本機私有 review skill |
| `debug-local` | Engineering workflow | `~/.skills/debug-local` | unknown | 僅看到本機 `SKILL.md` | 可視為本機私有 debug skill |
| `graphify` | Knowledge graph / analysis | `~/.skills/graphify` | unknown | 僅找到 GitHub sponsor 連結，未找到 repo 來源 | 建議後續補正式 source URL |
| `grill-me` | Decision review | `~/.skills/grill-me` | unknown | 僅看到本機 `SKILL.md` | 保留本機使用即可 |
| `image-workflow` | Content workflow | `~/.skills/image-workflow` | unknown | 僅看到本機 `SKILL.md` | 若要分享可補 manifest 與 README |
| `local-workflow` | Engineering workflow | `~/.skills/local-workflow` | unknown | 僅看到本機 `SKILL.md` | 可作為共用本機工作流範本 |
| `lovable-github-cloudflare-worker` | Delivery / deployment | `~/.skills/lovable-github-cloudflare-worker` | unknown | 僅看到本機 `SKILL.md` | 已納管至 `custom_skills/lovable_github_cloudflare_worker/` |
| `mcp-builder` | Tooling / MCP setup | `~/.skills/mcp-builder` | unknown | 僅看到本機 `SKILL.md` | 已納管至 `custom_skills/mcp_builder/` |
| `prompt-master` | Prompt engineering | `~/.skills/prompt-master` | confirmed | 本機目錄含 `.git`，`origin=https://github.com/nidhinjs/prompt-master.git` | 已可視為外部來源 skill |
| `research-local` | Engineering workflow | `~/.skills/research-local` | unknown | 僅看到本機 `SKILL.md` | 可視為本機私有 research skill |
| `rumor-buster` | Analysis / communication | `~/.skills/rumor-buster` | unknown | 僅看到本機 `SKILL.md` | 保留本機使用即可 |
| `skill-creator` | Skill authoring | `~/.skills/skill-creator` | unknown | 僅看到本機 `SKILL.md` | 適合後續整併到 skill-writing 流程 |
| `systematic-debugging` | Engineering workflow | `~/.skills/systematic-debugging` | unknown | 僅看到本機 `SKILL.md` | 可與 `debug-local` 對齊整理 |
| `tdd-local` | Engineering workflow | `~/.skills/tdd-local` | unknown | 僅看到本機 `SKILL.md` | 可視為本機私有 TDD skill |
| `to-prd` | Product / documentation | `~/.skills/to-prd` | unknown | 僅看到本機 `SKILL.md` | 已納管至 `custom_skills/to_prd/` |
| `write-a-skill` | Skill authoring | `~/.skills/write-a-skill` | unknown | 僅看到本機 `SKILL.md` | 已納管至 `custom_skills/write_a_skill/` |

## Summary

- Total local skills: 18
- Confirmed GitHub repo: 1
- GitHub referenced in local docs: 1
- Source currently unknown from local evidence: 16
- Managed in `my-ai-skills`: 4

## Recommended Next Steps

1. 先補其餘 `unknown` skills 的 source metadata，例如 `source`, `visibility`, `owner`, `last_verified_at`
2. 若要繼續納管，下一批建議優先處理：`build-fix-local`, `debug-local`, `code-review-local`, `research-local`
3. 若要公開或同步到 GitHub，先為每個已納管 skill 補範例、測試 prompt、與版本維護規則
