# 🧱 Content Model

## 📌 Content entities

| Entity | Description | Count observed |
|---|---|---:|
| Assignment question | Standalone HTML document for one question. | 8 question groups. |
| Q3 subpage | One page in the multi-page navigation exercise. | 3 pages. |
| Screenshot | Existing PNG file linked to an assignment. | 9 images. |
| Documentation page | Markdown file describing the project and its concepts. | Grows with documentation. |

## 🔗 Relationships

- Each assignment question has one or more HTML source files.
- Q3 is one assignment composed of three linked HTML documents.
- Screenshot images are organized in a question-oriented hierarchy.
- Documentation pages describe source artifacts; they are not consumed by HTML pages.

## 🚫 Data not present

No database schema, application user, API payload, or server-side content model was found in inspected repository.
