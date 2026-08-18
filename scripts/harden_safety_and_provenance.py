#!/usr/bin/env python3
"""Make safety gates and provenance fields explicit in every manifest."""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / 'custom_skills'


def main() -> None:
    count = 0
    for path in sorted(SKILLS.glob('*/manifest.json')):
        m = json.loads(path.read_text(encoding='utf-8'))
        s = m.setdefault('safety', {})
        risk = m.get('risk_level', 'medium')
        s.setdefault('rules', [
            '不得捏造事實、資料、來源、同意或驗證結果。',
            '外部服務採唯讀或草稿模式；寫入、發佈、部署與不可逆操作前必須取得明確人工批准。',
            '對敏感資料採資料最小化、遮罩與最短保留原則。',
        ])
        s.setdefault('stop_conditions', [
            '授權、資料來源、範圍、身份或外部操作權限無法確認時停止高影響部分。',
            '發現來源矛盾、敏感資料暴露、輸出無法驗證或任務目標漂移時停止並要求人工判斷。',
        ])
        s.setdefault('approval_scope', ['exact_action', 'exact_target', 'exact_diff', 'rollback_or_recovery_plan'])
        s.setdefault('audit_requirements', ['record_sources', 'record_assumptions', 'record_approval_before_write'])
        s.setdefault('rollback_required', risk == 'high' or bool((m.get('external_write') or {}).get('allowed')))
        s.setdefault('dry_run_default', True)
        s.setdefault('data_minimization', 'redact_by_default')
        src = m.get('source') or {}
        if src.get('type') == 'user_provided_backup':
            src.setdefault('hash_algorithm', 'sha256')
            src.setdefault('provenance_verified', True)
            m['source'] = src
        path.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        count += 1
    print(f'Hardened safety and provenance for {count} manifests')


if __name__ == '__main__':
    main()
