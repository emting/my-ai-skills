#!/usr/bin/env python3
"""Sync staged Notion skill pages into custom_skills/.

Each staged file is Markdown with a small header::

    ---
    repo_id: agent-task-packaging
    title: Agent 任務封包 Skill
    description: 一句話描述（新增技能必填；既有技能可省略）
    notion_url: https://app.notion.com/p/...
    version: v1.1
    last_edited: 2026-09-24T00:59:00Z
    ---
    <Notion page body converted to Markdown>

Existing skills keep their repository contract sections (from ``## 標準執行契約``
onward); only the instruction body is replaced. Unknown IDs are created with the
same contract generator used by ``import_skill_zip.py``. Nothing is deleted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from scripts import import_skill_zip as zipimp

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / 'custom_skills'
REGISTRY_PATH = ROOT / 'skills.json'
CONTRACT_MARKER = re.compile(r'\n(?:---\s*\n+)?## 標準執行契約')
HEADER_RE = re.compile(r'\A---\n(.*?)\n---\n', re.S)
SYNC_VERSION = '1.0.0'


def parse_staged(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding='utf-8')
    match = HEADER_RE.match(text)
    if not match:
        raise ValueError(f'{path.name}: missing header')
    meta: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(':')
        meta[key.strip()] = value.strip()
    if not meta.get('repo_id') or not meta.get('notion_url'):
        raise ValueError(f'{path.name}: repo_id and notion_url are required')
    return meta, text[match.end():].strip()


def semver(version: str) -> str | None:
    found = re.match(r'v?(\d+)\.(\d+)(?:\.(\d+))?', version or '')
    return f'{found.group(1)}.{found.group(2)}.{found.group(3) or 0}' if found else None


def newer(candidate: str | None, current: str) -> bool:
    if not candidate:
        return False
    key = lambda v: tuple(int(p) for p in v.split('.'))  # noqa: E731
    return key(candidate) > key(current)


def clean_body(body: str, title: str) -> str:
    return zipimp.demote_extra_h1(body, title)


def provenance(meta: dict[str, str], body: str) -> dict[str, Any]:
    return {
        'type': 'notion_page',
        'notion_url': meta['notion_url'],
        'notion_version': meta.get('version', ''),
        'notion_last_edited': meta.get('last_edited', ''),
        'synced_at': str(date.today()),
        'sync_script_version': SYNC_VERSION,
        'hash_algorithm': 'sha256',
        'sha256': hashlib.sha256(body.encode('utf-8')).hexdigest(),
    }


def update_existing(skill_id: str, meta: dict[str, str], body: str) -> str:
    skill_dir = SKILLS_ROOT / skill_id
    skill_path = skill_dir / 'SKILL.md'
    manifest_path = skill_dir / 'manifest.json'
    old = skill_path.read_text(encoding='utf-8')
    front = zipimp.FRONTMATTER_RE.match(old)
    if not front:
        raise ValueError(f'{skill_id}: SKILL.md has no frontmatter')
    split = CONTRACT_MARKER.search(old)
    if not split:
        raise ValueError(f'{skill_id}: no contract section to preserve')
    contract = old[split.start():].lstrip('\n')
    contract = re.sub(r'\A---\s*\n+', '', contract)
    contract = re.sub(
        r'\n## Notion 同步紀錄\n.*?(?=\n## |\Z)', '', contract, flags=re.S
    ).rstrip() + '\n'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    name = meta.get('title') or manifest['name']
    new_body = clean_body(body, manifest['name'])
    sync_note = (
        '\n## Notion 同步紀錄\n\n'
        f"本技能的指令本文同步自 Notion「Skill 頁面整理庫」頁面 {meta['notion_url']}"
        f"（Notion 版本 {meta.get('version', '未標示')}，最後編輯 {meta.get('last_edited', '未標示')}）。"
        '上方內容以 Notion 為準；標準執行契約為本 repository 的安全治理補充，同步時不會被覆蓋。\n'
    )
    updated = f"{front.group(0).rstrip()}\n\n{new_body}\n\n---\n\n{contract.rstrip()}\n{sync_note}"
    skill_path.write_text(updated, encoding='utf-8')
    candidate = semver(meta.get('version', ''))
    if newer(candidate, manifest.get('version', '0.0.0')):
        manifest['version'] = candidate
    manifest['source'] = {**manifest.get('source', {}), 'notion': provenance(meta, new_body)}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return f'updated {skill_id} ({name})'


def create_new(skill_id: str, meta: dict[str, str], body: str, ordinal: int) -> str:
    if not zipimp.ID_RE.fullmatch(skill_id):
        raise ValueError(f'invalid skill id: {skill_id}')
    description = meta.get('description')
    if not description:
        raise ValueError(f'{skill_id}: description is required for new skills')
    name = skill_id
    classified = zipimp.classification(skill_id, name, description, body)
    source_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()
    lines = (1, len(body.splitlines()))
    skill_dir = SKILLS_ROOT / skill_id
    if skill_dir.exists():
        raise FileExistsError(skill_dir)
    skill_dir.mkdir(parents=True)
    title = meta.get('title') or skill_id
    content = zipimp.build_skill_markdown(
        skill_id, title, description, body, classified, meta['notion_url'], 'notion page', lines, [], source_hash
    )
    content = content.replace(
        f"此技能由 `{meta['notion_url']}` 內的 `notion page` 正規化而來，來源項目 SHA-256 為 `{source_hash}`，原始行號範圍為 {lines[0]}–{lines[1]}。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。",
        f"此技能同步自 Notion「Skill 頁面整理庫」頁面 {meta['notion_url']}（Notion 版本 {meta.get('version', '未標示')}，最後編輯 {meta.get('last_edited', '未標示')}），"
        f"本文 SHA-256 為 `{source_hash}`，並補上輸入、輸出、權限、安全、人工核准與停止契約。",
    )
    (skill_dir / 'SKILL.md').write_text(content, encoding='utf-8')
    manifest = zipimp.build_manifest(
        skill_id, title, description, classified, meta['notion_url'], 'notion page', lines,
        source_hash, source_hash, ordinal, [], [],
    )
    semantic = semver(meta.get('version', ''))
    if semantic:
        manifest['version'] = semantic
    manifest['source'] = {
        **manifest['source'],
        'type': 'notion_page',
        'file': meta['notion_url'],
        'notion': provenance(meta, body),
    }
    (skill_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    registry = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
    if all(item.get('id') != skill_id for item in registry['skills']):
        entry = zipimp.registry_entry(manifest)
        entry['tags'] = [t for t in entry['tags'] if t != 'imported'] + ['notion-sync']
        registry['skills'].append(entry)
    REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return f'created {skill_id}'


def main() -> int:
    parser = argparse.ArgumentParser(description='Sync staged Notion skill pages into custom_skills/.')
    parser.add_argument('--staging', type=Path, required=True, help='Directory of staged *.md files.')
    parser.add_argument('--dry-run', action='store_true', help='Report actions without writing.')
    args = parser.parse_args()
    files = sorted(args.staging.glob('*.md'))
    ordinal = sum(1 for _ in SKILLS_ROOT.glob('*/manifest.json'))
    for path in files:
        meta, body = parse_staged(path)
        skill_id = meta['repo_id']
        exists = (SKILLS_ROOT / skill_id / 'manifest.json').is_file()
        if args.dry_run:
            print(f"would {'update' if exists else 'create'} {skill_id}")
            continue
        if exists:
            print(update_existing(skill_id, meta, body))
        else:
            ordinal += 1
            print(create_new(skill_id, meta, body, ordinal))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
