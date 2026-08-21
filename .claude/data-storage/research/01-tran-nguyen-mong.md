# Level 1 — Nhà Trần vs Nguyên Mông (1258–1288)

**Play pattern: sacrifice to survive.** The player starts strong and must deliberately give up
territory, treasury and short-term popularity to win. Every correct move looks like losing.

> ⚠️ This file is a **research scaffold**, not content. The spine below came from the sources listed
> at the bottom; anything marked `VERIFY` was not confirmed and must be checked before use. Card
> text (`prompt`, `outcome`, `historicalNote`) is written by the team, from sources, in vi + en.

---

## Confirmed spine

| Year | Event | Confirmed by |
| --- | --- | --- |
| 1258 | First invasion. Thăng Long taken, then Mongol withdrawal. Đông Bộ Đầu associated with this campaign | vi.wikipedia; kidsup summary |
| 1285 | Second invasion, much larger. Đại Việt counteroffensive after initial losses. Hàm Tử / Chương Dương / Tây Kết associated with this campaign | vi.wikipedia; kidsup summary |
| 1287–88 | Third invasion. Vân Đồn, then decisive victory at **Bạch Đằng (1288)** | vi.wikipedia; kidsup summary |
| — | Commander **Trần Hưng Đạo**; tactics include **scorched earth** and **strategic retreat** | vi.wikipedia |
| — | Outcome: sovereignty preserved, with nominal submission to the Mongol empire | vi.wikipedia |

`VERIFY` — the total fighting time is given by vi.wikipedia as roughly **nine months across the three
campaigns**, spread over 1258–1288. Worth confirming, because it is a striking fact and useful for
the How-To-Play screen.

### ✅ Hội nghị Diên Hồng — verified 15 Aug 2026

| | |
| --- | --- |
| Year | **1284** |
| Where | Thăng Long, before the Diên Hồng hall |
| Convened by | **Thượng hoàng Trần Thánh Tông** — the *Retired Emperor*, not the reigning one |
| Attending | **bô lão** (village elders) from across the country |
| Question put | **hòa hay đánh** — make peace, or fight |
| Answer | **"Đánh"** — reportedly shouted in unison |
| Position | immediately **before the second invasion (1285)** |
| Recorded in | **Đại Việt sử ký toàn thư** |

Two design notes fall out of this:

**It was consultative, not a command.** The court *asked* and was answered. That is what makes it a
legitimate `long_dan` carrier — the cost is the throne binding itself to a popular answer it then
cannot walk back. Model the cost as `than` down (the court cedes standing by consulting commoners)
and make the flag **irrevocable** once granted: having asked the nation and been told "fight", the
player can no longer choose to sue for peace. That is a rule the history generates directly.

**Convened by the Thượng hoàng.** The Trần ran a dual monarchy — a retired senior emperor alongside
the reigning one. That is a distinctive Trần institution, not generic monarchy, and it is a strong
candidate for a level-specific mechanic if you want a second culture-driven rule (e.g. a second
adviser voice whose approval is a separate resource). Optional; do not let it expand scope.

---

## Candidate preparation flags

Design proposal. The team confirms each against a source before it becomes a flag.

| Flag | Represents | Carrier card — real event | Status |
| --- | --- | --- | --- |
| `tieu_tho` | Scorched earth; deny the invader supply | Decision to empty and abandon Thăng Long | tactic confirmed; tie to a specific dated decision — `VERIFY` |
| `long_dan` | Popular consent to a war of endurance | **Hội nghị Diên Hồng, 1284** | ✅ **CONFIRMED** — see below |
| `coc_bach_dang` | Naval trap prepared in advance | Stakes planted in the Bạch Đằng riverbed | tactic strongly associated with 1288; `VERIFY` the preparation timeline |
| `hau_can_dich` | Cutting the enemy supply fleet | **Vân Đồn** (1287) | `VERIFY` commander and effect |

Four flags is one more than needed. Pick **three** for the final trial and let the fourth be an
optional card that eases a stat cost — that rewards a second playthrough without gating victory.

### Costs to attach (the cost rule)

Each carrier choice must hurt when taken:

- `tieu_tho` → `kho` down hard, `dan` down (people lose homes), `binh` unchanged
- `long_dan` → `than` down (the court cedes authority by consulting commoners)
- `coc_bach_dang` → `kho` down, and time/`binh` diverted from conventional forces

Historically these were real costs. Find what each actually cost and use that, rather than inventing
numbers first and justifying them later.

---

## Final trial

```
finalTrial: Nguyên Mông, third invasion (1288)
  requireAll:        [tieu_tho, long_dan, coc_bach_dang]
  insufficientAlone: [binh]
  defeatByStatsText: must explain that meeting this army in open conventional
                     battle is precisely how the campaign is lost
```

`insufficientAlone: [binh]` is the point of the level. The Trần did not out-muster the Yuan. A player
who maxed `binh` and skipped the preparations must lose, and be told why.

---

## Reading

Start here, then move to real scholarship — Wikipedia is a finding aid, **not** an acceptable sole
citation for the report.

- `https://vi.wikipedia.org/wiki/Chiến_tranh_Nguyên_Mông_–_Đại_Việt` — encyclopedia, accessed 15 Aug 2026
- `https://www.kidsup.net/3-lan-chong-quan-mong-nguyen/` — school-level summary, useful only for the campaign-name mnemonic
- `http://www.quan8.hochiminhcity.gov.vn/dantaphaibietsuta/` — government local-history portal
- **Đại Việt sử ký toàn thư** — the primary chronicle. At least one card per flag should cite it.
- SGK Lịch sử lớp 7 — matches the level the game teaches at, and is a defensible citation.
