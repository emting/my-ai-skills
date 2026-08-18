from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BACKUP = ROOT / "docs" / "sources" / "Skills_Full_Configurations_Backup_20260818.md"
REGISTRY_PATH = ROOT / "skills.json"
CATALOG_PATH = ROOT / "docs" / "skill-archive-catalog.md"

HEADING_RE = re.compile(r"^(?:##|\\#\\#)\s+(\d+)\\?\.\s+(.+?)\s*$")
MARKER_RE = re.compile(r"^\\?---\s*$")
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
DESCRIPTION_RE = re.compile(r"^description:\s*(.+?)\s*$")
ALLOWED_TOOLS_RE = re.compile(r"^allowed-tools:\s*(.+?)\s*$")
TOP_CATEGORY_RE = re.compile(r"^\\?#\s+([一二三四五六七八九十]+、.+?)\s*$")

RELATED: dict[str, list[str]] = {
    "ai-research-lab": ["research-lab"],
    "notion-smart-doc-role-adapter": ["adapting-notion-docs"],
    "business-model-canvas-diagnosis": ["analyzing-business-models"],
    "pricing-strategy-conversion-system": ["designing-pricing-systems"],
    "decision-making-superpowers": ["making-decisions"],
}

HIGH_RISK_TERMS = re.compile(
    r"金融|現金流|損益|預算|廣告投放|合約|談判|危機|客訴|退費|家長|學生|客戶|個資|私域|房地產|房屋|部署|權限|憑證|API Key|Token|自動化|發送|發佈|刪除|交易|支付|敏感",
    re.I,
)
MEDIUM_RISK_TERMS = re.compile(
    r"研究|競品|市場|品牌|定價|商業模式|決策|Notion|Google|Threads|Instagram|Facebook|YouTube|新聞|資料|內容",
    re.I,
)
SENSITIVE_TERMS = re.compile(
    r"個資|敏感|私域|家長|學生|客戶|客服|Email|email|電話|地址|姓名|金流|現金流|損益|收入|合約|房地產|房屋|personal|private",
    re.I,
)
NETWORK_TERMS = re.compile(
    r"即時|web search|搜尋|競品|市場研究|趨勢|API|MCP|Google|YouTube|Instagram|Threads|Facebook|LinkedIn|Cloudflare|Gemini|MiMo|OpenClaw|Notion|Drive|Docs|Sheets|新聞|來源|research",
    re.I,
)
BROWSER_TERMS = re.compile(r"browser|瀏覽器|登入|爬取|crawl|scrap", re.I)
WRITE_TERMS = re.compile(r"匯出|同步|寫入|建立|更新|產出|記錄|存檔|排程|發佈|發送|匯入|整理", re.I)
API_KEY_TERMS = re.compile(r"API Key|金鑰|Token|憑證", re.I)
GIT_TERMS = re.compile(r"GitHub|git|repository|repo", re.I)
NOTION_TERMS = re.compile(r"Notion", re.I)
NOTION_WRITE_TERMS = re.compile(r"Notion.{0,80}(更新|建立|同步|寫入)|(?:更新|建立|同步|寫入).{0,80}Notion", re.I)
MCP_WRITE_TERMS = re.compile(r"MCP.{0,80}(寫入|建立|更新)|(?:寫入|建立|更新).{0,80}MCP", re.I)

UNESCAPE_RE = re.compile(r"\\([#*_+&~=().<>!?|{}\[\]-])")


def normalize_markdown(value: str) -> str:
    value = value.replace("\\#", "#")
    value = value.replace("\\*", "*")
    value = value.replace("\\_", "_")
    value = value.replace("\\-", "-")
    value = value.replace("\\+", "+")
    value = value.replace("\\&", "&")
    value = value.replace("\\~", "~")
    value = value.replace("\\=", "=")
    value = value.replace("\\.", ".")
    value = value.replace("\\(", "(").replace("\\)", ")")
    value = UNESCAPE_RE.sub(r"\1", value)
    value = value.replace("🟢", "[低風險]")
    value = value.replace("🟡", "[需補充]")
    value = value.replace("🔵", "[需人工判斷]")
    value = value.replace("🔴", "[高風險]")
    return value


def display_name(raw_title: str, skill_id: str) -> str:
    match = re.search(r"`([^`]+)`", raw_title)
    if match:
        candidate = match.group(1).strip()
        if candidate == skill_id:
            return skill_id.replace("-", " ").title()
        return normalize_markdown(candidate)
    return skill_id.replace("-", " ").title()


def parse_backup(path: Path) -> list[dict[str, Any]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    headings: list[tuple[int, int, str, str]] = []
    category = "未分類"
    for index, line in enumerate(lines):
        category_match = TOP_CATEGORY_RE.match(line)
        if category_match:
            category = normalize_markdown(category_match.group(1))
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, int(match.group(1)), match.group(2), category))

    skills: list[dict[str, Any]] = []
    for position, (start, number, title, section_category) in enumerate(headings):
        end = headings[position + 1][0] if position + 1 < len(headings) else len(lines)
        section = lines[start:end]
        marker_indices = [idx for idx, line in enumerate(section) if MARKER_RE.match(line)]
        header_start = marker_indices[0] if marker_indices else 1
        header_end = marker_indices[1] if len(marker_indices) > 1 else header_start
        header = section[header_start:header_end]
        body_lines = section[header_end + 1 :]
        if body_lines and body_lines[0].strip().lower() in {"```", "```markdown"}:
            body_lines = body_lines[1:]
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()
        if body_lines and body_lines[-1].strip() == "```":
            body_lines.pop()
        name_match = next((NAME_RE.match(line) for line in header if NAME_RE.match(line)), None)
        description_match = next((DESCRIPTION_RE.match(line) for line in header if DESCRIPTION_RE.match(line)), None)
        tools_match = next((ALLOWED_TOOLS_RE.match(line) for line in header if ALLOWED_TOOLS_RE.match(line)), None)
        skill_id = normalize_markdown(name_match.group(1).strip()) if name_match else ""
        description = normalize_markdown(description_match.group(1).strip()) if description_match else f"{skill_id} instruction skill"
        body = normalize_markdown("\n".join(body_lines)).strip()
        skills.append(
            {
                "number": number,
                "id": skill_id,
                "name": display_name(title, skill_id),
                "description": description,
                "category": section_category,
                "body": body,
                "allowed_tools": normalize_markdown(tools_match.group(1).strip()) if tools_match else "",
                "source_start_line": start + 1,
                "source_end_line": end,
            }
        )
    return skills


def classify(skill: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(
        str(skill.get(key, "")) for key in ("id", "name", "description", "body", "allowed_tools")
    )
    high = bool(HIGH_RISK_TERMS.search(text))
    medium = bool(MEDIUM_RISK_TERMS.search(text))
    network = bool(NETWORK_TERMS.search(text))
    browser = bool(BROWSER_TERMS.search(text))
    filesystem_read = bool(re.search(r"檔案|文件|資料|素材|報告|email|csv|excel|輸入|source|brief", text, re.I))
    filesystem_write = bool(WRITE_TERMS.search(text))
    api_key = bool(API_KEY_TERMS.search(text))
    git = bool(GIT_TERMS.search(text))
    notion_read = bool(NOTION_TERMS.search(text))
    notion_write = notion_read and bool(NOTION_WRITE_TERMS.search(text))
    mcp_write = bool(MCP_WRITE_TERMS.search(text)) and "mcp" in text.lower()
    third_party = network or browser or notion_read
    risk = "high" if high else "medium" if medium else "low"
    requires_confirmation = risk == "high" or browser or notion_write or mcp_write or bool(re.search(r"發佈|發送|排程|部署|交易|預算|合約", text, re.I))
    tags = ["imported", "instruction-only"]
    tag_rules = {
        "research": r"研究|research|競品|市場|來源",
        "business": r"商業|創業|定價|營收|損益|現金流|startup",
        "content": r"內容|文案|社群|Threads|Instagram|Podcast|電子報|newsletter|YouTube",
        "decision": r"決策|談判|問題|question|decision",
        "governance": r"治理|Agent|自動化|SOP|權限|安全|OpenClaw|Hermes",
        "education": r"課程|學習|教學|家長|學生|quiz|study",
        "design": r"設計|視覺|logo|logotype|portfolio|presentation",
        "local-business": r"餐廳|商家|商品|房地產|real-estate|merchant",
    }
    for tag, pattern in tag_rules.items():
        if re.search(pattern, text, re.I):
            tags.append(tag)
    permissions = {
        "filesystem_read": filesystem_read,
        "filesystem_write": filesystem_write,
        "network": network,
        "api_key_required": api_key,
        "browser_automation": browser,
        "third_party_processing": third_party,
        "shell": bool(re.search(r"Warp|OpenClaw|terminal|CLI|shell", text, re.I)),
        "git": git,
        "google_ads_read": bool(re.search(r"Google Ads", text, re.I)),
        "google_ads_write": False,
        "notion_read": notion_read,
        "notion_write": notion_write,
        "n8n_write": bool(re.search(r"n8n", text, re.I) and WRITE_TERMS.search(text)),
        "mcp_write_tools": mcp_write,
    }
    safety_rules = [
        "先確認任務目標、輸入來源、使用授權、範圍與輸出格式；缺少關鍵資訊時先列出假設並提出最少必要問題。",
        "不得捏造事實、數據、案例、評價、客戶反饋、媒體報導、認證或研究來源；無法驗證的內容必須標示為假設或待驗證。",
        "只使用使用者提供或明確授權的內容；不得繞過登入、CAPTCHA、付費牆、存取控制或第三方服務限制。",
        "外部服務一律採唯讀或草稿模式；發送、發佈、建立、更新、刪除、部署、交易、預算變更與權限變更前必須取得明確人工批准。",
    ]
    if SENSITIVE_TERMS.search(text):
        safety_rules.append("對個人、客戶、學生、財務、合約或私有資料採資料最小化；輸出前遮罩識別資訊，避免複製原始敏感資料。")
    if network:
        safety_rules.append("涉及外部資料時記錄來源、擷取時間與查證限制；將可觀察事實、推論與建議分開呈現。")
    if risk == "high":
        safety_rules.append("此技能只提供分析、草稿與驗證建議，不代表法律、財務、醫療、投資或營運承諾；高風險決策須由合適的人員覆核。")
    disallowed = [
        "不得用於未授權存取、憑證收集、冒充他人、垃圾訊息、操縱或規避平台政策。",
        "不得把未經授權的第三方內容、個資或機密資料重新發布到公開服務。",
    ]
    if risk == "high":
        disallowed.append("不得在沒有明確批准、完整上下文與可回溯驗證的情況下執行高影響外部操作。")
    return {
        "text": text,
        "risk": risk,
        "permissions": permissions,
        "safety_rules": safety_rules,
        "disallowed_uses": disallowed,
        "requires_confirmation": requires_confirmation,
        "handles_sensitive_data": bool(SENSITIVE_TERMS.search(text)),
        "tags": list(dict.fromkeys(tags)),
    }


def build_body(skill: dict[str, Any], classification: dict[str, Any], source_ref: str) -> str:
    body = skill["body"] or "本技能以 instruction-only 模式提供可重複的任務方法。"
    if skill["allowed_tools"]:
        body += f"\n\n## 工具提示\n\n來源備份標示的可用工具：`{skill['allowed_tools']}`。此提示不等於已授權連接或執行；仍須依專案整合邊界與人工核准規則操作。"
    related = RELATED.get(skill["id"], [])
    related_text = "、".join(f"`{item}`" for item in related) if related else "無"
    safety_lines = "\n".join(f"- {rule}" for rule in classification["safety_rules"])
    disallowed_lines = "\n".join(f"- {rule}" for rule in classification["disallowed_uses"])
    confirmation = "需要人工確認" if classification["requires_confirmation"] else "預設可先產出分析或草稿，但仍不得代替使用者做外部高影響決策"
    return f"""---
name: {skill['id']}
description: {skill['description']}
---

# {skill['name']}

{body}

## 標準執行契約

### 觸發與輸入

使用者明確要求此主題，或輸入與本技能描述高度相符時才啟用。先確認目標、受眾、上下文、資料來源、限制條件與希望的輸出格式；未提供的資訊不得自行補成事實。

### 執行順序

1. 盤點輸入與授權，標記缺口、敏感資料與可能的外部依賴。
2. 依本技能的核心流程逐步處理，將事實、推論、假設與建議分開。
3. 產出可直接審閱的結果，並列出引用、未驗證事項、風險與需要人工決策的節點。
4. 執行輸出前檢查，確認沒有虛構證據、洩漏敏感資料或超出使用者範圍的動作。

### 輸出契約

至少提供：

- **結果或草稿**：依使用者要求產出分析、策略、腳本、內容、清單或計畫。
- **假設與限制**：明確標示資料不足、未驗證推論與適用範圍。
- **驗證紀錄**：列出使用的來源、檢查方式或尚待確認的項目。
- **風險與下一步**：指出人工核准點、低成本驗證方式與可恢復的後續行動。

### 安全與人工核准

目前風險等級：**{classification['risk']}**。{confirmation}。

{safety_lines}

### 禁止用途

{disallowed_lines}

### 停止條件

若使用授權、資料來源、範圍、關鍵數字、身份或外部操作權限無法確認，先停止執行高影響部分並回報缺口。若發現來源互相矛盾、任務目標漂移、敏感資料暴露或輸出無法驗證，保留已完成的安全分析，暫停後續動作並要求人工判斷。

## 關聯技能

本技能與 {related_text} 有功能相近或可互補的既有技能；選擇時以使用者明確需求、資料來源與權限邊界為準，不要平行重複執行相同的高影響操作。

## 來源追蹤

此技能由 `{source_ref}` 的第 {skill['number']} 項正規化而來（原始行號 {skill['source_start_line']}–{skill['source_end_line']}）。來源內容已補上本 repository 的輸入、輸出、權限、安全與停止契約。
"""


def io_fields(skill: dict[str, Any], classification: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    inputs: dict[str, dict[str, Any]] = {
        "request": {"type": "text", "required": True, "description": "使用者希望完成的任務、問題或產出目標。"},
        "context": {"type": "text", "required": False, "description": "背景、受眾、現況、限制與已知決策脈絡。"},
        "source_materials": {"type": "text_or_files", "required": False, "description": "使用者提供或明確授權的文件、資料、逐字稿、表格或連結。"},
        "constraints": {"type": "list", "required": False, "description": "時程、格式、語氣、預算、權限與不得變更事項。"},
    }
    if classification["network"] if "network" in classification else classification["permissions"]["network"]:
        inputs["source_materials"]["description"] = "使用者提供或明確授權的資料與外部來源；需要即時資訊時應記錄來源與擷取時間。"
    outputs: dict[str, dict[str, Any]] = {
        "result": {"type": "markdown", "required": True, "description": "依技能目的產出的分析、策略、腳本、內容、清單或計畫。"},
        "assumptions_and_risks": {"type": "markdown", "required": True, "description": "假設、未驗證事項、風險、限制與人工核准點。"},
        "verification": {"type": "markdown", "required": True, "description": "來源、檢查方式、驗收條件與尚待確認事項。"},
    }
    return inputs, outputs


def build_manifest(skill: dict[str, Any], classification: dict[str, Any], backup_name: str) -> dict[str, Any]:
    inputs, outputs = io_fields(skill, classification)
    permissions = classification["permissions"]
    return {
        "id": skill["id"],
        "name": skill["name"],
        "version": "1.0.0",
        "description": skill["description"],
        "entrypoint": "SKILL.md",
        "runtime": "instruction_only",
        "requirements": [],
        "inputs": inputs,
        "outputs": outputs,
        "permissions": permissions,
        "safety": {
            "handles_sensitive_data": classification["handles_sensitive_data"],
            "requires_user_confirmation": classification["requires_confirmation"],
            "destructive": False,
            "rules": classification["safety_rules"],
            "disallowed_uses": classification["disallowed_uses"],
            "forbidden_without_explicit_approval": [
                "對外發送或發佈內容",
                "建立、更新或刪除第三方服務資料",
                "部署、改變權限、改變預算或執行不可逆操作",
            ],
            "always_forbidden": [
                "繞過身份驗證、CAPTCHA、付費牆或存取控制",
                "捏造來源、證據、數據、認證或使用者同意",
            ],
        },
        "risk_level": classification["risk"],
        "activation_policy": "explicit_request" if classification["risk"] == "high" else "intent_match_with_scope_check",
        "default_config": {
            "mode": "draft_or_read_only",
            "language": "zh-TW",
            "source_archive": backup_name,
            "source_item": skill["number"],
        },
        "platforms": ["markdown", "manus", "codex", "copilot"],
        "source": {
            "type": "user_provided_backup",
            "file": backup_name,
            "section_number": skill["number"],
            "start_line": skill["source_start_line"],
            "end_line": skill["source_end_line"],
            "status": "normalized_and_hardened",
        },
        "related_skills": RELATED.get(skill["id"], []),
    }


def manifest_to_registry(skill: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    def list_fields(fields: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
        return [
            {"name": name, **{key: value for key, value in field.items() if key != "extensions"}}
            for name, field in fields.items()
        ]

    folder = f"custom_skills/{skill['id']}/"
    entry = {
        "id": skill["id"],
        "name": skill["name"],
        "visibility": "public",
        "type": "instruction",
        "description": skill["description"],
        "location": folder,
        "entrypoint": f"{folder}SKILL.md",
        "instruction_file": f"{folder}SKILL.md",
        "manifest": f"{folder}manifest.json",
        "runtime": "instruction_only",
        "inputs": list_fields(manifest["inputs"]),
        "outputs": list_fields(manifest["outputs"]),
        "permissions": manifest["permissions"],
        "risk_level": manifest["risk_level"],
        "activation_policy": manifest["activation_policy"],
        "tags": classification_tags(manifest),
        "source": manifest["source"],
    }
    if manifest.get("related_skills"):
        entry["related_skills"] = manifest["related_skills"]
    return entry


def classification_tags(manifest: dict[str, Any]) -> list[str]:
    tags = ["imported", "instruction-only"]
    permissions = manifest.get("permissions", {})
    if permissions.get("network"):
        tags.append("network-aware")
    if manifest.get("safety", {}).get("handles_sensitive_data"):
        tags.append("privacy-sensitive")
    if manifest.get("risk_level") == "high":
        tags.append("human-gated")
    return tags


def update_registry(skills: list[dict[str, Any]], manifests: dict[str, dict[str, Any]]) -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    registry["version"] = "1.2.0"
    registry["description"] = "Open-source AI skills library for agents, coding assistants, and automation tools, including a normalized 66-skill archive import."
    existing = registry.get("skills", [])
    existing_ids = {item.get("id") for item in existing if isinstance(item, dict)}
    for skill in skills:
        if skill["id"] in existing_ids:
            continue
        existing.append(manifest_to_registry(skill, manifests[skill["id"]]))
    registry["skills"] = existing
    REGISTRY_PATH.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_catalog(skills: list[dict[str, Any]], manifests: dict[str, dict[str, Any]]) -> None:
    rows = []
    for skill in skills:
        manifest = manifests[skill["id"]]
        permissions = manifest["permissions"]
        related = ", ".join(f"`{item}`" for item in manifest.get("related_skills", [])) or "—"
        description = skill["description"].replace("|", "\\|")
        rows.append(
            f"| {skill['number']} | `{skill['id']}` | {skill['category']} | {description} | {manifest['risk_level']} | {'是' if permissions['network'] else '否'} | {related} |"
        )
    content = """# 附件 Skills 整併目錄

> 本目錄由 `scripts/import_skill_archive.py` 產生。它將 `Skills_Full_Configurations_Backup_20260818.md` 的 66 項技能逐一正規化為 `custom_skills/<id>/SKILL.md` 與 `manifest.json`，並補上輸入、輸出、權限、安全、人工核准與停止契約。

## 整併原則

所有匯入技能均採 `instruction_only` runtime，預設以分析、草稿或唯讀方式運作。附件中的原始內容保留為技能核心流程，但補上不可捏造、資料最小化、來源追蹤、外部寫入人工核准與停止條件。涉及相近能力的技能不覆蓋既有實作，而是以獨立 ID 納管並在 manifest 中標示關聯，避免破壞既有相容性。

| # | ID | 類別 | 描述 | 風險 | 網路能力 | 關聯既有技能 |
|---:|---|---|---|---|:---:|---|
""" + "\n".join(rows) + "\n"
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import and harden the user skill archive.")
    parser.add_argument("--backup", type=Path, default=DEFAULT_BACKUP)
    args = parser.parse_args()
    backup = args.backup.resolve()
    if not backup.exists():
        raise SystemExit(f"backup does not exist: {backup}")
    if backup.suffix.lower() == ".zip":
        try:
            from .import_skill_zip import import_zip_archive
        except ImportError:
            from import_skill_zip import import_zip_archive
        result = import_zip_archive(backup)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    skills = parse_backup(backup)
    if len(skills) != 66 or any(not skill["id"] for skill in skills):
        raise SystemExit(f"expected 66 named skills, found {len(skills)}")

    try:
        source_ref = str(backup.relative_to(ROOT))
    except ValueError:
        source_ref = backup.name

    manifests: dict[str, dict[str, Any]] = {}
    for skill in skills:
        classification = classify(skill)
        # Keep the network decision available to io_fields without duplicating heuristics.
        classification["network"] = classification["permissions"]["network"]
        skill_dir = ROOT / "custom_skills" / skill["id"]
        skill_dir.mkdir(parents=True, exist_ok=True)
        manifest = build_manifest(skill, classification, source_ref)
        (skill_dir / "SKILL.md").write_text(build_body(skill, classification, source_ref), encoding="utf-8")
        (skill_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        manifests[skill["id"]] = manifest

    update_registry(skills, manifests)
    write_catalog(skills, manifests)
    print(f"imported={len(skills)}")
    print(f"manifest_root={ROOT / 'custom_skills'}")
    print(f"registry={REGISTRY_PATH}")
    print(f"catalog={CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
