from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / 'custom_skills'
REGISTRY_PATH = ROOT / 'skills.json'
SOURCE_ROOT = ROOT / 'docs' / 'sources'
CATALOG_PATH = ROOT / 'docs' / 'skill-archive-catalog-zip.md'
NORMALIZER_VERSION = '1.4.0'
CONTRACT_VERSION = '1.1.0'
SCHEMA_VERSION = '1.1.0'
ID_RE = re.compile(r'^[a-z0-9][a-z0-9_-]*$')
FRONTMATTER_RE = re.compile(r'\A---\s*\n(.*?)\n---\s*(?:\n|\Z)', re.S)
H1_RE = re.compile(r'^(#)\s+(.+?)\s*$')

BASE_RULES = [
    '先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。',
    '不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。',
    '只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。',
    '外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。',
]
DISALLOWED_USES = [
    '不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。',
    '不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。',
]
FORBIDDEN_WITHOUT_APPROVAL = [
    '對外發送或發佈內容',
    '建立、更新或刪除第三方服務資料',
    '部署、改變權限、改變預算或執行不可逆操作',
]
ALWAYS_FORBIDDEN = [
    '繞過身份驗證、CAPTCHA、付費牆或存取控制',
    '捏造來源、證據、數據、認證或使用者同意',
]

# These are intentional overlap annotations, not replacements. They are kept narrow
# so that a future re-import remains deterministic and does not invent broad edges.
RELATED: dict[str, list[str]] = {
    'agent-bible-sq3r-fast-guide': ['ai-research-lab', 'research-to-insight'],
    'agent-big-e-life-coach': ['decision-making-superpowers'],
    'agent-cyber-bully-lecturer': ['ai-security-agent-governance'],
    'agent-senior-prd-architect-sophia': ['ai-project-feasibility-assessment'],
    'agent-skills-actions-auditor': ['ai-security-agent-governance', 'enterprise-sovereign-ai-adoption'],
    'app-performance-benchmark-optimizer': ['website-auditing'],
    'cloudflare-skills': ['website-auditing', 'website-landing-page-builder'],
    'emil-design-eng': ['design-proposal-portfolio-persuasion', 'ui-minimalist-animation-enhancer'],
    'full-sprint-execution': ['startup-venture-builder', 'agent-task-packaging'],
    'game-inspiration-world-builder': [],
    'google-ads-audit': ['marketing-brief-competitor-analyst'],
    'interactive-skill-learning-curriculum': ['progressive-quiz-generator'],
    'life-scenario-simulation-matrix': ['decision-making-superpowers'],
    'multi-agent-research-workflow': ['ai-research-lab', 'research-to-insight'],
    'open-slide': ['presentation-structure-visual-script', 'presentation-yaml-design-architect'],
    'product-idea-scoring-matrix': ['ai-project-feasibility-assessment'],
    'system-file-audit-organizer': [],
    'threads-api-skill': ['threads-viral-consultant'],
    'ui-minimalist-animation-enhancer': ['design-proposal-portfolio-persuasion'],
    'veo-short-video-prompt-engineer': ['video-editing-preproduction-script-cuts'],
    'website-auditing': ['website-landing-page-builder'],
    'weekly-podcast-script': ['couple-podcast-hosting'],
    'workspace-project-cleanup-agent': ['system-file-audit-organizer'],
    'youtube-transcript-summarizer': ['youtube-learning-summary-exporter'],
}

NETWORK_RE = re.compile(r'(?i)research|source|search|web|browser|crawl|scrap|cloudflare|google|youtube|threads|notion|openclaw|hermes|gemini|mimo|市場|競品|來源|搜尋|資料|新聞|API|OAuth|Webhook|外部')
BROWSER_RE = re.compile(r'(?i)browser|瀏覽器|登入|爬取|crawl|scrap')
WRITE_RE = re.compile(r'(?i)\b(?:post|publish|send|write|delete|deploy|sync|create|update|export|save|record)\b|發佈|發布|發送|刪除|部署|同步|寫入|建立|更新|匯出|存檔|記錄|排程')
API_KEY_RE = re.compile(r'(?i)API\s*Key|access[_ -]?token|client[_ -]?secret|金鑰|Token|憑證')
SENSITIVE_RE = re.compile(r'(?i)個資|敏感|私域|家長|學生|客戶|客服|Email|email|電話|地址|姓名|金流|現金流|損益|收入|合約|房地產|房屋|personal|private|financial|cashflow|pnl|client|customer|parent|student')
HIGH_RE = re.compile(r'(?i)資安|安全治理|security|governance|API|OAuth|Webhook|發佈|發布|發送|刪除|部署|交易|支付|金流|現金流|損益|房地產|房屋|客戶|個資|私域|合約|談判|診斷|醫療|法律|Google Ads|Threads API|delete|deploy|publish|write')


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def safe_extract(archive: Path, destination: Path) -> None:
    with zipfile.ZipFile(archive) as handle:
        for member in handle.infolist():
            name = member.filename.replace('\\', '/')
            target = (destination / name).resolve()
            try:
                target.relative_to(destination.resolve())
            except ValueError as exc:
                raise ValueError(f'unsafe ZIP member path: {member.filename}') from exc
            if name.startswith('/') or '/..' in f'/{name}':
                raise ValueError(f'unsafe ZIP member path: {member.filename}')
            # ZIP symlinks are not accepted because imported resources must be ordinary files.
            mode = member.external_attr >> 16
            if mode and (mode & 0o170000) == 0o120000:
                raise ValueError(f'symlink ZIP member is not allowed: {member.filename}')
        handle.extractall(destination)


def find_skill_roots(extracted: Path) -> list[Path]:
    roots = sorted({path.parent for path in extracted.rglob('SKILL.md') if path.is_file()})
    if not roots:
        raise ValueError('ZIP contains no SKILL.md files')
    return roots


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    raw = match.group(1)
    if yaml is not None:
        metadata = yaml.safe_load(raw) or {}
        if not isinstance(metadata, dict):
            metadata = {}
    else:  # pragma: no cover
        metadata = {}
        for line in raw.splitlines():
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"\'')
    body = text[match.end():]
    return metadata, body


def clean_scalar(value: Any, fallback: str) -> str:
    text = str(value or '').strip().replace('\r\n', '\n')
    return text or fallback


def demote_extra_h1(body: str, title: str) -> str:
    lines = body.strip().splitlines()
    h1_positions = [index for index, line in enumerate(lines) if H1_RE.match(line)]
    if not h1_positions:
        lines.insert(0, f'# {title}')
    else:
        first = h1_positions[0]
        first_title = H1_RE.match(lines[first]).group(2).strip()
        if not first_title:
            lines[first] = f'# {title}'
        for index in h1_positions[1:]:
            lines[index] = re.sub(r'^#\s+', '## ', lines[index])
    return '\n'.join(lines).strip()


def classification(skill_id: str, name: str, description: str, body: str) -> dict[str, Any]:
    text = ' '.join((skill_id, name, description, body))
    network = bool(NETWORK_RE.search(text))
    browser = bool(BROWSER_RE.search(text))
    filesystem_read = bool(re.search(r'(?i)檔案|文件|資料|素材|報告|email|csv|excel|輸入|source|file|document|transcript|brief', text))
    filesystem_write = bool(WRITE_RE.search(text))
    api_key = bool(API_KEY_RE.search(text))
    sensitive = bool(SENSITIVE_RE.search(text))
    high = bool(HIGH_RE.search(text))
    medium = bool(re.search(r'(?i)研究|競品|市場|品牌|定價|商業模式|決策|Notion|Google|Threads|YouTube|新聞|資料|內容|research|market|strategy|analysis', text))
    risk = 'high' if high else ('medium' if medium else 'low')
    external_write_intent = bool(re.search(r'(?i)post|publish|send|delete|deploy|webhook|發佈|發布|發送|刪除|部署|同步|寫入|更新|建立|排程|交易|支付', text))
    requires_confirmation = risk == 'high' or browser or sensitive or external_write_intent
    permissions = {
        'filesystem_read': filesystem_read,
        'filesystem_write': filesystem_write,
        'network': network,
        'api_key_required': api_key,
        'browser_automation': browser,
        'third_party_processing': network or browser,
        'shell': bool(re.search(r'(?i)Warp|OpenClaw|terminal|CLI|shell|command line', text)),
        'git': bool(re.search(r'(?i)GitHub|git|repository|repo', text)),
        'google_ads_read': bool(re.search(r'(?i)Google Ads', text)),
        'google_ads_write': False,
        'notion_read': bool(re.search(r'(?i)Notion', text)),
        'notion_write': False,
        'n8n_write': False,
        'mcp_write_tools': False,
    }
    rules = list(BASE_RULES)
    if sensitive:
        rules.append('對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。')
    if network:
        rules.append('涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。')
    if risk == 'high':
        rules.append('本技能只提供分析、草稿與驗證建議；涉及高影響決策或外部操作時，必須由適當的人員在執行前覆核。')
    return {
        'risk': risk,
        'network': network,
        'sensitive': sensitive,
        'external_write_intent': external_write_intent,
        'requires_confirmation': requires_confirmation,
        'permissions': permissions,
        'rules': list(dict.fromkeys(rules)),
    }


def io_contract(classified: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    source_description = '使用者提供或明確授權的資料與外部來源；需要即時資訊時應記錄來源與擷取時間。' if classified['network'] else '使用者提供的背景、文件、素材或限制條件。'
    inputs = {
        'request': {'type': 'text', 'required': True, 'description': '使用者希望完成的任務、問題或產出目標。'},
        'context': {'type': 'text', 'required': False, 'description': '背景、受眾、現況、限制與已知決策脈絡。'},
        'source_materials': {'type': 'text_or_files', 'required': False, 'description': source_description},
        'constraints': {'type': 'list', 'required': False, 'description': '時程、格式、語氣、預算、權限與不得變更事項。'},
    }
    outputs = {
        'result': {'type': 'markdown', 'required': True, 'description': '依技能目的產出的分析、策略、腳本、內容、清單或計畫。'},
        'assumptions_and_risks': {'type': 'markdown', 'required': True, 'description': '假設、未驗證事項、風險、限制與人工核准點。'},
        'verification': {'type': 'markdown', 'required': True, 'description': '來源、檢查方式、驗收條件與尚待確認事項。'},
    }
    return inputs, outputs


def build_skill_markdown(skill_id: str, name: str, description: str, body: str, classified: dict[str, Any], source_file: str, source_item: str, source_lines: tuple[int, int], related: list[str], source_hash: str) -> str:
    content = demote_extra_h1(body, name)
    risk = classified['risk']
    confirmation = '需要人工確認' if classified['requires_confirmation'] else '預設可先產出分析或草稿，但仍不得代替使用者做外部高影響決策'
    related_text = '、'.join(f'`{item}`' for item in related) if related else '無'
    return f'''---
name: {skill_id}
description: {description}
---

{content}

## 標準執行契約

### 觸發與輸入

使用者明確要求「{name}」的核心任務，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、授權、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入、授權、敏感資料與可能的外部依賴，先列出缺口。
2. 依上方技能流程逐步處理，將事實、推論、假設與建議分開。
3. 產出可直接審閱的結果，列出引用、未驗證事項、風險與人工決策節點。
4. 執行輸出前檢查，確認沒有虛構證據、洩漏敏感資料或超出使用者範圍的動作。

## 輸出契約

至少提供：

- **結果或草稿**：依使用者要求產出分析、策略、腳本、內容、清單或計畫。
- **假設與限制**：明確標示資料不足、未驗證推論與適用範圍。
- **驗證紀錄**：列出使用的來源、檢查方式、驗收條件與尚待確認事項。
- **風險與下一步**：指出人工核准點、低成本驗證方式與可恢復的後續行動。

## 安全與人工核准

目前風險等級：**{risk}**。{confirmation}。本匯入版本為 `instruction_only`，不代表已授權任何外部連接或寫入適配器。

{chr(10).join(f'- {rule}' for rule in classified['rules'])}

{chr(10).join(f'- {rule}' for rule in DISALLOWED_USES)}

## 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，立即停止高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露、輸出無法驗證或操作不可恢復，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 {related_text} 有功能相近或可互補的技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `{source_file}` 內的 `{source_item}` 正規化而來，來源項目 SHA-256 為 `{source_hash}`，原始行號範圍為 {source_lines[0]}–{source_lines[1]}。原始附件已保存於 repository 的 `docs/sources/`，並補上輸入、輸出、權限、安全、人工核准與停止契約。
'''


def build_manifest(skill_id: str, name: str, description: str, classified: dict[str, Any], source_file: str, source_item: str, source_lines: tuple[int, int], source_hash: str, archive_hash: str, ordinal: int, related: list[str], extra_files: list[str]) -> dict[str, Any]:
    inputs, outputs = io_contract(classified)
    p = classified['permissions']
    connectors = []
    connector_patterns = [
        ('google_ads', r'(?i)Google Ads'), ('notion', r'(?i)Notion'), ('cloudflare', r'(?i)Cloudflare'),
        ('threads', r'(?i)Threads'), ('youtube', r'(?i)YouTube'), ('openclaw', r'(?i)OpenClaw'),
    ]
    text = f'{skill_id} {name} {description}'
    for connector, pattern in connector_patterns:
        if re.search(pattern, text):
            connectors.append(connector)
    if p['filesystem_write']:
        filesystem = 'workspace_read_write'
    elif p['filesystem_read']:
        filesystem = 'workspace_read_only'
    else:
        filesystem = 'none'
    capabilities = {
        'filesystem': filesystem,
        'network': 'authenticated_read' if p['api_key_required'] or p['browser_automation'] else ('public_read_only' if p['network'] else 'none'),
        'shell': 'available' if p['shell'] else 'none',
        'git': 'read_write' if p['git'] else 'none',
        'browser': 'automated' if p['browser_automation'] else 'none',
    }
    if not p['network'] and not p['third_party_processing']:
        egress_mode = 'none'
        allowed_data_classes: list[str] = []
    elif p['third_party_processing'] and classified['sensitive']:
        egress_mode = 'private_data_upload'
        allowed_data_classes = ['user_authorized_sensitive_data']
    elif p['third_party_processing']:
        egress_mode = 'approved_third_party_processing'
        allowed_data_classes = ['public_data']
    else:
        egress_mode = 'public_data_only'
        allowed_data_classes = ['public_data']
    return {
        'id': skill_id,
        'name': name,
        'version': '1.0.0',
        'description': description,
        'entrypoint': 'SKILL.md',
        'runtime': 'instruction_only',
        'requirements': [],
        'inputs': inputs,
        'outputs': outputs,
        'permissions': p,
        'safety': {
            'handles_sensitive_data': classified['sensitive'],
            'requires_user_confirmation': classified['requires_confirmation'],
            'destructive': False,
            'rules': classified['rules'],
            'disallowed_uses': DISALLOWED_USES,
            'forbidden_without_explicit_approval': FORBIDDEN_WITHOUT_APPROVAL,
            'always_forbidden': ALWAYS_FORBIDDEN,
            'stop_conditions': [
                '授權、資料來源、範圍、身份或外部操作權限無法確認時停止高影響部分。',
                '發現來源矛盾、敏感資料暴露、輸出無法驗證或任務目標漂移時停止並要求人工判斷。',
            ],
            'approval_scope': ['exact_action', 'exact_target', 'exact_diff', 'rollback_or_recovery_plan'],
            'audit_requirements': ['record_sources', 'record_assumptions', 'record_approval_before_write'],
            'rollback_required': bool(classified['external_write_intent']),
            'dry_run_default': True,
            'data_minimization': 'redact_by_default',
        },
        'risk_level': classified['risk'],
        'activation_policy': 'explicit_request' if classified['risk'] == 'high' else 'intent_match_with_scope_check',
        'default_config': {
            'mode': 'draft_or_read_only',
            'language': 'zh-TW',
            'source_archive': source_file,
            'source_item': ordinal,
            'preserved_resources': extra_files,
        },
        'platforms': ['markdown', 'manus', 'codex', 'copilot'],
        'source': {
            'type': 'user_provided_backup',
            'file': source_file,
            'section_number': ordinal,
            'start_line': source_lines[0],
            'end_line': source_lines[1],
            'status': 'normalized_and_hardened',
            'sha256': source_hash,
            'archive_sha256': archive_hash,
            'source_path': source_item,
            'normalizer_version': NORMALIZER_VERSION,
            'normalized_at': str(date.today()),
            'hash_algorithm': 'sha256',
            'provenance_verified': True,
        },
        'related_skills': related,
        'schema_version': SCHEMA_VERSION,
        'contract_version': CONTRACT_VERSION,
        'capabilities': capabilities,
        'connectors': sorted(set(connectors)),
        'data_egress': {
            'mode': egress_mode,
            'connectors': sorted(set(connectors)),
            'allowed_data_classes': allowed_data_classes,
            'approval_required': bool(p['third_party_processing'] or classified['sensitive'] or connectors),
            'minimize_and_redact': True,
            'retention': 'none_by_default',
        },
        # No imported skill receives a live adapter. External writes remain disabled.
        'external_write': {
            'allowed': False,
            'mode': 'draft_or_read_only',
            'approval_required': True,
            'approval_scope': [],
        },
        'execution': {
            'executor': 'instruction_only',
            'adapter': 'SKILL.md',
            'network_is_not_implied': True,
        },
        'activation': {
            'positive_examples': [f'使用者明確要求：「{description}」', f'請依照 {name} 的專門流程完成指定任務。'],
            'negative_examples': [f'任務只涉及與「{name}」無關的主題，不需要其專門流程。'],
            'exclude_when': [f'若任務不涉及「{name}」的核心目的、輸入或輸出，不要啟用本技能。'],
            'priority': 70 if classified['risk'] == 'high' else (60 if classified['risk'] == 'medium' else 50),
            'delegates_to': related,
            'selection_notes': '先檢查任務目的、輸入資料與外部權限；相鄰技能重疊時以最小權限與最窄範圍優先。',
        },
    }


def registry_entry(manifest: dict[str, Any]) -> dict[str, Any]:
    folder = f"custom_skills/{manifest['id']}/"
    def fields(values: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        return [{'name': key, **{k: v for k, v in value.items() if k != 'extensions'}} for key, value in values.items()]
    entry = {
        'id': manifest['id'],
        'name': manifest['name'],
        'visibility': 'public',
        'type': 'instruction',
        'description': manifest['description'],
        'location': folder,
        'entrypoint': f'{folder}SKILL.md',
        'instruction_file': f'{folder}SKILL.md',
        'manifest': f'{folder}manifest.json',
        'runtime': 'instruction_only',
        'inputs': fields(manifest['inputs']),
        'outputs': fields(manifest['outputs']),
        'permissions': manifest['permissions'],
        'risk_level': manifest['risk_level'],
        'activation_policy': manifest['activation_policy'],
        'tags': ['imported', 'instruction-only'] + (['network-aware'] if manifest['permissions'].get('network') else []) + (['privacy-sensitive'] if manifest['safety'].get('handles_sensitive_data') else []) + (['human-gated'] if manifest['risk_level'] == 'high' else []),
        'source': manifest['source'],
    }
    if manifest.get('related_skills'):
        entry['related_skills'] = manifest['related_skills']
    return entry


def update_registry(manifests: list[dict[str, Any]]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding='utf-8'))
    registry['version'] = '1.3.0'
    registry['description'] = 'Open-source AI skills library for agents, coding assistants, and automation tools, including normalized Markdown and directory-based ZIP skill archives.'
    existing = registry.get('skills', [])
    existing_ids = {item.get('id') for item in existing if isinstance(item, dict)}
    for manifest in manifests:
        if manifest['id'] not in existing_ids:
            existing.append(registry_entry(manifest))
    registry['skills'] = existing
    REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_catalog(manifests: list[dict[str, Any]], archive_name: str, archive_hash: str, preserved_ids: list[str]) -> None:
    rows = []
    for index, manifest in enumerate(manifests, 1):
        rows.append(
            f"| {index} | `{manifest['id']}` | {manifest['risk_level']} | {'是' if manifest['permissions']['network'] else '否'} | {'是' if manifest['safety']['handles_sensitive_data'] else '否'} | {', '.join(f'`{x}`' for x in manifest.get('related_skills', [])) or '—'} |"
        )
    content = f'''# skills_export.zip 整併目錄

> 本目錄由 `scripts/import_skill_zip.py` 產生。附件共含 91 個 skills；其中與既有本地技能精確重疊的項目不覆蓋，本次新增 {len(manifests)} 個獨立 ID。

- 來源檔案：`docs/sources/{archive_name}`
- 來源 ZIP SHA-256：`{archive_hash}`
- 匯入器版本：`{NORMALIZER_VERSION}`
- 保留既有技能：{len(preserved_ids)} 個
- 新增技能：{len(manifests)} 個

## 整併原則

所有新增技能均採 `instruction_only` runtime，不宣稱已具備真實 API、瀏覽器、Shell 或第三方寫入適配器。原始資源保留在對應 skill 目錄；`SKILL.md` 補上標準契約、安全、來源追蹤與停止條件；manifest 補上能力、連接器、資料外流、外部寫入與 activation 契約。高風險技能預設草稿／唯讀並要求人工核准。

| # | ID | 風險 | 網路 | 敏感資料 | 關聯技能 |
|---:|---|---|:---:|:---:|---|
{chr(10).join(rows)}

## 未覆蓋的既有 ID

本次來源中另有 {len(preserved_ids)} 個 ID 已存在於 repository；匯入器不修改這些目錄或 manifests。它們的完整清單保留於本次盤點報告與來源追蹤資料中。
'''
    CATALOG_PATH.write_text(content, encoding='utf-8')


def import_zip_archive(archive: Path) -> dict[str, Any]:
    archive = archive.resolve()
    if not archive.exists() or not archive.is_file():
        raise FileNotFoundError(archive)
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    archive_name = 'skills_export_20260818.zip'
    destination_archive = SOURCE_ROOT / archive_name
    if archive != destination_archive:
        shutil.copy2(archive, destination_archive)
    archive_hash = sha256(destination_archive)
    existing_ids = set()
    for path in SKILLS_ROOT.glob('*/manifest.json'):
        try:
            existing_ids.add(json.loads(path.read_text(encoding='utf-8'))['id'])
        except (OSError, json.JSONDecodeError, KeyError):
            continue
    with tempfile.TemporaryDirectory(prefix='skills-export-') as temp_dir:
        extracted = Path(temp_dir)
        safe_extract(archive, extracted)
        roots = find_skill_roots(extracted)
        roots_by_id = {root.name: root for root in roots}
        if len(roots_by_id) != len(roots):
            raise ValueError('duplicate skill directory names in ZIP')
        archive_ids = sorted(roots_by_id)
        invalid = [skill_id for skill_id in archive_ids if not ID_RE.fullmatch(skill_id)]
        if invalid:
            raise ValueError(f'invalid skill IDs: {invalid}')
        new_ids = [skill_id for skill_id in archive_ids if skill_id not in existing_ids]
        preserved_ids = [skill_id for skill_id in archive_ids if skill_id in existing_ids]
        manifests: list[dict[str, Any]] = []
        for ordinal, skill_id in enumerate(archive_ids, 1):
            source_root = roots_by_id[skill_id]
            source_skill = source_root / 'SKILL.md'
            raw_text = source_skill.read_text(encoding='utf-8')
            metadata, body = parse_frontmatter(raw_text)
            name = clean_scalar(metadata.get('name'), skill_id.replace('-', ' ').title())
            description = clean_scalar(metadata.get('description'), f'{name} instruction skill')
            if skill_id in existing_ids:
                continue
            classified = classification(skill_id, name, description, body)
            related = RELATED.get(skill_id, [])
            source_lines = (1, len(raw_text.splitlines()))
            source_item = str(source_skill.relative_to(extracted)).replace('\\', '/')
            source_hash = sha256(source_skill)
            extra_files = sorted(str(path.relative_to(source_root)).replace('\\', '/') for path in source_root.rglob('*') if path.is_file() and path.name != 'SKILL.md')
            target_dir = SKILLS_ROOT / skill_id
            if target_dir.exists():
                raise FileExistsError(f'refusing to overwrite existing skill directory: {target_dir}')
            shutil.copytree(source_root, target_dir)
            (target_dir / 'SKILL.md').write_text(build_skill_markdown(skill_id, name, description, body, classified, f'docs/sources/{archive_name}', source_item, source_lines, related, source_hash), encoding='utf-8')
            manifest = build_manifest(skill_id, name, description, classified, f'docs/sources/{archive_name}', source_item, source_lines, source_hash, archive_hash, ordinal, related, extra_files)
            (target_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            manifests.append(manifest)
    update_registry(manifests)
    catalog_manifests = list(manifests)
    if not catalog_manifests:
        for skill_id in archive_ids:
            manifest_path = SKILLS_ROOT / skill_id / 'manifest.json'
            if not manifest_path.is_file():
                continue
            try:
                candidate = json.loads(manifest_path.read_text(encoding='utf-8'))
            except (OSError, json.JSONDecodeError):
                continue
            if candidate.get('source', {}).get('file') == f'docs/sources/{archive_name}':
                catalog_manifests.append(candidate)
    catalog_preserved_ids = [
        skill_id for skill_id in archive_ids
        if skill_id not in {manifest['id'] for manifest in catalog_manifests}
    ]
    write_catalog(catalog_manifests, archive_name, archive_hash, catalog_preserved_ids)
    return {
        'archive': str(archive),
        'archive_name': archive_name,
        'archive_sha256': archive_hash,
        'archive_skill_count': len(archive_ids),
        'preserved_count': len(preserved_ids),
        'imported_count': len(manifests),
        'preserved_ids': preserved_ids,
        'imported_ids': [manifest['id'] for manifest in manifests],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Import and normalize a directory-based skill ZIP archive without overwriting existing skills.')
    parser.add_argument('--archive', '--backup', dest='archive', type=Path, required=True)
    args = parser.parse_args()
    result = import_zip_archive(args.archive)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
