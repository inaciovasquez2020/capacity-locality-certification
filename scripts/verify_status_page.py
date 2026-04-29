#!/usr/bin/env python3
from __future__ import annotations

import html as _html
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

REPO_NAME = "capacity-locality-certification"
ARTIFACT_TYPE = "capacity-locality certification artifact"

REQUIRED_NON_CLAIMS: tuple[str, ...] = (
    "does not prove sat lower bounds",
    "does not prove",
    "p versus np",
    "csp lower bounds",
    "circuit lower bounds",
    "communication-complexity lower bounds",
    "theorem-complete capacity-locality closure",
    "not claimed",
)

FORBIDDEN_POSITIVE_CLAIMS: tuple[str, ...] = (
    "solves p vs np",
    "solves p versus np",
    "proves p vs np",
    "proves p versus np",
    "proves sat lower bounds",
    "proves csp lower bounds",
    "proves the capacity-locality theorem",
    "proves capacity-locality theorem",
    "lower-bound proof",
    "theorem-complete proof",
    "millennium solution",
    "resolves p vs np",
    "resolves p versus np",
)

NEGATION_MARKERS: tuple[str, ...] = (
    "does not prove",
    "does not claim",
    "do not prove",
    "do not claim",
    "not claimed",
    "not proved",
    "no ",
    "without ",
    "never ",
    "rather than",
    "instead of",
)

NEGATION_WINDOW = 80

REQUIRED_SECTIONS: tuple[str, ...] = (
    "claim flags",
    "artifact metadata",
    "verifier",
    "closed surfaces",
    "open surfaces",
    "conditional surfaces",
    "certification map",
    "status interpretation",
)

REQUIRED_CSS_MARKERS: tuple[str, ...] = (
    "surf closed",
    "surf open",
    "surf cond",
    "tag closed",
    "tag open",
    "tag cond",
)


@dataclass
class Report:
    ok: bool = True
    failures: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.ok = False
        self.failures.append(msg)

    def note(self, msg: str) -> None:
        self.notes.append(msg)


_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"\s+")
_SENT_RE = re.compile(r"[^.!?\n]+[.!?\n]")


def strip_html(raw: str) -> str:
    no_script = re.sub(r"<script\b[^>]*>.*?</script>", " ", raw, flags=re.IGNORECASE | re.DOTALL)
    no_style = re.sub(r"<style\b[^>]*>.*?</style>", " ", no_script, flags=re.IGNORECASE | re.DOTALL)
    text = _TAG_RE.sub(" ", no_style)
    text = _html.unescape(text)
    text = _WS_RE.sub(" ", text).strip()
    return text


def sentences(text: str) -> list[str]:
    found = _SENT_RE.findall(text)
    if not found:
        return [text]
    return [s.strip() for s in found if s.strip()]


def check_existence(path: Path, report: Report) -> str | None:
    if not path.exists():
        report.fail(f"status page not found at {path}")
        return None
    raw = path.read_text(encoding="utf-8")
    if len(raw.strip()) < 200 or "<html" not in raw.lower():
        report.fail(f"status page at {path} does not look like HTML")
        return None
    report.note(f"status page found ({len(raw)} bytes)")
    return raw


def check_artifact_type(text_lower: str, report: Report) -> None:
    if REPO_NAME not in text_lower:
        report.fail(f"repository name '{REPO_NAME}' not visible on the page")
    if ARTIFACT_TYPE not in text_lower:
        report.fail(f"declared artifact type '{ARTIFACT_TYPE}' not visible")


def check_required_non_claims(text_lower: str, report: Report) -> None:
    for needle in REQUIRED_NON_CLAIMS:
        if needle not in text_lower:
            report.fail(f"required non-claim phrase missing: {needle!r}")


def check_forbidden_claims(text: str, report: Report) -> None:
    lower = text.lower()
    for bad in FORBIDDEN_POSITIVE_CLAIMS:
        start = 0
        while True:
            idx = lower.find(bad, start)
            if idx < 0:
                break
            window = lower[max(0, idx - NEGATION_WINDOW): idx + len(bad) + NEGATION_WINDOW]
            if not any(m in window for m in NEGATION_MARKERS):
                excerpt = text[max(0, idx - 40): idx + len(bad) + 40].strip()
                report.fail(f"forbidden positive claim outside negation: {bad!r} near: {excerpt!r}")
            start = idx + len(bad)


def check_sections(text_lower: str, report: Report) -> None:
    for sec in REQUIRED_SECTIONS:
        if sec not in text_lower:
            report.fail(f"required section missing: {sec!r}")


def check_css_separation(raw_html: str, report: Report) -> None:
    raw_lower = raw_html.lower()
    for marker in REQUIRED_CSS_MARKERS:
        if marker not in raw_lower:
            report.fail(f"required CSS marker missing (visual separation): {marker!r}")


def run(path: Path) -> Report:
    report = Report()
    raw = check_existence(path, report)
    if raw is None:
        return report
    visible = strip_html(raw)
    text_lower = visible.lower()
    check_artifact_type(text_lower, report)
    check_required_non_claims(text_lower, report)
    check_forbidden_claims(visible, report)
    check_sections(text_lower, report)
    check_css_separation(raw, report)
    return report


def format_report(report: Report) -> str:
    lines: list[str] = []
    lines.append("capacity-locality-certification :: status-page verifier")
    lines.append("=" * 60)
    for n in report.notes:
        lines.append(f"  · {n}")
    if report.ok:
        lines.append("RESULT: PASS")
    else:
        lines.append("RESULT: FAIL")
        for f in report.failures:
            lines.append(f"  ✗ {f}")
    return "\n".join(lines)


def default_path() -> Path:
    return Path(__file__).resolve().parent.parent / "docs" / "status.html"


def main(argv: Iterable[str]) -> int:
    args = list(argv)
    path = Path(args[0]) if args else default_path()
    report = run(path)
    print(format_report(report))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
