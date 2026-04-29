from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"
DOCS = REPO_ROOT / "docs"

sys.path.insert(0, str(SCRIPTS))

import verify_status_page as v  # noqa: E402


def _write(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "status.html"
    p.write_text(
        "<!doctype html><html><head><title>t</title></head>"
        f"<body>{body}</body></html>",
        encoding="utf-8",
    )
    return p


def _full_valid_body() -> str:
    return f"""
    <h1>{v.REPO_NAME} — Capacity-Locality Certification Status</h1>
    <p>Status: <strong>{v.ARTIFACT_TYPE}</strong></p>
    <p>This repository does not prove SAT lower bounds, CSP lower bounds,
       circuit lower bounds, communication-complexity lower bounds,
       P versus NP, or theorem-complete capacity-locality closure.
       These are not claimed.</p>
    <h2>Claim flags</h2><h2>Artifact metadata</h2>
    <h2>Verifier &amp; CI surfaces</h2>
    <h2>Closed surfaces</h2><ul class="surf closed"><li><span class="tag closed">CLOSED</span> x</li></ul>
    <h2>Open surfaces</h2><ul class="surf open"><li><span class="tag open">OPEN</span> y</li></ul>
    <h2>Conditional surfaces</h2><ul class="surf cond"><li><span class="tag cond">CONDITIONAL</span> z</li></ul>
    <h2>Certification map</h2>
    <h2>Status interpretation</h2>
    """


def test_real_status_page_passes():
    page = DOCS / "status.html"
    assert page.exists(), f"missing {page}"
    report = v.run(page)
    assert report.ok, "shipped status page failed verifier:\n" + "\n".join(report.failures)


def test_synthetic_minimal_valid_passes(tmp_path):
    p = _write(tmp_path, _full_valid_body())
    report = v.run(p)
    assert report.ok, report.failures


def test_missing_file_fails(tmp_path):
    report = v.run(tmp_path / "nope.html")
    assert not report.ok
    assert any("not found" in f for f in report.failures)


def test_missing_artifact_type_fails(tmp_path):
    body = _full_valid_body().replace(v.ARTIFACT_TYPE, "something else")
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok
    assert any("artifact type" in f for f in report.failures)


def test_missing_non_claim_fails(tmp_path):
    body = _full_valid_body().replace("does not prove", "DOES")
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok
    assert any("non-claim phrase missing" in f for f in report.failures)


def test_forbidden_claim_outside_negation_fails(tmp_path):
    body = _full_valid_body() + "<p>This repository proves SAT lower bounds.</p>"
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok
    assert any("forbidden positive claim" in f for f in report.failures)


def test_forbidden_claim_inside_negation_passes(tmp_path):
    body = _full_valid_body() + (
        "<p>This repository does not prove SAT lower bounds and makes no "
        "lower-bound proof.</p>"
    )
    p = _write(tmp_path, body)
    report = v.run(p)
    assert report.ok, report.failures


def test_missing_section_fails(tmp_path):
    body = _full_valid_body().replace("Conditional surfaces", "Other things")
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok
    assert any("conditional surfaces" in f.lower() for f in report.failures)


def test_missing_css_separation_fails(tmp_path):
    body = _full_valid_body().replace('class="surf cond"', 'class="surf"')
    body = body.replace('class="tag cond"', 'class="tag"')
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok
    assert any("CSS marker missing" in f for f in report.failures)


def test_strip_html_removes_scripts_and_styles():
    raw = "<html><head><style>.x{color:red}</style></head><body><script>bad()</script><p>hello</p></body></html>"
    assert "bad()" not in v.strip_html(raw)
    assert "color:red" not in v.strip_html(raw)
    assert "hello" in v.strip_html(raw)


def test_sentences_split():
    s = v.sentences("A. B! C? D")
    assert len(s) >= 3


@pytest.mark.parametrize("phrase", v.FORBIDDEN_POSITIVE_CLAIMS)
def test_every_forbidden_phrase_is_blocked(tmp_path, phrase):
    body = _full_valid_body() + f"<p>This repository {phrase} today.</p>"
    p = _write(tmp_path, body)
    report = v.run(p)
    assert not report.ok, f"phrase should have been blocked: {phrase}"


def test_main_returns_zero_on_real_page(capsys):
    rc = v.main([str(DOCS / "status.html")])
    out = capsys.readouterr().out
    assert "RESULT: PASS" in out
    assert rc == 0


def test_main_returns_one_on_missing(tmp_path, capsys):
    rc = v.main([str(tmp_path / "missing.html")])
    out = capsys.readouterr().out
    assert "RESULT: FAIL" in out
    assert rc == 1
