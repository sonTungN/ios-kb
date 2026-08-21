# `_source/` — superseded originals (DO NOT LOAD)

These are the **original, pre-restructure** source materials, retained for provenance and rollback safety.

> ⚠️ **Excluded from routing. Never load these to answer a question.**
> Their content has been fully migrated into the topical KB under `.claude/context/{brief,decision,build,reference}/`.
> Loading them duplicates content the router already covers, wastes tokens, and risks answering from a raw, noisy copy.

## Provenance

| Artifact | What it is |
| --- | --- |
| `.claude/docs/GroupProjectCanvas.html` | The **original saved Canvas page** — `https://rmit.instructure.com/courses/172067/assignments/1251174`, "Assignment 2", saved from the authenticated Canvas web view. This is the ultimate source of truth. Kept outside `_source/` because it is the raw web artifact, not KB prose. |
| `canvas-extract-raw.md` (this folder) | A mechanical, zero-loss text extraction of every `user_content` block in that HTML (55,252 chars), produced 13 Aug 2026. Contains **all** assignment text including the rubric, plus Canvas UI noise (form controls, rubric-editor template rows) that is *not* assignment content. |

## Where the content went

| Section of the Canvas page | Migrated into |
| --- | --- |
| Header (course, weight, deadline, team size, feedback, late work) | `brief/01` |
| Learning Objectives + Ready for Life and Work | `brief/01` |
| The Hackathon Challenge, theme, International Group Option, Core Concept & game types, inspiration areas, Scope & Framework Restrictions | `brief/02` |
| Technical Requirements §1 (Architecture, User Management, Persistence & Sync) | `brief/03` |
| Technical Requirements §2 (Game Structure and Views) | `brief/04` |
| Technical Requirements §3–§6 (Gameplay/UX, Compatibility, Week 7 Industry Requirements, Optional Advanced) + Aesthetic and User-Centric Design | `brief/05` |
| Documentation and Presentation (Report + Video) | `brief/06` |
| Deliverables, Project Deliverables, Submission Instructions (header, environment, ZIP) | `brief/01` |
| Assigned GitHub Repository, invitation, repository/development-history/README requirements + Teamwork (PM/TL) | `brief/07` |
| Rubric "iOS Rubric Assignment 2" (7 criteria, 40 pts) | `brief/09` |
| Canvas due-date metadata (epoch `1789120800`) | `brief/01`, `build/02` |

**Known noise in `canvas-extract-raw.md` that is deliberately NOT in the KB** (it is Canvas editor chrome, not assignment content): the file-upload form, the "Find a Rubric" dialog, the blank 5-pt "Description of criterion / Full Marks / No Marks" rubric-editor template rows, and the second empty rubric template block. The real rubric totals **40/40**.

## Deleting this folder

Once the migration has been spot-checked and the project is under version control (the team's assigned GitHub repository), this folder can be deleted safely — the original HTML in `.claude/docs/` already preserves full fidelity.
