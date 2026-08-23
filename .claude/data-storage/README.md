# data-storage

Authoring workspace for the game's cultural content. **Not** part of the Xcode project — this is
where the data is researched, written and checked before it is exported into the app bundle.

> 🔄 **21 Aug 2026 — subject pivot.** The game keeps its engine and now teaches **nghề làm tranh dân
> gian Đông Hồ** (tutor-endorsed; see `DEC-01` D1b). The active content set is
> `research/04-dong-ho-tranh-dan-gian.md` + `design/dongho-game-design.md` + `content/dongho/`.
> The Trần/war set (`research/01–03`, `content/tran/`) is **archive**: it remains the pipeline's
> worked example and validator fixture, but it is no longer game content — do not extend it.

```
data-storage/
  design/     win-condition-model.md   ← read this first
  schema/     card + dynasty JSON Schema, the contract the data must satisfy
  research/   per-dynasty sourced scaffolds with VERIFY markers
  templates/  copy-per-card / copy-per-level starting files
  tools/      validate_data.py — content linter
  content/    ← you create this; the actual data lives here
```

`content/` layout:

```
content/
  dongho/          THE game: one continuous run 1938–2025 (36 spine cards, 3 chapters).
                   dynasty.json + level-map.md (+ cards/*.json — the team writes these)
  tran/            ARCHIVE — the war-concept worked example; kept for pipeline reference
```

Reachability is machine-checked: `tools/trace_run.py` mirrors the 36-card table and beam-searches
the choice space — change a number in the map, change it there, re-run.

(`dynasty.json`/`dynastyId` are naming debt from the war era — the contract is subject-neutral;
rename to `level.json`/`levelId` only as a single sweep, or not at all. See the design doc.)

---

## What is here vs what you write

| Provided | Yours |
| --- | --- |
| The win-condition mechanism and why it earns the top rubric band | Every card's `prompt`, `outcome`, `historicalNote` in vi + en |
| JSON Schema for cards and levels | Which events become cards, and their stat numbers |
| Sourced spine of each dynasty, with unverified points flagged | Verifying each `VERIFY`, and citing a real source per card |
| Candidate preparation flags per level | Confirming or replacing them from the sources |
| A linter that enforces the design rules | Running it until it is clean |

The historical text is the part that has to be yours: it is what Report section 2 documents, and it
is what you would have to defend if asked to explain the work.

---

## Three rules the data must obey

**1 · Victory is decided by flags, never by stats.** `finalTrial` reads preparation flags and
counters only. A stat may gate survival; it may never win. See `design/win-condition-model.md`.

**2 · Every victory flag costs something.** Any choice granting a flag in `requireAll` must carry a
negative stat effect. Otherwise the flags become a checklist and the tension is gone. The linter
fails the build on this.

**3 · Facts do not branch.** `historicalNote` is identical after either choice. The player's decision
changes `outcome` (which may be counterfactual) — never the record.

---

## Scope

**One craft, one continuous run, 36 spine cards** (team decision 22 Aug 2026): three eras as
chapters inside a single progress. Do not add cards past 36 — trim, don't thicken — and the
"Coming soon" arts (gốm, quan họ) get menu tiles only, **zero content**.

Every string ships in **Vietnamese and English** (`BRIEF-04` requires multi-language support). One
card is roughly six text blocks — prompt, two labels, two outcomes, historical note — so:

| | Cards | Text blocks | ×2 languages |
| --- | --- | --- | --- |
| 36 spine | 36 | ~216 | **~432** |
| weave pool (17, chapter-tagged; 11 drafted) | 6 new | ~36 | ~72 |
| system prose (banners, trial, crises reuse) | | ~50 | ~100 |
| **Đông Hồ total** | | | **≈ 620–700** |

One-third less than the 3-màn plan it replaces, and 40% less than the 3-dynasty plan before that —
one subject, one JSON, one trial, one map; the paintings catalog is shared by the codex and the
match minigame. Per-card text canon: prompt ≤ 2 câu · outcome ≤ 2 câu · historicalNote ≤ 2 câu.

That is written alongside five required views, auth, Firebase sync, CRUD, leaderboard with charts,
an interactive tutorial, a 30-page report and a 10-minute video — in four weeks, by five people. The
fourth dynasty is where the schedule breaks.

**Split by chapter, not by task.** One owner per chapter (12 + 10 + 14 cards) researches, writes and verifies it end to end;
otherwise nobody holds the whole timeline and the chronology drifts. This also produces the per-member
contribution evidence the Project Responsibilities table needs.

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
python3 tools/validate_data.py content/
```

It checks: both languages present and TODO-free · every card sourced · `historicity` set and
consistent with `year` · `order` agreeing with chronology · no reference to undeclared stats or flags
· every stat having a two-sided failure with an explanation · `finalTrial` not collapsing to a stat
check · **the cost rule**.

---

## Health warning on the research files

`research/*.md` are scaffolds built from a first pass of web sources — encyclopedias, a military
journal, press features, a government local-history portal. They are a **map of what to go and
confirm**, not citable content. Anything marked `VERIFY` is unconfirmed.

### Verification pass — 15 Aug 2026

A second pass resolved the two flagged traps and confirmed most of Levels 2 and 3.

| Item | Result |
| --- | --- |
| Level 2 date tension | ✅ Not a contradiction — war ends **16 Dec 1427** (Hội thề Đông Quan), Bình Ngô đại cáo is **1428**, written after as a proclamation |
| Level 3 "stakes at Như Nguyệt" | ✅ **Contamination confirmed and corrected** — Như Nguyệt is an earth rampart + bamboo palisade **on the bank** + spike pits, *not* riverbed stakes. Bạch Đằng is the riverbed one |
| Hội nghị Diên Hồng | ✅ **1284**, convened by Thượng hoàng Trần Thánh Tông, elders asked "hòa hay đánh", answered "Đánh", before the 2nd invasion, recorded in ĐVSKTT |
| Lam Sơn timeline | ✅ Fully dated 1418 → 1428, incl. Lê Lai 1419, Nguyễn Chích 1424, Tốt Động–Chúc Động 1426, Chi Lăng–Xương Giang 1427 |
| Nam quốc sơn hà authorship | ⚠️ **Weaker than "disputed"** — most scholars say anonymous, recent view is that it predates Lý Thường Kiệt entirely. Do not attribute it to him |

Still open: the Vân Đồn 1287 commander and effect; the "≈9 months of fighting across 30 years"
figure; whether "tâm công" is the correct term for the Lam Sơn subversion campaign.

Three of these findings are worth a paragraph each in Report section 2 — correcting a widely believed
error is exactly the "depth and specificity of cultural research" the top rubric band asks for.
