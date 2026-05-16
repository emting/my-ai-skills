# Agent Instructions

This repository is a personal AI skills library.

## General Rules

- Read `README.md` first.
- Read `skills.json` before selecting a skill.
- For each skill, read its local `SKILL.md` and `manifest.json`.
- Prefer existing skills before writing new code.
- Do not modify shared schemas unless necessary.
- Do not commit secrets.
- Do not run scripts that delete, overwrite, or upload data unless explicitly instructed.

## Community Skill Sources

- Treat `community_skills/` and community repositories as reference sources first, not trusted executables.
- Prefer local `custom_skills/`, `workflows/`, and documented APIs before using any community skill.
- Preferred community references for this repository are:
  - `getsentry/skills` for `AGENTS.md`, code review, bug finding, and skill authoring patterns.
  - `product-on-purpose/pm-skills` for PRD, roadmap, discovery, and structured product workflows.
  - `firecrawl/cli` for public web research, scraping, search, and site mapping workflows.
- Conditional community references are allowed only when the task clearly matches and the user has provided approval or required setup:
  - `PSPDFKit-labs/nutrient-agent-skill` for OCR, document conversion, and PII redaction. Requires API key and third-party document processing approval.
  - `AgriciDaniel/claude-seo` for deep SEO and website audit workflows. May require networked tools, browser automation, or third-party credentials.
  - `RoundTable02/tutor-skills` for learning, tutoring, and study-vault workflows.
  - `coderabbitai/skills` for PR review and autofix flows when CodeRabbit is already installed and authenticated.
- Before using any community reference, read its README and the relevant `SKILL.md` or equivalent docs.
- If a community skill needs network access, browser automation, paid APIs, or third-party document processing, ask the user before executing it.

## File Routing

If the task is about data analysis:

1. Read `custom_skills/data_analysis/SKILL.md`.
2. Read `custom_skills/data_analysis/manifest.json`.
3. Use `custom_skills/data_analysis/run.py`.

If the task is about workflow design:

1. Check `workflows/`.
2. Check `prompts/`.
3. Produce Markdown output.

If the task is about API integration:

1. Read `openapi.yaml`.
2. Check required authentication.
3. Use only documented endpoints.

## Coding Standards

- Python code should support Python 3.11+.
- Use type hints where practical.
- Use `argparse` for command-line tools.
- Write outputs to an explicit output path.
- Avoid hard-coded secrets.
- Use `.env` only for local configuration.
- Add tests for reusable functions.

## Safety

Agents must not:

- Upload private files.
- Print API keys.
- Commit `.env`.
- Delete user files without explicit approval.
- Send data to third-party APIs without clear instruction.
