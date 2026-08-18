#!/usr/bin/env python3
"""Add explicit execution, connector, data-egress and external-write semantics."""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / 'custom_skills'
CONTRACT_VERSION = '1.1.0'

EXTERNAL_KEYS = {
    'browser_automation': 'browser',
    'google_ads_read': 'google_ads',
    'google_ads_write': 'google_ads',
    'notion_read': 'notion',
    'notion_write': 'notion',
    'n8n_write': 'n8n',
    'mcp_write_tools': 'mcp',
}
WRITE_KEYS = {'google_ads_write', 'notion_write', 'n8n_write', 'mcp_write_tools'}


def capability(manifest: dict) -> dict:
    p = manifest.get('permissions') or {}
    read = bool(p.get('filesystem_read'))
    write = bool(p.get('filesystem_write'))
    net = bool(p.get('network'))
    shell = bool(p.get('shell'))
    git = bool(p.get('git'))
    return {
        'filesystem': 'workspace_read_write' if write else ('workspace_read_only' if read else 'none'),
        'network': 'authenticated_read' if p.get('api_key_required') or p.get('browser_automation') else ('public_read_only' if net else 'none'),
        'shell': 'available' if shell else 'none',
        'git': 'read_write' if git else 'none',
        'browser': 'automated' if p.get('browser_automation') else 'none',
    }


def connectors(manifest: dict) -> list[str]:
    p = manifest.get('permissions') or {}
    return sorted({value for key, value in EXTERNAL_KEYS.items() if p.get(key)})


def external_write(manifest: dict) -> dict:
    p = manifest.get('permissions') or {}
    allowed = any(p.get(k) for k in WRITE_KEYS) or bool(p.get('git'))
    return {
        'allowed': allowed,
        'mode': 'draft_or_read_only' if not allowed else 'draft_only_until_approval',
        'approval_required': True,
        'approval_scope': ['exact target', 'exact diff', 'rollback or recovery plan'] if allowed else [],
    }


def data_egress(manifest: dict, connectors_list: list[str]) -> dict:
    p = manifest.get('permissions') or {}
    s = manifest.get('safety') or {}
    third_party = bool(p.get('third_party_processing'))
    network = bool(p.get('network'))
    sensitive = bool(s.get('handles_sensitive_data'))
    if not network and not third_party:
        mode = 'none'
    elif third_party and sensitive:
        mode = 'private_data_upload'
    elif third_party:
        mode = 'approved_third_party_processing'
    else:
        mode = 'public_data_only'
    return {
        'mode': mode,
        'connectors': connectors_list,
        'allowed_data_classes': ['public_data'] if mode in {'public_data_only', 'approved_third_party_processing'} else (['user_authorized_sensitive_data'] if mode == 'private_data_upload' else []),
        'approval_required': bool(third_party or sensitive or connectors_list),
        'minimize_and_redact': True,
        'retention': 'none_by_default',
    }


def main() -> None:
    count = 0
    for path in sorted(SKILLS.glob('*/manifest.json')):
        m = json.loads(path.read_text(encoding='utf-8'))
        cs = connectors(m)
        m['contract_version'] = CONTRACT_VERSION
        m['capabilities'] = capability(m)
        m['connectors'] = cs
        m['data_egress'] = data_egress(m, cs)
        m['external_write'] = external_write(m)
        m.setdefault('execution', {})['executor'] = m.get('runtime', 'instruction_only')
        m['execution']['adapter'] = m.get('entrypoint', 'SKILL.md')
        m['execution']['network_is_not_implied'] = True
        path.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        count += 1
    print(f'Upgraded capability contract for {count} manifests to {CONTRACT_VERSION}')


if __name__ == '__main__':
    main()
