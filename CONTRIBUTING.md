# 🤝 Contributing

Thanks for helping improve Core HTML Assignment.

## 📌 Project scope
This repository is a set of static HTML coursework examples. Contributions should improve clarity, documentation, validation, or preserve original assignment work.

## 🔒 Protected coursework
Do not edit original assignment HTML pages or screenshots as part of routine documentation work:
- `Assignment_2_Core html/**/*.html`
- `Assignment_2_Core html/screenshot/**/*.png`

A source correction must be requested and approved separately. When useful, prefer separate corrected examples so original coursework remains available.

## 🧭 Suggested workflow
1. Read the [README](README.md) and [documentation hub](docs/README.md).
2. Inspect current pages before proposing changes.
3. Keep documentation factual and tied to source.
4. Avoid unnecessary dependencies and build systems.
5. Run relevant validation scripts.
6. Record tests that were not run.

## ✅ Documentation standards
- Use relevant emojis where they improve scanning.
- Keep links relative and verify them.
- Keep diagrams aligned with real files and links.
- Use descriptive titles, alt text, and headings.
- Never invent screenshots, test results, accessibility outcomes, or feature claims.

## 🔐 Privacy and security
Do not commit credentials, private keys, phone numbers, or unrelated personal information. Use synthetic sample data in examples and screenshots.

## 🧪 Local checks
```bash
python scripts/validate_docs.py
python scripts/validate_links.py
python scripts/validate_html.py
python scripts/validate_svg.py
```
