# Đông Hồ game design — the subject layer

The subject layer of the game: POV, stats, flags, chapters, minigames, endings. The engine it sits
on — spine/weave, two-sided stats, preparation flags, carriers with floors and costs, the
preparation-vs-capacity trial, difficulty as information and slack — is specified in
`win-condition-model.md`. Facts cited here are sourced in
`../research/01-dong-ho-tranh-dan-gian.md`; nothing below invents a date.

---

## 1 · POV — household, not village (D1b-POV assessment)

**Recommendation: the player is one craft household (hộ nghề) across generations. The village is the
world around them, not the seat they sit in.** Assessed both ways:

| Criterion | Gia đình (hộ nghề) | Làng nghề (village) |
| --- | --- | --- |
| Reigns mechanics need one decider | ✅ the household head — every card is someone at *your* door | ⚠️ a village is not an agent; needs an invented "trùm phường/trưởng làng" proxy |
| The historically true win-line | ✅ **family-scale**: the HTX was built by one man (Nguyễn Hữu Sam, 1967); the woodblock rescues were personal acts (Sam ~1990, 600+ per the one detailed account ⚠️; Chế — return dated 1985 or 1992 by different sources ❌ — ~400 sets); transmission ran inside 2 lineages | ❌ village-scale 1990s is a *loss* arc — >90% of households quit. Playing "the village" honestly means playing the side that lost |
| The 1990s trap has agency | ✅ "Cả làng đã chuyển sang vàng mã — nhà mình theo không?" is a *choice* | ❌ at village scale the vàng mã switch is the *outcome*, not a decision |
| UNESCO's own judgment unit | ✅ the 2025 inscription text counts **households**: "only several households are upholding the element" — the trial judges exactly what UNESCO judged | ⚠️ village-level judgment would contradict the decision text |
| Educational breadth (chợ tranh, đình, phường, 17 dòng họ) | ✅ enters as spine/weave events seen from the family's stall and seat — nothing is lost | ✅ native, but no exclusive gain |
| The transmission thesis as mechanic | ✅ truyền nhân flag = succession = the living-heritage message itself | ⚠️ diffuse |
| Tutor's own framing | ✅ his minigame example says "thằng cháu của **nhà** truyền thống" | — |

**One ethical-accuracy rule falls out of this POV** and must be stated in the report: the player's
household is a **fictional composite** — "một trong 17 dòng họ làng Mái" — never a named real family.
The real people (cụ Sam, cụ Chế, cô Oanh, anh Quả) appear where the record puts them: in
`historicalNote`, in the codex, and as **spine anchors** ("Năm 1967, cụ Nguyễn Hữu Sam được giao lập
HTX với 50 nghệ nhân — nhà mình có gửi người vào không?"). The framing household is
`historicity: invented`; the events around it stay `documented`. This is the same split the schema
already enforces, and it keeps the game from putting counterfactual words in living people's mouths.

*What the village POV would have bought* — communal-institution decisions (đình, phường, chợ) made in
first person — *is recovered* by giving the household a seat in them: a phường nghề vote is a card
someone brings to you, like everything else in Reigns.

---

## 2 · The four stats — NGHỀ · SINH KẾ · TIẾNG · NGƯỜI

The contract: fail at `≤ 0` **and** `≥ 100`; every overflow is a **documented failure mode
of the craft**, not an arbitrary game-over.

| Stat | It measures | `≤ 0` — documented | `≥ 100` — documented |
| --- | --- | --- | --- |
| `nghe` **NGHỀ** | Mastery & authenticity: điệp ground, natural pigments, ván khắc, the printing hand | **Thất truyền kỹ thuật** — the sheet stops being tranh Đông Hồ (offset prints and chemical dyes sold under the name; the anti-counterfeiting goal of the Đề án 2026 exists because this is real) | **Nệ cổ hóa thạch** — refusing every adaptation until the craft leaves daily life ("tục mua tranh Tết đã mai một"); a museum piece is not living heritage. `historicity: simplified` — the pattern is the CAND modernization debate + the đề án's design-innovation goal |
| `sinh_ke` **SINH KẾ** | The household economy: rice, paper stock, orders | **Đói — bỏ nghề đi làm thuê** (what >90% of households did after 1990) | **Xưởng thành xưởng mã** — money itself pulls the family off the craft: vàng mã pays 150–250k a piece while tranh income is "chưa ổn định"; wealth from the side-line eats the workshop |
| `tieng` **TIẾNG** | Reputation & demand: buyers at the phiên, visitors, orders, the wider world's regard | **Bị quên lãng** — the chợ tranh died mid-1940s because demand died; no market, no craft | **Thương mại hóa lố** — bulk orders that force sloppy printing, tourist-ware, fakes trading on the name (the Đề án 2026 lists anti-counterfeiting as a measure because fame invites fakes) |
| `nguoi` **NGƯỜI** | The hands that hold the craft: children, apprentices, the phường | **Không người nối nghề** — UNESCO's inscription reason verbatim: "the number of skilled and committed individuals… has become too small to sustain transmission" | **Đông tay, loãng chuẩn** — mass, uncommitted practice: 15-minute tour classes and licensed-out printing dilute exactly what UNESCO counts, which is *skilled and committed* people, not bodies. `historicity: simplified` |

Two of the eight edges (`nghe` high, `nguoi` high) are patterns argued from documented tensions
rather than single dated events — they are tagged `simplified` and their `failHighText` must say so.
The other six are directly documented.

**The double death is the syllabus.** Heritage dies of neglect *and* of commodification; a player
who discovers that farming TIẾNG to 100 kills the craft as surely as letting it hit 0 has learned
the central problem of heritage preservation — that is the two-sided stat model earning criterion 1.

---

## 3 · Structure — one economy, three sequential chapters

**One continuous economy, 1938 → 9 Dec 2025, played as three sequential chapters (levels).** A
chapter unlocks when the previous one is finished, opens on its era screen, and closes on a
summary/lesson screen; the Final Trial ends chapter III. **Stats, flags, ticks and spent crises
persist across chapters — nothing resets** — so the fire of the kháng chiến years still decides
2025, and the machine-checked reachability/solvency proofs carry over unchanged. Three design
requirements survive from the one-run thesis: every dated anchor is a public, checkable milestone
(~36 is what the record honestly supports — the hygiene factor); the whole educational arc including
the living-heritage present is one unbroken line (a demo plays the chapters back-to-back); and each
chapter now earns its own lesson screen, so the teaching lands three times instead of once.

**Continuity mechanics.** Chapter entry writes a **checkpoint** {stats, flags, ticks, spent crises,
weave seen}. Save & Exit / Resume / Restart act per chapter. Restarting an earlier chapter reloads
its checkpoint, **locks every later chapter** (their entry states are no longer true) and deals a
fresh seed; the home screen offers "chapter-restart / restart-all" with an explicit lock warning.
The home screen shows the persisted stats — they are the next chapter's starting line. Each chapter
declares required objectives: C1 `giu_van`+`giu_bi_quyet` · C2 ticks 2–3 of `truyen_thua` · C3
`phuc_hoi_van`+`truyen_nhan`+`ho_so`.

| | Chương I · **Giữ lửa** (1938–54) | Chương II · **Giữ nếp** (1967–90) | Chương III · **Hồi sinh** (1992–2025) |
| --- | --- | --- | --- |
| Cards | 1–12 | 13–22 | 23–36 |
| The question | *Which things must not burn?* | *Can transmission outlast the institution carrying it?* | *Can you stop doing what saved you?* |
| New educational elements | the loop; craft & Tết customs; the ledger; `mg_match` | the counter; echoes; the economics of a craft | the expiring window; ceiling dangers; `mg_assemble`; heritage policy & today |
| Danger profile | floors (poverty, war) | the trap era (vàng mã takes a tick) | **ceilings** (fame, commodification) + the clock |

`BRIEF-05` §3 is satisfied on the direct reading — chapters ARE the *levels*, sequential and
unlocking, each adding mechanics and content; the **Chọn di sản** screen's "Gốm · Quan họ — sắp ra
mắt" tiles extend the dimension to future arts. Difficulty is re-selectable mid-playthrough and the
leaderboard records the lowest difficulty used — see `DEC-01` D13 and `../content/game.json`.

**The structure is also the delivery safeguard:** the present day sits *inside the one deck* and
cannot be cut without cutting the game. The schedule lever is pool size (weave/ambient) and prose
polish, never structure. Budget: 36 spine + 17 weave + system ≈ **620–700 bilingual strings**, plus
≈ 250–300 `effectReasons` micro-chips written with the spine cards (weave + crisis chips already
shipped — `game_strategy_and_logic.md` §4) — one JSON, one trial, one map
(`../content/dongho/level-map.md`, machine-checked by `../tools/trace_run.py`).

---

## 4 · Flags, the counter, the trial — one judgment for one century

### The flag economy (7 flags + 1 counter across 36 cards)

| Card | Id | What it is | Cost lands as | Floor |
| --- | --- | --- | --- | --- |
| 7 | `giu_van` | The blocks carried through the fire (kháng chiến chống Pháp) | `sinh_ke −10 · tieng −10` | `nguoi ≥ 20` |
| 9 | `giu_bi_quyet` | The recipe taught in evacuation (1949ᵃ) — **mg_match** | `sinh_ke −5` | `nghe ≥ 25` |
| 12 · 15 · 20 | `truyen_thua` **counter +1 each** | Về làng 1954 · dạy con 1972ᵃ · con ở lại 1987ᵃ | each tick bills `sinh_ke` | — |
| 11 | *(trap)* | The dealer buys the rescued blocks — **revokes `giu_van`** | +25 `sinh_ke`, the ledger slot un-fills | — |
| 18 | `giu_mau_co` *(optional)* | The classics archived against "cải tiến" (1982ᵃ) | `sinh_ke −10 · tieng −5` | `nghe ≥ 25` |
| 22 | *(trap)* | 1990: the vàng mã switch — **revokes `giu_mau_co`, takes a tick back** | +25 `sinh_ke`, `nghe −15` | — |
| 23 | `phuc_hoi_van` | The buy-backs (1992ᵃ→) — the blocks' second road | `sinh_ke −15` | `sinh_ke ≥ 20` |
| 27 | `mo_cua` *(optional)* | Experience classes (2008) — **mg_match reprise** | `nghe −5 · sinh_ke −5` | `tieng ≥ 20` |
| 30 | `truyen_nhan` | The grandchild takes the craft (2015ᵃ) — **mg_assemble** | `sinh_ke −10` | `nguoi ≥ 20` |
| 31 / 33 | `ho_so` | The dossier, 2017 → the 31/3/2020 deadline — **expires**; card 33 is the dear last chance (conditional pair in one spine slot) | 31: `nghe −5 · sinh_ke −10` · 33: `nghe −10 · sinh_ke −15 · nguoi −5` | `tieng ≥ 25` |

Every carrier obeys the standing rules (cost rule · floor rule + `blockedText` · advisor before
every floored required carrier, suppressed on Khó). **Chapter III floor note:** `phuc_hoi_van`
floors the stat the trial calls insufficient — necessary to act, never sufficient to win — and its
blocked text carries both halves.

### The Final Trial — 9 Dec 2025, one trial, three questions

```
requireAll:      [giu_bi_quyet, truyen_nhan, ho_so]     — recognise
requireAny:      [giu_van, phuc_hoi_van]                — either road for the blocks
requireCounter:  {truyen_thua: 2}  (of 3 ticks; the 1990 trap can take one)  — sustain
statGate:        nghe 15 · sinh_ke 10 · tieng 10 · nguoi 15   — floor only
insufficientAlone: [sinh_ke]                            — the Committee did not count money
```

One judgment asks three kinds of question — recognise, sustain, reverse — and the `requireAny` pair is the design's mercy and its history in one mechanism: losing the blocks
in 1951 is not a 25-card death march; it opens the costlier documented road of 1992. All four
endings survive with their Đông Hồ names (Ghi danh · Giàu mà mất nghề · Kiệt sức · Nghề tàn), and
every one of them is a real fate some family had.

**Reachability is machine-checked** (`tools/trace_run.py`): canonical lines holding *all seven
flags* exist on Thường (exactly one accepted crisis) and on Khó (none); losing `giu_van` and
recovering via `phuc_hoi_van` also wins. The tool mirrors the card table — change one, change both.

### Minigames — the carrier ritual

A minigame is the **ritual of a carrier flag**, never a new gate: (1) the stat floor decides whether
the attempt lands; (2) the choice's cost is paid; (3) the minigame plays; (4) completion grants the
flag. **A minigame can be retried until completed at every difficulty** — if dexterity could
permanently fail a flag, difficulty would change outcomes, which it must never do. Khó strips hints,
never completion. Content comes from the researched catalog, never invented:

| Id | Type | Where | What the player learns |
| --- | --- | --- | --- |
| `mg_match` | **Nối tranh – nghĩa** (4↔4 match) | `giu_bi_quyet` (card 9) | The 4 graded pairs: Vinh hoa = mong con hiển đạt · Phú quý = vịt (cóc là Nhân nghĩa — distractor có sẵn) · Lợn đàn = xoáy âm dương/sinh sôi · Gà Đại cát = ngũ đức. **Đám cưới chuột excluded from grading** (contested reading — codex carries both layers) |
| `mg_assemble` | **Ghép ván in** (3×3, xoay 90°) | `truyen_nhan` (card 30) | One real mẫu assembled = the grandchild's first print; Dễ shows the finished sheet, Thường the outline, Khó nothing |
| `mg_sequence` **(revived — the cheapest build in the set: a reorderable 5-item list)** | **In đúng lớp** (kéo 5 lớp màu vào đúng trình tự) | `giu_mau_co` (card 18) | The documented order: one block per color, dried between, **nét đen in cuối cùng** — archiving the classics means knowing how they are printed |
| `mg_match` (materials reprise) | **Nối nguyên liệu – màu** (5↔5, same engine, zero new code) | `mo_cua` (card 27, optional) | than lá tre→đen · vỏ điệp→trắng · hoa hòe→vàng · lá chàm→xanh · sỏi son→đỏ — the five documented pigments |

Difficulty scaling for `mg_match`: Dễ labels shown · Thường labels shown once · Khó icons only, the
meanings must have been read in the codex. SwiftUI cost: `LazyVGrid` + drag / tap-rotate state
machines — inside `BRIEF-02` scope, and each shipped minigame counts toward the ≥3 distinct Game
View animations. Schema: the `minigame` object lives on the flag (`level.schema.json`); the
validator's minigame check (type known, contentRef resolves) is a logged follow-up.

## 5 · The named surfaces

The engine layer the build implements once and never varies by subject: the swipe loop and its
mid-drag preview canon (exact deltas, affected bars dimmed to 50%); the spine/weave split and the
weave's three laws (`year: null`, never a required flag, never `documented`); the solvency invariant
(`weavePolicy.maxWorstCaseSwing`); crisis bands and the one-rescue rule; the interstitial set; the
ledger's `when-not-what` disclosure policy; the difficulty table in `content/game.json`; the four
endings; the preparation-vs-capacity trial; per-chapter save/resume/restart with chapter locking;
the run review.

The surfaces this subject names:

| Surface | Name | Note |
| --- | --- | --- |
| Art select | **Chọn di sản** — Tranh Đông Hồ · Gốm *(sắp ra mắt)* · Quan họ *(sắp ra mắt)* | teaser tiles only — zero content behind them |
| Era turn | **Chapter banner** — era title, one line of bridge text, ledger snapshot | the `chapter` interstitial type, validator-supported |
| Preparation ledger | **Sổ gia truyền** | slots + floors + `when-not-what`; the woodblock pair is one slot, the counter a three-notch meter |
| Codex | **Bộ sưu tập tranh** | a collectible painting gallery: each unlocked entry is one real mẫu with its documented meaning and sources. Simultaneously the CRUD/search-filter surface (`BRIEF-03`/`BRIEF-05`), the Report §2 evidence, and `mg_match`'s content source — one screen, four requirements |
| Omen | **Điềm báo** — "tin từ tỉnh": chiến sự lan về vùng; lịch offset đã tới Hà Nội; đoàn khảo sát hồ sơ sắp về làng | on at every difficulty: each of these was genuinely knowable |
| Stat HUD | `NGHỀ · SINH KẾ · TIẾNG · NGƯỜI` | no synonyms, ever |


---

## 6 · Why this holds criterion 1's top band

The Excellent test — *"could not be transferred to an unrelated subject without the game breaking"* —
is carried by four locks, each welded to a researched fact:

1. **The win condition is transmission**, and transmission is the *definition* of living heritage.
   Re-skin the game to an unrelated subject and `truyen_nhan`/`ho_so` stop meaning anything.
2. **The two-sided stats encode the heritage double death** — neglect at 0, commodification at 100 —
   which is the actual policy problem the Đề án 2026–2035 exists to solve.
3. **The final trial is a real, dated event whose published decision text is the win check.** The
   game's judgment day happened, on 9 Dec 2025, at 14:38, and it judged preparation over wealth.
4. **The minigames teach the craft's own logic** — the meanings on the sheets, the order of the
   ván — content that only exists because the subject is this craft.

All four locks live in **the one run every player finishes** (§3), so no marker can reach the end
without meeting them. The schedule can thin the weave pool or the prose; it cannot cut the present
day out of the game.

**Presentation obligation:** chapter I's spine runs through famine, war and displacement, because
the craft's own timeline does. Every player verb is still a craft verb — carry, teach, share, return
— but a demo that walks chapter I front to back would show the hardship without the craft. The video
and report open on the customs cards + the codex + a minigame, then jump to chapter III, and say the
design choice out loud: *the war is weather, not the subject.*

And the quietest lock: **the player's reward for winning is the thing the player was playing about**
— the codex fills with the real paintings. Culture as the reward loop, not the wallpaper.
