# Screen–Stitch checklist · Living Heritage (Nhà Trần)

> Cập nhật **17 Aug 2026** · Project Stitch: [1689000862901928358](https://stitch.withgoogle.com/projects/1689000862901928358) · Atlas: <https://claude.ai/code/artifact/f037d911-7503-4b37-b8ba-bec1e6417ada>
>
> Quy ước chữ: **SCREEN** = nguyên màn điện thoại (HUD chỉ số + lá + info). **CARD** = riêng lá bài người chơi quẹt. Mọi mục dưới đây là *screen chứa card* trừ khi ghi khác.
>
> Trạng thái: ✅ có trên canvas · 🕐 đã đặt sinh 17 Aug, Stitch nhận nhưng index trả muộn (sẽ tự hiện trên canvas, xem §5) · ✂️ cần thao tác tay · 🔎 note.

---

## 1 · Bộ demo theo loại lá (theo `card-type-selfwritten.md`)

### 1.1 Decision cards

| Loại | Screen cần | Trạng thái | Tên trên canvas Stitch | Ghi chú demo (value & tradeoff) |
| --- | --- | --- | --- | --- |
| **Spine Normal · setup** | 1 | ✅ | `Spine Normal · Setup — Sứ đòi mượn đường` | 1258, lá 1/28. ▶ cho mượn: Dân −15, Kho +5, Thần +5 · ◀ từ chối: Dân +5, Thần −5 |
| **Spine Normal · pressure** | 1 | ✅ ✂️ | `Loại 1/8 — Spine · Lá đại sự` | Chính là **Hịch tướng sĩ**. Đổi tên tay → `Spine Normal · Pressure — Hịch tướng sĩ` |
| **Spine Normal · relief** | 1 | ✅ | `Spine Normal · Relief — Đê điều thủy lợi` | 1270. Hồi chỉ số nhưng luôn trả bằng chỉ số khác |
| **Spine Normal · trap** | 1 | ✅ | `Spine Normal · Trap — Mở rộng quân đội` | 1265, **lá 8/28** — mốc mà Echo gọi lại. +20 Binh là mồi |
| **Carrier (mini-boss)** | 1 | ✅ | `Loại 6/8 — Carrier · Lá trao cờ` | Diên Hồng 1284, khung vàng đôi, dải sàn `CẦN LÒNG DÂN ≥ 20 · HIỆN 40 ✓` |
| — thắng carrier: **giành cờ + stats mất** | 1 | ✅ | `08 Giành được chuẩn bị — sáng` | **Mới 17 Aug, đã render + đã vào canvas.** Cờ Lòng dân thống nhất ⬦ · SÀN ≥ 20 (có 50) ĐẠT · GIÁ ĐÃ TRẢ Triều thần −20 · sổ 1/3 |
| — hụt sàn: **mất stats, không cờ** | 1 | ✅ | `16 Preparation Blocked` | "KHÔNG THI HÀNH ĐƯỢC" — cần ≥ 25, hiện 18 thiếu 7; giá vẫn trừ: Dân −15, Kho −20, Thần −5 |
| **Weave — quan bị tố ăn hối lộ** | 1 | ✅ | `Loại 2/8 — Weave · Việc triều đình` | Card trong màn này chính là event "Quan lộ bị tố nhận của đút". Khung gạch đứt + "Không rõ năm" |
| **Weave — lão tướng xin về** | 1 | ✅ | `Weave · Lão tướng xin về` | Đã render + đã soi: khung gạch đứt, KHÔNG RÕ NĂM, LÁ 11/28, chữ thuần. ▶ cho về: Dân +6, Binh −8 · ◀ giữ lại: Binh +6, Thần −5. (Quirk: có tab bar dưới đáy — bỏ khi dựng thật) |
| **Weave — vỡ đê** *(bonus có sẵn)* | — | ✅ | `W1 Việc triều đình — vỡ đê` | Cặp giảng bài đẹp với Relief 1270: cùng đề tài, một lá có năm (spine) một lá không (weave) |
| **Crisis + highlight stat gây ra** | 1 | ✅ | `E2b Khủng hoảng — Quốc khố — sáng` | Chỉ số phạm vùng được **kéo hẳn ra giữa màn**: QUỐC KHỐ 18 đỏ + mini-bar. Hai phương án, phương án nào cũng trả bằng chỉ số khác; "CHỈ MỘT LẦN" |

### 1.2 Non-decision cards

| Loại | Screen cần | Trạng thái | Tên trên canvas | Ghi chú |
| --- | --- | --- | --- | --- |
| **Ambient** (1–2 screen) | 2 | ✅ ✅ | `Loại 3/8 — Ambient · Lá năm lành` (Được mùa: Dân +5, Kho +5) · `E5b Năm lành — Dân hoà thuận — sáng` (Dân +5, Thần +3) | Cả hai đều có HUD + chip xanh ngọc ↑, đúng "small, positive, supportive boost" |
| **Interstitial · Advisor** — cặp 2 màn | 2 | ✅ + ✅ | 1/2 `Loại 5/8 — Interstitial · Lá thông báo` ✂️ đổi tên → `Interstitial · Advisor — Cố vấn` · 2/2 `Cặp Advisor 2/2 — Bỏ Thăng Long` (đã render, đã soi: khung vàng đôi, sàn ≥ 25 hiện 55 ✓, GIÀNH ĐƯỢC: VƯỜN KHÔNG NHÀ TRỐNG; lưu ý màn này có tab bar icon dưới đáy — màn duy nhất có, bỏ khi dựng thật) | Chiều demo **ngược**: advisor nói giá trước (Dân −15 · Kho −20) → màn 2 là đúng lá đó, sàn LÒNG DÂN ≥ 25 |
| **Interstitial · Omen** — cặp 2 màn | 2 | ✅ + ✅ | 1/2 `Cặp Omen 1/2 — Đóng chiến thuyền` (đã render: 1286, LÁ 24/28, strip "SAU LÁ NÀY LÀ: ĐIỀM BÁO · 1287") · 2/2 `Interstitial · Omen — Điềm báo` | Vuốt xong lá 1286 → Điềm báo "Chúng sẽ sang lần thứ ba… mang theo thuyền lương · CÒN 1 LÁ NỮA" |
| **Interstitial · Echo** — cặp 2 màn | 2 | ✅ + ✅ | 1/2 `Spine Normal · Trap — Mở rộng quân đội` (tái dùng — chính lá gieo nhân) · 2/2 `Interstitial · Echo — Hệ quả muộn` | Echo 1269: "Đội quân năm ấy giờ phải ăn" — ô **VÌ NGƯƠI ĐÃ CHỌN · Mở rộng quân đội · 1265 · Lá 8** khớp đúng LÁ 8/28 trên màn Trap. Không tạo màn trigger riêng để tránh trùng lá |

### 1.3 Boss — Final Trial (không phải lá)

| Screen cần | Trạng thái | Tên trên canvas | Ghi chú |
| --- | --- | --- | --- |
| Preparation Ledger (Dễ/Thường) | ✅ | `Sổ chuẩn bị — sáng` | Mỗi cờ 1 trang: AI TRAO · **SÀN** (≥ 20 ✓) · GIÁ ĐÃ TRẢ (Thần −20); 2 ô trống chỉ lộ *khoảng năm* + *sàn* |
| Final Trial: cờ đã lấy + floor tối thiểu + nút **RA TRẬN** | ✅ | `Loại 8/8 — Final trial · Trận cuối` | Câu MỘT: ⬦⬦⬦ 3/3 ✓ (chỉ câu này quyết định thắng) · câu HAI: BINH 60 · DÂN 55 · KHO 25 · THẦN 30 trên sàn ✓ · nút RA TRẬN, "Không quay lại được" |
| Bảng kết quả finalize | ✅ | `F3b Kết quả — Bản ghi lịch sử — sáng` | Đã render, đã soi đủ: THẮNG "không phải vì mạnh hơn" · khối đen SỬ CHÉP THẾ NÀO · tóm tắt 4 chỉ số + 28 quyết định/3 cờ/0 khủng hoảng · timeline 3 lá ⬦ kèm giá từng lá |
| *(đường thua thứ 4 — đã có sẵn)* | ✅ | `15 Kiệt sức` | Đủ 3 cờ nhưng QUỐC KHỐ 6 < sàn 10 → KHÔNG ĐỦ. Đây là màn chứng minh statGate hoạt động |

### 1.4 Cách chơi (mid-drag, luật preview 17 Aug: delta chính xác + bar mờ 50%)

| Khoảnh khắc | Trạng thái | Tên trên canvas | Ghi chú |
| --- | --- | --- | --- |
| 1 · Nghỉ | 🔎 | `C1 Card — Rest` — **m vừa ẩn màn này (17 Aug tối)** | Ảnh vẫn dùng trong atlas. Nếu muốn khoảnh khắc Nghỉ có mặt trên canvas: bỏ ẩn, hoặc nói t sinh bản mới |
| 2b · Miniboss kéo PHẢI | ✅ | `M1b Miniboss · Kéo PHẢI — Bỏ Thăng Long` | Đã render + đã soi: ▼15/▼20/▼5 đỏ + bar mờ, Binh đậm nguyên, sàn ≥ 25 hiện 55 ✓, khung vàng đôi, dải BỎ TRỐNG KINH THÀNH, GIÀNH ĐƯỢC ◆ |
| 3b · Miniboss kéo TRÁI | ✅ | `M2b Miniboss · Kéo TRÁI — Giữ thành` | Đã render + đã soi: Binh ▼10 · Thần ▲5 (bar mờ đúng cột), cảnh báo "KHÔNG CỜ — CƠ HỘI KHÔNG QUAY LẠI", dải GIỮ THÀNH có chữ — bản kéo-trái sạch nhất hiện có |
| 2 · Đang kéo **phải** | ✅ | `Cách chơi · Kéo PHẢI — hiện mức thay đổi` (bản lá nghiêng, **giữ bản này**) | Dải đỏ CHO MƯỢN + HUD: Lòng dân ▼15 · Kho ▲5 · Thần ▲5 |
| 3 · Đang kéo **trái** | ✅ | `Cách chơi · Kéo TRÁI v2` — **chốt bản này** | Sạch glitch, nghiêng trái + delta đúng (Dân ▲5 · Thần ▼5, bar mờ). Khuyết duy nhất: dải đỏ chưa hiện chữ TỪ CHỐI (cơ chế dải-có-chữ đã demo ở kéo phải). Ẩn 2 bản cũ: bản glitch `ec283a90` + bản không lá `f539d226` |

---

## 2 · ✂️ Việc tay trên canvas (máy không làm được — API Stitch không có xoá/ẩn/đổi tên; `edit_screens` fork màn mới)

**Ẩn 5 màn thừa** (đợt dọn trước m đã ẩn 24 màn — các màn "xoá" thực chất là *hidden*, vẫn nằm trong project; t cũng thấy m đã tự ẩn thêm `C1 Card — Rest` và `05b · Card — Diên Hồng` tối 17 Aug):

| Ẩn màn | Nhận diện bằng mắt |
| --- | --- |
| `DELETED · Validation Test` (`86d0a2bd`) | Màn **đỏ đặc chữ DELETED** — sót từ đợt dọn trước |
| `Cách chơi · Kéo PHẢI — hiện mức thay đổi` (`9576a355`) | Bản **trang tutorial**: có nav "← CÁCH CHƠI", lá màu đỏ mận. Bản giữ là bản lá đen nghiêng bị cắt mép phải |
| `Kéo phải v2` (`7f618d6c`) | Render hỏng — trắng 2/3 màn dưới |
| `Cách chơi · Kéo TRÁI — hiện mức thay đổi` (`f539d226`) | Bản hỏng: có HUD, **không có lá** |
| `Cách chơi · Kéo TRÁI — hiện mức thay đổi` (`ec283a90`) | Bản glitch: có dải TỪ CHỐI nhưng **lòng lá dính một mảnh UI thu nhỏ**. Bản giữ là `Cách chơi · Kéo TRÁI v2` (lá sạch, không dải chữ) |

**Đổi tên 2 màn** (để tên khớp taxonomy):

- `Loại 1/8 — Spine · Lá đại sự` → **`Spine Normal · Pressure — Hịch tướng sĩ`**
- `Loại 5/8 — Interstitial · Lá thông báo` → **`Interstitial · Advisor — Cố vấn`**

**Kéo-trái đã chốt:** giữ `Cách chơi · Kéo TRÁI v2`, ẩn 2 bản cũ như bảng trên (§1.4).

---

## 3 · 🔎 Góp nhặt từ các màn TỐI (nội dung gameplay chưa có bản sáng)

Quét đủ 24 màn tối còn hiện + nhóm đã ẩn. Không sửa màn tối (theo yêu cầu). Đây là những **nội dung** đáng giữ khi redesign sang sáng:

| Nội dung gameplay | Màn tối đang giữ nó | Bản sáng? | Đề xuất |
| --- | --- | --- | --- |
| **Level Briefing** — luật "chạm 0 chết, chạm 100 cũng chết", 28 quyết định, 3 lần giặc sang, stat khởi đầu | `Level Briefing` | ✗ | Nên có sớm — đây là màn dạy luật trước ván |
| **Run Review** — timeline từng lá kèm delta đã trả, đánh dấu ⬦ carrier | `Run Review` | ✗ (F3b 🕐 mới cover phần tóm tắt) | Làm sau F3b; là "sổ hoá đơn" đầy đủ |
| **Dynasty Falls** — thua vì chỉ số sập: NGUYÊN NHÂN + bar 100 đỏ + ô sự thật lịch sử | `Dynasty Falls` | ✗ | ⚠ màn tối đang lộ chữ **"TODO — đoạn sử… Nguồn: TODO"** ngay trên UI — content phải viết trước khi demo |
| **Stat Warning** — cảnh báo *sắp* vào vùng nguy ("Quốc khố 8 · còn 16 thẻ nữa") | `Stat Warning` | ✗ | Đây là bước *trước* crisis (crisisBands theo `game.json`) — bản sáng chưa có khái niệm này |
| **Pause / Save-Resume** — thẻ 21/28, năm, chuẩn bị 2/3, khủng hoảng đã dùng | `Pause — Save and Resume` | ✗ | Gameplay-adjacent; cần cho auth/cloud-sync flow sau này |
| **14 Dynasty Unlocked** — mở Lam Sơn "bắt đầu từ số không" + huy hiệu | `14 · Dynasty Unlocked` | ✗ | Meta progression giữa các level |
| **Dynasty Select** — 3 triều đại + tagline đúng 3 shape thắng (requireAll → requireCounter → expiresBefore) | `Dynasty Select` | ✗ | Giữ nguyên cấu trúc khi làm sáng — tagline đang khớp win-condition-model |
| Nhãn 2 lựa chọn hiện sẵn ở chân lá lúc nghỉ (**HÒA \| ĐÁNH**) + tranh chân dung trên lá | `05b · Card — Diên Hồng`, `Advisor — Diên Hồng` | ✗ | Quyết định UX cần chốt: bản sáng hiện chỉ lộ lựa chọn *khi kéo*. Nếu team thích lộ trước, thêm 2 nhãn mờ ở 2 góc dưới lá |
| Advisor dạng bảng **CÁI GIÁ** có cả cột được lẫn mất (+15 / −20) | `Advisor — Diên Hồng` | một phần (advisor sáng chỉ ghi giá mất) | Cân nhắc format bảng 2 dòng cho advisor sáng |
| Omen kèm **mức chuẩn bị gợi ý** ("BINH 75 · DÂN 50 · KHO 35 · THẦN 30 — CHUẨN BỊ ĐI") | `Omen — The Third Storm` | ✗ (omen sáng chỉ nói định tính) | Đúng tinh thần "Dễ nhiều thông tin hơn" — có thể chỉ hiện ở mode Dễ |
| **F1 Warning / Kiệt sức / C1 Rest / W1 vỡ đê / M1 / M2** | các màn cùng tên | ✅ các màn này **đã nền kem/sáng sẵn** | Không cần làm lại; M1/M2 chỉ cần update theo luật preview mới (§4) |
| Splash · Menu · Codex (Sử liệu, có search/filter) · A1–A4 · Profile/Leaderboard | shell tối | — | Ngoài phạm vi quét gameplay theo yêu cầu; Codex lưu ý là chỗ gánh **search/filter** (BRIEF-05) |

**Trùng lặp nội dung cần biết:** `W1 vỡ đê` (weave, không năm) và `Spine Relief — Đê điều 1270` dùng cùng nhân vật hà đê chánh sứ với văn bản khác nhau — giữ cả hai *có chủ đích* làm cặp giảng spine↔weave, đừng gộp.

---

## 4 · Việc còn lại (backlog màn)

1. ✅ **Hết hàng chờ render.** Toàn bộ màn đặt sinh 17 Aug đã về, đã soi, đã vá vào atlas: Lão tướng · M1b · M2b · `Chọn độ khó` (`13c9cdc6` — 3 panel đúng game.json, THƯỜNG tag MẶC ĐỊNH, KHÓ viền đỏ). Trên canvas m chỉ cần kéo các màn mới về đúng nhóm.
2. Các bản sáng theo §3 khi tới lượt redesign: Level Briefing → Dynasty Falls (viết content thay TODO trước) → Run Review → Stat Warning → Pause → Dynasty Unlocked/Select.

## 5 · Ghi chú vận hành Stitch (để khỏi giẫm lại)

- **"Xoá" trong UI thực chất là ẩn** (`hidden: true` trong project) — 24 màn m dọn hôm nay vẫn nằm trong data, chỉ biến khỏi canvas. Muốn tìm lại thì bật hidden.
- **`edit_screens` không sửa màn — nó fork màn mới** (đã kiểm chứng, sinh ra chính `86d0a2bd`). Không dùng để đổi tên/sửa.
- **Timeout ≠ thất bại.** 5 màn "fail" hôm trước đều đã sinh muộn (tạo ra đợt trùng vừa phải dọn). Quy trình đúng: đặt sinh 1 lần → chờ → check bằng `get_project`/listing, không retry.
- **Index (`list_screens` / `screenInstances`) trễ hàng chục phút** so với màn thật. Màn mới sẽ tự hiện trên canvas khi UI refresh — đừng lấy việc "chưa thấy" làm bằng chứng thất bại rồi sinh lại (nguồn gốc của mọi bản trùng từ trước tới nay).
- Design system sáng "Lacquer & Silk — Light" (`assets/13743454115436243051`) đã gắn ở tầng project — prompt mô tả light là tự nhận đúng hệ.
