# 🖥️ Page-by-Page Documentation

This inventory is derived from the eight checked-in assignment pages and the three Question 3 pages. It describes source content, not a live browser test.

## 🗺️ Assignment index

| Assignment | File | Purpose | Source elements/concepts |
|---|---|---|---|
| Q1 | [question1.html](../Assignment_2_Core%20html/question1.html) | Text formatting examples. | `strong`, `i`, `u`, `mark`, `sup`, `sub`, `small`, `del`. |
| Q2 | [question2.html](../Assignment_2_Core%20html/question2.html) | External website navigation. | Heading elements and external anchors. |
| Q3 Home | [index.html](../Assignment_2_Core%20html/question3/index.html) | Personal introduction page. | Header, nav, relative links, headings, paragraphs. |
| Q3 Web Development | [webdevelopment.html](../Assignment_2_Core%20html/question3/webdevelopment.html) | Overview of development disciplines. | Navigation, headings, paragraphs. |
| Q3 Web Design | [webdesign.html](../Assignment_2_Core%20html/question3/webdesign.html) | Overview of web design concepts. | Navigation, headings, paragraphs. |
| Q4 | [question4.html](../Assignment_2_Core%20html/question4.html) | Glossary-style HTML tag list. | Ordered list and inline examples. |
| Q5 | [question5.html](../Assignment_2_Core%20html/question5.html) | Full-stack stack terms and descriptions. | Description list concepts and embedded CSS. |
| Q6 | [question6.html](../Assignment_2_Core%20html/question6.html) | HTML/CSS/JavaScript comparison. | Captions, tables, th/td, lists. |
| Q7 | [question7.html](../Assignment_2_Core%20html/question7.html) | Table of contents hierarchy. | Nested unordered lists and CSS pseudo-element. |
| Q8 | [question8.html](../Assignment_2_Core%20html/question8.html) | Conference timetable. | Table headers, `rowspan`, `colspan`. |

## 1. ✍️ Q1, Text formatting

**File:** `Assignment_2_Core html/question1.html`

The document demonstrates bold/strong text, italic text, underline, highlighting, superscript, subscript, small text, and deleted text. It has basic language, character encoding, viewport, and title metadata.

**Review note:** the current mark example places the closing `</p>` before `</mark>`. This is an invalid nesting pattern to review separately; the original file is preserved.

## 2. 🔗 Q2, External hyperlinks

**File:** `Assignment_2_Core html/question2.html`

A heading introduces three descriptive external links: Great Learning Academy, W3Schools Python, and Netflix India. These are destinations linked by the example, not integrations owned by the project.

**Review note:** check external link destinations and link text periodically. No external site availability check is claimed.

## 3. 🧭 Q3, Three-page mini-site

**Files:** `question3/index.html`, `question3/webdevelopment.html`, `question3/webdesign.html`

### Home page
Contains a navigation bar with Home, Web Development, and Web Design labels, followed by introduction, passion/motivation, and key skills paragraphs. It currently contains a personal introduction naming Sourav Halder. Preserve the source content unless a separately scoped correction is requested.

### Web Development page
Describes front-end, back-end, full-stack development, responsive design, frameworks/libraries, continuous learning, and collaboration.

### Web Design page
Describes user-centric design, UI/UX, visual elements, responsive design, and typography/readability.

### Navigation behavior
All three pages link to the other two using relative filenames. The Home label is plain text on the home page, while links to the other pages are anchors. See [navigation structure](navigation-structure.md).

## 4. 🏷️ Q4, HTML tag glossary

**File:** `Assignment_2_Core html/question4.html`

Presents an ordered list of common HTML tags and brief descriptions. Several list entries wrap tag names in elements to visually illustrate them.

**Review note:** some examples are incomplete or invalid as semantic demonstrations, including an anchor without `href`, form/article/embed elements used as inline wrappers, and incomplete descriptions. This file is preserved.

## 5. 📚 Q5, Full-stack technology definition list

**File:** `Assignment_2_Core html/question5.html`

Groups frontend (HTML/CSS/JavaScript), backend (Node.js/Express/MongoDB/MySQL), and full-stack tools (Git/GitHub/VS Code), using `dt` and `dd` concepts.

**Review note:** nested `dt`/`dd` elements inside a `dd` should be validated against intended HTML structure. The assignment remains unchanged.

## 6. 📊 Q6, Technology comparison tables

**File:** `Assignment_2_Core html/question6.html`

Contains separate HTML, CSS, and JavaScript tables. The HTML and JavaScript rows include unordered lists of features/benefits; the CSS row uses a sentence in the final cell.

**Review note:** review header associations, duplicate HTML bullet text, and whether table layout is best for the content.

## 7. 🪜 Q7, Nested table of contents

**File:** `Assignment_2_Core html/question7.html`

Builds a hierarchy of four parts with nested subsections, sub-subsections, and further nested topics. CSS adds blue underlined list text and black markers.

**Review note:** the file currently uses separate top-level unordered lists for Part 1 and the remaining parts. Consider one coherent list in a separate correction task.

## 8. 🗓️ Q8, Conference schedule

**File:** `Assignment_2_Core html/question8.html`

Creates a conference schedule with Time and Room 1–4 columns, including keynote/session labels, lunch break, and cells spanning multiple rows/columns.

**Review note:** the second timetable row contains a time string in a room column due to the current table cell arrangement. Validate intended time-slot alignment before any correction.

## 📸 Screenshots

Existing screenshots are stored under `Assignment_2_Core html/screenshot/`. See [screenshot catalog](assets/screenshots.md). Screenshots are preserved and must not be represented as freshly captured validation evidence.
