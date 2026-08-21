# GroupProject (Assignment 2) — project kernel

**This file is always in context. Everything else is loaded on demand, by address.**
Detailed catalog: `.claude/context-index.md` · Retrieval protocol: `.claude/rules/context-map.mdc` · KB rationale: `OVERVIEW.md`

---

## Identity

| | |
| --- | --- |
| **Project** | An **educational iOS game** on the theme **"Living Heritage — Vietnam: Culture in Play"** — cultural heritage embedded in the game mechanics, not as decoration |
| **Assignment** | COSC3062 / COSC3063 iPhone Software Engineering — **Assignment 2 (Group Project)**, Semester 2026B, **team of 5**, **40%** of the course |
| **Deadline** | **Friday 11 Sep 2026, 17:00** (Vietnam time) — "5PM Friday of week 11", verified against Canvas metadata (`BUILD-02`). ZIP + report + video URL land together |
| **Environment** | Marked on **Xcode 26.4.1 / iOS 26.4.1 / iPhone 17 Pro simulator**; UI must also work on iPhone 17 / 17 Pro / 17 Pro Max / **11-inch iPad Air**, light & dark |
| **State** | **Early-decision.** KB initialized 13 Aug 2026. Game category closed (card game, 15 Aug); concept is a proposal pending the next meeting. No repo, no code → `BUILD-01`, `DEC-01` |

---

## Invariants — never violate

**Product.** **MVVM mandatory** (Models / Views / ViewModels / persistence & data services separated — `BRIEF-03`). **SwiftUI-primary; GameKit & SpriteKit outside taught scope**, own-risk (`BRIEF-02`). **Culture must shape the mechanics** — the 6-pt rubric's Excellent test: the concept "could not be transferred to an unrelated subject without the game breaking" (`BRIEF-02`, `BRIEF-09`). **Five required views** + ≥3 distinct Game View animations + auth/profiles + CRUD + **cloud sync** + **two Week 7 industry requirements** (`BRIEF-03`–`BRIEF-05`).

**Process.** Only the assigned **private org repo** (`rmit-vietnam-computing-technologies`) — no personal/public repos, no mirrors; ZIP **must equal the final commit** (`BRIEF-07`, `BRIEF-01`). Exact deliverable names (`SourceCode/`, `Document.pdf`, `GitHub.txt`, `Youtube.txt` — `BRIEF-01`). **All 5 members appear and speak in the ≤10-min video** or that member gets zero for it (`BRIEF-06`). Commit history is assessed: regular commits from **every** member across all ~4 weeks (`BRIEF-07`). Mandatory source-file header on every file (`BRIEF-01`).

**Phase.** **Only the game category is decided** — card game (`DEC-01` D1a, 15 Aug 2026). The concept, dynasties, names, roles and stack are all still open; D1b is a proposal awaiting the team meeting. Do not present anything else as chosen; do not import Assignment 1 (`MigratoryYear`) rules — several are inverted here (A1 banned view models; A2 **requires** them).

---

## Router — question → address

Read the addressed file **before** answering. Two to four files is a normal answer.

| Address | Read it when the question is about |
| --- | --- |
| **BRIEF-01** | Deadline · late policy · deliverables · ZIP/filenames · file header · marking environment · learning objectives |
| **BRIEF-02** | The theme · what topic qualifies · culture-shapes-play rule · game categories · international option · SpriteKit/GameKit |
| **BRIEF-03** | MVVM · registration/login/profiles · CRUD · Core Data/SwiftData/Firebase/UserDefaults · cloud sync |
| **BRIEF-04** | What each of the five required views must contain |
| **BRIEF-05** | Levels · music/sound · splash · search/filter · device matrix · dark mode · **Week 7 industry requirements** · optional advanced features · aesthetics |
| **BRIEF-06** | The 12 report sections, 30-page limit · every video rule |
| **BRIEF-07** | GitHub repo/invites · branch & commit expectations · README (demo account!) · PM & Technical Lead roles |
| **BRIEF-09** | Marks, rubric bands, weighting, what to prioritise |
| **DEC-01** | What is (not) decided — the open-decision register D1–D12 |
| **BUILD-01** | What exists today · urgent actions · standing obligations |
| **BUILD-02** | Due-date derivation · week map · runway · proposed milestones |
| **BUILD-03** | The first team meeting — agenda & preparation |
| **REF-01** | Any link: Canvas files, GitHub org, policy pages |
| **REF-02** | An unfamiliar term |

**Common bundles:** first meeting → `BUILD-03` + `DEC-01` + `BRIEF-02` · evaluate a concept → `BRIEF-02` + `BRIEF-09` + `BRIEF-03/04` · repo setup → `BRIEF-07` + `BRIEF-01` · pre-submission audit → `BRIEF-01` + `BRIEF-07` + `BRIEF-06` + `BRIEF-09`.

---

## Protocol

1. **Route, then read.** Load by address — do not glob or grep the KB as a first move.
2. **Never answer from memory** when a requirement, number, filename, deadline or status is involved — and never from Assignment 1 memory.
3. **Cite addresses** in answers (`per BRIEF-04…`) so claims are checkable.
4. **Never load `.claude/context/_source/`** — raw originals, fully migrated.
5. **Authority on conflict:** `brief > reality > decision > blueprint > reference`. *Reality* = `BUILD-01…03`. Answer from the higher tier **and name the stale file**.
6. **Keep the KB true.** Decision made → `DEC-01` (+`BUILD-01`). State changed → `BUILD-01`. Meeting held → `BUILD-03`. File set changed → `context-index.md` + this router.

---

## Layout

```
CLAUDE.md                     ← this kernel (always loaded)
OVERVIEW.md                   ← why the KB is built this way
.claude/
  context-index.md            ← full catalog + question→address + task bundles
  rules/context-map.mdc       ← retrieval protocol (alwaysApply)
  context/
    brief/     BRIEF-01…07,09 external truth — what the assignment demands
    decision/  DEC-01         decision register (D1a closed; rest open)
    build/     BUILD-01…03    status, timeline, first-meeting agenda
    reference/ REF-01…02      links, glossary
    _source/                  raw Canvas extraction — DO NOT LOAD
    (design/ + data/ reserved — created after the concept decision closes)
  docs/GroupProjectCanvas.html← the saved Canvas assignment page (source)
  skills/                     context-engineering, deep-research
data-storage/                 ← content authoring: schema, research, templates, linter
```
