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
