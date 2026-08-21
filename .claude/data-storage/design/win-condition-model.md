# Win-condition model

The mechanism that separates this game from a reskinned Reigns. Read this before writing any card.

---

## The problem it solves

A stat-threshold victory (`if army >= 60 → win`) is transferable to any theme. Rubric criterion 1
(6 pts) reserves its top band for a concept that **"could not be transferred to an unrelated subject
without the game breaking"** and where cultural knowledge **"directly generates the core gameplay
mechanic."**

So victory is not decided by stats. It is decided by **whether the player assembled the specific
historical preparations that the real victory required** — and each of those preparations **costs**
stats, so acquiring them feels like losing at the time.

That is the whole design. Everything below is bookkeeping for it.

---

## Three kinds of state

| Kind | Example | Decides victory? | Fails the run? |
| --- | --- | --- | --- |
| **Stat** — continuous, two-sided | `binh`, `dan`, `kho`, `than` | ❌ never on its own | ✅ at `<= 0` **and** at `>= 100` |
| **Preparation flag** — boolean, sticky | `tieu_tho`, `coc_bach_dang` | ✅ this is the win check | ❌ |
| **Counter** — tiered, for graded conditions | `chinh_danh: 0..3` | ✅ via threshold | ❌ |

Stats create pressure. Flags decide the ending. Keeping these separate is what stops the game
collapsing back into "make the numbers big".

### Two-sided stat failure

Reigns kills the player at **both** extremes, and that is what creates tension — you cannot simply
farm every stat upward. Map each overflow onto a real failure mode of the dynastic system:

| Stat | `<= 0` | `>= 100` |
| --- | --- | --- |
| `binh` military | no army, invasion succeeds | warlordism / kiêu binh — generals depose the throne |
| `dan` popular support | uprising | populist paralysis, court cannot levy or conscript |
| `kho` treasury | famine, no logistics | ruinous taxation feeding a bloated court |
| `than` court/mandarins | administration collapses | quyền thần — a minister eclipses the throne |

Each overflow is a **documented pattern in Vietnamese dynastic history**, not an arbitrary game-over.
Cite the pattern in the card that triggers it — that is educational content delivered through play.

---

## The victory check

Each dynasty ends in a `finalTrial`. It evaluates **flags and counters only**:

```
finalTrial:
  requireAll:      [ list of preparation flags ]
  requireAny:      [ optional alternatives ]
  requireCounter:  { counterId: minimum }
  statGate:        { statId: min }        # survival floor only, never sufficient
  insufficientAlone: [ statId, ... ]      # documented: high value here does NOT win
```

`insufficientAlone` is doing pedagogical work. It is the field that says *"raw military strength does
not defeat this enemy"* — the exact lesson the level teaches. Surface it in the defeat screen.

**Defeat text must explain the historical reason**, not just "you lost". A player who dumped
everything into `binh` and lost to the Yuan should be told that meeting the Mongols in open
conventional battle is how you lose, and what was done instead.

### The trial is the last mini-boss, and it asks two separate questions

The carriers are mini-bosses: a floor to attempt them, a cost to clear them, and failing one leaves
the run playable but no longer winnable. **The final trial is the same shape, one size up** — and it
checks two things that must not be confused:

| | Question | Field | Decides victory? |
| --- | --- | --- | --- |
| **Preparations** | Did you assemble what the real victory required? | `requireAll` | ✅ **this is the win check** |
| **Capacity** | Is there enough of a state left to fight at all? | `statGate` | ❌ floor only — never sufficient |

Holding all three flags with every stat under 10 must not be a victory. That is a court that did
every correct thing and then collapsed before it could use any of it, and counting it as a win would
say preparation is a checklist rather than something a functioning state has to *execute*.

**Trần's gate: `binh ≥ 15 · dan ≥ 15 · kho ≥ 10 · than ≥ 10`.** Every floor is deliberately low, and
`kho` lowest of all, because the level's argument is that the correct player arrives **poor**. Raise
these and the argument silently inverts into *end the game rich*, which is the opposite of what
happened. The traced demo run ends `binh 60 · dan 55 · kho 25 · than 30` — clearing by 45 / 40 / 15 / 20.

Three rules the linter enforces on the gate:

1. **No floor at or above half a stat's range.** Past that the trial is being decided by stats after
   all, which is the one thing this whole model exists to avoid.
2. **Every floor must sit below its crisis band** (`≤20` on Thường). Otherwise a player can fail the
   trial on a stat that never once triggered the rescue that would have warned them — the crisis has
   to be the first signal, always.
3. **A gate requires `defeatByExhaustionText`.** Losing *with* all the preparations in hand is a
   completely different ending from losing without them, and it is the more affecting of the two. It
   needs its own words and its own screen.

That fourth ending — **Spent** — is what the gate creates. See `user-journey.md` § *The four endings*.

---

## The cost rule — non-negotiable

> **Every choice that grants a victory flag must carry at least one negative stat effect.**

Without this the flags become a checklist to tick and the tension disappears. With it, each
preparation is a genuine dilemma at the moment it is offered — which is the dilemma the historical
court actually faced.

`tools/validate_data.py` enforces this mechanically; a dataset that violates it fails validation.

Design each carrier card so the cost lands **before** the payoff. Abandoning the capital should look
and feel like losing when the player does it. The vindication arrives only at the final trial.

---

## Floors, not thresholds — the means to act

The cost rule above says every preparation is *paid for*. It does not say every preparation is
*possible*. Those are different, and the gap between them is where the design was thin: a player who
had ground the people into famine could still order the capital emptied, because they knew the flag
was there. The court would have been ordering something it no longer had the capacity to do.

So each required flag may declare a **`statFloor`** — a minimum the stat must hold **before** the
choice, or the preparation does not land. The cost is still paid. The flag is not granted, and
`blockedText` says why, in the language of the period rather than the language of the game.

| Flag | Floor | What it means |
| --- | --- | --- |
| `long_dan` Diên Hồng | `dan ≥ 20` | The elders must still be willing to come |
| `tieu_tho` Bỏ Thăng Long | `dan ≥ 25` | You cannot order a starving city to burn itself |
| `coc_bach_dang` Cọc Bạch Đằng | `binh ≥ 25` | Stakes are wood without men on both banks |

### The number is the whole argument

> **A floor says the court needs the means to act. It must never say the court needs to be strong.**

That distinction decides whether this feature strengthens the design or destroys it, and the gap is
narrow. Take Bạch Đằng. A floor of `binh ≥ 25` and a threshold of `binh ≥ 60` look like the same
mechanism with a different constant. They are not:

- **Historically**, `60` is false. The Trần were outnumbered through all three invasions and won by
  *refusing* open battle — abandoning the capital twice to avoid it. Requiring a strong army to
  spring the Bạch Đằng trap encodes the opposite of what happened, and of what the level teaches.
- **Mechanically**, `60` breaks the level's central trap. Card 8 (`mở rộng quân đội`, `+20 binh` for
  `−20 kho`) exists to tempt the player into buying an army that the final trial ignores. Put the
  floor above the starting value of 55 and that card stops being a trap and becomes correct play —
  and the run goes back to whoever farmed `binh`, which is exactly what `insufficientAlone` exists to
  refute.
- **Pedagogically**, a floor near the middle of the range becomes the visible goal. Flags are
  abstract; numbers are legible. Whichever one the player can see is the one they will play toward.

`validate_data.py` therefore warns on any floor above **half** the stat's range, naming it a
threshold and asking for confirmation — and warns again if the floor sits above the stat's starting
value, because that silently converts the level's first act into a farming phase.

### Three rules the linter enforces

1. **`blockedText` is mandatory.** A preparation that fails silently is the cruellest thing this
   design can do — the player finds out fifteen cards later, at the trial, with no way to connect it
   to the moment it happened.
2. **Every floored required flag must have an advisor interstitial before its carrier.** A gate the
   player cannot see coming at *any* difficulty is a trap, not a challenge. Trần Quốc Tuấn saying
   *"we need men on both banks, or the stakes are only wood"* is both the warning and good writing.
   Khó suppresses advisors deliberately — that only works if there is one to suppress.
3. **A floor on a stat declared `insufficientAlone` warns, not errors.** It is coherent — necessary
   to act, not sufficient to win — but it reads as a contradiction, so the blocked text has to carry
   both halves. Hence *"wood does not fight the battle for you — and no number of men fights it
   without the wood."*

### What is still unchecked

Whether the floors are *reachable* on every path through the level cannot be verified until the 28
spine cards exist as JSON — it needs a run trace, not a static rule. That is the same gap as the
card 16 treasury gate in `../content/tran/level-map.md`, and both should be closed by the same
reachability pass. Until then the floors are validated against the traced demo run only, which clears
them by 20 / 30 / 45 points.

---

## Why this reaches backwards through the level

Because the final trial ignores stats, every mid-game card is re-evaluated by the player. The
question stops being *"does this number go up?"* and becomes *"does this build toward the way we
actually won?"*

That is how the design answers the Very Good band's ceiling — *"not sustained across the whole game
system"* — **without needing extra cards**. Same deck, payoff wired differently.

---

## Three shapes — where difficulty actually comes from

`BRIEF-05` §3 requires "levels or stages of **increasing difficulty**" that "**progressively
introduce new educational elements**". There are two ways to satisfy that, and only one of them is
worth building.

**The cheap way is numbers**: lower the starting stats, raise the costs, tighten the thresholds. It
is an afternoon's work, it teaches nothing, and in this game it is actively wrong — Level 1's whole
argument is *the historical path is affordable, but only just*. Tighten the numbers and that argument
becomes a different argument. Loosen them and it disappears.

**The real way is shape.** Each dynasty asks a different *kind* of question, so the player has to
think differently rather than merely more carefully. A new shape is genuinely a new educational
element. A lower starting stat is not. This is also where `BRIEF-09` §1's top band is won — cultural
logic visible in **how the player thinks and decides** — because the shape is the thinking.

The schema already anticipated this: `finalTrial` carries `requireAny` and `requireCounter`, both
currently unused. And the research scaffolds already describe all three shapes without being asked
to — the histories genuinely differ in kind, which is the luckiest thing about this concept.

| | **Level 1 · Trần** | **Level 2 · Lam Sơn** | **Level 3 · Lý** |
| --- | --- | --- | --- |
| Demand | **Recognise** | **Sustain** | **Reverse** |
| The question | *Which cards matter?* | *How much, how fast, and can I survive the wait?* | *When — and can I stop doing what just worked?* |
| Win rule | `requireAll` — three flags | `requireCounter` + flags | phase-gated flag + attrition counter |
| Failure feels like | arriving strong and unprepared | never quite getting there | having been right, too late |
| Source | `../content/tran/level-map.md` | `../research/02-lam-son-le-loi.md` | `../research/03-ly-thuong-kiet.md` |

### 1 · Trần — recognition

Three preparations, each on one identifiable card, each with a price. The goal is discoverable (the
ledger opens after the first flag) and once you know what to look for the difficulty is paying for
it. **Three correct decisions across twenty-eight.**

### 2 · Lam Sơn — accumulation under attrition

Not "which card" but "how much". `chinh_danh` (legitimacy) is a **counter, 0–3**, and the research
scaffold arrives at this independently: *"legitimacy accumulates… it belongs in `requireCounter`, not
`requireAll`."* The uprising ran **1418–1427**: years of losing, Lê Lai dying to buy an escape, the
1424 redirection into Nghệ An, and legitimacy earned only by winning visibly at Tốt Động – Chúc Động.

The player starts at the floor — no treasury, no army, no throne — which inverts Level 1's opening.
Roughly fifteen decisions each contribute a little, and the Ming actively take it back. **You cannot
solve this level by spotting three cards**, which is precisely why it comes second: it requires the
player to already understand that preparation beats strength, and then asks them to do it slowly,
under pressure, with a resource that can go down.

### 3 · Lý — reversal

The hardest shape, and the research names it flatly: *"an offensive phase where waiting is punished,
then a defensive phase where attacking is punished. **The player must reverse their own strategy
mid-level. No other level does this.**"*

- **Phase 1 (1075–76), `tiên phát chế nhân`.** The pre-emptive strike into Ung Châu is available for
  several cards and gets worse every card it is delayed — and the game gives the player every reason
  to wait, because striking first is expensive, aggressive, and the court hates it. Miss the window
  and it closes. The run then continues for fifteen more cards while the player slowly discovers
  they already lost.
- **Phase 2 (1077), Như Nguyệt.** Now aggression is the mistake. The line is an **earthen rampart
  with a bamboo palisade and concealed spike pits** — a fortification held for months against
  repeated assault, *not* Bạch Đằng's stakes in the riverbed. Model it as **attrition across several
  waves**, not a one-shot flag. Getting this distinction right is cheap, visible evidence of real
  research; blurring the two is the most common popular error.

**Schema gap.** Phase 1 needs something the schema does not yet have: a flag that **expires**.
Proposed minimal addition — `expiresBefore: <cardId>` on the flag declaration, meaning the carrier
choice stops granting it once that card is reached. `validate_data.py` already checks that the named
card exists and that the carrier precedes it. Everything else in this shape is expressible with
`requireCounter`, which exists.

### The ordering problem — read this before fixing the level order

Trần → Lam Sơn → Lý is **1258 → 1418 → 1075**. Not chronological, and that is a deliberate cost.

The alternative is to order by calendar (Lý → Trần → Lam Sơn) and assign shapes to fit. **Do not do
this.** The shapes are not interchangeable labels — Trần's history genuinely *is* "prepare three
specific things", Lam Sơn's genuinely *is* "accumulate legitimacy over ten years", Lý's genuinely
*is* "strike first, then hold". Forcing a different shape onto a dynasty to satisfy the calendar
breaks the exact test `BRIEF-09` §1 is scored on: that the concept could not be transferred without
the game breaking.

**So the shape follows the history, and the order follows the shape.** The campaign is three
problems, not one timeline — the dynasty-select screen should present it that way, and the report
should say so explicitly rather than let a marker notice the dates and assume carelessness.

*Level order is not yet a team decision — see `DEC-01` D13.*

---

## Authoring checklist per dynasty

1. Identify the historical victory and **how** it was actually achieved (not that it was).
2. Decompose that *how* into 3–4 preparations → these become the flags.
3. For each flag, find the real event where that preparation was decided → that card is the carrier.
4. Give each carrier a real cost, drawn from what it actually cost historically.
5. Fill the remaining slots with pressure cards that tempt the player toward the generic path
   (build the army, tax the people) so the historical path stays a real sacrifice.
6. Write the defeat text for "high stats, missing flags" — this is the most important text in the
   level, because it is where the learning lands.
