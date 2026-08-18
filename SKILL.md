# AI Skills Library Instruction

## Purpose

This repository contains reusable AI skills, scripts, workflows, prompts, API definitions, and agent instructions.

AI Agents should use this repository as a structured toolbox.

## Skill Selection Rules

When a user asks for a task, follow this order:

1. Check `skills.json` for an available skill.
2. Check `custom_skills/` for executable scripts.
3. Check `workflows/` for multi-step procedures.
4. Check `openapi.yaml` for available API endpoints.
5. Check `community_skills/` only if no custom skill is suitable.

## Preferred Community References

Use community skills only after local options are exhausted. Treat them as reference-first resources and read their docs before execution.

Priority community references:

- `getsentry/skills`: `AGENTS.md` maintenance, code review, bug finding, skill writing.
- `product-on-purpose/pm-skills`: PRD, discovery, roadmap, stakeholder alignment, technical discovery.
- `firecrawl/cli`: public web research, scraping, search, crawling, and site mapping.

Conditional community references:

- `PSPDFKit-labs/nutrient-agent-skill`: use only with explicit approval for third-party document processing and required API keys.
- `AgriciDaniel/claude-seo`: use for advanced SEO or website audit tasks when networked analysis is acceptable.
- `RoundTable02/tutor-skills`: use for tutoring, study-vault, or curriculum-style knowledge workflows.
- `coderabbitai/skills`: use only when CodeRabbit is already available for the repository or PR.

## Execution Rules

Before running any script:

1. Read the skill's `SKILL.md`.
2. Read the skill's `manifest.json`.
3. Check required inputs.
4. Check whether environment variables are needed.
5. Do not execute destructive actions unless explicitly requested.
6. Never expose secrets or private data.
7. For community skills, confirm whether the skill is reference-only or requires network access, browser automation, paid APIs, or third-party data processing.

## Available Skill Categories

### Data Processing

Used for CSV analysis, Excel analysis, report generation, and chart generation.

Location: `custom_skills/data_analysis/`

### Web Research

Used for crawling public web pages, summarizing public information, and extracting website metadata.

Location: `custom_skills/web_scraper/` when implemented, or `workflows/website_audit.md` for SOP-only workflows.

### Knowledge Management

Used for Markdown organization, SOP generation, meeting notes, summaries, and structured documents.

Location: `workflows/` and `prompts/`

## Output Rules

Unless otherwise specified, outputs should be generated in Markdown.

Preferred output formats:

- `.md` for reports
- `.json` for structured data
- `.csv` for tables
- `.png` for charts
- `.html` only when explicitly needed

## Public Repository Contract

This is a public, MIT-licensed skills library. Every skill tracked in `custom_skills/` is intended to be shareable unless a separate distribution policy says otherwise. Do not use `private` metadata as an access-control mechanism; keep private skills and private inputs outside this repository.

The local `manifest.json` is the source of truth for a skill's name, description, runtime, inputs, outputs, permissions, safety rules, and risk level. The matching entry in `skills.json` is an index and must stay metadata-compatible with the manifest. Use the canonical permission keys `filesystem_read`, `filesystem_write`, `network`, `browser_automation`, `third_party_processing`, `shell`, and `git` where applicable. Legacy aliases such as `read_files` and `write_files` are not accepted.

## Safety Contract

Skills that handle sensitive data must describe the handling boundary and must not print or upload secrets, credentials, personal data, or private documents. Read-only analysis is the default for external services. Any write, spend-impacting, deployment, permission, credential, mass-delete, or destructive operation must stop for explicit user approval unless the calling platform provides an equivalent approval gate.

The data analysis CLI redacts common personal-data columns in previews by default. Use `--sensitive-column` for domain-specific private fields, and use `--preview-rows 0` when a report should contain no data preview.

## Validation

Run the repository checks before opening a pull request:

```bash
python scripts/validate_repo.py
pytest -q
python -m compileall -q custom_skills tests scripts
```

Changes to manifests, schemas, workflows, prompts, or integration configuration should include corresponding documentation or tests. Community submodules are reference sources first and must not be treated as trusted executables without reviewing their documentation and provenance.
