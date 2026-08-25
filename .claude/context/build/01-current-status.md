---
id: BUILD-01
title: Current status — what exists today, and the immediate action list
domain: build
authority: reality
scope: Ground truth for the project state — what exists (a KB, a researched and machine-checked content design, a UI mock-up), what does not (any code), and the urgent obligations.
keys: [status, progress, current, what exists, not started, next, todo, urgent, setup, checklist, guest lecture, sign up, repo, invitation, data-storage, content, research, Đông Hồ]
related: [BUILD-02, BUILD-03, DEC-01, BRIEF-05, BRIEF-07]
source: Direct inspection of the project folder on 2026-08-25
---

# Current status

> **AUTHORITY: reality.** Re-verify by listing the folder before relying on this. Last inspection: **25 Aug 2026**.

**One-line summary: a knowledge base, a researched content design, and a UI mock-up exist — there is no code.** No Xcode project, no assigned GitHub repo cloned.

## What exists

| Item | State |
| --- | --- |
| Embedded KB (`.claude/`, `CLAUDE.md`, `OVERVIEW.md`) | Routed from the saved Canvas spec into `brief/01–09`, with the decision register in `DEC-01` |
| Assignment spec | Saved at `.claude/docs/GroupProjectCanvas.html`; extracted to `_source/`; routed into `brief/` |
| Xcode project | **Does not exist** |
| Assigned GitHub repo | **Not cloned** — created by the teaching team per `BRIEF-07` |
| Subject research | `.claude/data-storage/research/01-dong-ho-tranh-dan-gian.md` — the craft's timeline, process, painting catalog and present-day revival, 17 cited URLs across 15 domains, every claim status-marked (✅ / ⚠️ / ❌ with both readings recorded). The high-stakes claims — the UNESCO decision, the dated milestones, the process steps — were re-checked against live sources |
| Win-condition model | `.claude/data-storage/design/win-condition-model.md` — victory is decided by preparations, never by stats. Each preparation is a gated encounter: a `statFloor` to attempt it, a stat cost to clear it, and failing one leaves the run playable but no longer winnable. The trial asks two separate questions — *did you prepare* (decides victory) and *is there a household left to act* (floor only), which creates the fourth ending, **Kiệt sức**. Floors are machine-checked to stay floors rather than thresholds |
| Subject design | `.claude/data-storage/design/dongho-game-design.md` — POV, the four stats and their two-sided documented failures, the flag economy, the chapters, the minigames, the endings |
| Level structure | `.claude/data-storage/content/dongho/level.json` + `level-map.md` — **one continuous run 1938→2025, 36 dated spine cards in three chapters**, plus a 17-card weave pool drawn 4 per run, 8 ambient beats drawn ≤3, 8 stat-triggered crises and 14 interstitials. One Final Trial: the UNESCO inscription of 9 Dec 2025. Structure complete and machine-checked; **card prose still unwritten (~620–700 bilingual strings)** |
| Reachability proof | `.claude/data-storage/tools/trace_run.py` — beam-searches the whole choice space and confirms canonical lines taking every preparation exist on both Thường and Khó. Re-run after any number change |
| Content linter | `.claude/data-storage/tools/validate_data.py` — enforces the cost rule, the floors, the weave laws, the solvency invariant, the ledger/win-condition match, and bilingual TODO-free text. Current state: clean apart from the 8 expected "carrier does not exist yet" errors and 15 warnings documented in the workspace README |
| Difficulty model | `.claude/data-storage/content/game.json`. Two axes: **across chapters** difficulty comes from the shape of the problem and the danger profile (floors → the trap era → ceilings), per `BRIEF-05` §3; **inside the run** the Dễ/Thường/Khó control changes only information and slack, never numbers or the win rule. The linter enforces the separation |
| UI mock-up | Google Stitch project `1689000862901928358` — a full screen set for the swipe loop, the interstitials, the endings and the side flows, on a light and a dark design system. **Mock-up only: not SwiftUI, not exported, no code behind it**, and its visual design is being redone as a live task on the board |
| Task board | Trello — *IOS Group Project*: 6 backlog tickets with owners, sub-task checklists, definitions of done and progress checkpoints |
| Team decisions | **Concept settled**: card game · subject tranh Đông Hồ · household POV · one continuous 36-card run to the 2025 UNESCO trial · win by preparation · two minigames · vi+en. Roles, names, stack, industry requirements and workload split remain open — see `DEC-01` |

## 🔴 Urgent actions (time-sensitive)

1. **Week 7 Guest Lecture material** — the lecture (10–14 Aug) has passed. Two industry requirements from it are mandatory (`BRIEF-05` §5) and cannot be chosen until the content is in hand. Recover slides/notes/recording from whoever attended or from Canvas, then close `DEC-01` D9.
2. **GitHub invitations** — when the teaching team creates the repo, every member must **accept within 7 days** or the invite expires (`BRIEF-07`). Confirm every member's GitHub username is on record.
3. **Fill the two mandatory roles (`DEC-01` D3/D4)** — `BRIEF-07` assesses both, and the Technical Lead gatekeeps the default branch, so nothing can land properly until D4 closes.
4. **Start the Xcode project** — every remaining rubric criterion depends on code existing, and the content prose can be written in parallel with it.

**Runway check: 17 days to the deadline as of 25 Aug 2026, and there is no code.** See `BUILD-02`.

## Standing obligations from day one

- **Commit hygiene from the first commit:** history is assessment evidence — regular commits from every member across the full four weeks, purposeful branches (`BRIEF-07`).
- **Source-file header** on every file from the first file (`BRIEF-01`).
- **Work only in the assigned private org repo** once it exists — never in personal/public repos (`BRIEF-07`).

## Update discipline

When anything changes (repo cloned, decision closed, code started), update this file in the same turn, and move closed items out of `DEC-01`/`BUILD-03`.
