#!/usr/bin/env python3
"""Generate a deterministic recommendation index and ranked registry from test results."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output-registry", type=Path, required=True)
    parser.add_argument("--output-markdown", type=Path, required=True)
    args = parser.parse_args()

    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    evaluation = json.loads(args.results.read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = evaluation["results"]
    by_id = {result["id"]: result for result in results}
    registry_items = registry.get("skills", [])
    registry_ids = {item.get("id") for item in registry_items}
    missing = sorted(set(by_id) - registry_ids)
    if missing:
        raise SystemExit(f"results contain unregistered skills: {', '.join(missing)}")

    ranked_items: list[dict[str, Any]] = []
    auxiliary_items: list[dict[str, Any]] = []
    for item in registry_items:
        if item.get("id") not in by_id:
            auxiliary_items.append(dict(item))
            continue
        result = by_id[item["id"]]
        enriched = dict(item)
        enriched["recommendation"] = {
            "rank": result["rank"],
            "score": result["recommendation_score"],
            "level": result["recommendation_level"],
            "status": result["status"],
            "test_scope": result["test_scope"],
            "check_count": result["check_count"],
            "passed_checks": result["passed_checks"],
            "connector_count": result["connector_count"],
            "external_write_allowed": result["external_write_allowed"],
            "reason": result["recommendation_reason"],
        }
        ranked_items.append(enriched)
    ranked_items.sort(key=lambda item: (item["recommendation"]["rank"], item["id"]))
    # Keep OpenAPI/MCP/workflow compatibility references after ranked skills.
    ranked_items.extend(auxiliary_items)

    ranked_registry = dict(registry)
    ranked_registry["version"] = "1.4.0"
    ranked_registry["description"] = (
        "Open-source AI skills library with normalized contracts, safety metadata, "
        "reproducible evaluation results, and recommendation-ranked registry entries."
    )
    ranked_registry["recommendation_index"] = {
        "method": "contract-risk-safety-v1",
        "source_commit": "fead9bd",
        "source_results": "docs/evaluations/github-skills-test-results.json",
        "documentation": "docs/recommendation-index.md",
        "scope": "108 installed skills; instruction-only contract dry-runs plus one offline executable smoke test; auxiliary registry references are unranked",
        "external_actions_executed": False,
        "levels": {
            "A｜優先推薦": "PASS、low risk、無 connector、external_write.allowed=false",
            "A-｜條件優先推薦": "PASS、medium risk 且無外部寫入；仍需人工覆核",
            "B｜條件推薦": "PASS 但具有 high risk、connector 或外部寫入邊界；必須人工批准",
            "C｜暫不推薦": "測試失敗或無法以安全方式驗證",
        },
    }
    ranked_registry["skills"] = ranked_items
    args.output_registry.write_text(json.dumps(ranked_registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    levels = Counter(result["recommendation_level"] for result in results)
    risks = Counter(result["risk_level"] for result in results)
    lines = [
        "# Skills 推薦索引與排序",
        "",
        "> 本索引依 GitHub `main` 的 `fead9bd` commit 產生，資料來源為 `docs/evaluations/github-skills-test-results.json`。它是技能選擇的治理與安全輔助，不是專業品質、成功率或投資報酬率保證。",
        "",
        "## 使用方式",
        "",
        "優先依排名與分級選擇候選 skill，再閱讀該 skill 的 `SKILL.md` 與 `manifest.json`。如果任務涉及外部服務、帳戶、個資、部署、付費、發送、發佈、刪除或其他高影響行為，必須以 manifest 的人工核准點、停止條件與 rollback 規則為準，不得只依賴排名直接執行。",
        "",
        "## 排名方法",
        "",
        "| 分級 | 數量 | 判定 |",
        "|---|---:|---|",
        f"| A｜優先推薦 | {levels.get('A｜優先推薦', 0)} | 測試通過、low risk、無 connector、無外部寫入。 |",
        f"| A-｜條件優先推薦 | {levels.get('A-｜條件優先推薦', 0)} | 測試通過、通常無外部寫入，但為 medium risk；需人工覆核。 |",
        f"| B｜條件推薦 | {levels.get('B｜條件推薦', 0)} | 測試通過但有 high risk、connector 或外部寫入邊界。 |",
        f"| C｜暫不推薦 | {levels.get('C｜暫不推薦', 0)} | 測試失敗或無法安全驗證；本次為 {levels.get('C｜暫不推薦', 0)}。 |",
        "",
        "| 維度 | 統計 |",
        "|---|---:|",
        f"| 技能總數 | {len(results)} |",
        f"| 測試通過 | {evaluation['pass_count']}/{evaluation['package_count']} |",
        f"| 風險分布 | low {risks.get('low', 0)}；medium {risks.get('medium', 0)}；high {risks.get('high', 0)} |",
        "| 外部操作 | 0 次；所有 instruction-only 技能只做唯讀 dry-run |",
        "",
        "## 完整排名",
        "",
        "| 排名 | Skill ID | 名稱 | Runtime | Risk | 分數 | 分級 | 測試範圍 | Connector | 外部寫入 | 狀態 |",
        "|---:|---|---|---|---|---:|---|---|---:|---|---|",
    ]
    for result in results:
        name = str(result["name"]).replace("|", "\\|").replace("\n", " ")
        description = str(result.get("description", "")).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {result['rank']} | `{result['id']}` | {name} | `{result['runtime']}` | {result['risk_level']} | {result['recommendation_score']:.2f} | {result['recommendation_level']} | {result['test_scope']} | {result['connector_count']} | {result['external_write_allowed']} | {result['status']} |"
        )
        # Keep description available in a collapsible-style adjacent paragraph without HTML.
        lines.append(f"  描述：{description}")
    lines.extend([
        "",
        "## 測試解讀限制",
        "",
        "107 個 `instruction_only` skills 的通過結果代表封裝、manifest、標準段落、activation、來源與四類 eval 案例通過；它們沒有被擅自執行外部服務操作。唯一的 Python skill `data_analysis` 使用隔離 CSV fixture 完成離線 smoke test。真實 connector、部署、發送、付費與第三方寫入仍需另行取得人工批准與 integration test。",
        "",
        "## 相關檔案",
        "",
        "- [`skills.json`](../skills.json)：108 個完整 skills 依推薦排名排序；OpenAPI、MCP 與 workflow 輔助 entries 保留於排序區段之後，且不虛構測試分數。",
        "- [`docs/evaluations/github-skills-test-results.json`](evaluations/github-skills-test-results.json)：逐一測試的機器可讀結果。",
        "- [`docs/evaluations/github-skills-test-results.csv`](evaluations/github-skills-test-results.csv)：適合試算表與分析工具的平面結果。",
        "- [`docs/manifest-contract.md`](manifest-contract.md)：manifest 欄位與權限資料流契約。",
        "",
        "## References",
        "",
        "[1]: https://github.com/emting/my-ai-skills GitHub repository：emting/my-ai-skills",
        "[2]: https://github.com/emting/my-ai-skills/blob/main/evals/skills.json 技能契約 eval 案例",
        "[3]: https://github.com/emting/my-ai-skills/blob/main/scripts/smoke_test_skills.py 安全 dry-run 工具",
    ])
    args.output_markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"ranked_skills={len(results)}")
    print(f"output_registry={args.output_registry}")
    print(f"output_markdown={args.output_markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
