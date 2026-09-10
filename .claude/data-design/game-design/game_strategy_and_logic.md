# Chiến lược & logic game — chia bài, kinh tế chỉ số, và lý do

> **Tài liệu này quy định:** mọi thẻ ngoài trục chính đến tay người chơi bằng cách nào (việc
> chia bài), vì sao các con số chỉ số có hình dạng như hiện tại (kinh tế chỉ số), và giao kèo
> rằng mỗi thay đổi chỉ số phải tự giải thích được (lý do). Nó nằm dưới `win-condition-model.md`
> (thắng là gì) và song song với `dongho-game-design.md` (chủ đề là gì). Không điều nào ở đây
> được mâu thuẫn với chính sách độ khó trong `../content/game.json` hay các luật weave trong
> `game_contents.json`.

**Luận đề, gói trong một câu:** *việc chia bài quyết định người chơi gặp câu hỏi nào — nó không
bao giờ quyết định câu trả lời của họ ngã ra sao.* Người chơi thua phải chỉ được vào quyết định
của chính mình trong màn Xem lại ván; và một chiến thắng mang cùng một ý nghĩa ở mọi độ khó —
cùng chỉ số khởi đầu, cùng cái giá, cùng phiên xét cuối. Mọi thứ bên dưới tồn tại để hai câu đó
là sự thật.

---

## 1 · Nền nghiên cứu — thể loại này thật ra làm gì

### Reigns thật sự chia bài như thế nào

Reigns **không phải** một bộ bài xáo trộn. François Alliot mô tả một **túi bài có lọc và có
trọng số**, được dựng lại trước mỗi lần chia:

> "Khi sắp chọn lá bài tiếp theo cho người chơi, việc đầu tiên tôi làm là **bỏ khỏi túi mọi lá
> không hợp với trạng thái vương quốc**." — những lá vừa ra gần đây cũng bị loại, và "lá càng
> *to* thì càng chiếm nhiều chỗ trong túi". Các chuỗi bị khoá (hầm ngục, đấu tay đôi) chạy
> trong một **túi con** chỉ vài lá.
> — [Game Design Deep Dive: adaptive narrative in Reigns](https://www.gamedeveloper.com/design/game-design-deep-dive-creating-an-adaptive-narrative-in-i-reigns-i-)
> *(Nguyên văn: "When I'm about to select the next card shown to the player, I start by removing
> from the bag every card that doesn't fit the state of the Kingdom.")*

Vậy ba ý tưởng chịu lực của thể loại này là: **lọc theo điều kiện** (trạng thái quyết định thẻ
nào *được phép* xuất hiện), **loại thẻ vừa ra** (không lặp), và **trọng số** (trạng thái quyết
định thẻ nào *dễ ra*). Theo [bài Wikipedia về *Reigns: Her Majesty*](https://en.wikipedia.org/wiki/Reigns:_Her_Majesty),
phần tiếp nối tăng lên ~1.200–1.300 thẻ so với ~800 của bản gốc (bài
[phỏng vấn Her Majesty](https://www.gamedeveloper.com/business/-i-reigns-her-majesty-s-i-francois-alliot-on-making-a-more-complex-swipe-em-up)
xác nhận hướng đi: nội dung mới "sẽ làm game gốc phình gấp đôi") — thể loại này mở rộng bằng
**kích thước pool**, không bao giờ bằng cách đổi luật chia bài.

### Khung công bằng: ngẫu nhiên đầu vào và ngẫu nhiên đầu ra

Lý thuyết thiết kế game chia ngẫu nhiên theo *thời điểm* nó rơi so với quyết định (khung phân
loại quen thuộc của Geoff Engelstein, được [Joe Slack](https://boardgamedesigncourse.com/the-2-types-of-randomness/)
trình bày cho board game):

- **Ngẫu nhiên đầu vào (input randomness)** — tình huống là ngẫu nhiên, phản ứng là của người
  chơi (thẻ nào tới tay). Nó *nuôi* chiến lược: nhìn thấy tình huống rồi mới chọn.
- **Ngẫu nhiên đầu ra (output randomness)** — người chơi quyết, rồi xúc xắc mới quyết là có
  thành công không. Slack thừa nhận nó có thể tạo phấn khích (chiến đấu trong D&D), nhưng khi
  nó chi phối kết cục thì kế hoạch của người chơi hết còn ý nghĩa.

**Bằng chứng thực nghiệm thì trái chiều, và tài liệu này nói thẳng điều đó.** Một thí nghiệm
trên game thẻ bài sưu tầm ([arXiv:2107.08437](https://arxiv.org/pdf/2107.08437)) phát hiện ngẫu
nhiên đầu vào lại **làm giảm** mức hài lòng khi chơi, trong bối cảnh thẻ bài sưu tầm mang tính
đối kháng. Mình vẫn chọn chỉ dùng đầu vào, và lý do là ở bối cảnh chứ không phải giáo điều: đây
là một ván chơi đơn, được biên soạn sẵn, mang tính giáo dục và **không có đối thủ** — lời hứa
của nó là *thua thì truy được nguyên nhân*, không phải *canh bạc thì hồi hộp*. Ngẫu nhiên đầu
ra sẽ phá đúng thứ mình đang bán (màn Xem lại ván như một bài học); ngẫu nhiên đầu vào chỉ làm
mất một chút cảm giác phấn khích của người chơi thẻ bài đối kháng — thứ game này chưa bao giờ
bán.

**Vậy: chỉ ngẫu nhiên đầu vào.** Hiệu ứng của một lựa chọn đã in trên thẻ và được áp dụng đúng
y như vậy; không có tỉ lệ trúng, không có biên độ ngẫu nhiên, không có hệ số bất ngờ. Hành vi
ngẫu nhiên duy nhất trong cả vòng lặp là *thẻ weave/ambient nào lấp vào một slot* — và bất biến
solvency (§3) chặn trần cả lần lấp ác nghiệt nhất còn hợp lệ.

### Bộ công cụ ngẫu-nhiên-công-bằng

Từ tài liệu thực hành ([itch.io: How to design better randomness](https://itch.io/blog/882292/how-to-design-better-randomness-in-video-games)):
**túi xáo (shuffle bag)** — thứ đã rút ra không quay lại túi cho tới khi túi cạn, đảm bảo phủ hết
và triệt tiêu chuỗi trùng; **chặn chuỗi xui / bộ đếm thương hại (pity timer)** — ép một kết quả
khác sau N lần xui liên tiếp; **rút có trọng số**; **gieo lại ngầm (hidden reroll)**; và **seed**
(tái lập lại đúng ván đã chơi). §2 nói rõ mình dùng cái nào và **cố tình từ chối** cái nào.

### Những chỗ mình cố tình KHÔNG bắt chước Reigns

| Reigns | Game này | Vì sao |
| --- | --- | --- |
| Cái chết rẻ, hài hước, và **chính là** tiến trình — phần thưởng mở khoá kéo dài qua nhiều triều đại ([Wikipedia](https://en.wikipedia.org/wiki/Reigns_(video_game))) | Cái chết hiếm, được báo trước, và là một bài học — phần thưởng nằm ở màn Xem lại ván | Một triều đại 2 phút thì chịu được cái chết ngẫu nhiên; một buổi ngồi 15–20 phút mang tính giáo dục thì không. "Meta-progression" của mình là codex, không phải xác chết |
| Chỉ cho thấy chỉ số *nào* nhúc nhích (chấm tròn), không bao giờ cho biết mức độ hay chiều | Preview lúc kéo thẻ hiện **đúng con số**; màn kết quả hiện **vì sao** | Reigns bán sự bất ngờ kiểu hài đen; mình bán sự hiểu. Giấu biên độ + một ván dài = những lần thua thấy vô lý — đúng cảm giác mà thiết kế này không bao giờ được tạo ra |
| Vòng lặp chơi lại vô tận san đều sự bất công qua nhiều ván | Một ván được biên soạn, nên công bằng phải **chốt từ trước**: khả năng đi tới đích được máy chứng minh trước khi ship (`trace_run.py`) | Không thể hứa với người chơi một ván sau công bằng hơn, khi cả sản phẩm chỉ có một ván |
| Trọng số thẻ thay đổi động (thẻ "to") | Trọng số phẳng trong từng túi | Chứng minh solvency giả định rút đều; trọng số được liệt vào mục còn bỏ ngỏ (§7) vì **phải chứng minh lại**, chứ không phải vì nó sai |

---

## 2 · Chia bài — ba lớp, một thuật toán

Ván chơi là một **bộ xương cố định với phần thịt được rút ra**. Lớp một không bao giờ xê dịch;
lớp hai là ngẫu nhiên duy nhất; lớp ba phản ứng chứ không ngẫu nhiên.

| Lớp | Thẻ | Ngẫu nhiên? | Nhiệm vụ |
| --- | --- | --- | --- |
| **Spine** (trục chính) | 36 thẻ có ngày tháng, thứ tự cố định | Không bao giờ | Luận điểm của game |
| **Thẻ rút chèn vào** | weave (4 thẻ/ván từ pool 17) · ambient (≤3/ván từ pool 8) | **Có — ngẫu nhiên duy nhất** | Biến thiên giữa các ván, chất liệu đời thường, khoảng thở |
| **Thẻ phản ứng** | khủng hoảng (dải chỉ số) · echo (nhớ lựa chọn) · advisor/omen/banner (neo cố định) | Không — do kích hoạt hoặc neo sẵn | Cứu trợ, hệ quả, nhịp |

### Thuật toán (giao kèo để build — dựng đúng thế này trong ViewModel)

```
LÚC BẮT ĐẦU VÁN — một lượt xếp lịch TOÀN CỤC, không phải mỗi chương một lượt
  seed      ← seed ngẫu nhiên mới; ghi log lại (màn Xem lại ván hiện seed; cùng seed và
              cùng chuỗi lựa chọn sẽ tái hiện chính xác ván đó). Ván chơi trải qua ba
              chương tuần tự: mỗi cửa chương ghi một CHECKPOINT {chỉ số, cờ, tick,
              khủng hoảng đã dùng, weave đã gặp}; restart một chương nạp lại checkpoint
              của nó với SEED MỚI và khoá mọi chương sau — không gì reset giữa các
              chương, nên mọi chứng minh bên dưới phủ nguyên ván ba chương
  với mỗi chương C: bag[C] ← xáo pool weave của C theo seed      # trọng số phẳng
  gaps      ← mọi khe hợp lệ trong cả ván (luật đặt chỗ bên dưới;
              khe "sau thẻ spine N" thuộc về chương của thẻ N, và khe đã chứa sẵn một
              interstitial cố định — advisor, omen, banner — thì không hợp lệ, điều này
              tự nó giải quyết ranh giới thẻ-12/banner)
  schedule  ← chọn theo seed 2 khe C1 + 1 khe C2 + 1 khe C3 cho weave và
              ≤ ambientCap khe cho ambient, sao cho MỌI luật giãn cách đều thoả
              KỂ CẢ QUA RANH GIỚI CHƯƠNG (luật 4 là luật toàn cục). Nếu một lần chọn
              vi phạm giãn cách, bốc lại đúng khe đó; bảng kiểm khe bên dưới chứng minh
              luôn tồn tại một cách xếp hợp lệ, nên việc bốc lại chắc chắn dừng.

MỖI LẦN CHIA (khi mạch chơi tới một khe đã xếp lịch)
  candidates ← bag[C] trừ đi các thẻ đã hiện trong ván này        # noRepeatWithinRun
  candidates ← candidates trừ đi thẻ có `conditions` không thoả   # lọc theo điều kiện
  nếu candidates rỗng: bỏ qua khe đó trong im lặng                # không bao giờ chia thẻ lạc quẻ
  chia candidates.first                                           # thứ tự trong túi = kết quả xáo

SAU MỖI LẦN GIẢI QUYẾT THẺ
  nếu một chỉ số vừa bước vào dải khủng hoảng và khủng hoảng phía đó chưa dùng:
      chèn khủng hoảng đó làm màn kế tiếp (mỗi chỉ số mỗi phía một lần trong ván)
  nếu một khủng hoảng vừa nổ và khe đã xếp lịch nằm ngay sau:
      dời khe đó sang khe hợp lệ kế tiếp trong chương; hết khe → bỏ qua
      (luật 5 là luật lúc chạy — không thể biết trước khủng hoảng khi xếp lịch)
  nếu điều kiện của một echo vừa thành đúng và tới neo của nó:
      chèn echo tại đúng vị trí neo
```

**Bảng kiểm khe (vì sao bộ xếp lịch luôn dừng):** theo các luật bên dưới và các neo interstitial
trong `game_contents.json`, C1 có **6** khe hợp lệ (sau thẻ 3, 4, 7, 9, 10, 11 — các khe omen-6 và
advisor-7/9 đã bị chiếm), C2 có **8**, C3 có **7**. Tải tối đa — 4 weave + 3 ambient = 7 thẻ
chèn trên 21 khe với giãn cách toàn cục 3 — là thoả được (ví dụ weave sau 3/9/14/24, ambient sau
17/21/27). Chú ý điều bảng kiểm còn nói: **nhiều nhất một thẻ chèn lọt vào trước thẻ 7**, và cả
chương I nhiều nhất chỉ ~3 thẻ — chương I chơi chật hơn cái pool của nó gợi ra, và đó là chủ ý.

**Lọc theo điều kiện (`conditions`) chính là bộ lọc trạng thái của Reigns, làm cho tử tế.** Một
thẻ weave có thể khai `{allOf/anyOf/noneOf}` trên id các cờ và các ký ức `chose:<tag>`; thẻ nào
không còn hợp với trạng thái ván sẽ bị *gỡ khỏi túi*, không bao giờ được chia và cũng không bị
thế bằng thẻ khác một cách gượng ép. Ví dụ đã ship: `phuong-vay-van` ("phường hỏi mượn ván") mang
`noneOf: [chose:sell]` — một nhà đã bán ván cứu được cho lái buôn ở thẻ 11 thì đơn giản là sẽ
không bao giờ bị hỏi mượn. Bộ từ vựng ký ức là **được khai báo, không phải bịa ra**: một lựa chọn
trên thẻ spine có thể mang `tag: "sell"`, chọn nó thì ghi lại `chose:sell`, và linter kiểm tra
mọi token được tham chiếu đều dẫn về đúng một lựa chọn spine. Việc lọc có thể gỡ mất một thẻ mà
cận trên đang trông cậy, nên phép kiểm solvency mô hình hoá luôn cả trường hợp bỏ khe: đóng góp
tệ nhất còn hợp lệ của mỗi khe được chặn sàn ở mức "không có thẻ nào cả" (xem §3) — cận trên vẫn
đứng vững **cùng với** `conditions`, chứ không phải bất chấp nó.

### Luật đặt chỗ — thẻ chèn được rơi vào đâu

Các khe được chọn trong số **khe hợp lệ** giữa các thẻ spine, ngẫu nhiên theo seed nhưng trong
khuôn khổ luật:

1. Nằm trong chính chương của khe đó, không bao giờ vắt qua một banner.
2. Không bao giờ nằm giữa một advisor/omen và thẻ mà nó báo trước, cũng không nằm giữa banner
   chương và thẻ đầu tiên của chương ấy — lời báo trước phải dính liền với thứ nó báo.
3. Không bao giờ trước thẻ spine 3 (ván mở màn bằng chính chân mình) và không bao giờ sau thẻ
   spine 33 (đoạn kết 34→36 chạy liền một mạch tới phiên xét cuối).
4. Cách nhau ít nhất 3 thẻ spine giữa hai thẻ chèn bất kỳ; riêng ambient còn phải tôn trọng
   `minCardGap` của chính nó là 4.
5. Không bao giờ nằm ngay sau một màn khủng hoảng — sự cứu trợ cần một nhịp để lắng xuống.

### Những điều việc chia bài KHÔNG BAO GIỜ được làm — và lý do từng điều

- **Không ngẫu nhiên đầu ra.** Hiệu ứng đã in là hiệu ứng được áp. Luôn luôn.
- **Không thiên vị túi bài theo độ khó.** Khó giữ lại tầm nhìn trước (dải cảnh báo, sổ, advisor,
  gợi ý); nó không bao giờ nhồi túi (`game.json` `_weaveNote`). Một chiến thắng ở Khó phải mang
  đúng ý nghĩa như mọi chiến thắng khác.
- **Không chia bài "co giãn ngầm" theo phong độ.** Mình từ chối các mẹo gieo-lại-ngầm/thích-nghi
  trong bộ công cụ: **khủng hoảng là toàn bộ hệ cứu trợ của game này** — nhìn thấy được, có giá
  trả bằng một chỉ số khác, mỗi cạnh một lần. Một lớp cứu trợ thứ hai vô hình nằm trong việc chia
  bài sẽ làm mờ đúng bài học game sinh ra để dạy: *màn Xem lại ván phải truy được mọi kết cục về
  một quyết định.* (Chống chuỗi xui đã có sẵn về mặt cấu trúc ở nơi các con số cho phép nó có ý
  nghĩa: trong một ván, `noRepeatWithinRun` cấm lặp thẳng thừng; với pool 12 thẻ của C1 thì túi
  xáo thật sự làm các ván khác nhau, còn pool 3 của C2 và pool 2 của C3 khiến cái túi chỉ còn
  danh nghĩa — một nửa số ván sẽ mở màn weave chương III bằng cùng một thẻ. Những thẻ weave mới
  đầu tiên mà team viết nên rơi vào C2/C3; mở rộng pool vừa là núm chỉnh độ biến thiên, vừa là
  núm chỉnh lịch chia.)
- **Không ép chia từ một túi đã cạn hoặc đã bị lọc sạch.** Khe không còn thẻ hợp lệ thì bị bỏ qua
  và ván ngắn đi một màn. Việc bỏ khe **có thể** làm người chơi mất một lá đáng lẽ tử tế — chính
  vì thế cận trên solvency phủ hẳn cả trường hợp không-có-thẻ (§3).

---

## 3 · Kinh tế chỉ số — vì sao các con số có hình dạng như vậy

### Dòng chảy đã kiểm toán (tái tạo bằng `python3 tools/trace_run.py --audit`)

Mọi chỉ số đều phải **kiếm được và mất được ở mọi chương** — một chỉ số chỉ có đường xuống là
một cái chết được viết sẵn, không phải tài nguyên; bộ kiểm toán gọi đó là MONOTONE và báo lỗi.
Trục chính hiện tại, máy kiểm toán CLEAN:

| Chương | NGHỀ | SINH KẾ | TIẾNG | NGƯỜI |
| --- | --- | --- | --- | --- |
| I (1–12) | +25 / −30 | +125 / −75 | +35 / −45 | +25 / −55 |
| II (13–22) | +30 / −30 | +100 / −60 | +15 / −25 | +15 / −30 |
| III (23–36) | +30 / −45 | +90 / −85 | +65 / −35 | +25 / −20 |

Hãy đọc *hình dạng*, vì hình dạng **chính là** luận điểm: **SINH KẾ là đồng tiền áp lực** — dòng
chảy rộng nhất ở mọi chương, bởi cả ba tick lẫn ba thẻ carrier bắt buộc đều tính tiền vào nó,
phiên xét cuối đặt cổng cho nó thấp nhất (10, ngang với TIẾNG), và ngân sách dao động weave siết
chặt nhất cũng ở nó (12). **NGƯỜI hao mạnh nhất ở chương I** (chiến tranh làm người ly tán) và
dịu lại ở chương III (phục hưng gom người về). **TIẾNG lật sang phía nguồn ở chương III** (+65) —
đó đúng là lý do vì sao *trần* của nó (danh tiếng, thương mại hoá) thay chỗ cho sàn để trở thành
hiểm hoạ giai đoạn cuối. Kinh tế chỉ số và hồ sơ hiểm hoạ (sàn → thời kỳ bẫy → trần) là cùng một
sự thật nhìn từ hai phía.

### Ba luật kinh tế (đều được máy kiểm)

1. **Nguồn và cống** — mọi chỉ số, mọi chương, cả hai chiều.
   *Được thực thi bởi:* `trace_run.py --audit` (hiện soi trên bản mirror của trục chính; linter
   kế thừa khi `cards/*.json` ra đời).
2. **LUẬT ĐÁNH ĐỔI (THE TRADE RULE)** — một lựa chọn chỉ được thắng lựa chọn kia trên **mọi** chỉ
   số nếu nó **trả giá bằng cờ**. Hai cặp áp đảo chỉ số trong ván là bằng chứng luật này hoạt
   động: thẻ 11 trả +25 SINH KẾ *và thu hồi `giu_van`* (chính sự áp đảo LÀ cái bẫy); phía dễ của
   thẻ 33 bỏ qua `ho_so` bắt buộc (chính sự áp đảo LÀ hạn chót). Áp đảo chỉ số mà
   grants/revokes/counters y hệt nhau = một lựa chọn chết = linter báo **error**.
   *Được thực thi bởi:* `validate_data.py` (weave + cards), `--audit` (bản mirror trục chính).
3. **Việc chia bài không bao giờ làm dịch chuyển NGƯỜI sau chương I** — cả weave *lẫn* ambient:
   hai beat ambient có chạm NGƯỜI đều được gắn thẻ chương `C1`, và linter từ chối beat nào không
   gắn. Ở C1, chuyện đứa trẻ xin học nghề là chất liệu đời thường; từ chương II trở đi, ai ở lại
   và ai rời đi **chỉ thay đổi qua các quyết định có ngày tháng, qua tick, và qua các khủng hoảng
   NGƯỜI mà người chơi chấp nhận** — truyền thừa là chủ đề của game, và chủ đề thì không bao giờ
   là thời tiết.
   *Được thực thi bởi:* `validate_data.py` (vòng lặp weave + vòng lặp ambient).

**Bảng trên chứng minh điều gì và KHÔNG chứng minh điều gì.** Nó chứng minh tính hai chiều, không
chứng minh biên độ dư dả: vài nguồn lớn nhất trong bảng bị **tẩm độc bằng cờ** một cách có chủ ý
(+25 sinh_ke của C1 chính là cái bẫy thu hồi `giu_van`; +20 trong tổng sinh_ke của C3 nằm trên
những lựa chọn bỏ qua chuẩn bị bắt buộc) — đó là luật đánh đổi đang chạy, và người đọc đừng nhầm
dòng chảy gộp với tiền cho không. Bảng cũng không nói gì về *thời điểm* dòng chảy tới, mà đó lại
đúng là thứ các sàn quan tâm — nên `--audit` còn in thêm **FLOOR TIMING**: giá trị tệ nhất còn
với tới được của từng chỉ số bị đặt sàn, tại đúng thẻ carrier của nó, tính bằng đáy bi quan của
trục chính cộng với lượt weave khắc nghiệt nhất có thể xếp lịch. Phán quyết hiện tại: năm cái sàn
từ thẻ 18 trở đi là **LIVE**; sàn thẻ 7 chỉ chặn được khi gặp lượt rút thù địch tối đa cộng với
lối chơi tự huỷ; sàn thẻ 9 thì **không thể chặn** (nghe tệ nhất còn với tới là 34 so với sàn 25)
— và đó là chủ ý. Hai cái sàn đầu là **sàn tập dượt**: chương I dạy cơ chế sàn ở nơi nó không thể
phục kích (advisor kể trước một cái cổng mà người chơi chắc chắn qua được), còn các sàn ở chương
III mới là bài thi thật. Đó chính là thiết kế độ khó theo chương (học → cầm cự → lật ngược) áp
dụng cho các cổng.

Solvency nằm dưới cả ba luật: `weavePolicy.maxWorstCaseSwing` bảo đảm rằng **không lượt rút hợp
lệ nào** — ác nghiệt nhất, hào phóng nhất, **hay bị bỏ khe** (phép kiểm chặn sàn đóng góp tệ nhất
của mỗi khe ở mức "không có thẻ") — làm thay đổi *việc ván đó có thắng được hay không*, mà chỉ
thay đổi cái giá phải trả. Ambient nằm ngoài ngân sách này theo thiết kế: nó toàn dương, bị chặn
bởi số lượng (≤3), bởi từng hiệu ứng (≤8) và bởi tổng lợi ích (<35), nên việc loại nó ra chỉ có
thể **đánh giá thấp** vị thế người chơi chứ không bao giờ đánh giá cao. Đó là dạng toán học của
câu "user không thua vì cách chia bài".

---

## 4 · Giao kèo về lý do — mỗi thay đổi chỉ số tự giải thích chính nó

**Vấn đề** (phát hiện khi đọc lại `khach-dat-tranh-cuoi`): "giải thích tranh" tốn SINH KẾ −2, và
người viết biết vì sao — ngồi giảng thì mất nửa buổi chợ — nhưng **không có gì trên màn hình nói
điều đó**. Một thay đổi chỉ số mà nguyên nhân chỉ nằm trong đầu người viết sẽ bị đọc thành một
khoản thuế ngẫu nhiên, và chỉ một khoản thuế không giải thích được là đủ để phá hỏng cả một ván
đầy những khoản sòng phẳng.

**Giao kèo:** mọi hiệu ứng khác 0 trên mọi lựa chọn đều mang một **chip `effectReasons`** — một
mẩu song ngữ, ≤ 8 từ / ~60 ký tự mỗi ngôn ngữ, gọi tên *nguyên nhân trong thế giới của game*:

```jsonc
"choices": [{
  "label":   { "vi": "Ngồi giảng nghĩa từng lớp tranh", ... },
  "effects": { "tieng": 4, "sinh_ke": -2 },
  "effectReasons": {
    "tieng":   { "vi": "khách hiểu tranh, nhắc tên nhà",  "en": "they understood — and repeat the name" },
    "sinh_ke": { "vi": "nửa buổi chợ ngồi giảng chuyện",  "en": "half a market morning spent talking" }
  }
}]
```

**Quy tắc viết chip:**
- Gọi tên nguyên nhân trong thế giới của gia đình làm nghề ("củi đốt sấy tốn thêm tiền"), không
  bao giờ gọi tên cơ chế ("chi phí cân bằng"). **Nếu không viết nổi cái chip thì hiệu ứng đó là
  tuỳ tiện — hãy sửa hiệu ứng, đừng sửa chip.**
- Chip là một mẩu, không phải một câu. Phần `outcome` (≤ 2 câu) kể chuyện; chip nêu nguyên nhân.
  Linter cảnh báo khi vượt 60 ký tự.
- Chip là bắt buộc với lựa chọn weave, lựa chọn trên thẻ spine, và cả phần cứu trợ của khủng
  hoảng.

**Khi một hành động là nguyên nhân của cả hai thay đổi** (một buổi sáng đám cưới ngồi giảng
tranh chính là thứ *mua* lấy tiếng bằng sinh kế), hãy viết cùng một nguyên nhân đó từ phía của
từng chỉ số — hai cái chip vang vọng nhau là cái giá sòng phẳng của việc rõ ràng theo từng chỉ
số, và một dạng "nguyên nhân dùng chung" là thứ **cố tình không** được mô hình hoá.

**Người chơi nhìn thấy chip ở đâu:** trên **màn kết quả**, ngay dưới từng thay đổi chỉ số, và
trong các dòng của **màn Xem lại ván** — tức là dạy sau khi người chơi đã cam kết. **Không** hiện
trên preview lúc kéo thẻ: preview cho con số chính xác (thứ bạn sắp đánh đổi), màn kết quả cho lý
do (cuộc đánh đổi ấy nghĩa là gì). Và chip **không phải một núm chỉnh độ khó** — được khai trong
`game.json` mục `neverChanges`: độ khó giữ lại *tầm nhìn trước*, không bao giờ giữ lại *cái nhìn
lại*.

*Được thực thi bởi:* `validate_data.py` báo lỗi khi thiếu chip, khi có chip mồ côi (lý do cho một
chỉ số không hề dịch chuyển), và khi còn TODO; schema: `card.schema.json` `$defs/choice`.
Hiện trạng: toàn bộ 34 lựa chọn weave và 8 phần cứu trợ khủng hoảng đều đã có chip; thẻ spine sẽ
nhận chip khi được viết ra (bước 8 trong checklist soạn thảo ở `win-condition-model.md`).

---

## 5 · Mỗi lời hứa công bằng dựa trên cái gì

| Trải nghiệm của người chơi | Điều được bảo đảm | Do đâu thực thi |
| --- | --- | --- |
| "Tôi thua là do lựa chọn của tôi" | Mọi ngẫu nhiên đều là ngẫu nhiên đầu vào; hiệu ứng áp đúng như đã preview | Luật thiết kế §2; trong mô hình dữ liệu không hề tồn tại cơ chế giải quyết ngẫu nhiên |
| "Việc xáo bài không thể đẩy tôi vào đường chết" | Bất biến solvency: không lượt rút hợp lệ nào đổi được việc ván có thắng nổi hay không | Lỗi SOLVENCY của `validate_data.py` |
| "Việc xáo bài không thể dội thẻ trùng vào mặt tôi" | Túi xáo theo chương + `noRepeatWithinRun` + luật giãn cách | Thuật toán chia bài §2 |
| "Không thẻ nào mâu thuẫn với ván tôi đang chơi" | Bộ lọc `conditions` (gỡ ra, không bao giờ ép vào) | Phép kiểm conditions của `validate_data.py` |
| "Mọi câu hỏi đều là câu hỏi thật" | LUẬT ĐÁNH ĐỔI — không có lựa chọn chết | Lỗi dominance của `validate_data.py` · `--audit` |
| "Tôi luôn có đường gượng dậy — một lần, và phải trả giá" | 8 khủng hoảng, mỗi chỉ số mỗi phía một lần, cứu trợ tính giá bằng một chỉ số khác | Luật crisis của `validate_data.py` |
| "Game có nói cho tôi biết vì sao" | effectReasons trên mọi thay đổi khác 0, ở mọi độ khó | Chip trong `validate_data.py` · `neverChanges` trong `game.json` |
| "Chế độ khó chơi đẹp" | Độ khó không bao giờ đổi nội dung túi bài hay cái giá của bất kỳ quyết định nào. Nó có đổi lượng cứu trợ miễn phí được xếp lịch — ambient ≤3 beat (tổng ≤ +24) ở Dễ/Thường so với ≤1 (≤ +8) ở Khó/Cực khó — và đó chính là nghĩa đã khai của chữ "slack" | `mayChange`/`mayNotChange` trong `game.json` + linter |
| "Thắng là thắng" | Cùng khởi đầu, cùng cái giá, cùng bộ cờ, cùng phiên xét cuối ở mọi độ khó; ván tái lập được bằng seed; đổi độ khó giữa chừng thì leaderboard ghi mức thấp nhất từng dùng | `game.json` + RNG theo seed §2 |
| "Cả cỗ máy này thật sự chạy được" | Tồn tại đường đi chuẩn lấy đủ mọi chuẩn bị trên cả Thường lẫn Khó; kinh tế chỉ số kiểm toán CLEAN | `trace_run.py` + `--audit` |

---

## 6 · Tương tác với độ khó (tham chiếu chéo)

Việc chia bài đọc **trạng thái ván** (cờ, lựa chọn, chỉ số — cho khủng hoảng) và **không bao giờ
đọc thiết lập độ khó**. Bốn độ khó — **Dễ / Thường / Khó / Cực khó** — vặn năm núm chỉnh
(`crisisBands`, `ledgerDisclosure`, `advisors`, `ambientCap`, `minigameHints`); `ledgerDisclosure`
giờ là núm **phạm vi sổ**: một sổ lớn mở mọi lúc (Dễ) · ba sổ theo chương (Thường/Khó) · không sổ
(Cực khó). `ambientCap` là núm duy nhất chạm tới *số lượng* thẻ chèn (3/3/1/1, dưới trần cứng
`maxPerRun` là 3). **Độ khó đổi được giữa ván** và áp dụng ngay — an toàn đúng vì không núm nào
chạm số: dải khủng hoảng đánh giá theo độ khó *tại thời điểm resolve thẻ*, rescue đã dùng không
bao giờ được hoàn lại, và **leaderboard ghi độ khó thấp nhất từng dùng** trong ván. Mô hình:
`../content/game.json` · lý lẽ: `DEC-01` D13.

---

## 7 · Những núm còn bỏ ngỏ — đã đánh dấu, chưa quyết

| Núm | Nó sẽ thêm được gì | Vì sao còn chờ |
| --- | --- | --- |
| Trọng số thẻ kiểu Alliot (thẻ "to" khi tình thế căng) | Nhịp kịch tính mạnh hơn | Phá vỡ giả định rút đều nằm dưới chứng minh solvency; phải chứng minh lại trước khi bật |
| Giảm trọng số theo số lần đã gặp, lưu qua nhiều ván | Chơi lại tươi hơn cho bàn demo | Cần thiết kế lưu trữ (D7); độ biến thiên trong một ván thì túi xáo đã bảo đảm |
| Chia sẻ seed ("chơi lại ván của tôi") | Mục leaderboard kiểm chứng được, dùng được trong lớp học | Cần thêm UI + lớp lưu trữ; rẻ thôi một khi D7 chốt |
| Túi con nối chuỗi (kiểu hầm ngục của Reigns) | Chuỗi mini nhiều thẻ nằm trong ván | Với 36+17 thẻ thì chưa có nhu cầu nội dung; chỉ xét lại nếu một chương cần một chuỗi dẫn dắt |

---

*Viết dựa trên: `content/dongho/game_contents.json` (weave/ambient/khủng hoảng/các policy) ·
`content/game.json` (độ khó) · `tools/validate_data.py` (các luật) · `tools/trace_run.py`
(khả năng tới đích + `--audit`). Nếu một trong số đó thay đổi, chạy lại cả hai tool và đọc lại §3.
Mức nền dự kiến khi phần lời thẻ spine chưa viết: linter thoát với mã 1, đúng **8 lỗi** (thiếu
thẻ carrier) và 15 cảnh báo — xem README của workspace; ngoài số đó ra thì đều là phát hiện thật.*
