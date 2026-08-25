---
id: BUILD-02
title: Timeline — due date derivation, week map, and runway
domain: build
authority: reality
scope: The verified due date and how it was derived, the semester week map for the assignment window, and the remaining runway. Contains a proposed (NOT decided) milestone shape for the first meeting to react to.
keys: [deadline, due date, 11 September, week 11, timeline, runway, weeks, schedule, milestones, calendar, days remaining]
related: [BRIEF-01, BUILD-01, BUILD-03, DEC-01]
source: Canvas due-date metadata in _source/canvas-extract-raw.md (epoch 1789120800) + A1 week anchoring. The due date is fixed; the runway below is computed — re-derive it against today's date before relying on it
---

# Timeline & runway

## The due date — verified, not assumed

- The brief's header says **"Deadline: 5PM Friday of week 11."**
- The Canvas assignment's machine-readable due-date field in the saved page is epoch **`1789120800`** = **2026-09-11 10:00 UTC** = **Friday 11 September 2026, 17:00 Vietnam time (ICT, UTC+7)**.
- The Canvas sidebar in the same page renders it as **"Due Sep 11 by 17:00"** and shows the assignment **available after Mon 10 Aug 2026, 10:00** — the window 10 Aug → 11 Sep is the brief's "~4 weeks".
- Cross-check: Assignment 1 was due 5pm **Friday of week 6 = 7 Aug 2026**; five weeks later is **11 Sep 2026** — the weeks are consecutive and all anchors agree. (The page's rendered "09/11/2026" elsewhere is US mm/dd order, *not* 9 November.)

> **Due: Friday 11 September 2026, 17:00 (Vietnam time).** Everything — ZIP (code + `Document.pdf` + `GitHub.txt` + `Youtube.txt`) and the YouTube video — land together (`BRIEF-01`).

## Week map for the assignment window

| Week | Dates (Mon–Fri) | Notes |
| --- | --- | --- |
| Week 7 | 10–14 Aug 2026 | **Guest lecture week** — the two industry requirements come from it (`BRIEF-05` §5). **Past**: the material must now be obtained from whoever attended, or from Canvas. |
| Week 8 | 17–21 Aug 2026 | Past. |
| Week 9 | 24–28 Aug 2026 | **Current week** (as of Tue 25 Aug 2026). |
| Week 10 | 31 Aug – 4 Sep 2026 | |
| Week 11 | 7–11 Sep 2026 | **Due Friday 11 Sep, 17:00.** |

**Runway: the window 10 Aug → 11 Sep is the brief's "~4 weeks". As of 25 Aug 2026, 17 days remain**
— two and a half working weeks, with no code yet written.

## Proposed milestone shape — ⚠️ NOT DECIDED, input for the first meeting

A neutral starting point for the meeting to accept, reshape, or replace (`BUILD-03`); the real plan belongs to the PM once roles exist:

| Window | Candidate focus |
| --- | --- |
| Done | Concept, subject research, win-condition model, level structure and content map — all machine-checked |
| **Overdue** | Roles (D3/D4); repo access; guest-lecture requirements (D9); task breakdown & workload agreement (D11) — all were due by wk 8 and none has closed |
| Week 9 (now) | MVVM skeleton; auth + persistence spike; core game loop + Game View; Menu; spine prose begins in parallel |
| Week 10 | Leaderboard, How To Play, Settings; industry requirements; advanced features; content/localization |
| Week 11 | Polish, device matrix testing (incl. lab iMac), report, video recording, ZIP dry-run — submit **before** Fri 17:00 |

Hard scheduling facts to respect regardless of the chosen plan:

- The **video needs all 5 members on camera** — recording cannot be left to the last hours (`BRIEF-06`).
- **Lab iMac verification** must precede submission (`BRIEF-01`).
- Commit history must show **regular commits from every member across the whole window** — a back-loaded plan is itself mark-losing (`BRIEF-07`).
- The report's Project Responsibilities percentages must be **agreed by the whole team** — schedule that conversation, don't improvise it at the deadline (`BRIEF-06` §11).
