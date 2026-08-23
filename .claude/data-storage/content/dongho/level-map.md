# Hành trình một mạch — Tranh Đông Hồ 1938–2025 · full card map (36 dated cards + 4 drawn)

**Team decision, 22 Aug 2026: one game, one continuous run.** The three eras are **chapters inside a
single progress** (banner interstitials at the era turns), not separate levels — so a marker or an
Experience Day visitor experiences the whole educational arc, including the living-heritage present,
in one sitting. `BRIEF-05` §3 is satisfied on its own wording — *"levels **or stages** of increasing
difficulty"* — each chapter introduces new mechanics and new educational elements; the Chọn di sản
screen's "Gốm · Quan họ — sắp ra mắt" tiles keep the *levels* dimension visible.

Facts and statuses: `../../research/04-dong-ho-tranh-dan-gian.md`. Design rationale:
`../../design/dongho-game-design.md`. **Reachability is machine-checked**: the card table below is
mirrored in `../../tools/trace_run.py`, which beam-searches the full choice space — change a number
here, change it there, re-run. This closes the reachability gap open since the Trần card-16 finding.

**Starting stats** — `nghe 60 · sinh_ke 50 · tieng 55 · nguoi 50`. Every stat fails at `≤ 0` and
`≥ 100`. POV: one fictional composite household among the 17 dòng họ; real people appear in anchors
and `historicalNote` only.

---

## Chapter structure (sub-progress inside one run)

| Chương | Cards | Years | New educational elements | Banner |
| --- | --- | --- | --- | --- |
| I · **Giữ lửa** | 1–12 | 1938–1954 | The loop; craft process & Tết customs; ledger; `mg_match` at card 9 | (opening briefing) |
| II · **Giữ nếp** | 13–22 | 1967–1990 | The counter (truyền thừa); echoes; the economy of a craft under an institution | chapter banner before card 13 |
| III · **Hồi sinh** | 23–36 | 1992–2025 | The expiring window; ceiling crises become the danger; `mg_assemble`; heritage policy & the present day | chapter banner before card 23 |

A chapter banner is a **non-decision interstitial**: era title, one line of bridge text, and a
snapshot of the Sổ gia truyền — the "sub-progress" moment made visible.

---

## The cards

Legend — Role: `setup` · `pressure` · `carrier` (grants) · `relief` · `trap`. Effects
`nghe / sinh_ke / tieng / nguoi`. His: ✅ documented · `S` simplified (year/framing approximated —
declared in JSON) · `D` design/invented. ᵃ = year approximated within its documented span.

| # | Year | Card id | Anchor | Role | Choice A → | Choice B → | Mechanics |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1938 | `phien-cho-thang-chap` | Chợ tranh, 5 phiên tháng Chạp `S` | setup | bày đủ năm phiên `0/+5/+5/0` | chỉ phiên chính `0/+10/−5/0` | |
| 2 | 1940 | `von-lieng-cua-nghe` | Supply chains: dó Đống Cao, điệp, thuốc cái `S` | relief | sắm đủ `+10/−15/0/0` | đồ cũ `−5/+5/0/0` | |
| 3 | 1941 | `mua-cuoi-hoang-kim` | 17 dòng họ printing `S` | pressure | thuê thợ mở xưởng `0/−5/+5/+10` | giữ nếp nhỏ `+5/+5/0/−5` | |
| 4 | 1944ᵃ | `phien-cho-vang` | The chợ dies mid-40s `S` | setup | vẫn dọn đủ phiên `0/−5/+10/0` | nghỉ chợ chạy hàng xén `0/+10/−10/0` | |
| 5 | 1945 | `doi-at-dau` | Ất Dậu famine ✅ | pressure | chia gạo `0/−10/0/+5` | đóng cửa `0/+5/−10/−10` | echo (chose:share) |
| 6 | 1946 | `toan-quoc-khang-chien` | War begins ✅ | setup | tản cư sớm `0/−10/0/0` | nán lại giữ xưởng `+5/+5/0/−10` | omen before |
| **7** | **1947ᵃ** | **`lang-chay`** | Village burns, blocks scatter `S` | **carrier** | **ôm ván `0/−10/−10/0` → `giu_van`** | gánh hàng `−15/+10/0/0` | floor `nguoi ≥ 20` · advisor |
| 8 | 1948 | `ben-kia-song-duong` | Hoàng Cầm's poem ✅ | relief | chép thơ `0/0/+10/0` | thơ không đổi gạo `0/+5/0/−5` | |
| **9** | **1949ᵃ** | **`tan-cu-day-nghe`** | The recipe passes in evacuation `S` | **carrier** | **mở lớp `+5/−5/0/+5` → `giu_bi_quyet`** | ai lo phận nấy `−10/+5/0/−5` | floor `nghe ≥ 25` · advisor · **mg_match** |
| 10 | 1950 | `viec-tot-thanh-pho` | Wartime city work `S` | pressure | cho con ra phố `0/+20/0/−15` | ở cùng nhau `0/−5/0/0` | echo (chose:send) |
| **11** | **1951ᵃ** | **`lai-buon-do-co`** | Dealer bids for the rescued blocks `S` | **trap** | **bán ván `0/+25/0/0` — revokes `giu_van`** | không bán `0/−5/0/0` | echo (chose:sell) |
| 12 | 1954 | `ve-lang` | Return at peace ✅ | carrier-tick | về làng `0/−5/+5/+5` → **tick +1** | ở lại nơi làm ăn được `0/+15/−10/−5` | |
| 13 | 1967 | `htx-thanh-lap` | HTX founded — 50 artisans ✅ | relief | gửi người vào HTX `0/+15/+5/−5` | giữ xưởng riêng `+5/−5/−5/0` | chapter banner before |
| 14 | 1970ᵃ | `mau-cai-tien` | "Cải tiến" orders `S` | pressure | in mẫu mới `−10/+10/0/0` | xin giữ lối cũ `+5/−5/−5/0` | |
| 15 | 1972ᵃ | `day-con-trong-xuong` | Teaching your child `S` | carrier-tick | dạy con sau giờ `0/−5/0/+5` → **tick +1** | cho con thoát nghề `0/+5/0/−10` | |
| 16 | 1975 | `dat-nuoc-lien-mot-dai` | Reunification ✅ (market framing `S`) | setup | đem tranh vào nam `0/+5/+5/0` | chưa vội `0/0/0/+5` | |
| 17 | 1980ᵃ | `don-xuat-khau` | Export era `S` | pressure | nhận đơn lớn `−5/+15/0/0` | làm ít giữ kỹ `+10/−5/0/0` | |
| **18** | **1982ᵃ** | **`luu-mau-co`** | Archiving the classics `S` | **carrier** *(optional)* | **âm thầm lưu bộ mẫu `+5/−10/−5/0` → `giu_mau_co`** | mẫu cũ để bụi `0/+5/0/0` | floor `nghe ≥ 25` |
| 19 | 1986 | `doi-moi` | Đổi mới ✅ | setup | đón thị trường `0/+10/0/−5` | dè chừng `0/−5/0/0` | |
| 20 | 1987ᵃ | `con-muon-o-lai` | A child chooses the craft `S` | carrier-tick | cho con ở lại xưởng `0/−10/0/+5` → **tick +1** | con ra chợ lớn `0/+10/0/−10` | |
| 21 | 1989ᵃ | `lich-offset-tran-ve` | Offset calendars flood Tết `S` | pressure | hạ giá đấu lịch `0/−5/+5/0` | giữ giá mặc kệ `+5/−5/−10/0` | omen before |
| **22** | **1990** | **`htx-giai-the`** | HTX dissolves; the mã trade calls ✅ | **trap** | **chuyển xưởng sang mã `−15/+25/0/0` — revokes `giu_mau_co`, tick −1** | giữ xưởng tranh `0/−5/0/0` | echo (chose:ma) |
| **23** | **1992ᵃ** | **`nhat-ve-tung-tam`** | The buy-backs begin `S` | **carrier** | **dốc vốn chuộc ván `0/−15/+5/0` → `phuc_hoi_van`** | tiền đâu mà chuộc `0/+5/0/0` | floor `sinh_ke ≥ 20` · advisor · chapter banner before |
| 24 | 1995ᵃ | `khach-tay-dau-tien` | First foreign visitors `S` | relief | tiếp chuyện kể nghề `0/+5/+5/0` | ngại, từ chối `0/0/−5/+5` | |
| 25 | 2000ᵃ | `hang-du-lich` | Tourist-ware temptation `S` | pressure | in nhanh hàng chợ `−10/+15/0/0` | giữ lối in tay `+5/−5/0/0` | |
| 26 | 2006 | `dung-nha-trung-bay` | The private center rises ✅ | pressure | dồn của dựng nhà trưng bày `0/−15/+5/0` | chưa phải lúc `0/+5/−5/0` | |
| **27** | **2008** | **`mo-cua-don-khach`** | Experience classes open ✅ | **carrier** *(optional)* | **mở lớp trải nghiệm `−5/−5/+5/+5` → `mo_cua`** | xưởng không phải chỗ chơi `+5/+5/−5/0` | floor `tieng ≥ 20` · **mg_match reprise** |
| 28 | 2012 | `di-san-quoc-gia` | QĐ 5079 — national heritage ✅ | setup | rước bằng về xưởng `0/−5/+5/0` | nhận lặng lẽ `0/+5/0/0` | |
| 29 | 2013ᵃ | `doan-truong-den-xuong` | School groups `S` | relief | đón các đoàn `0/+5/0/+5` | bận đơn `0/+10/−5/−5` | |
| **30** | **2015ᵃ** | **`chau-noi-nghe`** | The grandchild takes the craft `S` | **carrier** | **lễ nhận cháu vào nghề `0/−10/0/+10` → `truyen_nhan`** | cháu làm văn phòng `0/+10/0/−10` | floor `nguoi ≥ 20` · advisor · **mg_assemble** |
| **31** | **2017** | **`ho-so-khoi-dong`** | The dossier work starts `S` | **carrier** | **cùng tỉnh làm hồ sơ `−5/−10/+5/0` → `ho_so`** | giấy tờ không in ra tranh `0/+5/0/0` | floor `tieng ≥ 25` · advisor |
| 32 | 2019ᵃ | `noi-tieng-tren-mang` | Viral fame `D` | pressure | nhận hết đơn `−10/+10/+10/0` | giữ nhịp xưởng `+5/−5/−5/0` | |
| **33** | **2020** | **`han-chot-31-3`** | The 31 Mar deadline ✅ | **carrier** *(last chance)* | **chạy nước rút `−10/−15/0/−5` → `ho_so`** (only if not yet held) | lỡ hẹn / đã nộp xong `0/+5/0/0` | floor `tieng ≥ 25` · omen before · `ho_so` **expires after this card** |
| 34 | 2023 | `trung-tam-nha-nuoc` | State center opens ✅ | setup | gửi ván quý sang trưng bày `0/0/+10/0` | giữ hết ở nhà `+5/0/−5/0` | |
| 35 | 2025 | `tranh-len-ao-dai` | Đông Hồ on Tết áo dài ✅ | relief | hợp tác nhà thiết kế `−5/+5/+10/0` | tranh để in, không để mặc `+5/0/−5/0` | |
| 36 | 2025 | `dem-truoc-new-delhi` | The eve of 20.COM `D` | setup | thắp hương ông bà `0/0/+5/0` | soạn lại ván in `+5/0/0/0` | |

→ **FINAL TRIAL: 9 Dec 2025, New Delhi — the Committee reads the ledger.** One trial, three
questions, three mechanisms — the three "shapes" fused:

- **Recognise** (`requireAll`): `giu_bi_quyet` · `truyen_nhan` · `ho_so` — the knowledge chain, an
  heir, the story told in time.
- **Either path for the blocks** (`requireAny`): `giu_van` **or** `phuc_hoi_van` — carried through
  the fire, or bought back sheet by sheet. Both are the documented history; losing the blocks in
  1951 is not death, it is the opening of the costlier road.
- **Sustain** (`requireCounter`): `truyen_thua ≥ 2` of 3 ticks (về làng 1954 · dạy con 1972 · con ở
  lại 1987) — and the 1990 trap can **take one back**.
- **Capacity floor** (`statGate`): `nghe ≥ 15 · sinh_ke ≥ 10 · tieng ≥ 10 · nguoi ≥ 15` — never
  sufficient, `sinh_ke` declared `insufficientAlone`. `mo_cua` and `giu_mau_co` are bonus slots.

### Carrier floors — the means to act

| Card | Flag | Floor | Cannot, because |
| --- | --- | --- | --- |
| 7 | `giu_van` | `nguoi ≥ 20` | blocks are heavy; no hands, no rescue |
| 9 | `giu_bi_quyet` | `nghe ≥ 25` | you cannot teach what you no longer hold |
| 18 | `giu_mau_co` | `nghe ≥ 25` | archiving needs a hand that knows what matters |
| 23 | `phuc_hoi_van` | `sinh_ke ≥ 20` | you cannot buy back with nothing |
| 27 | `mo_cua` | `tieng ≥ 20` | no one visits an unheard-of workshop |
| 30 | `truyen_nhan` | `nguoi ≥ 20` | a lineage of one has no one to receive |
| 31/33 | `ho_so` | `tieng ≥ 25` | a dossier no one has heard of persuades no one |

All floors sit below half-range and below every start (three sit at the band edge, 25); advisors
precede cards 7, 9, 23, 30, 31 (Khó suppresses them — its premise). **Card 33 is a conditional pair occupying one spine
slot** (holder → confirmation setup; non-holder → the dear last chance): exactly one version always
appears, so the spine is never skipped.

---

## Why the maths works — machine-checked

`python3 tools/trace_run.py` (beam 6000, crisis accept/refuse branching) proves:

- **Canonical line exists on Thường** taking *all seven flags*, all 3 ticks, refusing both traps,
  showing both minigames, with exactly **one accepted crisis** (`vay_phuong` as the ch-I squeeze
  bites): `1A 2A 3B 4B 5A 6B 7A 8A 9A 10B 11B 12A(+cx) 13A 14B 15A 16A 17A 18A 19A 20A 21B 22B 23A
  24A 25A 26B 27A 28B 29A 30A 31A 32A 33B 34B 35A 36B` → end `nghe 70 · sinh_ke 65 · tieng 65 ·
  nguoi 70`.
- **Canonical line exists on Khó** (no crises at all), same completeness → end `60/55/60/60`.
- Thousands of distinct winning end-states exist on both difficulties (hundreds crisis-free on
  Thường), and lines that lose `giu_van` at card 11 can still win through `phuc_hoi_van` — the
  requireAny recovery works as designed.

**The chapter-I squeeze is intact**: on historical lines `sinh_ke` bottoms at 5–20 through cards
9–12 (the intended crisis window). The *optimized* end-states are comfortable — see balance note 1.

### Balance register (v1 — the honest list)

1. **Optimized play ends richer than the historical flavour line** (~65 sinh_ke). Accepted and
   reframed: *the historical path is squeezed; a knowing replayer can arrive comfortable.* The trial
   still ignores wealth (`insufficientAlone`).
2. **The 1990 trap has teeth against the win condition**: `−1 truyen_thua` tick — a family with all
   3 ticks survives it (slack rewards preparation); with 2 it quietly unwins. The run review must
   name it.
3. **Chapter III band pressure is deliberately hot** (fame-era ceilings) — the canonical Thường line
   brushes a ceiling once (offer refused). Playtest the ceiling texts.
4. **Forced-death and blocked-floor corners** at deep-poverty entries to cards 23/26/33 exist on
   Khó by premise — and on Thường, a player who spent the `sinh_ke` rescue in the chapter-I squeeze
   approaches the card-23 floor (`sinh_ke ≥ 20`) without a net. Run-review copy must name them.
5. **First-run discovery**: ledger opens at the first flag (card 7 of 36 — 29 cards of runway,
   better than Trần's 15). Demo account still ships on Dễ per README notes.
6. **Sim accounting**: refused crisis offers are silent in the printed line; the tool's "crises
   fired" counts accepts only.

---

## Beyond the 36: drawn and triggered

| Type | Fires | Notes |
| --- | --- | --- |
| `chapter` | before cards 13, 23 | NEW interstitial type: era banner + bridge text + ledger snapshot |
| `advisor` | before 7, 9, 23, 30, 31 | off on Khó |
| `omen` | before 6, 21, 33 | the war; the offset flood; **the closing window** — all genuinely knowable |
| `echo` | after 5, 10, 11, 22 | conditions `chose:share/send/sell/ma` |
| `ambient` | ≤3 per run, ≥4 apart | pool 8 (unchanged) |
| `crisis` | band entry, once per stat-side per run | the same 8; `oncePerLevel` now spans the whole run |
| `weave` | 4 per run | pool 17, chapter-tagged — below |

### Weave (pool 17, slots C1: 2 · C2: 1 · C3: 1)

C1 (12): the existing pool (`khach-dat-tranh-cuoi`, `con-gai-xin-hoc`, `phuong-vay-van`,
`mua-dam-hong-giay`, `thet-moi-dao-tu`, `thuong-lai-ep-gia`, `hang-xom-xin-mau`,
`tre-nghich-xuong`, `nguoi-la-hoi-nghe`, `gio-to-nghe`) + `kheo-tay-kiem-song` and
`ban-dat-hay-giu` **demoted from the old spine** (undated, no flags — legal weave).
C2 (3): `doan-van-cong` (retagged), `tem-phieu-thang-kho`, `can-bo-hoi-mau-moi`.
C3 (2): `phong-vien-ve-lang`, `khach-mua-do-gia`.
Laws unchanged: `year: null`, never a required flag, `simplified`/`invented` only, effects ≤ ±8,
solvency budget `sinh_ke ±12`, others ±15 (player-chosen worst case; forced weave loss ≤ 1 under
protective play).

### Run length

36 spine + 4 weave + 2 banners + ≤3 ambient + ~9 interstitials + 0–8 crises ≈ **50–62 screens ·
15–20 phút** — one full sitting, the whole arc (Khó lean ≈ 45). Per-card text canon: prompt ≤ 2
câu · outcome ≤ 2 câu · historicalNote ≤ 2 câu — the player did not come to read walls of text.

---

## What the team still writes

- **Spine prose**: 36 × 6 × 2 ≈ **432 strings** (each card cites `research/04`).
- **Weave prose**: 6 new/adapted cards ≈ 72 strings (11 already drafted).
- **System prose**: chapter banners/bridges, trial texts (drafted in JSON), crisis/ambient reuse
  ≈ 60 strings.
- **≈ 620–700 strings total — one-third less than the 3-màn plan**, one JSON, one trial, one map.
- **Validator follow-ups**: minigame check; conditional-pair (card 33) support; the sim covers
  reachability.
- **Codex obligation**: the "đỏ" pigment entry carries both traditions (sỏi son/gỗ vang **and**
  hoa hiên).
