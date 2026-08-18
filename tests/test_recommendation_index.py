from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills.json"
RESULTS_PATH = ROOT / "docs" / "evaluations" / "github-skills-test-results.json"
INDEX_PATH = ROOT / "docs" / "recommendation-index.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_ranked_registry_matches_evaluation_snapshot() -> None:
    registry = load_json(REGISTRY_PATH)
    evaluation = load_json(RESULTS_PATH)
    items = registry["skills"]
    results = evaluation["results"]

    ranked = [item for item in items if "recommendation" in item]
    auxiliary = [item for item in items if "recommendation" not in item]
    assert len(items) == 118
    assert len(ranked) == len(results) == 108
    assert len(auxiliary) == 10
    assert [item["recommendation"]["rank"] for item in ranked] == list(range(1, 109))
    assert {item["id"] for item in ranked} == {result["id"] for result in results}

    result_by_id = {result["id"]: result for result in results}
    for item in ranked:
        recommendation = item["recommendation"]
        result = result_by_id[item["id"]]
        assert recommendation["score"] == result["recommendation_score"]
        assert recommendation["level"] == result["recommendation_level"]
        assert recommendation["status"] == "PASS"
        assert recommendation["check_count"] == recommendation["passed_checks"]
        assert recommendation["test_scope"] == result["test_scope"]


def test_recommendation_distribution_and_documentation() -> None:
    registry = load_json(REGISTRY_PATH)
    ranked = [item for item in registry["skills"] if "recommendation" in item]
    levels = Counter(item["recommendation"]["level"] for item in ranked)
    assert levels == Counter({"B｜條件推薦": 57, "A-｜條件優先推薦": 30, "A｜優先推薦": 21})
    assert all(item["recommendation"]["status"] == "PASS" for item in ranked)

    index = INDEX_PATH.read_text(encoding="utf-8")
    assert "## 完整排名" in index
    assert "| 108 |" in index
    assert "OpenAPI、MCP 與 workflow 輔助 entries" in index
    assert "## References" in index
