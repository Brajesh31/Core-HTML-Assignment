# ⚠️ Known Issues and Source Review Notes

The following are observations from static inspection of the original HTML files. They are not all runtime-reproduced validation failures. Assignment HTML is preserved.

| ID | File | Observation | Potential impact | Suggested follow-up |
|---|---|---|---|---|
| K-01 | Q1 | The `mark` element closes after its containing paragraph. | Invalid nesting and parser correction. | Correct nesting in separately authorized source task. |
| K-02 | Q1/Q2/Q4/Q7 | Several pages use generic `Document` titles. | Poor browser tab identification. | Add meaningful unique titles. |
| K-03 | Q3 Home | Home label is plain text, unlike links to the other pages. | Inconsistent navigation behavior. | Decide whether Home should link to itself. |
| K-04 | Q3 all pages | Inline styles are repeated in navigation/content layout. | Harder to maintain consistent styling. | Optional separate CSS extraction task. |
| K-05 | Q4 | Several tag examples use elements such as article/form/embed in text-list positions; some descriptions are incomplete. | Demonstration markup may not communicate intended semantics. | Audit examples in a separate source correction. |
| K-06 | Q5 | Description list terms/descriptions are nested inside a description element. | Description-list semantics may be invalid or confusing. | Rebuild a valid description list after approval. |
| K-07 | Q6 | One HTML feature bullet repeats; HTML and JavaScript feature cells use lists while CSS uses a sentence. | Inconsistent content structure. | Review table content separately. |
| K-08 | Q7 | Top-level content is split into two separate unordered lists. | TOC hierarchy is divided. | Consolidate in a source correction task. |
| K-09 | Q8 | The 10:30–11:30 time label appears in the Room 1 cell rather than Time column. | Timetable alignment is likely incorrect. | Confirm intended schedule, then fix cell sequence/spans. |
| K-10 | README | Original README was a generic title and timestamp only. | No useful project/setup documentation. | Expanded README. |
| K-11 | Workflow | Hourly timestamp workflow committed to main and used personal email identity. | Commit churn and personal address exposure in commit metadata. | Narrow schedule and use GitHub noreply bot identity. |

## 🧪 Verification status

| Check | Status |
|---|---|
| Static page inspection | Completed for eight assignment questions and Q3's three-page mini-site. |
| Screenshot inventory | Existing PNG files enumerated in repository tree. |
| Full HTML conformance validation | Not performed during static review. |
| Live browser test | Not performed in this documentation pass. |
| Accessibility audit | Not performed. |
| Source fixes | None applied. |
