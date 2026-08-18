#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TARGETS = {
    'data_analysis': {
        'requires_user_confirmation': True,
        'approval_reason': '輸入可能含個人或業務敏感資料；輸出檔案前需確認資料範圍與遮罩結果。',
    },
    'full-sprint': {
        'requires_user_confirmation': True,
        'approval_reason': '長任務可修改多個檔案、執行 shell 或 git；每個高影響 checkpoint 必須人工核准。',
    },
    'optimizing-google-ads': {
        'requires_user_confirmation': True,
        'approval_reason': '廣告帳戶、預算、受眾與投放設定具商業與財務影響；任何寫入前需人工批准。',
    },
    'to_prd': {
        'requires_user_confirmation': True,
        'approval_reason': 'PRD 可能影響產品範圍、工程承諾與資源配置；輸出前需確認假設與決策邊界。',
    },
    'write_a_skill': {
        'requires_user_confirmation': True,
        'approval_reason': '技能文件可能改變 Agent 行為與權限邊界；納管前需人工審查契約與安全規則。',
    },
}

for ident, patch in TARGETS.items():
    path = REPO / 'custom_skills' / ident / 'manifest.json'
    m = json.loads(path.read_text(encoding='utf-8'))
    s = m.setdefault('safety', {})
    s['requires_user_confirmation'] = patch['requires_user_confirmation']
    s.setdefault('approval_reason', patch['approval_reason'])
    path.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Fixed safety exceptions: {len(TARGETS)}')
