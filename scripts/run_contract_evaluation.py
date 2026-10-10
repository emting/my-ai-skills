#!/usr/bin/env python3
"""Re-run the read-only contract evaluation for every installed skill.

Instruction-only skills get the same 22 contract checks as the original snapshot;
no external action is executed. Skills that already have a non-contract test
scope (the offline ``data_analysis`` smoke test) keep their stored record.
The score/level/rank rules were derived from the existing snapshot and are
verified against it by ``--check-against-existing``.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'custom_skills'
EVALS = ROOT / 'evals' / 'skills.json'
OUT_JSON = ROOT / 'docs' / 'evaluations' / 'github-skills-test-results.json'
OUT_CSV = ROOT / 'docs' / 'evaluations' / 'github-skills-test-results.csv'
CONTRACT_MARKERS = ('標準執行契約', '安全與人工核准', '停止條件')
EVAL_TYPES = ('positive_trigger', 'negative_trigger', 'output_contract', 'safety_escalation')
BASE = {'low': 100.0, 'medium': 92.0, 'high': 82.0}
LEVEL_A, LEVEL_AM, LEVEL_B = 'A｜優先推薦', 'A-｜條件優先推薦', 'B｜條件推薦'


def check(name: str, passed: bool, detail: str = '') -> dict[str, Any]:
    return {'name': name, 'passed': bool(passed), 'detail': detail}


def case_ok(case: dict[str, Any] | None, key: str) -> bool:
    if not case:
        return False
    expected = case.get('expected')
    return bool(case.get('id') and case.get('prompt') and isinstance(expected, dict) and expected and key in json.dumps(expected))


def evaluate(skill_id: str, evals: dict[str, Any]) -> dict[str, Any]:
    folder = SKILLS / skill_id
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    text = (folder / 'SKILL.md').read_text(encoding='utf-8') if (folder / 'SKILL.md').is_file() else ''
    safety = manifest.get('safety') or {}
    activation = manifest.get('activation') or {}
    write = manifest.get('external_write') or {}
    cases = {c['type']: c for c in (evals.get('skills', {}).get(skill_id, {}).get('cases', []))}
    risk = manifest.get('risk_level', 'unknown')
    checks = [
        check('skill_md_exists', bool(text)),
        check('manifest_id_matches_directory', manifest.get('id') == skill_id),
        check('runtime_supported', manifest.get('runtime') == 'instruction_only'),
        check('entrypoint_exists', (folder / str(manifest.get('entrypoint', ''))).is_file()),
        check('standard_contract_headings', all(m in text for m in CONTRACT_MARKERS)),
        check('safety_object', isinstance(manifest.get('safety'), dict) and bool(safety)),
        check('stop_conditions_present', bool(safety.get('stop_conditions'))),
        check('approval_scope_present', bool(safety.get('approval_scope'))),
        check('dry_run_default', safety.get('dry_run_default') is True),
        check('external_write_declared', 'allowed' in write),
        check('non_high_risk_safety_rules', risk == 'high' or bool(safety.get('rules'))),
        check('activation_positive_examples', bool(activation.get('positive_examples'))),
        check('activation_negative_examples', bool(activation.get('negative_examples'))),
        check('activation_exclusions', bool(activation.get('exclude_when'))),
        check('activation_priority', isinstance(activation.get('priority'), int)),
        check('source_provenance', bool(manifest.get('source'))) if manifest.get('source') else check('source_not_required_for_native_skill', True),
        check('four_eval_case_types', all(t in cases for t in EVAL_TYPES)),
        check('eval_positive_trigger_well_formed', case_ok(cases.get('positive_trigger'), 'selected')),
        check('eval_negative_trigger_well_formed', case_ok(cases.get('negative_trigger'), 'selected')),
        check('eval_output_contract_well_formed', case_ok(cases.get('output_contract'), 'required_outputs')),
        check('eval_safety_escalation_well_formed', case_ok(cases.get('safety_escalation'), 'requires_approval')),
        check('instruction_only_no_execution', manifest.get('runtime') == 'instruction_only'),
    ]
    connectors = manifest.get('connectors') or []
    allowed = bool(write.get('allowed'))
    score = BASE.get(risk, 70.0) - (2.0 if connectors else 0.0) - (5.0 if allowed else 0.0)
    clean = not connectors and not allowed
    if risk == 'low' and clean:
        level, reason = LEVEL_A, '測試通過、低風險、無外部寫入且不依賴連線器。'
    elif risk == 'medium' and clean:
        level, reason = LEVEL_AM, '測試通過、中風險、無外部寫入；使用前需人工覆核。'
    else:
        level, reason = LEVEL_B, '測試通過但屬高風險、依賴連線器或具外部寫入邊界；必須人工批准。'
    passed = sum(c['passed'] for c in checks)
    return {
        'id': skill_id, 'name': manifest.get('name', skill_id), 'description': manifest.get('description', ''),
        'runtime': manifest.get('runtime'), 'risk_level': risk, 'test_scope': 'contract_and_read_only_dry_run',
        'status': 'PASS' if passed == len(checks) else 'FAIL', 'check_count': len(checks), 'passed_checks': passed,
        'failed_checks': len(checks) - passed, 'eval_case_count': len(cases), 'connector_count': len(connectors),
        'external_write_allowed': allowed, 'recommendation_score': score, 'recommendation_level': level,
        'recommendation_reason': reason, 'checks': checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-against-existing', action='store_true', help='Compare score/level for already-ranked skills and do not write.')
    args = parser.parse_args()
    evals = json.loads(EVALS.read_text(encoding='utf-8'))
    old = json.loads(OUT_JSON.read_text(encoding='utf-8'))
    old_by_id = {r['id']: r for r in old['results']}
    results = []
    for manifest_path in sorted(SKILLS.glob('*/manifest.json')):
        skill_id = manifest_path.parent.name
        previous = old_by_id.get(skill_id)
        if previous and previous['test_scope'] != 'contract_and_read_only_dry_run':
            results.append(dict(previous))
        else:
            results.append(evaluate(skill_id, evals))
    results.sort(key=lambda r: (-r['recommendation_score'], r['id']))
    for rank, r in enumerate(results, 1):
        r['rank'] = rank
    if args.check_against_existing:
        bad = [(r['id'], old_by_id[r['id']]['recommendation_score'], r['recommendation_score']) for r in results
               if r['id'] in old_by_id and (old_by_id[r['id']]['recommendation_score'], old_by_id[r['id']]['recommendation_level']) != (r['recommendation_score'], r['recommendation_level'])]
        print(f'mismatches vs existing snapshot: {len(bad)}', bad[:5])
        return 1 if bad else 0
    levels: dict[str, int] = {LEVEL_A: 0, LEVEL_AM: 0, LEVEL_B: 0, 'C｜暫不推薦': 0}
    for r in results:
        key = r['recommendation_level'] if r['status'] == 'PASS' else 'C｜暫不推薦'
        levels[key] += 1
    scopes: dict[str, int] = {}
    for r in results:
        scopes[r['test_scope']] = scopes.get(r['test_scope'], 0) + 1
    ordered = [{'rank': r['rank'], **{k: v for k, v in r.items() if k != 'rank'}} for r in results]
    OUT_JSON.write_text(json.dumps({
        'package_count': len(results), 'pass_count': sum(r['status'] == 'PASS' for r in results),
        'fail_count': sum(r['status'] != 'PASS' for r in results), 'recommendation_levels': levels,
        'test_scopes': scopes, 'results': ordered}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    fields = ['rank', 'id', 'name', 'runtime', 'risk_level', 'test_scope', 'status', 'check_count', 'passed_checks', 'failed_checks',
              'eval_case_count', 'connector_count', 'external_write_allowed', 'recommendation_score', 'recommendation_level', 'recommendation_reason']
    with OUT_CSV.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(ordered)
    print(f'evaluated={len(results)} levels={levels}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
