#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO / 'custom_skills'
REGISTRY = REPO / 'skills.json'
SOURCE_TYPE = 'user_provided_backup'
REQUIRED_SECTIONS = [
    '## 標準執行契約',
    '## 輸出契約',
    '## 安全與人工核准',
    '## 停止條件',
    '## 關聯技能',
    '## 來源追蹤',
]


def manifests():
    return [json.loads(p.read_text(encoding='utf-8')) for p in sorted(SKILLS_DIR.glob('*/manifest.json'))]


def section(text: str, heading: str) -> bool:
    return heading in text


def completeness(ms):
    dirs = [p for p in SKILLS_DIR.iterdir() if p.is_dir() and ((p / 'manifest.json').exists() or (p / 'SKILL.md').exists())]
    okay = 0
    for m in ms:
        d = SKILLS_DIR / m['id']
        if d.is_dir() and (d / 'SKILL.md').exists() and (d / m.get('entrypoint', 'SKILL.md')).exists():
            okay += 1
    return okay / max(len(dirs), len(ms), 1), {'manifests': len(ms), 'skill_dirs': len(dirs), 'complete': okay}


def validator_passes():
    p = subprocess.run([sys.executable, str(REPO / 'scripts/validate_repo.py')], cwd=REPO, capture_output=True, text=True)
    return p.returncode == 0, (p.stdout + p.stderr)[-800:]


def provenance(ms):
    archive = [m for m in ms if (m.get('source') or {}).get('type') == SOURCE_TYPE]
    if not archive:
        return 1.0, {'archive': 0, 'complete': 0}
    fields = ('file', 'section_number', 'start_line', 'end_line', 'sha256', 'normalizer_version', 'normalized_at', 'hash_algorithm', 'provenance_verified')
    complete = sum(bool((m.get('source') or {}).get(k)) for m in archive for k in fields)
    return complete / (len(archive) * len(fields)), {'archive': len(archive), 'complete_fields': complete, 'expected_fields': len(archive) * len(fields), 'required_fields': list(fields)}


def documentation(ms):
    okay = 0
    duplicate_h1 = 0
    missing = {}
    for m in ms:
        p = SKILLS_DIR / m['id'] / 'SKILL.md'
        text = p.read_text(encoding='utf-8') if p.exists() else ''
        h1 = len(re.findall(r'^#\s+.+$', text, re.M))
        if h1 > 1:
            duplicate_h1 += 1
        absent = [s for s in REQUIRED_SECTIONS if not section(text, s)]
        if h1 == 1 and not absent:
            okay += 1
        if absent:
            missing[m['id']] = absent
    return okay / max(len(ms), 1), {'passing': okay, 'total': len(ms), 'duplicate_h1': duplicate_h1, 'missing': missing}


def permissions(ms):
    okay = 0
    missing = []
    for m in ms:
        if all(k in m for k in ('capabilities', 'connectors', 'data_egress', 'external_write')):
            okay += 1
        else:
            missing.append(m.get('id'))
    return okay / max(len(ms), 1), {'passing': okay, 'total': len(ms), 'missing': missing}


def activation(ms):
    okay = 0
    missing = []
    for m in ms:
        a = m.get('activation') or {}
        if all(a.get(k) not in (None, [], '') for k in ('positive_examples', 'negative_examples', 'exclude_when', 'priority')):
            okay += 1
        else:
            missing.append(m.get('id'))
    return okay / max(len(ms), 1), {'passing': okay, 'total': len(ms), 'missing': missing}


def safety(ms):
    okay = 0
    failures = []
    for m in ms:
        s = m.get('safety') or {}
        r = m.get('risk_level')
        rules = s.get('rules') or []
        stop = bool(s.get('stop_conditions')) or any('停止' in x or 'stop' in x.lower() for x in rules)
        approval = s.get('requires_user_confirmation') is True
        approval_scope = bool(s.get('approval_scope'))
        recovery = 'rollback_required' in s and 'dry_run_default' in s
        high_ok = r != 'high' or approval
        if rules and high_ok and stop and approval_scope and recovery:
            okay += 1
        else:
            failures.append(m.get('id'))
    return okay / max(len(ms), 1), {'passing': okay, 'total': len(ms), 'failures': failures}


def evals(ms):
    candidates = [REPO / 'evals' / 'skills.json', REPO / 'tests' / 'skill_evals.json']
    data = None
    for p in candidates:
        if p.exists():
            data = json.loads(p.read_text(encoding='utf-8'))
            break
    if not data:
        return 0.0, {'skills_with_cases': 0, 'total': len(ms)}
    cases = data.get('skills', data)
    okay = 0
    for m in ms:
        item = cases.get(m['id'], {}) if isinstance(cases, dict) else {}
        types = {c.get('type') for c in item.get('cases', [])} if isinstance(item, dict) else set()
        if {'positive_trigger', 'negative_trigger', 'output_contract', 'safety_escalation'} <= types:
            okay += 1
    return okay / max(len(ms), 1), {'skills_with_cases': okay, 'total': len(ms)}


def maintainability(ms):
    required = [REPO / 'scripts/import_skill_archive.py', REPO / 'scripts/install_local_skills.py', REPO / 'scripts/validate_repo.py']
    pass_count = sum(p.exists() for p in required)
    return pass_count / len(required), {'files': [str(p.relative_to(REPO)) for p in required if p.exists()], 'expected': len(required)}


def ci():
    workflows = list((REPO / '.github' / 'workflows').glob('*.yml')) + list((REPO / '.github' / 'workflows').glob('*.yaml'))
    text = '\n'.join(p.read_text(encoding='utf-8') for p in workflows)
    required = ['validate_repo.py', 'pytest', 'compileall']
    passed = sum(x in text for x in required)
    return passed / len(required), {'workflows': len(workflows), 'checks': {x: x in text for x in required}}


def main():
    ms = manifests()
    checks = {}
    checks['package_completeness'] = completeness(ms)
    valid, validator_tail = validator_passes()
    checks['registry_schema'] = (1.0 if valid else 0.0, {'validator_passed': valid, 'tail': validator_tail})
    checks['source_reproducibility'] = provenance(ms)
    checks['documentation_structure'] = documentation(ms)
    checks['permission_dataflow'] = permissions(ms)
    checks['activation_selection'] = activation(ms)
    checks['safety_governance'] = safety(ms)
    checks['behavior_evaluation'] = evals(ms)
    checks['maintainability'] = maintainability(ms)
    checks['ci_open_source'] = ci()
    total = sum(value for value, _ in checks.values()) * 10 / len(checks)
    print(json.dumps({'score': round(total, 3), 'dimensions': {k: {'score': round(v, 3), 'evidence': e} for k, (v, e) in checks.items()}}, ensure_ascii=False, indent=2))
    return 0 if total >= 9.5 else 1


if __name__ == '__main__':
    raise SystemExit(main())
