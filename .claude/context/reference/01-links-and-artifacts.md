---
id: REF-01
title: External links & artifacts
domain: reference
authority: reference
scope: Every URL and external artifact the brief references — Canvas files, GitHub org, RMIT policy pages, and the source HTML itself.
keys: [links, URL, Canvas, files, YouTube, GitHub organization, RMIT, academic integrity, rubric link, source]
related: [BRIEF-01, BRIEF-07]
source: _source/canvas-extract-raw.md — all hyperlinks and file references
---

# External links & artifacts

## The assignment itself

| Artifact | Location | Notes |
| --- | --- | --- |
| Canvas assignment page | `https://rmit.instructure.com/courses/172067/assignments/1251174` | Requires RMIT Canvas login. The live source of truth — re-check it for updates/announcements. |
| Saved copy (the KB's source) | `.claude/docs/GroupProjectCanvas.html` | Saved Canvas page, extracted into this KB on 13 Aug 2026. |
| Marking rubric | Canvas rubric `680963` on course 172067 (attached to the assignment page) | Transcribed in full in `BRIEF-09`. |

## Canvas-hosted files referenced by the brief (login required)

| File | Canvas path | What it is |
| --- | --- | --- |

## Other external links in the brief

| Link | Context |
| --- | --- |
| `https://www.youtube.com/watch?v=abjFdj7yexI` | Referenced in the Save-and-Resume optional feature — demonstrates fully removing an app from memory (`BRIEF-05` §6). *Verified 13 Aug 2026: exists — "iPhone 13's & 14's: How to Close Background Running Apps (Close Completely)".* |
| `https://github.com/rmit-vietnam-computing-technologies/` | The GitHub organization holding the assigned team repo (`BRIEF-07`). All repos are private — the page shows nothing without an accepted invitation; sibling RMIT orgs (`RMIT-Vietnam-Teaching`, `rmit-computing-technologies`) are publicly visible and follow the same pattern. |
| `https://www.rmit.edu.au/students/student-essentials/assessment-and-exams/academic-integrity` | RMIT academic integrity policy (Plagiarism section). *Verified 13 Aug 2026: 301-redirects (via `…/assessment-and-results/…`) to the live page below.* |
| `https://www.rmit.edu.au/students/student-essentials/assessment-and-results/academic-integrity` | RMIT Academic Integrity page (Support Resources section). *Both brief URLs resolve to the current canonical page `https://www.rmit.edu.au/students/my-course/assessment-results/academic-integrity`, which covers plagiarism and collusion.* |
| Apple Human Interface Guidelines | Named (not linked) as the professional standard for the aesthetic criterion (`BRIEF-05`); canonical: `https://developer.apple.com/design/human-interface-guidelines/`. |

**Environment facts, web-verified 13 Aug 2026:** Xcode **26.4.1** is a real, current release (Apple release notes; released ~16 Apr 2026; ships Swift 6.3) — matching the marking environment in `BRIEF-01`. The **iPhone 17 / 17 Pro / 17 Pro Max** (released Sep 2025) and the **11-inch iPad Air** are real devices with Xcode simulators, matching `BRIEF-05` §4.

## Sibling project (structure reference only)

`../MigratoryYear/` — the Assignment 1 project whose KB architecture this KB mirrors. **Its content (topic, invariants, state rules) does not apply to Assignment 2** — notably, A1 forbade view models while A2 *mandates* MVVM (`BRIEF-03`).
