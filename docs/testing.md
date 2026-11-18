# 🧪 Testing and Validation Strategy

## 📌 Current test context

The repository consists of static HTML documents and PNG screenshots. No package manifest, test runner, browser automation configuration, or build system was found in the original root.

## ✅ Validation layers

| Layer | Purpose | Suggested method |
|---|---|---|
| File inventory | Confirm expected HTML pages and screenshot assets exist. | Python path checks. |
| HTML syntax | Detect malformed tokens and common parser errors. | HTML5-capable parser or validator. |
| Link validation | Check local relative links and fragments. | Repository script + browser check. |
| Browser rendering | Confirm page opens and content renders. | Current browsers, manual review. |
| Navigation | Check all six Q3 relative links. | Click-through test. |
| Responsive | Inspect narrow and wide viewport behavior. | Browser device toolbar. |
| Accessibility | Keyboard, headings, tables, contrast, screen reader. | Manual checks and suitable audit tooling. |
| Screenshot comparison | Compare rendering to existing evidence. | Human visual comparison at same viewport. |

## ▶️ Run local checks

From repository root:

```bash
python scripts/validate_docs.py
python scripts/validate_links.py
python scripts/validate_html.py
python scripts/validate_svg.py
```

## 🧭 Manual browser test plan

1. Open each of the eight assignment documents.
2. Confirm the browser loads the file without a blank page.
3. Review headings, lists, links, and table content.
4. Open Question 3 Home and follow every navigation link in both directions.
5. Inspect at desktop and mobile widths.
6. Use keyboard navigation and inspect visible focus.
7. Compare the result with the corresponding pre-existing screenshot.
8. Record browser, viewport, commit, outcome, and any differences.

## 📄 Evidence format

Record results with [test report template](templates/test-report-template.md). Do not mark a test as passed unless it was executed and evidence was inspected.
