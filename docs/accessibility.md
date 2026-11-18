# ♿ Accessibility Review Guide

## 🎯 Objective

Use semantic HTML and test rendered pages with keyboard and assistive technology. This document is a review guide, not a statement that the current assignment conforms to WCAG.

## 🔍 Review checklist

| Area | What to inspect | Evidence to record |
|---|---|---|
| Document language | `html lang` accurately identifies page language. | Source and browser inspection. |
| Page title | Each document has a meaningful, unique title. | Title inventory. |
| Headings | Logical hierarchy without skipped levels for styling alone. | Heading outline per page. |
| Links | Descriptive link names and valid destinations. | Link table and keyboard test. |
| Keyboard | All interactive controls are reachable and operable. | Keyboard-only test. |
| Focus | Visible focus indication and sensible order. | Browser evidence. |
| Lists | List content uses valid list structure. | HTML validation. |
| Tables | Captions and header associations convey relationships. | Screen-reader/manual test. |
| Color | Text and meaningful visuals have sufficient contrast. | Measured contrast results. |
| Zoom/reflow | Content remains available at zoom and narrow widths. | Tested viewport notes. |

## ⚠️ Source-review observations

- Q1 contains mismatched nesting around a paragraph and mark element.
- Q2 uses generic title text and should be checked for clear page identification.
- Q3 has a visible navigation pattern but the Home label on the home page is not a link.
- Q4 uses some void/interactive elements in demonstration positions; verify examples are semantically valid.
- Q5 uses nested description-list terms/details, which should be reviewed.
- Q6 tables should be checked for meaningful header association and layout usefulness.
- Q7 nested lists should have structurally consistent parent/child relationships.
- Q8 needs table header and row/column span inspection.

## 📊 Conformance status

No complete accessibility audit or assistive-technology test was executed in this documentation pass. WCAG 2.2 AA may be used as an evaluation target, but no blanket conformance claim is made.
