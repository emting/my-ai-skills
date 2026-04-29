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
