#!/usr/bin/env python3
"""Add deterministic activation and delegation metadata to all skills."""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / 'custom_skills'

GROUPS = {
    'managing-public-relations': {
        'related': ['pr-brand-crisis-management'],
        'positive': '處理日常媒體關係、品牌訊息、採訪準備或一般公關溝通。',
        'negative': '處理已發生、正在擴散或需要危機應變的聲譽事件。',
        'exclude': '若已有聲譽危機、重大爭議或媒體危機，改由 pr-brand-crisis-management 主導。',
    },
    'pr-brand-crisis-management': {
        'related': ['managing-public-relations'],
        'positive': '處理已發生或正在升級的品牌危機、負面事件與聲譽修復。',
        'negative': '只需要一般公關排程、媒體名單或日常品牌訊息。',
        'exclude': '沒有實際危機或高影響聲譽事件時，不要因為出現 brand 或 PR 字樣而啟用。',
    },
    'ai-research-lab': {
        'related': ['research-lab'],
        'positive': '設計研究實驗、研究假設、研究方法或實驗室治理。',
        'negative': '只要求完成一般資料蒐集、查證或研究報告。',
        'exclude': '若重點是資料蒐集與報告產出，交由 research-lab；若重點是研究實驗設計才啟用。',
    },
    'research-lab': {
        'related': ['ai-research-lab', 'marketing-brief-competitor-analyst'],
        'positive': '進行資料蒐集、來源查證、研究整理或研究報告產出。',
        'negative': '只需要研究方法、實驗假設或研究團隊治理設計。',
        'exclude': '若主要任務是設計實驗方法而非交付研究結果，交由 ai-research-lab。',
    },
    'analyzing-business-models': {
        'related': ['business-model-canvas-diagnosis', 'startup-venture-builder'],
        'positive': '比較或分析商業模式、價值主張、收入來源與商業假設。',
        'negative': '只需要修補 Business Model Canvas 的欄位結構或缺口。',
        'exclude': '若需要逐格診斷 canvas，交由 business-model-canvas-diagnosis。',
    },
    'business-model-canvas-diagnosis': {
        'related': ['analyzing-business-models', 'startup-venture-builder'],
        'positive': '逐格檢查、診斷或重構 Business Model Canvas。',
        'negative': '只需要比較多個商業模式或做一般策略分析。',
        'exclude': '沒有 canvas 或不需要逐格診斷時，不要啟用。',
    },
    'making-decisions': {
        'related': ['decision-making-superpowers'],
        'positive': '需要一般性的選項比較、權衡、決策框架或決策紀錄。',
        'negative': '需要長期決策教練、認知訓練或高階決策能力培養。',
        'exclude': '若使用者明確要求教練式決策訓練，交由 decision-making-superpowers。',
    },
    'decision-making-superpowers': {
        'related': ['making-decisions'],
        'positive': '需要教練式決策訓練、認知偏誤檢查或高階決策能力提升。',
        'negative': '只需要對單一問題做一般選項比較與決策表。',
        'exclude': '若任務只需要一次性決策分析，使用 making-decisions。',
    },
    'designing-pricing-systems': {
        'related': ['pricing-strategy-conversion-system'],
        'positive': '設計定價架構、方案包裝、折扣規則或價格模型。',
        'negative': '只需要把既有定價轉成銷售頁轉換文案或轉換流程。',
        'exclude': '若核心是銷售轉換而非價格系統，交由 pricing-strategy-conversion-system。',
    },
    'pricing-strategy-conversion-system': {
        'related': ['designing-pricing-systems'],
        'positive': '把定價策略轉成銷售流程、轉換文案或成交機制。',
        'negative': '需要從零設計價格階梯、成本模型或折扣治理。',
        'exclude': '若核心是價格結構而不是轉換文案，交由 designing-pricing-systems。',
    },
    'website-custom-optimizer': {
        'related': ['website-landing-page-builder'],
        'positive': '已有網站，需要診斷、SEO、內容、轉換或技術優化。',
        'negative': '從零建立一個新的 landing page 或網站。',
        'exclude': '沒有既有網站可供審查時，交由 website-landing-page-builder。',
    },
    'website-landing-page-builder': {
        'related': ['website-custom-optimizer'],
        'positive': '從零建立 landing page、網站架構、頁面內容或元件。',
        'negative': '已有網站並只需要找出問題或優化現有頁面。',
        'exclude': '若任務是診斷既有網站，不要啟用建立型流程。',
    },
    'notion-ai-workflow-design': {
        'related': ['notion-smart-doc-role-adapter'],
        'positive': '設計 Notion、n8n 或 AI 驅動的工作流程與自動化架構。',
        'negative': '只需要改寫單份文件的角色、語氣或格式。',
        'exclude': '所有 Notion write、n8n write 或外部更新都必須先產生差異預覽並取得批准。',
    },
    'notion-smart-doc-role-adapter': {
        'related': ['notion-ai-workflow-design'],
        'positive': '將既有文件轉換成指定角色、受眾、格式或溝通語氣。',
        'negative': '需要設計跨頁面、自動化或資料同步工作流。',
        'exclude': '只改寫內容，不自動建立、更新或刪除 Notion 資料。',
    },
}


def slug_words(text: str) -> str:
    return text.replace('-', ' ').replace('_', ' ')


def main():
    count = 0
    for path in sorted(SKILLS.glob('*/manifest.json')):
        m = json.loads(path.read_text(encoding='utf-8'))
        ident = m['id']
        name = m.get('name', slug_words(ident))
        description = m.get('description', name)
        group = GROUPS.get(ident)
        if group:
            positive = group['positive']
            negative = group['negative']
            exclude = group['exclude']
            related = group['related']
        else:
            positive = f'使用者明確要求：{description}'
            negative = f'任務只涉及與「{name}」無關的主題，不需要其專門流程。'
            exclude = f'若任務不涉及「{name}」的核心目的、輸入或輸出，不要啟用本技能。'
            related = m.get('related_skills') or []
        priority = 80 if m.get('risk_level') == 'high' else (60 if m.get('risk_level') == 'medium' else 40)
        m['activation'] = {
            'positive_examples': [positive],
            'negative_examples': [negative],
            'exclude_when': [exclude],
            'priority': priority,
            'delegates_to': [],
            'selection_notes': '先檢查任務目的、輸入資料與外部權限；相鄰技能重疊時以最小權限與最窄範圍優先。',
        }
        m['related_skills'] = sorted(set(related) - {ident})
        path.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        count += 1
    print(f'Added activation contract to {count} manifests; curated overlap groups={len(GROUPS)}')


if __name__ == '__main__':
    main()
