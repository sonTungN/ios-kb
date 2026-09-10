# Kế hoạch viết 36 lá spine · Tranh Đông Hồ

Bản để duyệt trước khi bắt tay. Viết 08/09/2026. Số liệu trong đây đọc từ
`game_contents.json`, `card.schema.json`, `tools/validate_data.py` và `level-map.md` tại thời điểm
viết, không có con số nào tự nghĩ ra.

---

## 1 · Khoảng trống, và vì sao mọi thứ đang chờ nó

Engine đã xong và chạy hết một ván. Weave 17 lá, ambient 8, crisis 8, interstitial 14, trial, bốn
kết thúc: đã có prose thật, có `effectReasons` cho từng chỉ số dịch chuyển. Tranh minh hoạ đủ 36 lá
spine cộng 17 weave, 8 ambient, 8 crisis, 9 trang briefing.

Thiếu đúng một thứ: **`cards/*.json`, 36 lá bài có năm**. Chúng chưa từng được viết. Hệ quả:

| | Hiện tại | Sau khi có 36 file |
| --- | --- | --- |
| Bản DEBUG | Chơi được, nhưng mọi chữ là `[Nháp]` từ `PlaceholderSpine.swift`, không có chip lý do nào | Prose thật, chip thật, placeholder tự tắt |
| Bản Release | `spine` rỗng, `isContentReady` false, không bắt đầu ván được | Chơi được |
| Linter | 8 error, tất cả đều là "cờ X trỏ tới carrier không tồn tại" | 0 error |
| Echo sau lá 5, 10, 11, 22 | Không bao giờ nổ, vì không lá nào khai `chose:` tag | Nổ đúng theo lựa chọn |

Không cần sửa một dòng Swift nào. Bỏ file vào bundle là xong.

---

## 2 · Đầu ra

> Cập nhật 09/09/2026: 36 lá đã viết xong và gộp vào **một file** thay vì 36 file rời.

```
.claude/data-design/content/dongho/game_spine.json   ← soạn ở đây, linter và sim đọc ở đây
DaiViet/Resources/GameData/game_spine.json           ← copy sang đây (byte identical), app đọc ở đây
```

Cấu trúc: `{ "levelId": "dongho", "cards": [ lá 1, lá 2, ... lá 36 ] }`. Mỗi lá giữ nguyên schema
`card.schema.json`. **Id mang sẵn số thứ tự**, ví dụ `07-lang-chay`, để đọc file bằng mắt vẫn thấy
thứ tự; app vẫn sắp theo `order`. Mọi tham chiếu tới lá (carrierCardId, expiresBefore,
interstitial before/after, `trace_run.py`, `PlaceholderSpine.swift`) dùng đúng id có tiền tố này.

`CardDecoder` tìm `game_spine.json` như mọi file GameData khác, decode cả file, giữ lá có `levelId`
khớp level đang chơi. File hỏng thì báo lỗi như mọi file nội dung khác, không bỏ qua trong im lặng.

## 3 · Schema đầy đủ

Nguồn: `schema/card.schema.json`. Khoá lạ bị từ chối, trừ khoá bắt đầu bằng `_` (dùng để ghi chú
khi soạn, luôn được phép).

### Cấp lá

| Khoá | Bắt buộc | Kiểu | Ràng buộc |
| --- | --- | --- | --- |
| `id` | ✅ | string | kebab-case `^[a-z0-9]+(-[a-z0-9]+)*$`. Lấy đúng id trong `level-map.md`, không đặt mới |
| `levelId` | ✅ | string | `"dongho"` |
| `order` | ✅ | int ≥ 0 | 1 tới 36, đúng số thứ tự trong level map |
| `year` | ✅ trên thực tế | int hoặc null | Mọi lá trong `cards/` là spine nên **phải có năm**; linter báo lỗi nếu thiếu. `null` chỉ hợp lệ khi `historicity: invented`, và không lá spine nào ở trạng thái đó |
| `historicity` | ✅ | enum | `documented` / `simplified` / `invented`. Đây chính là ba nhóm Report mục 2 phải khai, nên khai thật thà |
| `sources` | ✅ | array ≥ 1 | Mỗi phần tử cần `title` và `type` (`primary`/`secondary`/`textbook`/`encyclopedia`); nên có thêm `url`, `locator`, `accessed`, `verifiedBy`. Chỉ có encyclopedia thì linter cảnh báo |
| `prompt` | ✅ | i18n | Tình huống, ≤ 2 câu |
| `choices` | ✅ | array **đúng 2** | Không hơn không kém |
| `historicalNote` | ✅ | i18n | Chuyện thật, **giống hệt nhau dù chọn A hay B** |
| `speaker` | ⬜ | i18n | Ai đang nói. Hiện ra dưới lá bài thay cho năm |
| `tags` | ⬜ | [string] | Nhãn tự do cho search và filter của màn Cách chơi |
| `appearsIf` | ⬜ | condition | `allOf` / `anyOf` / `noneOf` / `minOrder` / `maxOrder`. Bỏ trống với lá luôn xuất hiện |
| `oneShot` | ⬜ | bool | Mặc định true. Spine không cần khai |

### Cấp lựa chọn (`choices[i]`)

| Khoá | Bắt buộc | Kiểu | Ràng buộc |
| --- | --- | --- | --- |
| `label` | ✅ | i18n | Chữ trên banner chéo khi quẹt. Ngắn, là một hành động |
| `effects` | ✅ | {statId: int} | Chỉ `nghe`, `sinh_ke`, `tieng`, `nguoi`. Đúng bằng số trong level map |
| `outcome` | ✅ | i18n | Hậu quả của **lựa chọn này**, ≤ 2 câu. Được phép phản sự thật |
| `effectReasons` | ✅ trên thực tế | {statId: i18n} | **Một chip cho mỗi hiệu ứng khác 0**. ≤ 8 từ, ~60 ký tự mỗi ngôn ngữ. Thiếu chip là lỗi, chip mồ côi (cho chỉ số không dịch chuyển) cũng là lỗi |
| `grants` | ⬜ | [string] | Cờ chuẩn bị lá này trao |
| `revokes` | ⬜ | [string] | Cờ bị lấy đi. Chỉ hợp lệ trên lá bẫy |
| `counters` | ⬜ | {counterId: int} | Chỉ `truyen_thua`, giá trị +1 hoặc −1 |
| `tag` | ⬜ | string `^[a-z][a-z0-9_]*$` | Trí nhớ một từ. Chọn lá này thì ván ghi `chose:<tag>` |

### i18n

```jsonc
{ "vi": "chuỗi không rỗng", "en": "non-empty string" }
```

Thiếu một bên, để rỗng, hay còn chữ `TODO` đều là lỗi.

---

## 4 · Mười hai luật máy kiểm

`python3 tools/validate_data.py content/` bắt hết. Đây là những luật chạm tới lá spine:

1. **Hai ngôn ngữ, không TODO.** Mọi i18n phải có cả `vi` và `en`, không rỗng, không còn TODO.
2. **Giao kèo lý do.** Mỗi hiệu ứng khác 0 có một chip. Chip cho chỉ số không dịch chuyển là chip
   mồ côi, bị báo lỗi. Quá 60 ký tự thì cảnh báo. *Không viết nổi chip nghĩa là con số đó tuỳ tiện:
   sửa con số, đừng sửa chip.*
3. **Luật cái giá.** Lựa chọn trao cờ nằm trong `requireAll` (`giu_bi_quyet`, `truyen_nhan`,
   `ho_so`) **bắt buộc có ít nhất một hiệu ứng âm**. Không thì cờ thành ô tick miễn phí.
4. **Luật đánh đổi.** Nếu một bên tốt hơn hoặc bằng bên kia trên **mọi** chỉ số, và hai bên có
   `grants`/`revokes`/`counters` giống nhau, thì bên kia là lựa chọn chết, báo lỗi. Hai lá bẫy (11
   và 33) được phép trội về số **chính vì** chúng trả giá bằng cờ.
5. **Sự thật không rẽ nhánh.** `historicalNote` giống nhau sau cả hai lựa chọn. Người chơi đổi được
   `outcome`, không đổi được hồ sơ lịch sử.
6. **Mỗi lá một nguồn.** `sources` không rỗng. Chỉ có encyclopedia thì cảnh báo.
7. **Chronology.** `order` phải tăng cùng chiều với `year`. Lá order nhỏ hơn mà năm lớn hơn là lỗi.
8. **Không tham chiếu thứ chưa khai.** Stat, flag, counter đều phải tồn tại trong `game_contents.json`.
9. **Faucet và drain mỗi chương.** Khi một chương đủ lá (C1 12, C2 10, C3 14), mỗi chỉ số phải vừa
   có đường lên vừa có đường xuống trong chương đó. Chỉ số chỉ đi một chiều là kịch bản, không phải
   tài nguyên.
10. **`chose:` phải phân giải.** Mỗi tag do **đúng một** lựa chọn spine khai. Và mọi `chose:` mà
    echo hay weave `conditions` tham chiếu phải có lá khai nó. Hiện có bốn token đang chờ:
    `share`, `send`, `sell`, `ma`.
11. **Carrier có thật và có trao.** Mỗi cờ trỏ tới một lá tồn tại, và lá đó phải có ít nhất một
    lựa chọn `grants` cờ ấy. Đây chính là 8 error hiện tại.
12. **Cửa sổ hết hạn.** `ho_so` khai `expiresBefore: trung-tam-nha-nuoc` (lá 34). Carrier chính
    (lá 31) và cửa dự phòng (lá 33) đều phải nằm trước lá 34, và cửa dự phòng phải đắt hơn cửa
    chính.

Chạy thêm `python3 tools/trace_run.py` sau **bất kỳ** thay đổi số nào: nó beam-search toàn bộ không
gian lựa chọn và chứng minh dòng lấy đủ cờ vẫn tồn tại trên Thường và Khó.

---

## 5 · Đặc tả 36 lá

**Bảng trong `level-map.md` là đặc tả, và số trong đó đã khoá.** Nó đã được `trace_run.py` chứng
minh là thắng được, và mọi con số đều ăn khớp với nhau. Khi viết prose thì **chép số, không sửa
số**. Muốn sửa một con số thì sửa trong level map trước, sửa `trace_run.py`, chạy lại sim, rồi mới
viết.

13 lá có cơ chế đặc biệt, phải viết đúng:

| # | id | Cơ chế bắt buộc | Ghi chú khi viết |
| --- | --- | --- | --- |
| 5 | `doi-at-dau` | A khai `tag: "share"` | Thiếu tag thì echo sau lá 8 không bao giờ nổ |
| 7 | `lang-chay` | A `grants: ["giu_van"]`, floor `nguoi ≥ 20` | **Không được in năm 1947** ở bất kỳ chuỗi nào, xem mục 6 |
| 9 | `tan-cu-day-nghe` | A `grants: ["giu_bi_quyet"]`, floor `nghe ≥ 25`, minigame `match` | Cờ bắt buộc, phải trả giá âm |
| 10 | `viec-tot-thanh-pho` | A khai `tag: "send"` | |
| 11 | `lai-buon-do-co` | A `revokes: ["giu_van"]`, `tag: "sell"` | Lá bẫy. Được phép trội số vì trả giá bằng cờ |
| 12 | `ve-lang` | A `counters: {"truyen_thua": 1}` | Tick 1 trong 3 |
| 15 | `day-con-trong-xuong` | A `counters: {"truyen_thua": 1}` | Tick 2. Đây là mục tiêu của chương II |
| 18 | `luu-mau-co` | A `grants: ["giu_mau_co"]`, floor `nghe ≥ 25`, minigame `sequence` | Cờ tuỳ chọn, luật cái giá không bắt buộc nhưng nên có |
| 20 | `con-muon-o-lai` | A `counters: {"truyen_thua": 1}` | Tick 3 |
| 22 | `htx-giai-the` | A `revokes: ["giu_mau_co"]`, `counters: {"truyen_thua": -1}`, `tag: "ma"` | Lá bẫy thứ hai. Lấy lại một tick, đủ để âm thầm huỷ ván của người có 2 tick |
| 23 | `nhat-ve-tung-tam` | A `grants: ["phuc_hoi_van"]`, floor `sinh_ke ≥ 20` | Con đường thứ hai cho ván đã mất `giu_van` ở lá 11 |
| 27 | `mo-cua-don-khach` | A `grants: ["mo_cua"]`, floor `tieng ≥ 20`, minigame `match` | Cờ tuỳ chọn |
| 30 | `chau-noi-nghe` | A `grants: ["truyen_nhan"]`, floor `nguoi ≥ 20`, minigame `assemble` | Cờ bắt buộc |
| 31 | `ho-so-khoi-dong` | A `grants: ["ho_so"]`, floor `tieng ≥ 25` | Cờ bắt buộc |
| 33 | `han-chot-31-3` | A `grants: ["ho_so"]`, floor `tieng ≥ 25` | Cửa cuối, đắt hơn lá 31. Ai đã giữ `ho_so` thì lá này thành lá xác nhận |

Ba con số đích của ván, để hiểu mình đang viết cho cái gì:

- **Thắng cần** `giu_bi_quyet` + `truyen_nhan` + `ho_so` (đủ cả ba), **cộng** `giu_van` **hoặc**
  `phuc_hoi_van`, **cộng** `truyen_thua ≥ 2`.
- **Sàn sống sót** `nghe ≥ 15 · sinh_ke ≥ 10 · tieng ≥ 10 · nguoi ≥ 15`. Đủ cờ mà thủng sàn thì ra
  kết thúc Kiệt sức, không phải thắng.
- `sinh_ke` khai `insufficientAlone`: giàu không bao giờ là lý do thắng.

Chỉ số mở ván: `nghe 60 · sinh_ke 50 · tieng 55 · nguoi 50`. Chết ở `≤ 0` và `≥ 100` cho cả bốn.

---

## 6 · Ràng buộc từ nghiên cứu, không được vi phạm

`research/01-dong-ho-tranh-dan-gian.md` có mục "Contradictions & gaps register". Những mục sau
trực tiếp ràng buộc chữ trên lá:

| Mục | Ràng buộc |
| --- | --- |
| 3 | **Năm làng cháy không có nguồn.** Lá 7 mang 1947 chỉ để xếp thứ tự. Mọi chuỗi người chơi đọc được phải nói "trong kháng chiến chống Pháp", **không in 1947** trên prompt, outcome, chip hay note |
| 1 | Thế kỷ khởi nguồn có ba cách đọc. Game nói "khoảng 500 năm trước, thời Lê" |
| 2 | Chợ tranh **5 phiên** (6, 11, 16, 21, 26 tháng Chạp) trong lá bài; con số 6 phiên chỉ ghi trong codex |
| 4 | Năm mất của Nguyễn Hữu Sam có hai nguồn khác nhau. Tránh in năm |
| 5 | Năm Nguyễn Đăng Chế về nghề: 1985 hay 1992. Viết "từ giữa thập niên 1980, toàn tâm từ 1992" hoặc né |
| 7 | Kinh phí trung tâm nhà nước có hai con số. Né số, hoặc ghi kèm mốc thời gian |
| 9 | Không có tổng số mẫu tranh còn lại. **Không bao giờ in một con số đếm mẫu** |
| 10 | Số hộ còn làm: 2 dòng họ, 3 gia đình, "vài hộ". Dùng thì phải gắn năm |
| 12 | Không tìm được tổ nghề riêng của Đông Hồ. Lá giỗ tổ nói theo tục chung của làng nghề Việt, khai `historicity: invented` |

Người thật (Hoàng Cầm, Nguyễn Hữu Sam, Nguyễn Đăng Chế, Nguyễn Thị Oanh) chỉ xuất hiện trong
`historicalNote`, không bao giờ là nhân vật người chơi điều khiển. Điểm nhìn của ván là **một hộ
làm nghề hư cấu, gộp từ 17 dòng họ**.

---

## 7 · Chuẩn chữ

| Khối | Giới hạn | Vai trò |
| --- | --- | --- |
| `prompt` | ≤ 2 câu | Đặt tình huống, kết bằng một câu hỏi thật |
| `label` | vài từ | Một hành động, đọc được trên banner chéo lúc quẹt |
| `outcome` | ≤ 2 câu | Chuyện gì xảy ra sau lựa chọn này |
| `effectReasons` chip | ≤ 8 từ, ~60 ký tự | **Nguyên nhân trong thế giới của gia đình làm nghề** |
| `historicalNote` | ≤ 2 câu | Chuyện thật, không uốn theo lựa chọn |

Luật viết chip, lấy nguyên từ `design/game_strategy_and_logic.md` mục 4:

- Gọi tên nguyên nhân trong thế giới thật ("củi đốt sấy tốn thêm tiền"), **không bao giờ** gọi tên
  cơ chế ("chi phí cân bằng").
- Chip là một mẩu, không phải một câu. `outcome` kể chuyện, chip nêu lý do.
- Khi một hành động là nguyên nhân của cả hai thay đổi, viết cùng nguyên nhân đó từ phía của từng
  chỉ số. Hai chip vọng lại nhau là đúng, không phải trùng lặp.

Ví dụ đạt chuẩn, lấy từ lá weave đã ship `khach-dat-tranh-cuoi`:

```jsonc
"effects": { "tieng": 4, "sinh_ke": -2 },
"effectReasons": {
  "tieng":   { "vi": "khách hiểu tranh, nhắc tên nhà",  "en": "they understood, and repeat the name" },
  "sinh_ke": { "vi": "nửa buổi chợ ngồi giảng chuyện",  "en": "half a market morning spent talking" }
}
```

Ngoài ra: **không dùng dấu gạch ngang làm dấu câu** trong mọi chuỗi vi và en, theo luật văn phong
của nhóm. Gạch nối trong từ ghép, id kebab-case, khoảng năm 1938-2025 thì bình thường.

---

## 8 · Quy trình cho từng lá

1. Mở `level-map.md`, lấy nguyên dòng của lá: id, order, year, anchor, vai trò, hai nhãn, hai bộ
   số, cơ chế.
2. Mở `research/01`, tìm sự kiện đó trong bảng "Confirmed spine". Đọc cả trạng thái ✅ ⚠️ ❌.
3. Copy `templates/card.template.json` thành một phần tử mới trong `cards` của `game_spine.json`, id là `NN-<id>`.
4. Điền `id`, `levelId`, `order`, `year`, `historicity` (theo cột His trong level map: ✅ thành
   `documented`, `S` thành `simplified`, `D` thành `invented`).
5. Điền `sources` từ nghiên cứu, kèm `verifiedBy` là tên người viết lá này.
6. Viết `prompt`, hai `label`, hai `outcome`, `historicalNote`, cả vi và en.
7. Chép `effects` **y nguyên** từ level map. Thêm `grants` / `revokes` / `counters` / `tag` nếu lá
   đó có, theo bảng ở mục 5.
8. Viết một chip `effectReasons` cho **mỗi** hiệu ứng khác 0 của **mỗi** lựa chọn.
9. Chạy `python3 tools/validate_data.py content/`. Sửa tới khi lá đó không còn error.
10. Khi xong một chương, chạy `python3 tools/trace_run.py` và xác nhận cả hai dòng canonical vẫn WINS.

Xuất bản: copy `content/dongho/game_spine.json` sang `DaiViet/Resources/GameData/`, build, và mở bằng
probe để nhìn tận mắt:

```bash
xcrun simctl launch <udid> vn.edu.rmit.DaiViet -probeSlot check -probeState card7 -probeRoute gamePlay
```

Placeholder chỉ tự tắt khi lá thật decode được, nên còn thấy `[Nháp]` là lá đó chưa hợp lệ.

---

## 9 · Chia việc

Chia theo chương, không chia theo công đoạn. Một người ôm trọn một chương thì mốc thời gian mới
liền mạch, và đó cũng chính là bằng chứng đóng góp cá nhân mà bảng Project Responsibilities cần.

| Người | Phần | Khối lượng |
| --- | --- | --- |
| A | Chương I, lá 1 tới 12 | 12 lá, 3 carrier, 1 bẫy, 1 tick, 2 tag |
| B | Chương II, lá 13 tới 22 | 10 lá, 1 carrier, 1 bẫy, 2 tick, 1 tag |
| C | Chương III, lá 23 tới 36 | 14 lá, 4 carrier, cửa hết hạn |
| D | Viết lại 17 lá weave (11 lá đang là draft, 6 lá từ số không) và trả nợ nguồn cho 13 lá thiếu | |
| E | Prose hệ thống: banner chương, bridge, chữ trial, chữ crisis, mục codex | |

Ước lượng: 36 lá × 6 khối × 2 ngôn ngữ ≈ **432 chuỗi**, cộng **250 tới 300 chip**. Chương III nặng
nhất (14 lá, 4 cờ), nên giao cho người rảnh nhất.

Đề nghị thứ tự làm: **chương I trước**, vì nó chứa hai cờ bắt buộc đầu tiên và lá bẫy 11, tức là
sớm chạm hết mọi loại cơ chế. Xong chương I thì cả nhóm nhìn thấy một chương thật chạy trong app,
và ba người còn lại có mẫu để nhân ra.

---

## 10 · Định nghĩa hoàn thành

- [x] 36 lá tồn tại trong `content/dongho/game_spine.json`, id và order khớp level map.
- [ ] `validate_data.py` ra **0 error**. Warning còn lại chỉ được là những warning đã biết: nợ
      nguồn của lá weave, và 2 ghi chú cố ý về `sinh_ke`.
- [ ] `trace_run.py`: cả hai dòng canonical Thường và Khó vẫn WINS, vẫn lấy đủ cờ và đủ tick.
- [ ] Không lá nào còn `[Nháp]` hay `TODO` khi chạy trong app.
- [ ] Bốn `chose:` tag đã khai, và bốn echo nổ đúng khi chọn đúng nhánh.
- [ ] Ván Release bắt đầu được (nghĩa là spine đã decode thật, không còn dựa vào placeholder).
- [ ] Mỗi lá có `verifiedBy` ghi tên người đã đối chiếu nguồn.
- [ ] Không chuỗi nào in 1947, in số đếm mẫu tranh, hay in một con số đang tranh cãi mà không gắn mốc.

---

## 11 · Một lá viết đầy đủ, làm mẫu

Lá 7, vì nó chạm gần hết các trường: carrier, floor, luật cái giá, và ràng buộc "không in 1947".

```jsonc
{
  "id": "lang-chay",
  "levelId": "dongho",
  "order": 7,
  "year": 1947,
  "_yearNote": "Năm chỉ để xếp thứ tự. Nguồn không xác nhận năm làng cháy, nên không chuỗi nào dưới đây được in nó ra.",
  "historicity": "simplified",
  "sources": [
    {
      "title": "Làng tranh Đông Hồ trong kháng chiến chống Pháp",
      "url": "https://...",
      "type": "secondary",
      "locator": "phần về giai đoạn 1945-1954",
      "accessed": "2026-09-08",
      "verifiedBy": "TODO tên người kiểm"
    }
  ],
  "tags": ["war", "woodblock", "transmission"],
  "speaker": { "vi": "Người trong nhà", "en": "Someone in the house" },
  "prompt": {
    "vi": "Lửa đã bén sang dãy nhà đầu xóm. Ván khắc thì nặng, gánh hàng thì bán được ngay: nhà chỉ mang đi được một thứ.",
    "en": "The fire has reached the first row of houses. The blocks are heavy, the stock sells at once, and the household can carry only one."
  },
  "choices": [
    {
      "label": { "vi": "Ôm ván", "en": "Carry the blocks" },
      "effects": { "sinh_ke": -10, "tieng": -10 },
      "grants": ["giu_van"],
      "outcome": {
        "vi": "Cả nhà khiêng ván xuống thuyền, bỏ lại chỗ hàng đã in. Đói một mùa, nhưng bộ ván còn nguyên.",
        "en": "The family hauls the blocks to the boat and leaves the printed stock behind. A hungry season, and the blocks come through whole."
      },
      "effectReasons": {
        "sinh_ke": { "vi": "bỏ lại cả sạp hàng đã in", "en": "the printed stock left behind" },
        "tieng":   { "vi": "vắng mặt suốt mùa chợ Tết", "en": "absent for the whole Tết market" }
      }
    },
    {
      "label": { "vi": "Gánh hàng", "en": "Carry the stock" },
      "effects": { "nghe": -15, "sinh_ke": 10 },
      "outcome": {
        "vi": "Gánh tranh đi trước, ván nằm lại trong sân. Bán hết trong tháng, và không ai biết bộ ván trôi về đâu.",
        "en": "The prints go first and the blocks stay in the yard. The stock sells within the month, and no one knows where the blocks went."
      },
      "effectReasons": {
        "nghe":    { "vi": "mất bản khắc, mất tay nghề nhà", "en": "the blocks gone, the house's hand with them" },
        "sinh_ke": { "vi": "bán được cả gánh trong tháng", "en": "the whole load sold within the month" }
      }
    }
  ],
  "historicalNote": {
    "vi": "Trong kháng chiến chống Pháp, làng tranh bị thiêu rụi và nhiều bộ ván khắc thất lạc. Những bộ còn lại đến hôm nay là do từng nhà tự mang đi.",
    "en": "During the war against the French the print village was burned and many woodblock sets were lost. The sets that survive today are the ones individual households carried out themselves."
  }
}
```

Vì sao lá này hợp lệ: hai bên không bên nào trội trên mọi chỉ số nên qua luật đánh đổi; bốn hiệu
ứng khác 0 có đúng bốn chip; `historicalNote` không nhắc tới lựa chọn nào; và không chuỗi nào in
1947.

Một chỗ dễ hiểu nhầm: `giu_van` nằm trong `requireAny` chứ không phải `requireAll`, nên luật cái
giá **không** ép lựa chọn A phải có hiệu ứng âm. Lá này vẫn trả giá vì thiết kế muốn thế. Ba cờ bị
luật cái giá ép trả giá là `giu_bi_quyet` (lá 9), `truyen_nhan` (lá 30) và `ho_so` (lá 31 và 33).

---

## 12 · Rủi ro đã thấy trước

| Rủi ro | Cách xử |
| --- | --- |
| Viết prose rồi thấy con số "không hợp lý" và sửa số | Sửa số là sửa cả sim. Ghi vào một danh sách, cuối chương xử một lượt: sửa level map, sửa `trace_run.py`, chạy sim, rồi mới sửa JSON |
| Không viết nổi chip cho một hiệu ứng | Đó là dấu hiệu con số tuỳ tiện. Đưa vào cùng danh sách trên, đừng viết chip cho có |
| Ba người viết ba giọng khác nhau | Chương I làm trước và làm mẫu. Đọc chéo giữa hai chương liền kề trước khi merge |
| Bản tiếng Anh dịch máy | Luật văn phong nhóm cấm dấu gạch ngang làm dấu câu ở cả hai thứ tiếng; đọc to bản en trước khi commit |
| Lá 33 viết như lá 31 | Lá 33 là cửa cuối và phải đắt hơn. Người viết chương III giữ cả hai lá, viết liền nhau |
| Quên `tag` ở lá 5, 10, 11, 22 | Linter bắt được, vì echo trong `game_contents.json` đang tham chiếu bốn token đó |
