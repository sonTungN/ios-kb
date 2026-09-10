# GroupProject (Assignment 2) — Antigravity Project Kernel

**This file is always in context for Antigravity / Gemini.** Everything else is loaded on demand, by address using `view_file`.
Detailed catalog: `.claude/context-index.md` · Retrieval protocol: `.claude/rules/context-map.mdc` · KB rationale: `OVERVIEW.md`

---

## Identity

| | |
| --- | --- |
| **Project** | An **educational iOS game** on the theme **"Living Heritage — Vietnam: Culture in Play"** — cultural heritage embedded in the game mechanics, not as decoration |
| **Assignment** | COSC3062 / COSC3063 iPhone Software Engineering — **Assignment 2 (Group Project)**, Semester 2026B, **team of 5**, **40%** of the course |
| **Deadline** | **Friday 11 Sep 2026, 17:00** (Vietnam time) — "5PM Friday of week 11", verified against Canvas metadata (`BUILD-02`). ZIP + report + video URL land together |
| **Environment** | Marked on **Xcode 26.4.1 / iOS 26.4.1 / iPhone 17 Pro simulator**; UI must also work on iPhone 17 / 17 Pro / 17 Pro Max / **11-inch iPad Air**, light & dark |
| **State** | Concept settled (card game · subject **tranh Đông Hồ** · one continuous 36-card economy played as three sequential chapters, ending at the 2025 UNESCO trial). Codebase is implemented in `DaiViet/` → refer to `BUILD-01`, `DEC-01` |

---

## Invariants — never violate

**Product.** **MVVM mandatory** (Models / Views / ViewModels / persistence & data services separated — `BRIEF-03`). **SwiftUI-primary; GameKit & SpriteKit outside taught scope**, own-risk (`BRIEF-02`). **Culture must shape the mechanics** — the 6-pt rubric's Excellent test: the concept "could not be transferred to an unrelated subject without the game breaking" (`BRIEF-02`, `BRIEF-09`). **Five required views** + ≥3 distinct Game View animations + auth/profiles + CRUD + **cloud sync** + **two Week 7 industry requirements** (`BRIEF-03`–`BRIEF-05`).

**Process.** Only the assigned **private org repo** (`rmit-vietnam-computing-technologies`) — no personal/public repos, no mirrors; ZIP **must equal the final commit** (`BRIEF-07`, `BRIEF-01`). Exact deliverable names (`SourceCode/`, `Document.pdf`, `GitHub.txt`, `Youtube.txt` — `BRIEF-01`). **All 5 members appear and speak in the ≤10-min video** or that member gets zero for it (`BRIEF-06`). Commit history is assessed: regular commits from **every** member across all ~4 weeks (`BRIEF-07`). Mandatory source-file header on every file (`BRIEF-01`).

**Phase.** **The concept is settled and is not reopened**: a swipe-decision card game about **nghề làm tranh dân gian Đông Hồ**, played as one craft household across 1938–2025, won by preparation rather than by stats (`DEC-01`). Do not import Assignment 1 (`MigratoryYear`) rules: several are inverted here (A1 banned view models; A2 **requires** them; A1 forbade remote APIs; A2 **requires cloud sync**).

**Communication.** Always follow `@i-have-adhd` (`.claude/skills/i-have-adhd/SKILL.md`) and `.claude/rules/adhd-communication.mdc`: Answer in Vietnamese, keep it scannable, lead with the next action or verdict, number multi-step work, state concrete time estimates, no filler/recaps, no dash punctuation (per `.claude/rules/text-style.mdc`).

---

## Router — question → address

Read the addressed file via `view_file` **before** answering. Two to four files is a normal answer.

| Address | Target File Path | Read it when the question is about |
| --- | --- | --- |
| **BRIEF-01** | `.claude/context/brief/01-logistics-and-submission.md` | Deadline · late policy · deliverables · ZIP/filenames · file header · marking environment · learning objectives |
| **BRIEF-02** | `.claude/context/brief/02-theme-and-challenge.md` | The theme · what topic qualifies · culture-shapes-play rule · game categories · international option · SpriteKit/GameKit |
| **BRIEF-03** | `.claude/context/brief/03-architecture-and-data.md` | MVVM · registration/login/profiles · CRUD · Core Data/SwiftData/Firebase/UserDefaults · cloud sync |
| **BRIEF-04** | `.claude/context/brief/04-required-views.md` | What each of the five required views must contain |
| **BRIEF-05** | `.claude/context/brief/05-gameplay-ux-and-compatibility.md` | Levels · music/sound · splash · search/filter · device matrix · dark mode · **Week 7 industry requirements** · optional advanced features · aesthetics |
| **BRIEF-06** | `.claude/context/brief/06-report-and-video.md` | The 12 report sections, 30-page limit · every video rule |
| **BRIEF-07** | `.claude/context/brief/07-github-and-teamwork.md` | GitHub repo/invites · branch & commit expectations · README (demo account!) · PM & Technical Lead roles |
| **BRIEF-09** | `.claude/context/brief/09-rubric-and-marks.md` | Marks, rubric bands, weighting, what to prioritise |
| **DEC-01** | `.claude/context/decision/01-open-decisions.md` | What is settled (concept, subject, POV, structure, win rule, languages) and what is still open |
| **BUILD-01** | `.claude/context/build/01-current-status.md` | What exists today · urgent actions · standing obligations |
| **BUILD-02** | `.claude/context/build/02-timeline-and-runway.md` | Due-date derivation · week map · runway · proposed milestones |
| **BUILD-03** | `.claude/context/build/03-first-meeting-agenda.md` | The team meeting — agenda for open decisions |
| **REF-01** | `.claude/context/reference/01-links.md` | Any link: Canvas files, GitHub org, policy pages |
| **REF-02** | `.claude/context/reference/02-glossary.md` | An unfamiliar term |
| **the game itself** | `.claude/data-design/README.md` | Cards, stats, flags, win rules, screens, level maps in `.claude/data-design/` |

**Common bundles:** team meeting → `BUILD-03` + `DEC-01` + `BRIEF-07` · evaluate a concept → `BRIEF-02` + `BRIEF-09` + `BRIEF-03/04` · repo setup → `BRIEF-07` + `BRIEF-01` · pre-submission audit → `BRIEF-01` + `BRIEF-07` + `BRIEF-06` + `BRIEF-09`.

---

## Protocol

1. **Route, then read.** Load by address using `view_file` — do not glob or grep the KB as a first move.
2. **Never answer from memory** when a requirement, number, filename, deadline or status is involved — and never from Assignment 1 memory.
3. **Cite addresses** in answers (`per BRIEF-04…`) so claims are checkable.
4. **Never load `.claude/context/_source/`** — raw originals, fully migrated. Its `README.md` is the one exception: it is the migration map, not source text.
5. **Authority on conflict:** `brief > reality > decision > blueprint > reference`. *Reality* = `BUILD-01…03`. Answer from the higher tier **and name the stale file**.
6. **Keep the KB true.** Decision made → `DEC-01` (+`BUILD-01`). State changed → `BUILD-01`. Meeting held → `BUILD-03`. File set changed → `context-index.md` + this router.

---

## Layout

Catalog of every file + question→address lookup: `.claude/context-index.md`. The KB lives in
`.claude/context/` (`brief/` · `decision/` · `build/` · `reference/`); content authoring in
`.claude/data-design/` (design, research, schema, content, tools); the team's own notes in
`.claude/docs/self-written/`. **Never load `.claude/context/_source/`** — raw Canvas extraction,
fully migrated; its `README.md` (the migration map) is the one exception.
