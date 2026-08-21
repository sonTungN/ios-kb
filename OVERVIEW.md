# OVERVIEW — the knowledge base behind this project

**What this is:** a pre-loaded, always-ready context system for the COSC3062/COSC3063 **Assignment 2 group project**. It exists so that any question about this assignment — a requirement, a filename, a deadline, what the team has or hasn't decided — is answered from a **recorded fact** rather than from recall.

**Who this document is for:** the team. `CLAUDE.md` is written for the agent; this explains why the KB is shaped the way it is, and how to keep it working. It was initialized on **13 Aug 2026**, before the first team meeting, so it also serves as the meeting's briefing pack (`BUILD-03`).

---

## 1 · The problem this solves

There is a real tension in "always-loaded context":

> Everything relevant should be in the agent's head **before** it reasons — but the full assignment spec is ~55 KB of dense text, and loading it on every turn burns the budget and buries the one line that matters.

Attention is finite and unevenly distributed: material in the middle of a long context is reliably under-weighted. Past a point, loading more makes an agent *less* reliable, not more informed.

**The resolution is two tiers.**

| Tier | What | Cost | Contents |
| --- | --- | --- | --- |
| **Tier 0 — always loaded** | `CLAUDE.md` | ~1 file, every turn | Identity · the invariants that must never be wrong · the router · the answering protocol |
| **Tier 1 — loaded on demand** | 15 addressed files | 1–4 files per question | Everything else |

Tier 0 is deliberately small: it holds only what is dangerous to get wrong, plus the map to everything else. This is progressive disclosure — the same **Write / Select / Compress / Isolate** strategy described in `.claude/skills/context-engineering/`, applied to the KB itself. The architecture is deliberately identical to the sibling `../MigratoryYear/` (Assignment 1) KB, so anyone familiar with one can drive the other.

---

## 2 · How it is organised

Domains chosen so that a question lands in exactly one:

```
brief/     BRIEF-01…07,09 What the assignment demands.        External. Non-negotiable.
decision/  DEC-01        What the team has (not) decided.    Today: an all-OPEN register.
build/     BUILD-01…03   Status, timeline, meeting agenda.   Changes constantly.
reference/ REF-01…02     Links and glossary.
_source/                 The raw Canvas extraction.          Never loaded.
design/ + data/          RESERVED — created once the concept decision (D1) closes.
```

The split is by **question type**, not by source document. The Canvas page is one long scroll covering logistics, theme, tech specs, report rules, GitHub rules and the rubric — seven unrelated question types; a question about the deadline should not drag in the rubric. It is now eight `brief/` files. The complete section-by-section migration map is in `_source/README.md`.

### Addresses

Every file has a stable ID — `BRIEF-04`, `DEC-01` — used for routing and cross-references instead of paths. Addresses survive renames and are short enough to cite inline (*"per `BRIEF-06`, the report caps at 30 pages excluding appendices"*), which makes claims checkable in one read.

### Frontmatter

Each file opens with machine-readable metadata (`id`, `title`, `domain`, `authority`, `scope`, `keys`, `related`, `source`). `scope` and `keys` drive routing; `related` allows a controlled hop; `source` preserves provenance back to the extraction.

---

## 3 · The authority ladder — the part that prevents confident errors

```
brief  >  reality  >  decision  >  blueprint  >  reference
```

- **brief** — what the assignment demands. If anything contradicts it, the other thing is wrong.
- **reality** — `BUILD-01…03`: what exists *right now*. Today that is "a KB and nothing else."
- **decision** — `DEC-01`: settled choices. Today it records the *absence* of choices, which is itself the fact that prevents the worst failure mode of this phase: an agent (or a teammate) confidently describing a "chosen" concept that was never chosen.
- **blueprint** — will exist once design starts (`DES-xx`, `DATA-xx`).
- **reference** — supporting material; never overrides anything.

A second ladder matters here that Assignment 1 did not have: **this KB must not inherit Assignment 1's rules.** Several are inverted — A1 forbade view models and remote APIs; A2 **mandates MVVM** and **requires cloud sync**. The kernel and `context-map.mdc` both carry this warning explicitly.

---

## 4 · What the initialization added beyond transcription

**A verified deadline (`BUILD-02`).** The page header says only "5PM Friday of week 11". The Canvas machine-readable due field (epoch `1789120800`) resolves to **Friday 11 Sep 2026, 17:00 ICT**, and cross-checks against A1's anchor (week 6 Friday = 7 Aug). The page's rendered "09/11/2026" is US date order — recorded so nobody misreads it as 9 November.

**A week map with an urgent flag (`BUILD-02`, `BUILD-01`).** Week 7 — the **guest-lecture week whose content supplies two mandatory requirements** — is the week of 10–14 Aug, i.e. *now*. Surfaced as the top urgent action.

**The open-decision register (`DEC-01`).** Twelve decisions the team must make, each with its constraints and cross-references, all marked OPEN. The register turns "what do we need to talk about?" into a checklist.

**A first-meeting agenda (`BUILD-03`).** The register, sequenced into a runnable agenda with per-member preparation.

**Noise separation (`_source/README.md`, `BRIEF-09`).** The saved Canvas page contains rubric-editor template rows and form chrome that are not assignment content; the KB names exactly what was excluded and why, so "don't cut content" stays auditable.

---

## 5 · How to use it

**Just ask.** The router does the work — "when is it due?", "what must the Leaderboard show?", "what's still undecided?" Each resolves to one or two files.

**Prepare the meeting.** *"Get me ready for the first team meeting"* → `BUILD-03` + `DEC-01` + `BRIEF-02`.

**Evaluate an idea.** *"Would a game about X qualify?"* → `BRIEF-02` + `BRIEF-09` §1 — the graded test is whether the culture generates the mechanics.

**Nudge the address if you know it.** *"Per `BRIEF-06`, outline the report skeleton"* skips routing entirely.

### The four files at the top

| File | Audience | Role |
| --- | --- | --- |
| `CLAUDE.md` | agent | **Tier 0 kernel** — always loaded. Invariants + router + protocol. Keep it small; that is its whole value. |
| `.claude/context-index.md` | agent | **Full catalog** — per-address scope, question→address lookup, task bundles. |
| `.claude/rules/context-map.mdc` | agent | **Retrieval protocol** — routing, the authority ladder, the invariants restated. `alwaysApply: true`. |
| `OVERVIEW.md` | team | This document — the rationale. |

The invariants appear in both `CLAUDE.md` and `context-map.mdc` on purpose: they are the rules whose violation costs marks, and each file may be read without the other.

---

## 6 · Keeping it true

**A knowledge base that drifts is worse than none** — it converts uncertainty into confident error. In this phase the fastest-decaying files are the register and the build files:

| After you… | Update |
| --- | --- |
| Close any decision (concept, roles, names, stack) | `DEC-01` → `BUILD-01`; seed `design/`/`data/` when design starts |
| Clone the repo / create the Xcode project / write code | `BUILD-01` |
| Hold a meeting | `BUILD-03` (retire the agenda) + `DEC-01` |
| Learn the Week 7 industry requirements | `BRIEF-05` gets a dated addendum + `DEC-01` D9 |
| Add / move / remove a KB file | frontmatter → `context-index.md` §1–2 → the `CLAUDE.md` router |

---

## 7 · Housekeeping

1. **This folder is not yet a git repository.** The assessed history will live in the **assigned team repo** (`BRIEF-07`) once the teaching team creates it. When that happens, move/copy this KB into that repo (commit history is graded from day one — `BRIEF-07`) — or `git init` here in the interim so nothing is lost.
2. **`.claude/context/_source/`** holds the raw extraction; the original HTML stays in `.claude/docs/`. Once the migration is spot-checked and the KB lives in version control, `_source/` can be deleted; the HTML should stay.
3. **The live Canvas page outranks the saved copy** — if an announcement or edit changes the assignment, re-extract and update the affected `brief/` file(s), noting the date.

---

## 8 · The shape, in one line

> **A small always-on kernel that knows what must never be wrong and where everything else lives — and 15 addressed files that are read only when a question actually touches them.**
