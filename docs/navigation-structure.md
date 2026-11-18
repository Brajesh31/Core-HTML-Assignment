# 🧭 Navigation Structure

## 🗺️ Page map

The eight numbered HTML files are standalone assignment pages. Question 3 has a mini-site with three pages and local relative links.

```mermaid
flowchart TD
  Q3["Q3 Home · index.html"] --> DEV["Web Development"]
  Q3 --> DESIGN["Web Design"]
  DEV --> Q3
  DEV --> DESIGN
  DESIGN --> Q3
  DESIGN --> DEV
  Q1["Q1 · question1.html"]
  Q2["Q2 · question2.html"]
  Q4["Q4 · question4.html"]
  Q5["Q5 · question5.html"]
  Q6["Q6 · question6.html"]
  Q7["Q7 · question7.html"]
  Q8["Q8 · question8.html"]
```

## 🔗 Question 3 link table

| Source page | Link text | Target path |
|---|---|---|
| Home | Web Development | `webdevelopment.html` |
| Home | Web Design | `webdesign.html` |
| Web Development | Home | `index.html` |
| Web Development | Web Design | `webdesign.html` |
| Web Design | Home | `index.html` |
| Web Design | Web Development | `webdevelopment.html` |

## ⚠️ Navigation limitations

- No root-level index page linking all eight questions was found in the original assignment tree.
- Questions 1, 2, and 4–8 are independent documents.
- Q3 navigation is implemented with plain relative anchors.
- There are no server routes, client-side router, or JavaScript navigation state.
