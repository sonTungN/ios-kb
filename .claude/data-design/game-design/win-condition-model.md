# Win-condition model

The mechanism that separates this game from a reskinned Reigns. Read this before writing any card.

---

## The problem it solves

A stat-threshold victory (`if standing >= 60 → win`) is transferable to any theme. Rubric criterion 1
(6 pts) reserves its top band for a concept that **"could not be transferred to an unrelated subject
without the game breaking"** and where cultural knowledge **"directly generates the core gameplay
mechanic."**

So victory is not decided by stats. It is decided by **whether the player assembled the specific
things the craft's survival actually required** — and each of those preparations **costs** stats, so
acquiring them feels like losing at the time.

That is the whole design. Everything below is bookkeeping for it.

---

## Three kinds of state

| Kind | Example | Decides victory? | Fails the run? |
| --- | --- | --- | --- |
| **Stat** — continuous, two-sided | `nghe`, `sinh_ke`, `tieng`, `nguoi` | ❌ never on its own | ✅ at `<= 0` **and** at `>= 100` |
| **Preparation flag** — boolean, sticky¹ | `giu_van`, `truyen_nhan`, `ho_so` | ✅ this is the win check | ❌ |
| **Counter** — tiered, for graded conditions | `truyen_thua: 0..3` | ✅ via threshold | ❌ |

Stats create pressure. Flags decide the ending. Keeping these separate is what stops the game
collapsing back into "make the numbers big".

¹ *Sticky* means no ordinary card takes a granted flag away. The one exception is a **trap** choice
that explicitly `revokes` it (schema `choice.revokes`) — used twice in the shipped run: the dealer
who buys the rescued woodblocks, and the 1990 switch to votive paper, both of which visibly un-fill
a ledger slot. A revoke outside a trap is a design error.

### Two-sided stat failure

Reigns kills the player at **both** extremes, and that is what creates tension — you cannot simply
farm every stat upward. Map each overflow onto a real failure mode of the craft:

| Stat | `<= 0` | `>= 100` |
| --- | --- | --- |
| `nghe` craft | the technique is lost; the sheet stops being a Đông Hồ print | purism freezes it out of daily life — a glass-case relic |
| `sinh_ke` livelihood | the household quits for wage work | the side trade out-earns the craft and eats the workshop |
| `tieng` standing | nobody remembers the house makes prints | fame outruns the hand: rushed printing, fakes under the village name |
| `nguoi` people | no one left to receive the craft | many hands, thin standards — practice without commitment |

**This is the syllabus, not decoration.** Living heritage dies of neglect *and* of
commodification; a player who discovers that farming `tieng` to 100 kills the craft as surely as
letting it hit 0 has learned the central problem of heritage preservation. Cite the pattern in the
card that triggers it — that is educational content delivered through play.

---

## The victory check

The level ends in a `finalTrial`. It evaluates **flags and counters only**:

```
finalTrial:
  requireAll:      [ preparations that must all be held ]
  requireAny:      [ alternatives — one of the set suffices ]
  requireCounter:  { counterId: minimum }
  statGate:        { statId: min }        # survival floor only, never sufficient
  insufficientAlone: [ statId, ... ]      # documented: high value here does NOT win
```

`insufficientAlone` is doing pedagogical work. It is the field that says *"money did not decide
this"* — the exact lesson the level teaches. Surface it in the defeat screen.

**Defeat text must explain the documented reason**, not just "you lost". A player who ran a
profitable workshop and arrived without blocks, without an heir and without a dossier should be told
that what was being judged was transmission, and what the surviving households actually did.

### The trial asks two separate questions

The carriers are mini-bosses: a floor to attempt them, a cost to clear them, and failing one leaves
the run playable but no longer winnable. **The final trial is the same shape, one size up** — and it
checks two things that must not be confused:

| | Question | Field | Decides victory? |
| --- | --- | --- | --- |
| **Preparations** | Did you assemble what survival actually required? | `requireAll` · `requireAny` · `requireCounter` | ✅ **this is the win check** |
| **Capacity** | Is there a household left to act at all? | `statGate` | ❌ floor only — never sufficient |

Holding every preparation with every stat under 10 must not be a victory. That is a household that
did every correct thing and then collapsed before it could use any of it, and counting it as a win
would say preparation is a checklist rather than something a living practice has to *sustain*.

**The shipped gate: `nghe ≥ 15 · sinh_ke ≥ 10 · tieng ≥ 10 · nguoi ≥ 15`.** Every floor is
deliberately low, and `sinh_ke` lowest of all, because the level's argument is that the correct
player arrives **poor**. Raise these and the argument silently inverts into *end the game rich*,
which is the opposite of what happened.

Three rules the linter applies to the gate — **two as warnings, one as an error**, because only
the third can be judged without knowing the subject:

1. **No floor at or above half a stat's range** (warning). Past that the trial is being decided by stats after
   all, which is the one thing this whole model exists to avoid.
2. **Every floor must sit below its crisis band** (`≤20` on Thường) — warning. Otherwise a player can fail the
   trial on a stat that never once triggered the rescue that would have warned them — the crisis has
   to be the first signal, always.
3. **A gate requires `defeatByExhaustionText`** — this one is an **error**. Losing *with* all the preparations in hand is a
   completely different ending from losing without them, and it is the more affecting of the two. It
   needs its own words and its own screen.

That fourth ending — **Kiệt sức / Spent** — is what the gate creates. See `user-journey.md`
§ *The four endings*.

---

## The cost rule — non-negotiable

> **Every choice that grants a victory flag must carry at least one negative stat effect.**

Without this the flags become a checklist to tick and the tension disappears. With it, each
preparation is a genuine dilemma at the moment it is offered — which is the dilemma the household
actually faced.

`tools/validate_data.py` enforces this mechanically; a dataset that violates it fails validation.

Design each carrier so the cost lands **before** the payoff. Carrying woodblocks out of a burning
village instead of sellable goods should look and feel like losing when the player does it. The
vindication arrives only at the final trial.

---

## Floors, not thresholds — the means to act

The cost rule says every preparation is *paid for*. It does not say every preparation is
*possible*. Those are different, and the gap between them is where a design goes thin: a household
that had scattered its people could still "decide" to carry the blocks, because the player knew the
flag was there — when it no longer had the hands to do it.

So each flag may declare a **`statFloor`** — a minimum the stat must hold **before** the choice, or
the preparation does not land. The cost is still paid. The flag is not granted, and `blockedText`
says why, in the language of the period rather than the language of the game.

| Flag | Floor | What it means |
| --- | --- | --- |
| `giu_van` blocks through the fire | `nguoi ≥ 20` | Blocks are heavy; without hands they burn with the house |
| `giu_bi_quyet` the recipe taught | `nghe ≥ 25` | You cannot teach what you no longer hold |
| `phuc_hoi_van` blocks bought back | `sinh_ke ≥ 20` | You cannot buy back with nothing |
| `truyen_nhan` an heir takes it | `nguoi ≥ 20` | A lineage of one has no one to receive |
| `ho_so` the dossier | `tieng ≥ 25` | A craft nobody has heard of persuades nobody |
| `giu_mau_co` the classics archived *(optional)* | `nghe ≥ 25` | You cannot copy down what you can no longer read |
| `mo_cua` the workshop opened *(optional)* | `tieng ≥ 20` | Nobody travels to a village they have never heard of |

All seven carriers are floored — the two optional ones included, because an optional preparation
still has to be earned.

### The number is the whole argument

> **A floor says the household needs the means to act. It must never say the household needs to be
> strong.**

That distinction decides whether the feature strengthens the design or destroys it, and the gap is
narrow. Take the buy-backs. A floor of `sinh_ke ≥ 20` and a threshold of `sinh_ke ≥ 60` look like the
same mechanism with a different constant. They are not:

- **Historically**, `60` is false. The households that bought the blocks back were not rich; they
  spent savings on wood everyone else had written off.
- **Mechanically**, `60` breaks the level's traps. The votive-paper switch exists to tempt the
  player into money the final trial ignores. Put a floor above what a careful run holds and that
  trap becomes correct play — and the run goes back to whoever farmed `sinh_ke`, which is exactly
  what `insufficientAlone` exists to refute.
- **Pedagogically**, a floor near the middle of the range becomes the visible goal. Flags are
  abstract; numbers are legible. Whichever one the player can see is the one they will play toward.

`validate_data.py` therefore warns on any floor above **half** the stat's range, naming it a
threshold and asking for confirmation — and warns again if the floor sits above the stat's starting
value, because that silently converts the run's first act into a farming phase.

### Three rules the linter enforces

1. **`blockedText` is mandatory.** A preparation that fails silently is the cruellest thing this
   design can do — the player finds out twenty cards later, at the trial, with no way to connect it
   to the moment it happened.
2. **Every floored required flag must have an advisor interstitial before its carrier.** A gate the
   player cannot see coming at *any* difficulty is a trap, not a challenge. The guild head saying
   *"ván nặng thì gạo nhẹ — chọn lấy một gánh"* is both the warning and good writing. Khó suppresses
   advisors deliberately — that only works if there is one to suppress.
3. **A floor on a stat declared `insufficientAlone` warns, not errors.** It is coherent — necessary
   to act, not sufficient to win — but it reads as a contradiction, so the blocked text has to carry
   both halves.

### Flags that expire

A preparation with a real deadline declares **`expiresBefore: <cardId>`**: the carrier choice stops
granting it once that card is reached. This closes the grant window only — **a flag already held is
never removed**. The shipped use is the UNESCO dossier: the window opens in 2017, the deadline is
31 Mar 2020, and after it the chance is gone. `validate_data.py` checks that the named card exists
and that the carrier precedes it.

---

## Why this reaches backwards through the run

Because the final trial ignores stats, every mid-game card is re-evaluated by the player. The
question stops being *"does this number go up?"* and becomes *"does this build toward what actually
survived?"*

That is how the design answers the Very Good band's ceiling — *"not sustained across the whole game
system"* — **without needing extra cards**. Same deck, payoff wired differently.

---

## Where difficulty actually comes from

`BRIEF-05` §3 requires "levels or stages of **increasing difficulty**" that "**progressively
introduce new educational elements**". There are two ways to satisfy that, and only one is worth
building.

**The cheap way is numbers**: lower the starting stats, raise the costs, tighten the thresholds. It
is an afternoon's work, it teaches nothing, and here it is actively wrong — the run's argument is
*the historical path is affordable, but only just*. Tighten the numbers and that argument becomes a
different argument. Loosen them and it disappears.

**The real way is shape.** Each chapter asks a different *kind* of question, so the player has to
think differently rather than merely more carefully. A new shape is genuinely a new educational
element. A lower starting stat is not. This is also where `BRIEF-09` §1's top band is won — cultural
logic visible in **how the player thinks and decides** — because the shape is the thinking.

| | **Chương I · Giữ lửa** | **Chương II · Giữ nếp** | **Chương III · Hồi sinh** |
| --- | --- | --- | --- |
| Demand | **Recognise** | **Sustain** | **Reverse** |
| The question | *Which things must not burn?* | *Can transmission outlast the institution carrying it?* | *Can you stop doing what saved you?* |
| Win mechanism it feeds | `requireAll` · `requireAny` | `requireCounter` | the expiring flag |
| Danger profile | floors — poverty, dispersal | the trap era — the switch that pays | **ceilings** — fame, commodification |
| Failure feels like | saving the wrong things | outliving your own relevance | selling the revival |

**Inside the run = accommodation.** The player-facing Dễ/Thường/Khó control changes **only how much
the game tells you and how much slack it leaves**: crisis warning bands, when the preparation ledger
opens, whether advisors appear, how many ambient beats fire, how much the minigames label. It
never touches a starting stat, a
choice cost, a flag or the victory rule — so a Khó win and a Dễ win mean the same thing, and the
leaderboard stays comparable. **Khó is not a bigger bill; it is playing without hindsight.**
`validate_data.py` rejects any difficulty entry that reaches outside the permitted dials.

---

## Authoring checklist

The recipe that produced this run. It is written generically because it is the engine's
contract — if a future art (gốm, quan họ) is ever built, it is built this way.

1. Identify what the practice's survival actually required — **how** it survived, not that it did.
2. Decompose that *how* into 3–5 preparations → these become the flags.
3. For each flag, find the real event where that preparation was decided → that card is the carrier.
4. Give each carrier a real cost, drawn from what it actually cost the people who made the choice.
5. Fill the remaining slots with pressure cards that tempt the player toward the generic path (take
   the money, take the easier trade) so the historical path stays a real sacrifice.
6. Write the defeat text for "comfortable, missing preparations" — this is the most important text
   in the run, because it is where the learning lands.
7. Prove reachability with `tools/trace_run.py` before trusting any number, and run
   `tools/trace_run.py --audit` so the economy stays two-sided and every dominant choice pays.
8. Give every nonzero effect its `effectReasons` chip (vi+en, ≤ 8 từ) naming the in-world cause —
   if the chip cannot be written, the effect is arbitrary: change the effect, not the chip
   (`game_strategy_and_logic.md` §4).
