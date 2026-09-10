# Kế hoạch triển khai: User Profile và Lịch sử ván chơi (Past Game Records)

Tài liệu thiết kế chi tiết cho việc tinh gọn User Profile, lưu trữ lịch sử ván chơi, hiển thị Leaderboard theo lượt chơi và thiết kế lại giao diện Profile theo phong cách tranh Đông Hồ.

---

## 1. Quyết định kiến trúc cốt lõi

| Hạng mục | Quyết định | Lý do kỹ thuật |
| :--- | :--- | :--- |
| **User Profile Model** | Chỉ lưu `bio`, `avaImageName`, `pastGames` (kèm `id`, `email`, `displayName`) | Loại bỏ các chỉ số giả lập (Level, XP, Streak) không khớp với kinh tế và cốt truyện Đông Hồ. |
| **Past Game Storage** | Nhúng mảng `[PastGameRecord]` trực tiếp trong document `User` trên Firestore | Đọc 1 lần có ngay toàn bộ hồ sơ, không cần query join nhiều collection, tốc độ tải nhanh. |
| **Leaderboard Rule** | Lưu mỗi ván hoàn thành thành một document độc lập trong collection `leaderboard` | Top điểm theo từng lượt chơi: một người chơi có thể giữ nhiều vị trí top nếu chơi nhiều ván điểm cao. |
| **Profile UI** | Thẻ nghệ nhân mộc bản kết hợp danh sách con dấu hành trình đã qua | Bám sát ngôn ngữ thị giác tranh dân gian Đông Hồ: giấy điệp (#F0E6CB), đỏ son (#B63A2E), than tre (#20352D). |
| **Profile Edit** | Cho phép chỉnh sửa `displayName`, `bio`, và chọn `avaImageName` từ bộ avatar tranh Đông Hồ | Đầy đủ hai chức năng View và Update, đồng bộ thời gian thực với Firebase Auth và Firestore. |

---

## 2. Chi tiết các giai đoạn thực hiện

### Giai đoạn 1: Tinh gọn Model và Data Services (Ước tính: 20 phút)

1. **Cập nhật `User.swift` (`DaiViet/Models/User.swift`):**
   * Định nghĩa `PastGameRecord: Codable, Hashable, Identifiable`:
     - `id: String` (UUID ván chơi)
     - `score: Int` (Tổng điểm từ `ScoreBreakdown`)
     - `endingTitle: String` (Tên kết cục: Ghi danh UNESCO, Giàu mà mất nghề, Kiệt sức, Nghề tàn)
     - `endingRank: Int` (Thứ hạng kết cục từ 0 đến 3)
     - `durationSeconds: Int` (Thời lượng ván chơi)
     - `playedAt: Date` (Thời điểm hoàn thành)
   * Cập nhật `struct User: StorableModel`:
     - `let id: String`
     - `let email: String`
     - `var displayName: String?`
     - `var bio: String?`
     - `var avaImageName: String?`
     - `var pastGames: [PastGameRecord]?`

2. **Cập nhật `AuthViewModel.swift` (`DaiViet/ViewModel/Auth/AuthViewModel.swift`):**
   * Mở rộng hàm `updateProfile(displayName: String, bio: String?, avaImageName: String?) async -> Bool`.
   * Thêm hàm `recordCompletedGame(record: PastGameRecord) async`:
     - Thêm ván mới vào danh sách `currentUser.pastGames`.
     - Lưu document `User` lên Firestore qua `DatabaseHelper.shared.save(user)`.
     - Đẩy một bản ghi `LeaderboardEntry` mới vào collection `leaderboard` trên Firestore.

3. **Hook vào luồng kết thúc ván (`GamePlayViewModel.swift` / `GameSessionViewModel.swift`):**
   * Khi ván kết thúc (tại `evaluateTrial` hoặc khi đứt gánh), lấy `ScoreBreakdown` để tạo `PastGameRecord`.
   * Gọi `AuthViewModel.recordCompletedGame` nếu người chơi đã đăng nhập.

---

### Giai đoạn 2: Thiết kế lại giao diện ProfileView (Ước tính: 30 phút)

1. **Loại bỏ wireframe cũ:**
   * Gỡ bỏ hoàn toàn `PlayerProfile.mock` và các trường mock: Level 7, thanh XP 1760/2000, 18 Tranh, 12 Huy hiệu, 5 Ngày streak.
   * Gỡ bỏ các card thành tựu mẫu không có trong nội dung Đông Hồ.

2. **Cấu trúc màn hình `ProfileView.swift` mới:**
   * **Thanh tiêu đề (Header):** Khung gỗ mộc bản mang tiêu đề "Hồ sơ nghệ nhân", nút Chỉnh sửa (icon bút mộc).
   * **Khung chân dung nghệ nhân (Artisan Card):**
     - Avatar tranh Đông Hồ hiển thị qua `AvatarView(imageName: user.avaImageName)`.
     - Tên hiển thị (`displayName`) và email tài khoản.
     - Lời tự thuật (`bio`) đặt trong thẻ giấy điệp trang trọng.
   * **Hành trình đã qua (Lịch sử các ván chơi):**
     - Tiêu đề mục: "Hành trình đã qua" kèm số lượng ván đã hoàn thành.
     - Danh sách cuộn các thẻ ván chơi (`PastGameCard`):
       * Con dấu son khắc kết cục: "Ghi danh UNESCO", "Giàu mà mất nghề", "Kiệt sức", "Nghề tàn".
       * Điểm số tổng ván chơi nổi bật với màu đỏ son (#B63A2E).
       * Thời gian chơi (định dạng mm:ss) và ngày hoàn thành.
     - Trạng thái trống (Empty State): Lời nhắn trang nhã khi người chơi chưa có ván nào ("Chưa có hành trình nào được ghi dấu. Hãy bắt đầu ván chơi mới tại làng Đông Hồ").
   * **Khu vực điều hướng phụ:**
     - Nút mở Bảng xếp hạng.
     - Nút Cài đặt.
     - Nút Đăng nhập hoặc Đăng xuất.

---

### Giai đoạn 3: Hoàn thiện màn hình ProfileEditView (Ước tính: 25 phút)

1. **Cấu trúc màn hình `ProfileEditView.swift` mới:**
   * **Bộ chọn Avatar nghệ nhân (Avatar Selector Grid):**
     - Danh sách các avatar tranh Đông Hồ có sẵn trong tài nguyên dự án.
     - Cho phép người chơi chạm để chọn avatar đại diện.
     - Khung viền đỏ son nổi bật quanh avatar đang chọn.
   * **Biểu mẫu chỉnh sửa thông tin:**
     - Trường Tên hiển thị (`displayName`).
     - Trường Email (chỉ đọc, làm mờ).
     - Trường Lời tự thuật (`bio`, đa dòng).
   * **Nút hành động:**
     - Nút "Lưu thay đổi": Kích hoạt `authViewModel.updateProfile`, hiển thị trạng thái loading và quay lại màn hình Profile khi thành công.

---

### Giai đoạn 4: Đồng bộ Bảng xếp hạng Leaderboard (Ước tính: 15 phút)

1. **Cập nhật `LeaderboardView.swift`:**
   * Thay thế mảng mock tĩnh bằng việc tải dữ liệu từ Firestore collection `leaderboard` thông qua `DatabaseHelper`.
   * Sắp xếp theo điểm giảm dần (`score > $1.score`).
   * Hỗ trợ tìm kiếm theo tên người chơi.
   * Kiểm chứng: Nhiều lượt chơi của cùng một người chơi hiển thị độc lập trên các thứ hạng khác nhau.

---

### Giai đoạn 5: Kiểm thử và Hoàn thiện (Ước tính: 10 phút)

1. **Kiểm tra giao diện:** Đảm bảo hiển thị chuẩn trên iPhone 17 Pro và iPad Air 11-inch ở cả giao diện Sáng và Tối.
2. **Kiểm tra luồng dữ liệu:**
   * Đăng nhập -> Cập nhật bio và chọn avatar -> Thoát ra vào lại -> Dữ liệu giữ nguyên.
   * Chơi hoàn thành một ván -> Kiểm tra ván mới xuất hiện trong Profile -> Kiểm tra điểm xuất hiện trên Leaderboard.
