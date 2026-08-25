# data-storage

Authoring workspace for the game's cultural content. **Not** part of the Xcode project — this is
where the data is researched, written and checked before it is exported into the app bundle.

```
data-storage/
  design/     win-condition-model.md   ← read this first
              dongho-game-design.md    ← the subject: POV, stats, flags, chapters, minigames
              user-journey.md          ← the run as screens, the four endings, house canon
  schema/     card + level JSON Schema, the contract the data must satisfy
  research/   sourced scaffolds with per-claim status markers
  templates/  copy-per-card / copy-per-level starting files
  tools/      validate_data.py — content linter · trace_run.py — reachability sim
  content/    the actual data
```

`content/` layout:

```
content/
  dongho/          The game: one continuous run 1938–2025 (36 spine cards, 3 chapters).
                   level.json + level-map.md (+ cards/*.json — the team writes these)
  game.json        Game-wide config: the difficulty policy
```

Reachability is machine-checked: `tools/trace_run.py` mirrors the 36-card table and beam-searches
the choice space — change a number in the map, change it there, re-run.

---

## What is here vs what you write

| Provided | Yours |
| --- | --- |
| The win-condition mechanism and why it earns the top rubric band | Every card's `prompt`, `outcome`, `historicalNote` in vi + en |
| JSON Schema for cards and levels | Which events become cards, and their stat numbers |
| A sourced spine with every claim status-marked | Resolving each ⚠️, and citing a real source per card |
| The preparation flags, their carriers, floors and costs | Confirming each against the sources as you write |
| A linter that enforces the design rules, and a sim that proves the run is winnable | Running both until they are clean |

The cultural text is the part that has to be yours: it is what Report section 2 documents, and it is
what you would have to defend if asked to explain the work.

---

## Three rules the data must obey

**1 · Victory is decided by preparations, never by stats.** `finalTrial` reads flags and counters
only. A stat may gate survival; it may never win. See `design/win-condition-model.md`.

**2 · Every victory flag costs something.** Any choice granting a required flag must carry a negative
stat effect. Otherwise the flags become a checklist and the tension is gone. The linter fails the
build on this.

**3 · Facts do not branch.** `historicalNote` is identical after either choice. The player's decision
changes `outcome` (which may be counterfactual) — never the record.

---

## Scope

**One craft, one continuous run, 36 spine cards**: three eras as chapters inside a single progress.
Do not add cards past 36 — trim, don't thicken — and the "Coming soon" arts (gốm, quan họ) get menu
tiles only, **zero content**.

Every string ships in **Vietnamese and English** (`BRIEF-04` requires multi-language support). One
card is roughly six text blocks — prompt, two labels, two outcomes, historical note — so:

| | Cards | Text blocks | ×2 languages |
| --- | --- | --- | --- |
| 36 spine | 36 | 216 | **432** |
| weave pool (chapter-tagged; 11 exist as drafts to rewrite, 6 from nothing) | 17 | 102 | **204** |
| system prose (banners, trial, crises reuse) | | ~30 | **~60** |
| **Total** | | | **≈ 700** |

The **620** floor assumes the 11 weave drafts survive light editing instead of a rewrite. Budget for
700 and be pleased if it lands lower.

One subject, one JSON, one trial, one map; the paintings catalog is shared by the codex and the match
minigame. **Per-card text canon: prompt ≤ 2 câu · outcome ≤ 2 câu · historicalNote ≤ 2 câu** — the
player did not come here to read walls of text.

That is written alongside five required views, auth, cloud sync, CRUD, a leaderboard, an interactive
tutorial, a 30-page report and a 10-minute video — in four weeks, by five people. Treat the weave
pool as the dial that absorbs whatever schedule is left.

**Split by chapter, not by task.** One owner per chapter (12 + 10 + 14 cards) researches, writes and
verifies it end to end; otherwise nobody holds the whole timeline and the chronology drifts. This
also produces the per-member contribution evidence the Project Responsibilities table needs.

That covers three of five members. The other two own the **weave pool** (17 cards, the largest single
block after the spine) and the **system prose + codex entries** — both cut across all three chapters,
so they belong to whoever is not holding a chapter's chronology. Confirm the assignment when `DEC-01`
D11 closes.

---

## Two structural wins to exploit

**`historicity` writes part of your report.** Its three values — `documented` / `simplified` /
`invented` — are exactly the three buckets Report section 2 must declare: which aspects are
authentic, which were simplified for gameplay, which are creative reinterpretation. Tag honestly as
you write and that section becomes a query over your own data instead of an essay written from
memory.

**`sources[]` writes your references.** Every card carries its citation, with `verifiedBy` naming who
checked it.

---

## Validate before committing

```bash
python3 tools/validate_data.py content/     # the rules
python3 tools/trace_run.py                  # the run is still winnable
```

The linter checks: both languages present and TODO-free · every card sourced · `historicity` set and
consistent with `year` · `order` agreeing with chronology · no reference to undeclared stats, flags
or counters · every stat having a two-sided failure with an explanation · `finalTrial` not collapsing
to a stat check · the ledger matching the win condition · floors staying floors · the weave laws and
the solvency invariant · **the cost rule**.

**Expected while the spine prose is unwritten: `8 error(s), 15 warning(s)`.**

- **8 errors** — one per preparation flag (7), plus `ho_so`'s alternate carrier at card 33, each
  saying the card does not exist yet. The 36 spine
  cards are currently a *specification* (the table in `level-map.md`, mirrored in `trace_run.py`),
  not data: **`content/dongho/cards/` does not exist yet.** These clear as those files get written.
- **15 warnings** — 13 weave cards without `sources[]` (a real debt, listed in `level-map.md`), plus
  2 deliberate coherence notes about `sinh_ke` being gated *and* declared `insufficientAlone`.

Anything else is a real finding. The linter also runs the data against `schema/*.json`; that pass
needs `jsonschema` (`pip3 install jsonschema`) and warns if it is missing rather than silently
skipping.

The sim reports whether canonical lines that take every preparation still exist on Thường and on
Khó, and how many winning end-states there are. Run it after **any** number change.

---

## Health warning on the research file

`research/*.md` is a scaffold built from web sources — official heritage records, ministry and
provincial pages, national press, an arts journal, an encyclopedia used only as a finding aid. It is
a **map of what to cite**, not citable content itself. Every claim carries a status:

- ✅ — corroborated by two or more independent sources
- ⚠️ — a single source; usable, but say so or find a second
- ❌ — sources genuinely disagree; **both readings are recorded, and the register at the bottom of
  the file says which wording the game uses**. Never silently resolve one of these.

The ❌ items are not a weakness to hide — a contradiction correctly identified and openly handled is
exactly the "depth and specificity of cultural research" the top rubric band asks for, and three of
them are worth a paragraph each in Report section 2.
