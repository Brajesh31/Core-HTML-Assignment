#!/usr/bin/env python3
"""Validate local Markdown links in repository docs and root guides."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = [ROOT / name for name in ("README.md", "CONTRIBUTING.md", "SECURITY.md", "SUPPORT.md", "ROADMAP.md", "CHANGELOG.md")]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\((.*?)\)")
REF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
FENCE_RE = re.compile(r"(?s)^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE)
INLINE_RE = re.compile(r"`[^`]*`")

def files_to_scan():
    found = {p for p in ROOT_FILES if p.is_file()}
    docs = ROOT / "docs"
    if docs.exists():
        found.update(docs.rglob("*.md"))
    return sorted(found)

def main() -> int:
    errors, checked = [], 0
    for source_path in files_to_scan():
        text = FENCE_RE.sub("", source_path.read_text(encoding="utf-8"))
        text = INLINE_RE.sub("", text)
        for raw in LINK_RE.findall(text) + REF_RE.findall(text):
            target = raw.strip().strip("<>")
            if not target or "{{" in target or "}}" in target:
                continue
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:")):
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            candidate = (source_path.parent / path).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source_path.relative_to(ROOT)}: path escapes repository: {target}")
                continue
            checked += 1
            if not candidate.exists():
                errors.append(f"{source_path.relative_to(ROOT)}: missing target: {target}")
    if errors:
        print("\n".join(errors))
        print(f"{len(errors)} broken link(s) among {checked} checked.")
        return 1
    print(f"Local Markdown links passed ({checked} checked).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
