#!/usr/bin/env python3
"""Deterministically normalize skill docs and archive provenance metadata."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / 'custom_skills'
SOURCE = REPO / 'docs' / 'sources' / 'Skills_Full_Configurations_Backup_20260818.md'
NORMALIZER_VERSION = '1.3.0'
SCHEMA_VERSION = '1.1.0'


def source_hash() -> str:
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()


def frontmatter_end(lines: list[str]) -> int:
    if not lines or lines[0].strip() != '---':
        return -1
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return i
    return -1


def normalize_headings(text: str) -> str:
    lines = text.splitlines()
    end = frontmatter_end(lines)
    start = end + 1 if end >= 0 else 0
    seen_h1 = False
    output: list[str] = []
    for i, line in enumerate(lines):
        if i < start:
            output.append(line)
            continue
        if re.match(r'^#\s+\S', line):
            if not seen_h1:
                seen_h1 = True
                output.append(line)
            else:
                output.append('#' + line)
        else:
            output.append(line)
    return '\n'.join(output).rstrip() + '\n'


def bullets(values: list[str], fallback: str) -> str:
    if not values:
        return f'- {fallback}'
    return '\n'.join(f'- **{k}**：{v.get("description", "依技能規格提供") if isinstance(v, dict) else v}' for k, v in values)


def append_missing_contract(text: str, manifest: dict) -> str:
    blocks: list[str] = []
    risk = manifest.get('risk_level', 'medium')
    inputs = manifest.get('inputs', {})
    outputs = manifest.get('outputs', {})
    safety = manifest.get('safety', {})
    related = manifest.get('related_skills') or []
    source = manifest.get('source') or {}

    if '## 標準執行契約' not in text:
        blocks.append(
            '## 標準執行契約\n\n'
            '### 觸發與輸入\n\n'
            '僅在使用者需求與本技能描述相符時啟用。先確認目標、受眾、上下文、資料來源、限制與輸出格式；未提供的資訊不得自行補成事實。\n\n'
            '### 執行順序\n\n'
            '1. 盤點輸入、授權、敏感資料與外部依賴。\n'
            '2. 依技能核心流程處理，分開標示事實、推論、假設與建議。\n'
            '3. 產出可審閱結果，列出來源、未驗證事項、風險與人工決策點。\n'
            '4. 輸出前檢查範圍、引用、敏感資料與高影響操作。\n'
        )

    if '## 輸出契約' not in text:
        blocks.append('## 輸出契約\n\n' + bullets(list(outputs.items()), '依 manifest 的 outputs 產出結果、假設與驗證紀錄。') + '\n')

    if '## 安全與人工核准' not in text:
        rules = safety.get('rules') or ['不得捏造資料或來源。', '外部服務採唯讀或草稿模式；寫入、發佈、部署與不可逆操作前須人工批准。']
        blocks.append(
            '## 安全與人工核准\n\n'
            f'目前風險等級：**{risk}**。\n\n'
            + '\n'.join(f'- {r}' for r in rules)
            + '\n'
        )

    if '## 停止條件' not in text:
        blocks.append('## 停止條件\n\n若授權、來源、範圍、關鍵數字、身份或外部操作權限無法確認，停止高影響部分並回報缺口；若發現矛盾、敏感資料暴露或輸出無法驗證，暫停後續動作並要求人工判斷。\n')

    if '## 關聯技能' not in text:
        relation = ', '.join(related) if related else '目前沒有經人工確認的直接關聯技能'
        blocks.append(f'## 關聯技能\n\n本技能與 {relation} 有功能相近或可互補的關係；選擇時以任務範圍、資料來源與權限邊界為準。\n')

    if '## 來源追蹤' not in text:
        if source:
            source_text = f'來源：`{source.get("file", "未指定")}`，項次 {source.get("section_number", "未指定")}，原始行號 {source.get("start_line", "?")}–{source.get("end_line", "?")}。'
        else:
            source_text = '此技能為 repository 內既有技能；來源與維護責任以 manifest 為準。'
        blocks.append(f'## 來源追蹤\n\n{source_text}\n')

    if blocks:
        text = text.rstrip() + '\n\n' + '\n'.join(blocks)
    return text.rstrip() + '\n'


def main() -> None:
    digest = source_hash()
    changed = 0
    for manifest_path in sorted(SKILLS.glob('*/manifest.json')):
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        skill_path = manifest_path.parent / 'SKILL.md'
        text = skill_path.read_text(encoding='utf-8') if skill_path.exists() else ''
        normalized = append_missing_contract(normalize_headings(text), manifest)
        if normalized != text:
            skill_path.write_text(normalized, encoding='utf-8')
            changed += 1
        manifest['schema_version'] = SCHEMA_VERSION
        if (manifest.get('source') or {}).get('type') == 'user_provided_backup':
            manifest.setdefault('source', {})['sha256'] = digest
            manifest['source']['normalizer_version'] = NORMALIZER_VERSION
            manifest['source']['normalized_at'] = '2026-08-18'
            manifest['source']['status'] = 'normalized_and_hardened'
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Normalized {len(list(SKILLS.glob("*/manifest.json")))} manifests; rewrote {changed} SKILL.md files; source_sha256={digest}')


if __name__ == '__main__':
    main()
