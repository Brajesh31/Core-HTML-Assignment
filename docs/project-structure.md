# 🗂️ Project Structure and File Ownership

## 🌳 Repository map

| Path | Purpose | Ownership boundary |
|---|---|---|
| `Assignment_2_Core html/` | Original eight assignment tasks and Question 3 website. | **Protected coursework source.** |
| `Assignment_2_Core html/screenshot/` | Existing PNG screenshots for assignment questions. | **Protected original evidence.** |
| `.github/workflows/` | GitHub Actions automation. | Repository governance; may enhance carefully. |
| `.idea/` | IDE-specific project metadata. | Preserve; not required to run pages. |
| `docs/` | Product, page, content, architecture, accessibility, and quality documentation. | Documentation; may enhance. |
| `docs/assets/` | Original vector visuals and screenshot catalog. | Documentation visuals; may add. |
| `docs/templates/` | Reusable maintenance and review templates. | Documentation; may add. |
| `scripts/` | Read-only documentation and HTML validation scripts. | Support scripts; may add without rewriting assignment pages. |
| `README.md` | Repository entry point. | Documentation; may update. |
| `LICENSE` | Repository license notice. | Governance. |

## 📄 Original assignment files

| Question | Paths |
|---|---|
| Q1 | `Assignment_2_Core html/question1.html` |
| Q2 | `Assignment_2_Core html/question2.html` |
| Q3 | `Assignment_2_Core html/question3/index.html`, `webdevelopment.html`, `webdesign.html` |
| Q4 | `Assignment_2_Core html/question4.html` |
| Q5 | `Assignment_2_Core html/question5.html` |
| Q6 | `Assignment_2_Core html/question6.html` |
| Q7 | `Assignment_2_Core html/question7.html` |
| Q8 | `Assignment_2_Core html/question8.html` |

## 🔒 Protected-file policy

Documentation enhancement must not modify original assignment HTML or screenshot PNG files:
- `Assignment_2_Core html/**/*.html`
- `Assignment_2_Core html/screenshot/**/*.png`

It must also avoid introducing a new framework, dependencies, build configuration, or application code. Findings in assignment source are documented as findings. Any source correction is a separate scope requiring explicit authorization.

## ✅ Maintenance checklist

- [ ] File names/paths match the default branch.
- [ ] Every HTML page has a page guide.
- [ ] Existing screenshot links point to tracked PNG files.
- [ ] Diagrams describe actual page/navigation structure.
- [ ] Protected coursework files remain unchanged.
- [ ] No fabricated browser results or accessibility claims.
