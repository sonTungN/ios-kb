# Level 1 — Nhà Trần · full card map (28 dated cards, 1258–1288, + 6 drawn per run)

The complete playable structure of the level: sequence, roles, stat maths, flag carriers. Narrative
prose is **not** here — each row names the historical anchor the card sits on and its mechanical job;
the team writes `prompt`, `outcome` and `historicalNote` from `../../research/01-tran-nguyen-mong.md`.

The 28 below are the **spine**: dated, fixed, identical in every run. Six further decisions are
**drawn** from an undated pool each run — see *Spine and weave*, further down.

**Starting stats** — `binh 55 · dan 50 · kho 45 · than 60`. Every stat fails at `≤ 0` **and** at `≥ 100`.

---

## Act structure

| Act | Cards | Years | Job |
| --- | --- | --- | --- |
| I · The first storm | 1–6 | 1258 | Teach the loop. Show that surviving ≠ winning. |
| II · The long peace | 7–12 | 1258–1283 | Temptation. Every cheap option builds `binh`. None of it will matter. |
| III · The nation is asked | 13–19 | 1284–1285 | Two carriers land here. Both hurt. |
| IV · Between the tides | 20–26 | 1285–1288 | Rebuild, then the last preparation. |
| V · Eve | 27–28 | 1288 | No more choices that help. Commit. |

---

## The cards

Legend — **Role**: `setup` context · `pressure` tempts toward the generic path · `carrier` grants a
victory flag · `relief` lets the player recover a stat · `trap` looks good, costs the run.
Effects are written `binh / dan / kho / than`.

| # | Year | Card id | Historical anchor | Role | Choice A → | Choice B → | Flag | Src |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1258 | `mong-co-doi-duong` | Mongol envoys demand passage through Đại Việt toward Song | setup | refuse: `0/+5/0/−5` | allow: `0/−15/+5/+5` | | ✅ |
| 2 | 1258 | `giam-su-gia` | The envoys are detained | setup | `0/+5/0/−5` | `0/−5/0/+5` | | `VERIFY` |
| 3 | 1258 | `quan-mong-vao-thang-long` | Mongols take Thăng Long | setup | hold city: `−15/0/−10/+5` | withdraw: `−5/−10/0/−5` | | ✅ |
| 4 | 1258 | `dong-bo-dau` | Counterattack at Đông Bộ Đầu | pressure | strike: `+10/+10/−10/0` | wait: `−5/−10/+5/0` | | ✅ |
| 5 | 1258 | `mong-co-rut-quan` | The Mongols withdraw | setup | `0/+5/0/0` | `0/0/+5/0` | | ✅ |
| 6 | 1258 | `bai-hoc-dau-tien` | The court debates what the victory actually proved | pressure | "we were lucky": `−5/0/0/+10` | "we were strong": `+10/+5/0/−5` | | design |
| 7 | 1261 | `sac-phong-nha-nguyen` | Yuan investiture and tribute demands | pressure | accept: `0/−10/−10/+10` | resist: `0/+10/0/−15` | | `VERIFY` |
| 8 | 1265 | `mo-rong-quan-doi` | Expand the standing army | **trap** | expand: `+20/−10/−20/0` | hold: `0/0/+5/0` | | design |
| 9 | 1270 | `de-dieu-thuy-loi` | Dykes and irrigation works | relief | build: `0/+15/−15/0` | defer: `0/−5/+10/0` | | `VERIFY` |
| 10 | 1272 | `khoa-cu` | Examinations, recruiting mandarins | relief | hold exams: `0/0/−10/+15` | skip: `0/0/+5/−10` | | `VERIFY` |
| 11 | 1279 | `tong-mat` | The Song fall; the Yuan northern border is now Đại Việt's | setup | `0/−5/0/−5` | `0/0/−5/−5` | | ✅ |
| 12 | 1282 | `hoi-nghi-binh-than` | Council of nobles and commanders at Bình Than | setup | `+5/0/−5/+5` | `0/0/0/+10` | | `VERIFY` |
| **13** | **1284** | **`dien-hong-1284`** | **Hội nghị Diên Hồng** — the Retired Emperor asks the elders: peace or war | **carrier** | **ask the nation: `0/+15/0/−20` → grants `long_dan`** | decide in council: `0/−10/0/+10` | `long_dan` | ✅ |
| 14 | 1284 | `hich-tuong-si` | Trần Hưng Đạo's proclamation to the officers | pressure | `+10/+5/0/−5` | `0/0/+5/0` | | `VERIFY` |
| 15 | 1285 | `quan-nguyen-tran-sang` | The second invasion crosses the border in force | setup | `−10/0/−10/0` | `−5/−5/−5/0` | | ✅ |
| **16** | **1285** | **`bo-thang-long-1285`** | **Abandon the capital; leave nothing behind** | **carrier** | **empty the city: `0/−15/−20/−5` → grants `tieu_tho`** | defend it: `−25/+10/−15/+5` | `tieu_tho` | ✅ |
| 17 | 1285 | `sat-that` | Soldiers tattoo "Sát Thát" on their arms | relief | `+10/+10/0/0` | `0/0/0/+5` | | `VERIFY` |
| 18 | 1285 | `ham-tu-chuong-duong` | Hàm Tử, Chương Dương, Tây Kết | pressure | press: `+15/+10/−15/0` | consolidate: `0/0/+5/+5` | | ✅ |
| 19 | 1285 | `giac-rut-lan-hai` | The second invasion collapses | setup | `0/+10/0/0` | `0/+5/+5/0` | | ✅ |
| 20 | 1286 | `khoi-phuc-kinh-thanh` | Rebuilding a capital that was deliberately emptied | relief | rebuild: `0/+10/−20/+5` | leave it: `0/−10/+10/−5` | | design |
| 21 | 1286 | `thuong-hoang-va-vua` | Retired Emperor and reigning Emperor differ on what comes next | pressure | follow Thượng hoàng: `0/+5/0/+10` | follow the Emperor: `+10/0/−5/−10` | | `VERIFY` |
| 22 | 1287 | `tin-bao-lan-ba` | Word arrives: they are coming a third time | setup | `0/−5/0/−5` | `0/0/−5/−5` | | ✅ |
| 23 | 1287 | `trung-binh` | Conscription for the coming war | pressure | levy hard: `+20/−20/−10/0` | levy lightly: `+5/0/−5/0` | | design |
| 24 | 1287 | `doan-thuyen-luong` | The Yuan fleet is escorting a grain convoy | setup | `0/0/0/0` | `0/0/0/0` | | ✅ |
| 25 | 1287 | `van-don-1287` | **Vân Đồn** — strike the supply fleet | carrier *(optional)* | strike: `−10/0/+10/0` → grants `hau_can_dich` | shadow the army instead: `+5/0/0/0` | `hau_can_dich` | ✅ |
| **26** | **1288** | **`dong-coc-bach-dang-1288`** | **Drive stakes into the Bạch Đằng riverbed** | **carrier** | **prepare the river: `−10/0/−15/0` → grants `coc_bach_dang`** | mass the army instead: `+20/0/−5/0` | `coc_bach_dang` | ✅ |
| 27 | 1288 | `doi-con-nuoc` | Waiting on the tide | setup | `0/0/0/0` | `0/0/0/0` | | `VERIFY` |
| 28 | 1288 | `dem-truoc-tran` | The night before | setup | `0/+5/0/0` | `0/0/0/+5` | | design |

→ **Final trial: Bạch Đằng, 1288 — the last mini-boss.** It asks two separate questions:

- **Did you prepare?** `long_dan` + `tieu_tho` + `coc_bach_dang`. **This is what decides the battle.**
- **Is there a state left to fight it with?** `binh ≥ 15 · dan ≥ 15 · kho ≥ 10 · than ≥ 10`.
  A floor only — clearing it never wins anything.

Fail the first → **Defeat Despite Strength**. Fail the second while holding all three flags →
**Spent**, a separate ending: everything prepared correctly, and nothing left to execute it with.
The gate floors are deliberately low, `kho` lowest at 10, because the level's argument is that the
correct player arrives **poor** — the demo run ends `kho 25`. Every floor also sits below the crisis
band (20), so a player heading for a gate failure is always offered the rescue first.

`binh` is declared `insufficientAlone` — however high it is, it does not win this.

### Carrier floors — the means to act

Each required carrier also has a **`statFloor`**: a minimum the stat must hold *entering* the card,
or the preparation does not land. **The cost is still paid; the flag is not granted**, and
`blockedText` explains why in period terms. Full reasoning in `../../design/win-condition-model.md`
§ *Floors, not thresholds*.

| Card | Flag | Floor | Demo run enters at | Margin | The court cannot, because |
| --- | --- | --- | --- | --- | --- |
| 13 | `long_dan` | `dan ≥ 20` | `dan 40` | +20 | The elders will not come |
| 16 | `tieu_tho` | `dan ≥ 25` | `dan 55` | +30 | A starving city will not walk out and burn its own granary |
| 26 | `coc_bach_dang` | `binh ≥ 25` | `binh 70` | +45 | Stakes are wood with nobody on the banks |

**The floors are deliberately low, and `binh ≥ 25` is the one to defend.** A floor near 60 would be
false history — the Trần were outnumbered in all three invasions and won by refusing open battle —
and it would break card 8: the `+20 binh / −20 kho` trap becomes correct play the moment the floor
sits above the starting 55. The linter warns on any floor above half a stat's range for exactly that
reason. **A floor says you need *an* army. It must never say you need a *big* one.**

Every floored carrier already has an advisor interstitial before it (cards 13, 16, 26 — see below),
and the linter errors if one is missing: a gate nobody can see coming is a trap, not a challenge.

---

## Why the maths works

**The carriers cost, in total: `binh −10 · dan 0 · kho −35 · than −20`.**

Starting `kho` is 45, so a player who takes all three carriers ends around `kho 10` unless they used
the relief cards. That is the intended squeeze: the historical path is affordable, but only just, and
only with attention.

`dan` nets to zero across the carriers because Diên Hồng's `+15` offsets the capital's `−15` — the
nation consents to the sacrifice it is about to bear. That is the design saying something true.

**Card 8 (`mo-rong-quan-doi`) is the level's trap.** `+20 binh` for `−20 kho` is the single most
attractive-looking trade in the level, and `binh` is precisely what the final trial ignores. A player
who takes it, and then takes the `+20 binh` option on card 26 instead of preparing the river, arrives
at Bạch Đằng with a large army and loses. That run is the level working correctly.

**Two-sided failure is reachable, deliberately.** Taking every `binh` option climbs past 100 →
kiêu binh ending. Taking every `than` option does the same → quyền thần ending. Both are real Trần-era
failure modes and both should be reachable in a 28-card run.

A worked victory line — 28 cards with running stat totals — is in
`../../design/user-journey.md` § *The canonical demo run*. It ends `binh 60 · dan 55 · kho 25 · than 30`
with all three flags: a win on a middling army.

---

## Beyond the 28: what sits between the dated cards

The 28 numbered cards are the level's *argument*. Five other event types sit between them. All are
declared in `dynasty.json` — never in `cards/` — and all are machine-checked by
`../../tools/validate_data.py`. **`cards/` is the spine; `dynasty.json` holds everything that
floats.** That split is the whole architecture.

| Type | Fires | Choice? | Stat effect | Job |
| --- | --- | --- | --- | --- |
| **`advisor`** Cố vấn | before cards 13, 16, 26 | no | none | A named figure states what the coming choice costs, *before* it is made. Sacrifice you understand is drama; sacrifice you did not see coming is just a trap. |
| **`omen`** Điềm báo | before cards 15, 22 | no | none | Telegraphs the next invasion one card ahead, so banking resources becomes a plan rather than a guess. |
| **`echo`** Hệ quả muộn | 3–4 cards after a triggering choice | no | none | Calls back an earlier decision — the army you expanded now eats, the dykes you built now hold. History has lag; this is where the run starts feeling authored. |
| **`ambient`** Năm lành | ≤5 per run, ≥4 cards apart | no | small, mostly positive | Relief. Without these the stat curve only ever points down. Drawn 5 from a pool of 12. |
| **`crisis`** Khủng hoảng | a stat enters a danger band | **yes** | **yes** | The one way back from the edge. Not drawn — triggered by the player's own stats. |
| **`weave`** Việc triều đình | 6 per run, drawn by act | **yes** | **yes**, bounded | Ordinary governing between the great events. **The only source of run-to-run variety in the decisions themselves** — see *Spine and weave* below. |

The first four cannot be got wrong; they exist so the decisions that matter are made with open eyes.
Crisis and weave cards are real decisions, and both are constrained so they can never decide the run:
a crisis fires once per stat per side and always costs another stat, and the weave pool is bounded by
the solvency invariant.

### Crises — the level stops killing without warning

**This is the change that makes the level winnable.** Previously a stat touching `0` or `100` ended
the run on the spot, with no signal and no recourse. Now, crossing into a danger band injects a
crisis card offering a single costly rescue.

The band is the one thing here that difficulty moves: `≤30 / ≥70` on Dễ, `≤20 / ≥80` on Thường (the
figures used throughout this file), and **no band at all on Khó** — which restores the original
model exactly. See `../../content/game.json`.

Three rules keep it from turning the game into a walkover, and the linter enforces all three:

1. **`oncePerLevel`.** Each of the eight crises fires at most once. Run a stat to the edge a second
   time and it ends the run — the two-sided failure model is intact, it just now takes two mistakes
   instead of one.
2. **Every rescue is paid for out of another stat.** The cost rule that governs the victory flags
   applies here too: surviving a crisis *narrows the board*, it does not reset it. `kho +25` costs
   `than −15`; the treasury is refilled by princes the throne is now indebted to.
3. **Refusing is always allowed.** The rescue is an option, not a cutscene. A player who declines
   keeps their stats clean and their risk.

| Crisis | Stat | Fires at | Rescue | Cost |
| --- | --- | --- | --- | --- |
| Vương hầu góp của | `kho` | ≤ 20 | `kho +25` | `than −15` |
| Sưu thuế quá nặng | `kho` | ≥ 80 | `kho −20` | — (`dan +10`) |
| Dân xiêu tán | `dan` | ≤ 20 | `dan +25` | `kho −20` |
| Không thu được thuế | `dan` | ≥ 80 | `dan −20` | — (`kho +10`, `binh +5`) |
| Mộ binh từ thái ấp | `binh` | ≤ 20 | `binh +20` | `than −10` |
| Kiêu binh | `binh` | ≥ 80 | `binh −20` | `dan −5` |
| Triều đình rệu rã | `than` | ≤ 20 | `than +20` | `kho −15` |
| Quyền thần | `than` | ≥ 80 | `than −20` | `binh −10` |

The high-side rescues read as costless because pulling a stat *down* off `100` is itself the relief;
their price is the ground they give up elsewhere and the fact that they burn the stat's one rescue.

---

## ⚠️ Balance finding — card 16 has a hidden treasury gate

Traced 15 Aug 2026 by playing several lines against this table.
**Partly mitigated by the `kho` crisis; the incentive half is still open — the team decides.**

> **What the crisis fixed.** A player arriving at Act III with a drained treasury now trips
> `kho ≤ 20` *before* card 16 and gets `kho +25`, which lifts them clear of the dead zone below.
> The hard-lock — the state where card 16 kills you whatever you choose — is gone.
>
> **What it did not fix.** Everything below about the *incentive inversion* still stands, and the
> crisis makes it slightly worse: a player who has already spent their one `kho` rescue arrives at
> card 16 with no net at all.

Card 16 `bo-thang-long-1285` costs `kho` on **both** branches (`−20` to empty the city, `−15` to
defend it). Since `kho` fails at `≤ 0`, the card silently gates on the treasury the player walks in
with:

| `kho` entering card 16 | What actually happens |
| --- | --- |
| **≥ 21** | Both branches survive. Real choice. Intended. |
| **16 – 20** | Only "defend it" survives. The player is *mechanically forced* to forfeit `tieu_tho` — and therefore forced to lose at the final trial, 12 cards later, with no signal that it already happened. |
| **≤ 15** | Both branches hit `kho ≤ 0`. Dynasty Falls regardless of choice. The card is unwinnable. |

Two things are wrong with that, beyond the dead zone itself:

1. **The incentive is backwards at the worst moment.** Defending the capital (`−15`) is *cheaper*
   than the historically correct choice of emptying it (`−20`). A squeezed player is pushed toward
   the wrong history by the arithmetic, which is the opposite of what this level is arguing.
2. **Act III offers no treasury relief.** Cards 14 and 15 are both `kho`-neutral or negative, so a
   player who took the card 8 trap (`−20 kho`) has nothing between it and card 16 to recover with.
   The trap is meant to cost the *run*, not to make the run unplayable ten cards early.

The greedy-military line dies here rather than reaching its intended ending: taking card 8's expand
and card 13's council option arrives at card 16 around `kho 10–20`, and dies on the card. **Defeat
Despite Strength is therefore harder to reach than designed** — it currently requires a player who
managed the treasury *well* and still missed a flag, not a player who chased raw force.

**Candidate fixes** — pick one, do not stack them:

- **(a)** Give card 14 or 15 a `kho`-positive option, so Act III has one recovery beat.
- **(b)** Make "defend it" cost at least as much `kho` as "empty the city", so the correct choice is
  never the more expensive survivable one. Historically defensible — holding a city under siege is
  not cheap.
- **(c)** Lower card 8's trap cost from `−20 kho` to `−10`, keeping it a trap through `binh`
  overshoot rather than through bankruptcy.

**(b) is the smallest change and fixes the incentive inversion directly**; (a) is the most forgiving
but adds a card's worth of writing.

**Invariant to hold once fixed:** every path that reaches card 16 must leave at least one branch with
`kho > 0` *and* must not force the loss of `tieu_tho`. Worth adding to `../../tools/validate_data.py`
as a reachability check — it is the kind of thing that silently breaks again when effects are tuned.

> **The weave does not make this worse.** Adding drawn cards to a level with a hidden treasury gate is
> exactly how a shuffle turns into an unfair loss, so the solvency invariant was built for this case
> first: `kho` carries the tightest budget in `weavePolicy.maxWorstCaseSwing` (±12), and the harshest
> legal draw played well comes out at **`+3`**. No set of drawn cards can push a player under card 16
> who would otherwise have cleared it. Whichever fix the team picks for the incentive inversion, keep
> that budget tight or re-derive it.

---

## Spine and weave — what is fixed, and what is drawn

**The rule: history fixes *when* the great events happen. It does not fix what an ordinary year
looked like.** The deck is split on exactly that line, and the split is machine-enforced.

| | **Spine** — `cards/*.json` | **Weave** — `dynasty.json → weave[]` |
| --- | --- | --- |
| What it is | The 28 dated cards above | Ordinary court business: a dyke gives way, a magistrate is accused, an old general asks to go home |
| Has a `year` | **Required.** No year → linter error | **Must be `null`.** A year → linter error |
| Position | Fixed, and checked against the year | Belongs to an **act**, not a position |
| Between runs | **Never shuffled, skipped or moved** | Drawn fresh every run |
| May carry a required flag | Yes — all three live here | **Never.** Linter error |
| `historicity` | any | `simplified` / `invented` only — `documented` is an error, because if the record documents it, the record dates it |

The weave is not a loophole in the accuracy rule; it is that rule stated precisely. A card saying
*"a dyke gave way downstream"* claims nothing about 1270. A card saying *"Diên Hồng, 1284"* claims a
great deal, and never moves.

**Draw:**

| Act | Spine cards | Weave slots | Pool | Why |
| --- | --- | --- | --- | --- |
| I · The first storm | 6 | **0** | — | Teach the loop clean |
| II · The long peace | 6 | **3** | 6 | The act that is actually about governing |
| III · The nation is asked | 7 | **1** | 3 | Wartime texture, one beat, no dilution |
| IV · Between the tides | 7 | **2** | 3 | The rebuild is administration again |
| V · Eve | 2 | **0** | — | No more distraction. Commit |

`C(6,3) × C(3,1) × C(3,2)` = **180 distinct weave sets**, and ambient draws 5 from a pool of 12 for
another `C(12,5)` = **792**. Crises are not drawn at all — they fire off the player's own stats, so
a careful run may see none and a reckless one three. Run to run: **the same 28 arguments, a different
year around them.**

**Pool size and slot count are separate dials.** Pool = variety, slots = length. Add to the pool and
runs diverge more; the level does not get longer. Change the slots and it does. The linter errors when
a pool is smaller than its slots and warns when they are equal (every run sees the same set, so the
content bought no variety).

### The solvency invariant — the one rule that makes randomness safe

> **A draw may change how a run feels and what it costs. It may never change whether the run can be
> won.**

This is the thing an unguarded shuffle breaks, and it breaks it silently. Draw three
treasury-hungry cards in Act II and card 16's hidden gate becomes unreachable through no fault of the
player — the game would be deciding the outcome before they touched it.

`weavePolicy.maxWorstCaseSwing` prevents it, and `validate_data.py` proves it on every run. For each
stat the linter takes the **kindest branch of every card**, deals the **cruellest draw the slot counts
allow**, and requires the total to stay inside the budget — then does it again on the high side,
where overshoot kills instead. Current headroom:

| Stat | Worst legal draw, played perfectly | Most generous legal draw | Budget |
| --- | --- | --- | --- |
| `binh` | `0` | `0` | ±15 |
| `dan` | `+13` | `−2` | ±15 |
| `kho` | `+3` | `−3` | **±12** — tightest, because card 16 already gates on the treasury |
| `than` | `+11` | `−15` | ±15 |

Every worst case is at or above zero. A hostile draw costs the attentive player nothing; it only
takes options away from a careless one. That is the intended shape.

### Run length

28 spine + 6 weave = **34 decisions**, plus ≤5 ambient beats, 8 interstitials, and 0–8 crises —
roughly **47–55 screens** per run. Long for a card game, normal for the *Reigns* format. If playtest
says it drags, cut `slotsPerAct`, not the pool: that shortens the run without discarding writing.

---

## What the team still writes

**Spine** — for each of the 28 rows: `prompt`, both choice `label`s, both `outcome`s, and
`historicalNote`, in Vietnamese **and** English, plus at least one real source per card.
28 × 6 × 2 ≈ **340 strings**. This is all-or-nothing: the level does not run without every one.

**Weave** — 12 cards at the same 6 fields ≈ **144 strings**, plus **20** for the five new ambient
beats. Unlike the spine this is **incremental**: ship with a smaller pool and add to it later, and
the linter will tell you the moment a pool drops below its slot count. Draft prose is already in
`dynasty.json` for all 12 — what is actually owed there is **sourcing**, one citation per practice
(dyke administration, điền trang and nô tì, temple landholding, nông binh levies), not one per card.

**≈ 504 strings for the level in total.** This is the single largest piece of work in the project.

Rows marked `VERIFY` in the Src column are anchors that were **not** confirmed in the 15 Aug research
pass. Confirm or replace them before writing. Rows marked `design` have no specific historical
anchor — they are connective tissue, and must be tagged `historicity: "invented"` in the JSON so
Report §2 can declare them honestly.
