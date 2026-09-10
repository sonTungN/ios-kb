---
id: DEC-01
title: Decision register — what the project is, and what is still open
domain: decision
authority: decision
scope: Every decision the team must make. Settled ones are stated as facts about the project; open ones are listed with their constraints. How a decision was reached is not recorded here — it lives in the artefact the decision produced.
keys: [decisions, decided, open, undecided, TBD, game concept, heritage topic, Đông Hồ, app name, group name, roles, Project Manager, Technical Lead, persistence, Firebase, language, advanced features, industry requirements, POV, structure, minigames]
related: [BRIEF-02, BRIEF-03, BRIEF-05, BRIEF-07, BUILD-01]
source: Maintained by the team; consolidated 22 Aug 2026
---

# Decision register

> **Settled items are statements of what the project *is*.** They are not proposals and not up for
> re-argument; build against them. **Open items still need a team decision** — never present one as
> chosen. When an open item closes, move it up into *Settled* as a one-line statement and update
> `BUILD-01`.

---

## Settled

### D1a · Game category

**A card game** — swipe-decision cards in the *Reigns* format. An established format rebuilt; the
team's own work goes into the cultural content and its presentation, not into inventing a genre.
This is an allowed category under `BRIEF-02`, so no tutor confirmation is required on category
grounds.

### D1b · Heritage subject

**Nghề làm tranh dân gian Đông Hồ** — Đông Hồ folk woodcut painting, Vietnamese living heritage.
The craft's practices, knowledge and transmission generate the game's mechanics; the historical
setting is the pressure around them, never the subject.

Research base: `.claude/data-design/research/01-dong-ho-tranh-dan-gian.md` (sourced, statuses per claim).
Design: `.claude/data-design/design/dongho-game-design.md`.

### D1b-POV · Who the player is

**One craft household across the generations** — a *fictional composite* among the 17 dòng họ of the
village. The làng nghề is the world around the household, not the seat the player sits in. Real
artisans appear only where the record puts them (`historicalNote`, card anchors, the codex); the
game never puts counterfactual words in a living person's mouth.

### D1b-CS · Structure

**One continuous economy, 1938 → 9 Dec 2025, played as three sequential chapters** — *Giữ lửa*
(cards 1–12) · *Giữ nếp* (13–22) · *Hồi sinh* (23–36). The chapters are playable **levels**
(`BRIEF-05` §3 met on the "levels" reading directly): a chapter unlocks when the previous one is
finished, opens on its era screen, and ends on a summary/lesson screen; the Final Trial closes
chapter III. **Stats, flags, ticks and spent crises persist across chapters — nothing resets**, so
the 36-card reachability and solvency proofs remain valid unchanged. Each chapter entry writes a
**checkpoint** {stats, flags, ticks, spent crises, weave seen}; Save & Exit / Resume / Restart act
per chapter; restarting an earlier chapter reloads its checkpoint, **locks every later chapter**
(their entry states are now invalid) and deals a **fresh seed**. Each chapter declares at least one
required objective: C1 `giu_van` + `giu_bi_quyet` · C2 **ticks 2–3 of `truyen_thua`** (the
transmission chapter's requirement is the transmission counter — no data change) · C3
`phuc_hoi_van` + `truyen_nhan` + `ho_so`. Gốm and Quan họ stay "sắp ra mắt" menu tiles with **zero
content**.

Map: `.claude/data-design/content/dongho/level-map.md` · data: `content/dongho/game_contents.json` ·
reachability machine-checked by `.claude/data-design/tools/trace_run.py`.

### D1b-WIN · How the game is won

**Preparation decides victory; stats never do.** One Final Trial — the UNESCO inscription of
9 Dec 2025 — reads `requireAll` (bí quyết · truyền nhân · hồ sơ) + `requireAny` (giữ ván **or**
chuộc ván) + `requireCounter` (truyền thừa ≥ 2) over a low `statGate` floor, with `sinh_ke`
declared `insufficientAlone`. Every preparation costs stats to acquire and may declare a `statFloor`
— the means to act, never a threshold to farm. Model: `.claude/data-design/design/win-condition-model.md`.

### D1b-MG · Minigames

**Three engines, four placements — one per chapter plus an optional reprise:** `mg_match` (nối
tranh ↔ nghĩa, 4 graded pairs) at `giu_bi_quyet` (C1, card 9) · **`mg_sequence`** (kéo 5 lớp màu
vào đúng trình tự in — màu trước, nét đen sau cùng; a reorderable list, the cheapest build in the
set) at `giu_mau_co` (C2, card 18) · `mg_assemble` (ghép ván 3×3) at `truyen_nhan` (C3, card 30) ·
`mg_match` reprised with material↔pigment pairs (than lá tre→đen, vỏ điệp→trắng, hoa hòe→vàng, lá
chàm→xanh, sỏi son→đỏ — zero new code) at `mo_cua` (C3, card 27, optional). A minigame is the
*ritual* of a carrier flag, never an extra gate: the floor still gates the attempt, the cost is
still paid, and it is retryable until completed at every difficulty.

### D13 · Accuracy, run variety, and the two axes of difficulty

**Spine and weave.** History fixes *when* the great events happened, not what an ordinary year
looked like. Dated spine cards never move, never shuffle, and carry the required flags; drawn weave
cards must carry `year: null`, may never carry a required flag, and may never be tagged
`documented`. `historicalNote` is identical after either choice — the player's counterfactual never
overwrites the record. A **solvency invariant** guarantees no legal draw changes whether the run can
be won, only how it feels and what it costs. All of it is enforced by
`.claude/data-design/tools/validate_data.py`.

**Two axes, different jobs.** *Across chapters* = progression: it comes from the shape of the
problem (recognise → sustain → reverse) and the danger profile (floors → the trap era → ceilings),
never from harsher numbers. *Inside the run* = accommodation: the **Dễ/Thường/Khó/Cực khó** control
changes only **how much the game tells you and how much slack it leaves** (crisis bands, ledger
scope, advisors, ambient count, minigame hints). It never touches a starting stat, a cost, a flag or
the victory rule. **Difficulty is re-selectable mid-playthrough** and applies immediately (an alert
confirms) — safe precisely because no dial touches a number; the **leaderboard records the lowest
difficulty used** at any point, so the tag keeps meaning something. **Ledger is a scope dial**: Dễ =
one big ledger open anytime · Thường/Khó = three per-chapter ledgers · Cực khó = Khó with no ledger
at all (the flag split across chapters plus persistent stats is what makes Khó hard; taking the
ledger too is Cực khó's job). Declared in `.claude/data-design/content/game.json` and
machine-enforced.

### D2 · Heritage context

**Vietnamese.** The international option (`BRIEF-02`) requires a majority of non-Vietnamese members
and does not apply.

### D8 · Languages

**Vietnamese + English**, on every user-facing string, switchable in Game Settings (`BRIEF-04` §5).
The card schema requires both on every field and the whole content budget is built on it.

---

## Open

| | Decision | What it needs / constrains |
| --- | --- | --- |
| **D3** | **Project Manager** | Mandatory role: plans and controls tasks, chairs meetings, owns the Project Responsibilities table (`BRIEF-07`, `BRIEF-06` §11) |
| **D4** | **Technical Lead** | Mandatory role: major technical decisions, **gatekeeper of the default branch** (`BRIEF-07`) |
| **D5** | **Group name** | Appears in the repo name and the ZIP filename — needed when the teaching team creates the repo (`BRIEF-01`, `BRIEF-07`) |
| **D6** | **App name** (and slogan) | Appears in the ZIP name and folder structure (`BRIEF-01`). The Stitch mock-up's auto-generated wordmark is a placeholder, not a choice |
| **D7** | **Persistence & sync stack** | Full CRUD + cloud sync required. **Firebase is the working assumption for auth and cloud sync** (it is a live task on the board); the local store (SwiftData / Core Data / UserDefaults) and the split between them are still open, and the report must justify what lives where (`BRIEF-03`, `BRIEF-06` §4). `GoogleService-Info.plist` must be committed (`BRIEF-01`) |
| **D9** | **The two Week 7 industry requirements** | Two requirements from the guest lecture must be implemented and evidenced in the report (`BRIEF-05` §5, `BRIEF-06` §5). Blocked on the lecture content |
| **D10** | **Optional advanced features** | Worth 6/40 (`BRIEF-09` §3). **Save-and-resume is already designed in** (the run is long enough to need it); AI opponent · local notifications · accessibility (VoiceOver, dynamic type, contrast) are the remaining menu (`BRIEF-05` §6) — decide how many the schedule absorbs |
| **D11** | **Task breakdown & workload split** | Responsibilities + workload % per member totalling 100%, agreed by the team, finalised by the PM (`BRIEF-06` §11). Regular commits from **every** member are assessed (`BRIEF-07`) |
| **D12** | **Team logistics** | Meeting cadence, communication channel, branch/PR conventions (subject to the Tech Lead's gatekeeping). The task board is Trello — *IOS Group Project* |

---

**Still true: there is no code.** What exists is a knowledge base, a researched and machine-checked
content design, and a UI mock-up. The addressable `DES-xx` / `DATA-xx` domains are created when the
SwiftUI build begins; until then design questions are answered from `.claude/data-design/`, which is
working material rather than KB truth.
