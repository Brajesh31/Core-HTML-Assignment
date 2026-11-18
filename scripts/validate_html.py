#!/usr/bin/env python3
"""Read-only HTML checks for assignment documents.

The parser reports known legacy markup findings without rewriting coursework.
Severe parser failures and missing assignment pages fail the check; existing
misnesting observations are surfaced as warnings so docs CI can remain useful
while original assignment source is intentionally preserved.
"""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENT_DIR = ROOT / "Assignment_2_Core html"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
EXPECTED = [
    ASSIGNMENT_DIR / "question1.html",
    ASSIGNMENT_DIR / "question2.html",
    ASSIGNMENT_DIR / "question3" / "index.html",
    ASSIGNMENT_DIR / "question3" / "webdevelopment.html",
    ASSIGNMENT_DIR / "question3" / "webdesign.html",
    *[ASSIGNMENT_DIR / f"question{i}.html" for i in range(4, 9)],
]

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.warnings = []
        self.fatal = []
        self.has_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.has_title = True
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            self.warnings.append(f"Closing tag </{tag}> used for a void element.")
            return
        if tag not in self.stack:
            self.warnings.append(f"Unexpected closing tag </{tag}>.")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
            return
        self.warnings.append(f"Misnested </{tag}>; open elements at close: {' > '.join(self.stack)}.")
        self.stack = self.stack[:self.stack.index(tag)]

def main() -> int:
    errors, warnings = [], []
    for path in EXPECTED:
        if not path.is_file():
            errors.append(f"Missing assignment file: {path.relative_to(ROOT)}")
            continue
        parser = Checker()
        try:
            parser.feed(path.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: parser error: {exc}")
            continue
        if not parser.has_title:
            warnings.append(f"{path.relative_to(ROOT)}: missing <title>.")
        warnings.extend(f"{path.relative_to(ROOT)}: {issue}" for issue in parser.warnings)
    for item in warnings:
        print(f"WARNING: {item}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"HTML page inventory/parser check passed ({len(EXPECTED)} assignment pages; {len(warnings)} legacy warning(s)).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
