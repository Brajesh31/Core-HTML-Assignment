#!/usr/bin/env python3
"""Parse documentation SVGs and check basic accessibility metadata."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SVG_DIR = ROOT / "docs" / "assets"

def main() -> int:
    errors = []
    files = sorted(SVG_DIR.rglob("*.svg"))
    for path in files:
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            tags = {node.tag.split("}")[-1] for node in root.iter()}
            if root.tag.split("}")[-1] != "svg":
                errors.append(f"{path.relative_to(ROOT)}: root is not svg")
            if not {"title", "desc"}.issubset(tags):
                errors.append(f"{path.relative_to(ROOT)}: missing title/desc")
            for node in root.iter():
                tag = node.tag.split("}")[-1].lower()
                if tag in {"script", "foreignobject"}:
                    errors.append(f"{path.relative_to(ROOT)}: disallowed {tag} element")
                for attr in node.attrib:
                    if attr.lower().startswith("on"):
                        errors.append(f"{path.relative_to(ROOT)}: event handler {attr}")
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid XML: {exc}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"SVG checks passed ({len(files)} files).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
