# Tài liệu đặc tả thiết kế: Màn hình Bảng xếp hạng (Leaderboard)

Tài liệu quy chuẩn các thành phần giao diện (UI Components) và hệ thống thẩm mỹ dành cho designer thiết kế màn hình Bảng xếp hạng trò chơi tranh dân gian Đông Hồ ("Dong Ho Art").

---

## 1. Hệ thống thẩm mỹ cốt lõi (Design System)

| Yếu tố | Quy chuẩn kỹ thuật | Mô tả chi tiết |
| :--- | :--- | :--- |
| **Nền chính** | `#F0E6CB` (Giấy điệp) | Nền sáng ngà của giấy dó quét bột vỏ điệp, không dùng trắng tinh `#FFFFFF` |
| **Màu son chính** | `#B63A2E` (Đỏ son) | Dùng cho điểm số nổi bật, nút nhấn chính, con dấu son |
| **Màu phụ 1** | `#31536A` (Chàm mộc) | Dùng cho viền Hạng 2, các liên kết phụ |
| **Màu phụ 2** | `#D6A437` (Vàng điệp) | Dùng cho bục và viền Hạng 1 |
| **Màu mực nét** | `#20352D` (Than tre) | Nét viền mộc bản, văn bản nội dung, icon |
| **Nét viền** | 1.5pt đến 2.0pt | Nét viền cứng cáp mô phỏng nét khắc gỗ, góc bo 8pt đến 12pt |
| **Đổ bóng** | Hard shadow | Đổ bóng phẳng cứng offset x: 3pt, y: 3pt, không dùng bóng nhòe mờ |
| **Phông chữ tiêu đề** | Noto Serif | Dành cho tiêu đề màn hình, số thứ hạng lớn |
| **Phông chữ nội dung** | Be Vietnam Pro | Dành cho tên người chơi, nhãn điểm số, trường nhập liệu |

---

## 2. Danh sách các Component cần thiết kế

### Nhóm A: Điều hướng và Tìm kiếm (Header & Filter)

1. **`LeaderboardHeader`**
   * Tiêu đề: "Bảng Vàng Nghệ Nhân" (font Noto Serif, in đậm).
   * Nút Back: Nút mũi tên quay lại mang phong cách mộc bản, kích thước vùng chạm tối thiểu 44x44pt.
2. **`LeaderboardSearchBar`**
   * Ô tìm kiếm người chơi đặt ngay dưới thanh tiêu đề.
   * Icon kính lúp nét mực đen.
   * Placeholder: "Tìm nghệ nhân...".
   * Nền thẻ màu giấy điệp sáng hơn nền một chút, có viền nét than tre mỏng.
3. **`LeaderboardSegmentControl`**
   * Bộ chuyển đổi 2 chế độ xem:
     * Tab 1: "Bảng vinh danh" (Danh sách xếp hạng)
     * Tab 2: "Xu hướng điểm" (Biểu đồ tương tác)
   * Hiệu ứng chọn: Khối màu đỏ son hoặc nền khắc gỗ sẫm màu với chữ trắng ngà.

---

### Nhóm B: Bục Vinh Quang Top 3 (Podium Components)

4. **`PodiumContainer`**
   * Bố cục 3 bục chênh lệch độ cao: Hạng 1 ở giữa cao nhất, Hạng 2 bên trái, Hạng 3 bên phải.
5. **`PodiumCard`**
   * **Avatar Frame:** Khung tròn hiển thị tranh nghệ nhân Đông Hồ, viền theo thứ hạng:
     * Hạng 1: Viền vàng điệp `#D6A437` (dày 3pt)
     * Hạng 2: Viền chàm mộc `#31536A` (dày 2pt)
     * Hạng 3: Viền đỏ son trầm `#B63A2E` (dày 2pt)
   * **Con dấu thứ tự:** Huy hiệu tròn nhỏ đánh số 1, 2, 3 dạng con dấu mộc, gắn ở góc avatar.
   * **Thông tin hiển thị:**
     * Tên người chơi (1 dòng, cắt gọn nếu quá dài).
     * Điểm số: Hiển thị nổi bật, định dạng dấu chấm phân cách hàng nghìn (ví dụ: 2.840).
     * Con dấu kết cục: Dấu son mini ghi tên kết quả ván chơi (ví dụ: UNESCO, Giàu mất nghề).

---

### Nhóm C: Danh sách thứ hạng (Leaderboard List)

6. **`LeaderboardRow`** (Hạng 4 trở đi)
   * Chiều cao mỗi thẻ: 64pt đến 72pt.
   * Cột thứ tự: Số thứ hạng (font Noto Serif đậm).
   * Avatar nghệ nhân tròn: Kích thước 40x40pt.
   * Tên người chơi: Đặt cạnh avatar, kèm tag kết cục ván chơi bên dưới hoặc cạnh tên.
   * Điểm số tổng: Căn lề phải, màu đỏ son hoặc màu than tre đậm.
   * Thẻ nền bo góc 10pt có viền mực mộc bản và đổ bóng phẳng nhẹ.
7. **`CurrentPlayerStickyBar`** (Thanh cố định ở đáy)
   * Ghim ở đáy màn hình (trên safe area).
   * Nền màu đỏ son trầm hoặc giấy điệp viền đậm để phân biệt với danh sách cuộn.
   * Hiển thị vị trí thứ hạng và điểm kỷ lục của chính tài khoản hiện tại.

---

### Nhóm D: Biểu đồ thống kê điểm (Interactive Graph View)

8. **`ScoreSummaryCards`**
   * Cụm 3 thẻ con dấu vuông vắn đặt ngang:
     * Thẻ 1: Điểm kỷ lục (Điểm cao nhất từng đạt được).
     * Thẻ 2: Điểm trung bình qua các ván.
     * Thẻ 3: Tổng số ván đã hoàn thành.
9. **`ScoreTrendChartView`**
   * Khung biểu đồ (Swift Charts tương thích):
     * Trục hoành: Thứ tự các ván chơi gần đây (Ván 1, Ván 2, Ván 3...).
     * Trục tung: Điểm số đạt được (0 đến 3.500 điểm).
     * Đường vẽ xu hướng màu đỏ son `#B63A2E`, các điểm mốc (dot) tròn viền vàng điệp.
     * Vùng đổ màu mờ (gradient opacity thấp) phía dưới đường vẽ.
   * Trạng thái chạm tương tác: Chạm vào điểm mốc hiện tooltip nhỏ ghi ngày chơi và tên kết cục.

---

## 3. Lưu ý kỹ thuật cho Designer

1. **Một người chơi có thể có nhiều vị trí:** Hệ thống ghi nhận kỷ lục theo từng ván chơi (run), do đó nếu người chơi đạt điểm cao ở nhiều ván khác nhau, các lượt chơi đó sẽ xuất hiện độc lập trên bảng xếp hạng. Cần có tag con dấu kết cục hoặc ngày chơi để phân biệt.
2. **Hỗ trợ giao diện Sáng và Tối:**
   * Chế độ Sáng (Mặc định): Nền giấy điệp `#F0E6CB`.
   * Chế độ Tối: Nền than tre sẫm `#1C2520`, các thẻ màu gỗ mun `#2A3530`, chữ màu kem giấy điệp.
3. **Độ phân giải và tỉ lệ:** Thiết kế trên khung màn hình iPhone 17 Pro (393 x 852 pt), đảm bảo bố cục co giãn tốt trên màn hình iPad Air 11-inch.
