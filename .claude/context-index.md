# Context Index — the full catalog

The addressable map of this project's knowledge base. **`CLAUDE.md` carries the compact router that is always loaded; this file is the detailed catalog**, consulted when routing is ambiguous, when a question spans several domains, or when you need the exact scope of a file before loading it.

- **Load by address, not by glob.** Every file has a stable ID (`BRIEF-04`). Cite addresses in answers.
- **Read the whole file once you route to it.** Files are sized so that loading one is cheap; partial reads cause wrong answers.
- **Never load `.claude/context/_source/`** — raw originals, fully migrated. See `_source/README.md`.

---

## 1 · Address table

### `brief/` — external truth · authority **brief**
_What the assignment demands. Non-negotiable. Overrules everything else on any conflict._

| ID | File | Scope |
| --- | --- | --- |
| **BRIEF-01** | `brief/01-logistics-and-submission.md` | 40% weight, team of 5, due date, late policy, learning objectives, source-file header, marking environment (Xcode 26.4.1 / iOS 26.4.1 / iPhone 17 Pro), all four deliverables, exact ZIP structure & filenames |
| **BRIEF-02** | `brief/02-theme-and-challenge.md` | "Living Heritage — Vietnam: Culture in Play", the culture-shapes-play rule, international group option, allowed game categories, inspiration areas, SpriteKit/GameKit restriction |
| **BRIEF-03** | `brief/03-architecture-and-data.md` | Mandatory MVVM separation, registration/login/logout + profiles, full CRUD, persistence options (Core Data/SwiftData, Firebase, UserDefaults), cloud sync |
| **BRIEF-04** | `brief/04-required-views.md` | The marker's checklist for the five required views — Menu, Game, Leaderboard, How To Play, Game Settings |
| **BRIEF-05** | `brief/05-gameplay-ux-and-compatibility.md` | Progression/levels, music & sound, splash screen, search/filter, device matrix (iPhone 17 family + iPad Air 11"), system light/dark, the two Week 7 industry requirements, optional advanced features, aesthetic criteria |
| **BRIEF-06** | `brief/06-report-and-video.md` | All 12 report sections, 30-page limit, and every video rule (10 min, unlisted, two parts, all members speak) |
| **BRIEF-07** | `brief/07-github-and-teamwork.md` | Assigned org repo & invitation, no-personal-repos rule, what markers examine in history, README contract (incl. demo account), pre-submission checklist, PM & Technical Lead roles |
| **BRIEF-09** | `brief/09-rubric-and-marks.md` | The 7-criterion 40-point rubric with full band descriptors, and where marks concentrate |

### `decision/` — the decision record · authority **decision**
_D1a (game category) is closed; D1b (concept) is a proposal; everything else is open._

| ID | File | Scope |
| --- | --- | --- |
| **DEC-01** | `decision/01-open-decisions.md` | D1a game category CLOSED (card game); D1b concept PROPOSED; every other decision the team must make (roles, names, stack, languages, features, logistics), each with its constraints — status as of **15 Aug 2026** |

### `build/` — execution · authority **reality**

| ID | File | Scope |
| --- | --- | --- |
| **BUILD-01** | `build/01-current-status.md` | **What exists today** (this KB + `data-storage/`), urgent time-sensitive actions (guest lecture, invites), standing obligations (commit hygiene) |
| **BUILD-02** | `build/02-timeline-and-runway.md` | Verified due date (Fri 11 Sep 2026 17:00 ICT) and its derivation, the week map (weeks 7–11), runway, and a **proposed, not decided** milestone shape |
| **BUILD-03** | `build/03-first-meeting-agenda.md` | The ready-to-run first-meeting agenda + per-member preparation, mapped to `DEC-01` items |

### `reference/` · authority **reference**

| ID | File | Scope |
| --- | --- | --- |
| **REF-01** | `reference/01-links-and-artifacts.md` | Every URL/artifact: Canvas assignment & files, GitHub org, RMIT policy pages, the saved HTML, the A1 sibling project |
| **REF-02** | `reference/02-glossary.md` | Definitions: living heritage, killer feature, MVVM, PM/TL, demo account, save-and-resume bar, etc. |

### Reserved domains (do not exist yet)

`design/` (`DES-xx`) and `data/` (`DATA-xx`) will be created **after** the team's concept decision (D1b) closes. Working material for the pending proposal lives in `data-storage/`, which is not addressable KB. Until then, no design or data questions have recorded answers — say so rather than inventing.

---

## 2 · Question → address

### About the assignment
| If the question is about… | Read |
| --- | --- |
| When is it due / late penalties / what to submit / ZIP or filenames | `BRIEF-01` |
| The file header / marking environment / Xcode or iOS versions | `BRIEF-01` |
| The theme / what topic qualifies / is this idea "cultural enough" | `BRIEF-02` (+ `BRIEF-09` §1 for the graded bar) |
| Allowed game types / SpriteKit or GameKit / scope | `BRIEF-02` |
| MVVM / login / profiles / CRUD / Firebase / persistence / sync | `BRIEF-03` |
| What a required view must contain | `BRIEF-04` |
| Music, sound, splash, search, devices, dark mode | `BRIEF-05` |
| The Week 7 guest lecture / industry requirements | `BRIEF-05` + `BUILD-01` |
| Optional advanced features | `BRIEF-05` (+ `BRIEF-09` §3 for marks) |
| Report sections, page limit, screenshots | `BRIEF-06` |
| Video rules / who must appear | `BRIEF-06` |
| GitHub repo, invitation, branches, commits, README, demo account | `BRIEF-07` |
| PM / Technical Lead / contribution assessment | `BRIEF-07` |
| Marks, rubric, weighting, what to prioritise | `BRIEF-09` |

### About decisions & status
| If the question is about… | Read |
| --- | --- |
| What has been decided / is X decided yet | `DEC-01` |
| What exists / current progress / what to do next | `BUILD-01` |
| The due date derivation / weeks / runway / schedule | `BUILD-02` |
| The first meeting / agenda / what to prepare | `BUILD-03` |
| A link or a Canvas file | `REF-01` |
| An unfamiliar term | `REF-02` |

---

## 3 · Task bundles

| Task | Load in this order |
| --- | --- |
| **Prepare/run the first team meeting** | `BUILD-03` → `DEC-01` → `BRIEF-02` → `BUILD-02` |
| **Evaluate a game concept candidate** | `BRIEF-02` → `BRIEF-09` §1 → `BRIEF-03`/`BRIEF-04` (can it carry the plumbing?) → `BUILD-02` (fits runway?) |
| **Set up the repo / first commits** | `BRIEF-07` → `BRIEF-01` (header) → `BUILD-01` |
| **Plan any feature work** (post-decision) | `BRIEF-04` + `BRIEF-03` + `BRIEF-05` → then the future `DES-xx` |
| **Write a report section** | `BRIEF-06` → the relevant domain file |
| **"Are we on track?"** | `BUILD-01` → `BUILD-02` → `DEC-01` |

---

## 4 · External artifacts — pointer only, not KB prose

| Artifact | Purpose | Summarised in |
| --- | --- | --- |
| `.claude/docs/GroupProjectCanvas.html` | The saved Canvas assignment page — ultimate source | `_source/README.md`, routed via `brief/` |
| Canvas assignment 1251174 (live) | Source of truth for updates/announcements | `REF-01` |
| `.claude/skills/` | Installed skills (context-engineering, deep-research) | — |
| `data-storage/` | Content-authoring workspace for the D1b proposal: win-condition model, JSON schema, sourced research scaffolds, templates, linter. **Not** part of the Xcode project | its own `README.md` |
| `../MigratoryYear/` | A1 sibling project — KB architecture reference only; **its rules do not apply here** | `REF-01` |

---

## 5 · Non-routable

`.claude/context/_source/` — the raw Canvas extraction. **Never load.** Fully migrated into `brief/01–09`; see `_source/README.md` for the section-by-section map.

---

## 6 · Maintaining the index

When a KB file is added, changed or removed:

1. Update its **frontmatter** (`scope`, `keys`, `related`).
2. Update **§1** (address table) and **§2** (question routing) here.
3. Update the router table in **`CLAUDE.md`** if the file set changed.
4. Update **`.claude/rules/context-map.mdc`** if routing behaviour changed.

Files whose `authority` is **reality** (`BUILD-01`, `BUILD-02`, `BUILD-03`) and the register `DEC-01` go stale fastest — after every meeting or decision, bring them current before relying on them.
