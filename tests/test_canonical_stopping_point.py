from pathlib import Path

def test_stopping_point_doc_exists():
    assert Path("docs/status/CANONICAL_STOPPING_POINT.md").exists()

def test_stopping_point_is_conditional():
    s = Path("docs/status/CANONICAL_STOPPING_POINT.md").read_text(encoding="utf-8")
    assert "Status: Conditional" in s

def test_no_false_promotion_gate_present():
    s = Path("docs/status/CANONICAL_STOPPING_POINT.md").read_text(encoding="utf-8")
    assert "Do not promote beyond Conditional" in s
