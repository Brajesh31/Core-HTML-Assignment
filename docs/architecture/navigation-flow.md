# 🧭 Question 3 Navigation Flow

```mermaid
flowchart LR
  HOME["Home · index.html"]
  DEV["Web Development · webdevelopment.html"]
  DESIGN["Web Design · webdesign.html"]
  HOME -->|"webdevelopment.html"| DEV
  HOME -->|"webdesign.html"| DESIGN
  DEV -->|"index.html"| HOME
  DEV -->|"webdesign.html"| DESIGN
  DESIGN -->|"index.html"| HOME
  DESIGN -->|"webdevelopment.html"| DEV
```

All edges are local relative links. They resolve against the directory containing the current HTML file. This is browser navigation between static documents, not client-side routing.
