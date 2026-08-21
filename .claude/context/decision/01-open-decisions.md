---
id: DEC-01
title: Decision register — D1a closed (card game), everything else open
domain: decision
authority: decision
scope: Every decision the team must make, its constraints from the brief, and its status. As of 15 Aug 2026 the game CATEGORY is closed (card game); everything else remains OPEN, with a concept proposal in progress for D1.
keys: [decisions, open, undecided, TBD, game concept, heritage topic, app name, group name, roles, Project Manager, Technical Lead, persistence, Firebase, language, advanced features, industry requirements, tutor]
related: [BRIEF-02, BRIEF-03, BRIEF-05, BRIEF-07, BUILD-03]
source: Synthesised from the brief on 13 Aug 2026 — pre-first-meeting phase
---

# Decision register

> ⚠️ **Phase: early-decision.** As of 15 Aug 2026 exactly **one** decision has closed — the game category (D1a). Everything else is OPEN, and the concept itself (D1b) is a **proposal awaiting the next team meeting**, not a team decision. When a decision closes, record it here (status → CLOSED, with date and rationale) and update `BUILD-01`/`BUILD-03`. **Do not present anything still marked OPEN or PROPOSED as chosen.**

## D1a · Game category — ✅ CLOSED 15 Aug 2026

- **Decision: card game.** Recorded from the team as "we choose the Cards & Boards game category as our solution."
- This is an allowed category under `BRIEF-02`, so no tutor confirmation is required on category grounds.

## D1b · Heritage topic & game concept — PROPOSED, not closed

> Status: one member's proposal, circulated ahead of the next meeting, where all members bring their own game-design proposals. **Not agreed by the team.**

> ⚠️ **19 Aug 2026 — tutor feedback challenges the theme alignment of this proposal.** The concept was
> emailed to the tutor (Tom Huynh); his written reply says the focus on military/dynastic history "is
> not clearly connected to the idea of 'living heritage'" and asks that practices, traditions, crafts,
> stories or festivals "play a stronger role in the core experience" — while explicitly allowing the
> historical setting to remain part of the game. He offered to discuss it at the tutorial. Full text:
> `.claude/docs/mail/`. **D1b cannot close in its current form** — it needs a re-frame or re-subject
> agreed with the tutor first.

**Proposal in brief.** A swipe-decision card game in the manner of *Reigns: Her Majesty*. The player
rules as the court of a Vietnamese dynasty; each card is a historical situation with two choices that
move court stats. Each level is one dynasty, ending in that dynasty's greatest foreign invasion.

**Design work already done** — see `data-storage/`:

- The **win-condition model** (`data-storage/design/win-condition-model.md`). Victory is decided by
  historically-derived preparation flags, never by a stat threshold; each flag costs stats to
  acquire. This exists specifically to clear the `BRIEF-09` §1 Excellent test rather than land in the
  "heritage as factual content" band.
- **JSON schema** for cards and levels, with mandatory `sources[]` and a `historicity` field
  (documented / simplified / invented) that maps onto the three buckets `BRIEF-06` §2 requires.
- **Sourced research scaffolds** for three candidate dynasties, verification pass done 15 Aug 2026.

**Open sub-questions for the meeting:**

| | Question | Current leaning |
| --- | --- | --- |
| D1b-i | How many dynasties? | 3 — the bilingual content cost makes 4 the point where the schedule breaks (see `data-storage/README.md`) |
| D1b-ii | Which dynasties? | Trần vs Nguyên Mông · Lam Sơn / Lê Lợi · Lý / Lý Thường Kiệt — chosen for *different play patterns*, not just different eras |
| D1b-iii | Who owns which dynasty's research and content? | Unassigned — ties to D11 |

### ✅ CLOSED — building on an existing game format is the agreed approach (15 Aug 2026)

**Team decision. Settled — do not reopen or re-raise this.**

Adapting a proven format (*Reigns*-style swipe cards) rather than inventing a new one, with the
team's work going into cultural content and presentation. Team's rationale:

- Designing and shipping a genuinely novel game is out of scope for a ~4-week window alongside every
  other requirement.
- Prior high-scoring projects in this course took the same route — established game formats rebuilt,
  differentiated by how well the content is presented.

This is consistent with the brief rather than in tension with it: `BRIEF-02` sets the scope by listing
**game categories** (board / card / dice / turn-based / resource-management / puzzle / route-planning /
simulation), which presupposes working in an established genre. And the `BRIEF-09` §1 originality test
is about the **heritage-to-mechanic link** — *"could not be transferred to an unrelated subject
without the game breaking"* — not about genre novelty. The win-condition model in `data-storage/` is
what carries that test; the swipe input is deliberately conventional and costs nothing.

No tutor confirmation needed on this point: the category (card game, D1a) is explicitly listed, so the
"confirm with your tutor if your concept does not clearly fit" clause in `BRIEF-02` does not apply.

**Standing constraints** (unchanged, from the brief): living Vietnamese heritage unless the
international option applies (`BRIEF-02`); culture must generate the core mechanic, not decorate it
(`BRIEF-02`, `BRIEF-09` §1); achievable in ~4 weeks on SwiftUI-primary tech (`BRIEF-02`); backed by
genuine reportable research (`BRIEF-06` §2).

⚠️ **Accuracy is a self-imposed hard requirement here.** The team's stated position is that the
historical events must be correct and correctly sequenced, with only their *consequences* branching
on player choice. The schema enforces this: `historicalNote` is identical after either choice.

## D2 · International group option — OPEN (likely N/A)

- Only available if the **majority of members are not Vietnamese** (`BRIEF-02`). Confirm team composition at the first meeting; if majority-Vietnamese, this closes automatically as "Vietnamese heritage".

## D3 · Project Manager — OPEN

- Mandatory role: plans/controls tasks, chairs meetings, team spirit; finalises the Project Responsibilities table (`BRIEF-07`, `BRIEF-06` §11).

## D4 · Technical Lead — OPEN

- Mandatory role: major technical decisions; **gatekeeper of the default branch** (`BRIEF-07`).

## D5 · Group name — OPEN

- Appears in the repo name and ZIP filename (`BRIEF-01`, `BRIEF-07`). Needed before/when the teaching team creates the repo.

## D6 · App name (and slogan, if any) — OPEN

- Appears in ZIP name and folder structure (`BRIEF-01`).

## D7 · Persistence & sync stack — OPEN

- Must implement full CRUD + cloud sync; choose **one or more** of Core Data (or SwiftData) / Firebase / UserDefaults and a cloud service (like Firebase), **justifying which data lives where** in the report (`BRIEF-03`, `BRIEF-06` §4). Config file (e.g. `GoogleService-Info.plist`) must be committed (`BRIEF-01`).

## D8 · Second language for multi-language support — OPEN (leaning Vietnamese)

- At least English + one other (e.g., Vietnamese) via picker/dropdown (`BRIEF-04` §5).
- The D1b card schema already assumes **vi + en** on every string, and the content-cost estimate in `data-storage/README.md` is built on it. Closing this as Vietnamese would simply confirm current practice; closing it as anything else would double the content work already scoped.

## D9 · The two Week 7 industry requirements — OPEN (blocked on attending the guest lecture)

- Two industry requirements from the Week 7 Guest Lecture must be implemented and discussed with evidence in the report (`BRIEF-05` §5, `BRIEF-06` §5). Cannot be chosen until the lecture content is known — sign-up is urgent (`BUILD-01`).

## D10 · Optional advanced features to attempt — OPEN

- Menu: AI opponent · local notifications · accessibility (VoiceOver, dynamic type, contrast) · save-and-resume surviving full app kill (`BRIEF-05` §6). Worth 6/40 marks (`BRIEF-09` §3) — decide how many the schedule can absorb.

## D11 · Task breakdown & workload split — OPEN

- Needed for the Project Responsibilities table: actual responsibilities + workload % per member, **totalling 100%**, agreed by the whole team, finalised by the PM (`BRIEF-06` §11). Regular commits from **every** member are assessed (`BRIEF-07`).

## D12 · Team logistics — OPEN

- Meeting cadence, communication channel, task board, branch/PR conventions (subject to the Tech Lead's gatekeeping).

## D13 · How much a run varies between playthroughs — OPEN (raised 16 Aug 2026)

**The question.** Does a second playthrough of the same level present the same sequence? Until 16 Aug
the answer was yes — one fixed order of dated cards, with only the player's choices differing.

**Not a rubric line.** Nothing in `BRIEF-05` or `BRIEF-09` marks replay value, and a marker very
likely plays once. Treat this as a game-quality decision, not a marks decision, and weigh it against
the content budget accordingly.

**The principle proposed, and now built into `data-storage/` as illustration:** *history fixes when
the great events happen; it does not fix what an ordinary year looked like.* The deck splits on that
line — a **spine** of dated cards that never moves, and a **weave** of undated court business drawn
fresh each run. This does not weaken the accuracy rule under D1b, it states it precisely: an undated
card is required to carry `year: null`, may never carry a required victory flag, and may never be
tagged `documented`. `validate_data.py` enforces all three, plus a **solvency invariant** — no legal
draw may change whether the level can be won, only how it feels and what it costs.

**Also relevant:** genuine variety *between* levels is a different and better-marked thing —
`BRIEF-05` §3 requires "levels or stages of increasing difficulty" that "progressively introduce new
educational elements". The card schema already supports it (`finalTrial` has unused `requireAny` and
`requireCounter` fields), so each dynasty can have a different *shape* of win condition rather than
different numbers. Currently only Trần's flag-based shape is designed.

**Open for the team:**

| | Question | Current leaning |
| --- | --- | --- |
| D13-i | Adopt the spine/weave split at all? | Yes — the accuracy rule survives intact and it is the only source of run-to-run variety in the decisions |
| D13-ii | How deep a weave pool per level? | 12 for Trần as built (≈144 strings). Incremental — shippable smaller, extended later |
| D13-iii | What does Dễ/Thường/Khó change? | **Information and slack, never numbers** — built as `content/game.json`, see below |
| D13-iv | Different starting court composition (tông thất / tướng lĩnh / văn quan)? | Worth it — zero new cards, only a different `start` vector, and historically grounded. **Not yet built** |
| D13-v | Give levels 2 and 3 genuinely different win-condition **shapes**? | Yes — and the research already describes them, see below |
| D13-vi | **Level order: by difficulty or by calendar?** | By difficulty (Trần → Lam Sơn → Lý = 1258 → 1418 → 1075). Reasoning in `data-storage/design/win-condition-model.md` § *The ordering problem* — the shape must follow the history, so the order follows the shape. **This is a real cost and needs an explicit team decision**, plus a line in the report so a marker does not read the dates as carelessness |

### Two axes of difficulty — they must do different jobs

The distinction is now built and machine-checked; what is open is whether the team accepts it.

**Across dynasties = progression.** Required by `BRIEF-05` §3 ("increasing difficulty… progressively
introduce new educational elements"). It comes from the **shape of the win condition**, never from
harsher numbers — a new shape is genuinely a new educational element; a lower starting stat is not.
The three shapes fall out of the research rather than being imposed on it: **Trần = recognise**
(`requireAll`, three flags) · **Lam Sơn = sustain** (`requireCounter`, legitimacy accumulated over
ten years while the Ming take it back) · **Lý = reverse** (strike first or lose the window, then hold
a line where attacking is the mistake — `research/03` calls this out unprompted as the one level
where the player must reverse their own strategy mid-way).

**Inside a dynasty = accommodation.** The player-facing Dễ/Thường/Khó control changes **only how much
the game tells you and how much slack it leaves**: crisis warning bands, when the preparation ledger
opens, whether advisors appear, how many ambient beats fire. It never touches a starting stat, a
choice cost, a flag or the victory rule — so a Khó win and a Dễ win mean the same thing, and the
leaderboard stays comparable. **Khó is not a bigger bill; it is playing without hindsight.**
`validate_data.py` rejects any difficulty entry that reaches outside the permitted dials.

⚠️ **Cost.** The weave and the deeper ambient pool add ≈164 bilingual strings to Level 1, taking it
from ≈340 to ≈504 — a ~48% increase on the largest single piece of work in the project, against an
11 Sep deadline. **D13-iii costs nothing and is built. D13-iv costs nothing and is not.** D13-v is
design work, not content work, and it is what `BRIEF-05` §3 is actually asking for. **Decide D13-ii
last, and treat it as the dial that absorbs whatever schedule is left.**

---

**Nothing else is closed.** There is **no code**. A data schema, a win-condition model, a full 28-card level structure for the Trần, and a 30-screen UI mock-up in Google Stitch now exist — but all of it belongs to the *pending* D1b proposal and is **not KB truth**. The addressable `DES-xx` and `DATA-xx` domains are created only once D1b closes. Until then, treat the mock-up as one member's illustration of the proposal, not as the team's agreed design: if the meeting picks a different concept, it is thrown away.

⚠️ **Placeholder names in the mock-up.** Screens 1 and 2 carry the auto-generated wordmark "ĐẠI VIỆT CHRONICLES". That is **not** an app-name decision — D6 below is open, and whatever the team picks replaces it.
