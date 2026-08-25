---
id: BUILD-03
title: Team meeting — agenda for the decisions still open
domain: build
authority: reality
scope: A ready-to-run agenda covering only the decisions DEC-01 still lists as open. Items the register has settled are not on it and are not reopened here.
keys: [meeting, agenda, preparation, discuss, decide, roles, workload, logistics]
related: [DEC-01, BUILD-01, BUILD-02, BRIEF-02, BRIEF-07]
source: Synthesised from the brief and DEC-01. Every item here maps to an Open row in DEC-01 — when a row closes, delete its item
---

# Team meeting — agenda

> Purpose: leave the meeting with the mandatory roles filled, chapter ownership assigned, logistics
> running, and every time-sensitive obligation owned. This agenda records **questions, not answers** —
> decisions get written into `DEC-01` after the team makes them.
>
> **Scope rule:** every item below is an Open row in `DEC-01`. The concept, subject, POV, structure,
> win rule, minigames and languages are **settled** and are not agenda items — §3 exists to share
> understanding of them, not to revisit them.

## Before the meeting — each member individually

- [ ] Read the theme and the central rule — `BRIEF-02` (10 min). The one-line test to keep in mind: *would the game break if the culture were swapped out?* (`BRIEF-09` §1, Excellent band.)
- [ ] Read the design and the level map (linked in §3) so §3 is a walkthrough, not a briefing.
- [ ] Confirm your **GitHub username** and that you can access the `rmit-vietnam-computing-technologies` org once invited (`BRIEF-07`).
- [ ] Bring the **Week 7 Guest Lecture** material — slides, notes, or the Canvas recording. The lecture has passed and D9 cannot close without it.

## Agenda

### 1 · Logistics & ground rules (10 min)

- Meeting cadence, channel, branch/PR conventions, task board (D12).

### 2 · Roles (10 min) — the longest-overdue item

- **Project Manager** (D3) — chairs meetings, owns the plan and the responsibilities table.
- **Technical Lead** (D4) — owns technical decisions and the default branch.
- Note: roles don't reduce anyone's expected development contribution; contribution is assessed per member (`BRIEF-07`), and the video needs a meaningful part from everyone (`BRIEF-06`).

### 3 · The game — shared understanding (15 min)

The concept is settled (`DEC-01`): a swipe-decision card game about **nghề làm tranh dân gian Đông Hồ**,
played as one craft household across a single 36-card run, won by preparation rather than by stats.
This slot is for everyone to arrive at the same understanding of it, not to reopen it.

- Walk the run: the three chapters, the preparations, the two traps, the Final Trial.
- Walk the four endings and why each one is a real fate a household had.
- Agree who owns which chapter's prose (12 / 10 / 14 cards) — ties to D11.

Read before the meeting: `.claude/data-storage/design/dongho-game-design.md` and
`.claude/data-storage/content/dongho/level-map.md`.

### 4 · Names (5 min — can stay open)

- Group name (D5 — needed for the repo and ZIP filenames) and app name (D6 — the team's own wording).

### 5 · Technical starting posture (15 min — orientation, not commitment)

- Persistence/sync stack options and what the justification in the report needs (D7, `BRIEF-03`).
- Which optional advanced features look plausible for 6 marks (D10, `BRIEF-05`/`BRIEF-09`).
- Week 7 guest-lecture industry requirements — pick the two from the material (D9).

### 6 · Immediate task assignments & close (10 min)

- Owners + dates for: chapter prose, repo access confirmation, guest-lecture requirements, next meeting.
- PM starts the task breakdown that will become the **Project Responsibilities table with % totalling 100%** (`BRIEF-06` §11).

## After the meeting

- Record closed decisions in `DEC-01` (status, date, rationale); update `BUILD-01`; put the next meeting and decision dates in `BUILD-02`'s plan once the PM owns it.
