# Level 2 — Khởi nghĩa Lam Sơn (1418–1427)

**Play pattern: build legitimacy from nothing.** The player starts at the floor — no treasury, no
standing army, no recognised throne. Opposite of Level 1, where the player starts strong and spends.

> ⚠️ Research scaffold. `VERIFY` markers are unconfirmed. Card text is written by the team.

---

## Confirmed spine

✅ **Timeline verified 15 Aug 2026** against vi.wikipedia "Khởi nghĩa Lam Sơn".

| Year | Event | Status |
| --- | --- | --- |
| 1407 | Ming annexes Đại Ngu, creates the province of Giao Chỉ; forced Hán-hoá policy breeds revolt | ✅ |
| 1418 | **Lê Lợi** raises the banner at **Lam Sơn, Thanh Hóa**. Early years go badly — weak resistance, heavy losses | ✅ |
| **1419** | **Lê Lai** volunteers to impersonate Lê Lợi to draw off Ming pursuit, letting Lê Lợi escape | ✅ |
| **1424** | **Nguyễn Chích's plan adopted**: drive into and liberate **Nghệ An**, use it as the springboard. The stated turning point of the whole uprising | ✅ |
| 1426 | Forces move north under **"tránh mạnh đánh yếu"**. **Tốt Động – Chúc Động** defeats Vương Thông's superior force; popular support swings behind the uprising | ✅ |
| 1426–27 | **Địch vận + tâm lý chiến** — psychological and subversion campaign, plus diplomacy, to talk besieged citadels into surrender | ✅ |
| 1427 | Minh Tuyên Tông sends **Liễu Thăng and Mộc Thạnh with 110,000 troops** in two columns to relieve Vương Thông | ✅ |
| 1427 | **Chi Lăng – Xương Giang** annihilates Liễu Thăng's main column; **Liễu Thăng killed**. Mộc Thạnh withdraws and is beaten in pursuit | ✅ |
| **16 Dec 1427** | **Hội thề Đông Quan** — Vương Thông surrenders, Ming permitted to withdraw safely | ✅ exact date |
| **1428** | **Nguyễn Trãi** writes **Bình Ngô đại cáo** for Lê Lợi. Lê Lợi takes the throne; Hậu Lê begins | ✅ |

✅ **Date tension resolved.** The uprising ends **1427** (Hội thề Đông Quan, 16 Dec); Bình Ngô đại cáo
is **1428**, written *after* the war as a proclamation of victory. Both dates stand — they are simply
sequential. Order your cards accordingly.

### The level's real shape, now confirmed

The sources describe exactly the arc the design wanted, which is unusually lucky:

1. **Start at the floor** (1418–1423): losing, hiding, Lê Lai dying to buy an escape.
2. **The redirection** (1424): abandon the home base for a viable one. Nguyễn Chích's plan is the
   documented turning point — this is a genuine `can_cu_moi` carrier, not a designer's invention.
3. **Legitimacy flips the war** (1426): after Tốt Động – Chúc Động the population comes over. Support
   is *earned by winning visibly*, which is exactly a `chinh_danh` counter.
4. **Talk, don't storm** (1426–27): citadels taken by subversion and diplomacy. `tam_cong` confirmed
   as a real strategy, not a romantic gloss.
5. **Kill the relief, not the city** (1427): Đông Quan was besieged and holding out *for the relief
   column*. Destroying that column ended the war. This is the level's signature dilemma, and it is
   historically load-bearing rather than invented.

---

## Candidate preparation flags

| Flag | Represents | Carrier card — real event | Status |
| --- | --- | --- | --- |
| `can_cu_moi` | Abandoning the home base for a viable one | **Nguyễn Chích's plan, 1424 — Nghệ An** | ✅ confirmed as the turning point |
| `tam_cong` | Winning by breaking enemy will rather than by killing | **địch vận / tâm lý chiến + diplomacy, 1426–27** | ✅ strategy confirmed; `VERIFY` only whether "tâm công" is the correct term and whether it is properly Nguyễn Trãi's |
| `chinh_danh` *(counter 0–3)* | Accumulated legitimacy — a state, not a rebellion | multiple; the swing after **Tốt Động – Chúc Động, 1426** is the big one | ✅ mechanism confirmed |
| `vien_binh_bi_chan` | Destroying the relief army instead of storming the city | **Chi Lăng – Xương Giang, 1427** | ✅ confirmed, incl. Liễu Thăng's death |

`chinh_danh` should be a **counter**, not a flag — legitimacy accumulates. It is also the natural
carrier of the level's lesson, so it belongs in `requireCounter`, not `requireAll`.

### Costs

- `can_cu_moi` → abandon accumulated position; `dan` down locally, `kho` down
- `tam_cong` → slower than fighting; the enemy strengthens meanwhile — `binh` opportunity cost
- `vien_binh_bi_chan` → deliberately **not** taking the city while it is within reach

That last one is the level's signature dilemma: the tempting move is to storm Đông Quan; the
historically correct move is to destroy the relief column first. Make the tempting move available and
let it lose.

---

## Final trial

```
finalTrial: expulsion of Ming forces (1427)
  requireAll:        [can_cu_moi, vien_binh_bi_chan]
  requireCounter:    { chinh_danh: 2 }
  insufficientAlone: [binh, kho]
  defeatByStatsText: a rebellion that never became a state cannot end a war by
                     treaty — it can only be crushed later
```

Note `insufficientAlone` includes `kho` here, unlike Level 1. Different level, different wrong
instinct: in Level 1 the trap is raw force, here it is trying to buy the outcome.

---

## Reading

- `https://vi.wikipedia.org/wiki/Khởi_nghĩa_Lam_Sơn` — encyclopedia, accessed 15 Aug 2026
- `http://www.quan8.hochiminhcity.gov.vn/dantaphaibietsuta/` — "Nhà Minh đô hộ Đại Việt (1407–1427)"
- `https://baothainguyen.vn/chinh-tri/200809/khoi-nghia-lam-son-...` — press feature
- **Bình Ngô đại cáo** — primary text, and quotable in-game with attribution
- **Lam Sơn thực lục**, **Đại Việt sử ký toàn thư** — primary chronicles
