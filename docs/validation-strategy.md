# ✅ Validation Strategy

## 🔎 Automated checks

The repository support scripts provide lightweight checks for:
- Required documentation paths and non-empty content.
- Local Markdown links in repository-owned documentation.
- Basic HTML parser diagnostics and selected structural issues in assignment pages.
- SVG XML parsing and title/description metadata.

These checks are intentionally conservative and do not modify source pages.

## 🧪 Checks that remain manual

- Browser layout and rendering.
- Link destination availability outside the repository.
- Full HTML conformance using a dedicated standards validator.
- Keyboard and screen-reader accessibility.
- Visual fidelity compared with existing screenshot images.
- Cross-browser behavior.

## ⚠️ Limitations

A parser check is not a full conformance audit. A passing local-link check does not establish that an external website is available. A screenshot file's presence does not prove the current page renders the same way.
