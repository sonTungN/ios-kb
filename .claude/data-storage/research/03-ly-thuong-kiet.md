# Level 3 — Nhà Lý vs Tống (1075–1077)

**Play pattern: strike first, then hold a line.** Two distinct halves — an offensive phase where
waiting is punished, then a defensive phase where attacking is punished. The player must reverse
their own strategy mid-level. No other level does this.

> ⚠️ Research scaffold. `VERIFY` markers are unconfirmed. Card text is written by the team.

---

## Confirmed spine

| Year | Event | Confirmed by |
| --- | --- | --- |
| 1075–76 | **Lý Thường Kiệt** attacks pre-emptively into Song territory; **Ung Châu** falls | vi.wikipedia (Chiến tranh Tống–Việt lần thứ hai) |
| — | Doctrine: **"tiên phát chế nhân"** — strike first to control the enemy | vi.wikipedia; tapchiqptd.vn |
| — | Stated aim: destroy the Song forward logistics base before it can be used | vov2.vov.vn; facebook history group |
| 1077 | Song counter-invasion halted at the **Như Nguyệt** river line; battle runs for **months** | vi.wikipedia |
| 1077 | Outcome: Song invasion will broken; Song forced to **recognise Đại Việt as a state** | vi.wikipedia |

### ✅ The Như Nguyệt line — verified, and it is NOT Bạch Đằng

The suspected contamination was real, and it is now resolved. The Như Nguyệt line was:

- an **earthen rampart** (lũy đất),
- faced with a **dense bamboo palisade** (cọc tre dày làm dậu) — *on the bank, as a fence*,
- with **concealed spike pits** (hố chông ngầm) on the river flats below.

That is a **land fortification along a river**. It is categorically different from Bạch Đằng 1288,
where stakes were set **in the riverbed** and timed to the tide to hole and trap ships.

Two consequences:

1. **Never write "cọc dưới lòng sông" for Như Nguyệt.** Popular sources blur the two; the chronicle
   picture does not. Getting this right is cheap evidence of real research.
2. **The levels stay mechanically distinct.** Bạch Đằng is a *trap sprung once* on a fleet; Như
   Nguyệt is a *line held for months* against repeated assault. Model them differently — a one-shot
   flag with tidal timing versus an attrition condition that must survive several waves.

### ✅ Nam quốc sơn hà — the attribution is weaker than "disputed"

The scholarly picture is stronger than first flagged, and more interesting:

- **Author unknown.** Most researchers list it as **khuyết danh** (anonymous).
- **Lê Mạnh Thát** attributes it to **Đỗ Pháp Thuận**.
- **Recent consensus:** the poem appeared under **Lê Đại Hành** and was *later reused* by Lý Thường
  Kiệt — so it **predates the 1077 campaign entirely**.
- Textually it is unstable: **35 book variants and 8 thần tích variants**.
- Earliest surviving text: **Việt điện u linh tập**. Best-known version: **Đại Việt sử ký toàn thư**,
  the first official chronicle to record it.
- It attaches to **two** wars: Lê Hoàn vs Song in **981**, and Lý Thường Kiệt vs Song in **1077**. In
  ĐVSKTT and Việt điện u linh it is *heard being recited from the shrine of Trương tướng quân at
  night* — presented as a portent, not as authorship.

**Do not write "Lý Thường Kiệt wrote Nam quốc sơn hà."** It is the single most repeated error about
this campaign.

The honest handling is also the highest-scoring one: `historicity: "simplified"`, keep the poem in
the game because the *morale effect* is what the chronicle actually describes, and let
`historicalNote` say plainly that authorship is unknown, that the poem likely predates Lý Thường
Kiệt, and that the chronicle frames it as a voice heard from a shrine. A player learning *that* has
learned something most Vietnamese adults have wrong — which is exactly the "genuine insight" the top
rubric band asks for.

---

## Candidate preparation flags

| Flag | Represents | Carrier card — real event | Status |
| --- | --- | --- | --- |
| `tien_phat` | Attacking before being attacked | The 1075 decision to cross the border | doctrine confirmed |
| `pha_hau_can` | Destroying the forward supply base | Ung Châu | confirmed; `VERIFY` details |
| `phong_tuyen` | A prepared defensive line on the right river | **Như Nguyệt: earth rampart + bamboo palisade + spike pits** | ✅ composition confirmed |
| `chinh_nghia` | Framing the war as defensive/just, at home and abroad | the Nam quốc sơn hà episode | ✅ usable — but as a *morale portent*, not as authorship |

### Costs

- `tien_phat` → `dan` down (an unprovoked foreign war is unpopular), diplomatic standing down
- `pha_hau_can` → `binh` down (real casualties), `kho` down
- `phong_tuyen` → `kho` down, must be built *before* the player can see the invasion coming

`phong_tuyen` is the level's best card: the player must spend on a defence while nothing visibly
threatens them. Offer a tempting alternative use for the same treasury on the same card.

---

## Final trial

```
finalTrial: Song counter-invasion halted (1077)
  requireAll:        [pha_hau_can, phong_tuyen]
  requireAny:        [tien_phat, chinh_nghia]
  insufficientAlone: [binh, dan]
  defeatByStatsText: a large army with no prepared line and an intact enemy
                     supply base is defeated in detail
```

---

## Alternative if this level proves too thin

**Tây Sơn / Quang Trung (1789, Ngọc Hồi – Đống Đa)** — the lightning Tết campaign against the Qing.
Its play pattern is *speed over preparation*, which is a genuine third axis and contrasts cleanly
with both Trần (endurance) and Lam Sơn (accumulation). Swap only if the Lý research runs dry; do not
add it as a fourth level — see the scope note in `../README.md`.

---

## Reading

- `https://vi.wikipedia.org/wiki/Chiến_tranh_Tống–Việt_lần_thứ_hai` — encyclopedia, accessed 15 Aug 2026
- `https://tapchiqptd.vn/vi/lich-su-quan-su-viet-nam/tu-tuong-tien-phat-che-nhan-...` — Tạp chí Quốc phòng toàn dân, military-history journal, the most citable of these
- `https://vov2.vov.vn/van-hoa-giai-tri/chien-luoc-quan-su-cua-ly-thuong-kiet-...` — VOV feature
- **Việt sử lược**, **Đại Việt sử ký toàn thư** — primary chronicles
- For the Nam quốc sơn hà attribution question, find a literary-history source specifically; general
  history sources tend to repeat the traditional attribution uncritically.
