# Pitch trực tiếp — Flame in Freefall (5–7 phút, tiếng Việt)

Dùng cho buổi chấm trực tiếp tại Hà Nội; slide và bài nộp bằng tiếng Anh, lời nói bằng tiếng Việt.
Giữ nguyên thuật ngữ tiếng Anh cho tên riêng (SAFFIRE-II, FLEX, ROC-AUC…). Tốc độ ~140 từ/phút → khoảng 850–900 từ.
`[ev-NN]` = id evidence trong app; `[model]` = `uv run flame_model.py` (14/11/2026). Không đọc các ký hiệu này thành lời.
Các số dưới đây đều có trong `submission.md`; chạy lại model trước giờ chấm.

| Phần | Tiêu chí | Slide | Thời lượng |
|---|---|---|---|
| Mở đầu | — | 1 | 0:30 |
| 1 | **Impact** | 2, 7 | 1:00 |
| 2 | **Creativity** | 5 | 1:00 |
| 3 | **Validity** | 3, 4, 6 | 1:30 |
| 4 | **Relevance** | 2, 3 | 0:45 |
| 5 | **Presentation** (demo trực tiếp) | app | 1:15 |
| Kết | — | 7 | 0:20 |
| | | | **≈ 6:20** (dư ~40 s để thở/nhường chỗ cho Q&A) |

---

## Mở đầu (0:00–0:30) — slide 1

"Xin chào các thầy cô. Em là Zinnn. Apollo 1 và Mir — hai vụ cháy trên tàu vũ trụ. **[ĐIỀN 1 câu từ trang NASA bạn dán; nếu chưa có thì bỏ, chỉ giữ câu trước.]**
Sắp tới con người sẽ sống trong những căn cứ kín trên Mặt Trăng và Sao Hỏa. Câu hỏi của em: *lửa trong vi trọng lực hành xử thế nào, và chúng ta biết chắc được bao nhiêu?*"

## 1. Impact (0:30–1:30) — slide 2, 7

"Hôm nay thiết kế an toàn cháy cho tàu vũ trụ vẫn dựa nhiều vào tiêu chuẩn mặt đất. Chính NASA viết rằng trước Saffire, các thí nghiệm cháy trong vi trọng lực chỉ dùng mẫu từ 10 cm trở xuống, và đó là một rủi ro cố hữu, lớn dần khi tàu đi xa Trái Đất [ev-12].
Công cụ của em giúp một kỹ sư thiết kế khí quyển, hay một sinh viên, tự khám phá: oxy, áp suất, khí CO₂, heli hay nitơ đẩy ngọn lửa về phía tắt hay phía cháy mạnh — và quan trọng nhất, *dữ liệu NASA dừng ở đâu*.
Em nói rõ ngay: đây là công cụ khám phá, không phải công cụ chứng nhận an toàn."

## 2. Creativity (1:30–2:30) — slide 5

"Ba điều em kết hợp trong một app.
Một: bản đồ rủi ro từ 274 thí nghiệm giọt cháy thật trên ISS, mỗi dự đoán có khoảng tin cậy 90 % và các thí nghiệm NASA gần nhất.
Hai: 25 phát hiện có trích dẫn từ các tập dữ liệu và tài liệu NASA, xếp hạng theo mức liên quan đến nhà ở Mặt Trăng/Sao Hỏa, mỗi cái có cờ 'verified'.
Ba: tab Ask the Data — một LLM chỉ được trả lời từ 25 phát hiện đó và kết quả mô hình, và phải gắn mã nguồn sau mỗi câu. Ý tưởng khác biệt nhất là chỗ này: ô nào ngoài vùng dữ liệu NASA thì app *tô xám* và gọi đúng tên là ngoại suy, thay vì vẽ một bản đồ đẹp nhưng không có căn cứ."

## 3. Validity (2:30–4:00) — slide 3, 4, 6

"Bằng chứng mạnh nhất là SAFFIRE-II. Cùng kích thước mẫu 5 × 29 cm, cùng luồng khí 20 cm/s, oxy khoảng 22 %, NASA đốt ở vi trọng lực và ở 1 g. Màng silicone 0,27 mm cháy hết ở 1 g nhưng gần như không cháy trong vi trọng lực. Ngược lại vải cotton-fiberglass cháy hết cả 29 cm trong không gian, với tốc độ lan 2,1 và 2,6 mm/s. PMMA dày chỉ hỏng khoảng 10 cm với ngọn lửa bám ở gốc [ev-01, ev-02, ev-06]. Kết luận: thử ở 1 g có thể sai theo *cả hai chiều*.
Em cũng nói giới hạn: toàn bộ Saffire I đến III chỉ có hai mẫu lớn và chín mẫu nhỏ [ev-19].
Về mô hình: dữ liệu FLEX có 274 thí nghiệm, 186 ngọn lửa tự tắt. Em dùng hồi quy logistic và ridge, bootstrap 200 lần, và đánh giá bằng cross-validation *chia theo ngày thử*, để các thí nghiệm cùng ngày không nằm ở cả tập huấn luyện lẫn kiểm tra. Kết quả: ROC-AUC 0,881, balanced accuracy 0,762, R² của hằng số cháy K là 0,71.
Và điều em muốn thầy cô nhớ: mô hình chỉ áp dụng cho *giọt nhiên liệu lỏng*. Chỉ 19 % lưới mặc định nằm trong vùng NASA đã thử; 81 % còn lại là ngoại suy và bị tô xám. Vải, nhựa là bằng chứng, không phải đầu ra mô hình."

## 4. Relevance (4:00–4:45) — slide 2, 3

"Với thử thách Flame in Freefall: em làm đúng ba việc đề bài yêu cầu — tóm tắt, xếp hạng và diễn giải dữ liệu cháy vi trọng lực của NASA.
Về Mặt Trăng và Sao Hỏa: NASA nói Saffire I đến III chỉ phủ không khí gần giống ISS, chưa phủ khí quyển giàu oxy, áp thấp dự kiến cho tàu thám hiểm [ev-14]. App thể hiện đúng điều đó: bản đồ kéo ra ngoài vùng thử thì chuyển xám.
Và về chất dập lửa: CO₂ là chất dập dùng ở phía Mỹ của ISS, và có thể kém hiệu quả hơn mong đợi trong vi trọng lực [ev-16]; trong FLEX, giọt heptan trong heli cháy nhanh hơn trong CO₂ (K trung vị 0,65 so với 0,50 mm²/s) [ev-23]."

## 5. Presentation — demo trực tiếp (4:45–6:00) — mở app

1. (15 s) Bấm **ISS preset**, nhiên liệu Methanol. "Không khí ISS, giọt 3 mm: khả năng tự tắt 72 %, khoảng 62 đến 81 % [model]. Heptan thì 43 %." (chuyển radio sang Heptane)
2. (20 s) Kéo oxy lên 0,40 và áp suất lên 3 atm: "Vùng xám xuất hiện, cảnh báo Extrapolation. Con số ở đây không có dữ liệu đỡ."
3. (20 s) Đổi diluent sang CO₂ 25 %; chỉ vào bảng *Nearest real tests* bên phải. "Mọi dự đoán đều kèm thí nghiệm thật gần nhất."
4. (20 s) Sang tab **Evidence Ranking**, lọc topic 'solid flame spread', mở thẻ ev-02. "Có điều kiện, con số và trích dẫn."
5. (20 s) Tab **Ask the Data**, hỏi: "Does silicone burn in microgravity?" — chỉ vào mã `[ev-02]` cuối câu. *Nếu tab báo 'off' vì không có API key, nói thẳng: "tab này cần khóa API; hai tab còn lại không cần", và bỏ bước này.*

Dự phòng: chuẩn bị sẵn 3 ảnh chụp màn hình (slide 5) phòng khi mạng hỏng.

## Kết (6:00–6:20) — slide 7

"Tóm lại: dữ liệu mở của NASA, một mô hình trung thực về giới hạn của mình, và bằng chứng có thể kiểm chứng. AI em dùng để viết mã và soạn bài là Claude; bên trong app là mô hình học máy scikit-learn và một LLM qua OpenRouter ở tab hỏi đáp, chỉ trả lời từ bằng chứng có trích dẫn. Em xin cảm ơn và sẵn sàng nhận câu hỏi."

---

# 8 câu hỏi giám khảo dễ hỏi — và cách trả lời

**1. Mô hình có dự đoán được cháy vải, nhựa, hay cháy thật trong căn cứ không?**
Không. Mô hình chỉ về giọt nhiên liệu lỏng (metanol, heptan) trong điều kiện FLEX. Vải và nhựa nằm ở tab Evidence như bằng chứng có trích dẫn, và app ghi rõ điều đó. Em không tuyên bố gì về cháy thật.

**2. ROC-AUC 0,881 nghĩa là gì? Có bị overfit không?**
AUC đo khả năng xếp một ngọn lửa tự tắt cao hơn một ngọn không tắt; 0,881 là kết quả cross-validation 5 fold *nhóm theo ngày thử* trên 261 thí nghiệm có đủ đầu vào [model]. Chia theo ngày để tránh rò rỉ giữa các thí nghiệm gần nhau. Nhưng đây là dữ liệu nhỏ, của một thiết bị và hai loại nhiên liệu, nên em chỉ coi nó là mức chính xác *trong điều kiện FLEX*.

**3. Vì sao dùng giọt metanol/heptan để nói chuyện Mặt Trăng, Sao Hỏa?**
Vì đó là bảng duy nhất đủ kết quả để học máy: 274 hàng có nhãn. Em không tuyên bố nó đại diện cho cháy trên Mặt Trăng. Giá trị của nó là cho thấy xu hướng — oxy thấp thì tắt nhiều: 37/37 thí nghiệm metanol ở ≤ 15 % O₂ tắt, so với 13/35 ở trên 22 % [ev-15] — và cho thấy rõ vùng chưa có dữ liệu.

**4. 81 % lưới là ngoại suy — vậy app còn ích gì?**
Chính con số đó là một kết quả: nó cho biết phần lớn không gian điều kiện của một căn cứ chưa được thử. App không giấu điều đó mà tô xám. Trong vùng dữ liệu (19 %), người dùng thấy xu hướng kèm khoảng tin cậy; ngoài vùng, họ biết cần thí nghiệm mới.

**5. LLM có bịa không?**
Có thể sai, nên em hạn chế nó: nhiệt độ 0, chỉ nhận danh sách bằng chứng và đầu ra mô hình, phải gắn mã [ev-NN] sau mỗi câu, app kiểm tra mã có tồn tại, và dán nhãn 'AI summary, check the cited sources'. Nguồn sự thật là tab Evidence, không phải câu trả lời của LLM. Tab này cũng tắt khi không có API key.

**6. SAFFIRE-II chỉ có vài mẫu, sao kết luận được 0 g khác 1 g?**
Em chỉ kết luận điều dữ liệu cho thấy ở *những mẫu đó*: silicone mỏng cháy hết ở 1 g nhưng ≈ 0 ở 0 g, vải cháy hết ở cả hai. Không phải quy luật tổng quát. Chính bài báo Saffire nói cần nhiều mẫu và vật liệu hơn [ev-19]. Em cũng ghi chú rằng một mẫu SIBAL được kế hoạch ở 30 cm/s nhưng PSI-99 ghi 20 cm/s [ev-01].

**7. Ai sẽ dùng, và tác động thực tế là gì?**
Nhà thiết kế khí quyển, sinh viên, người làm an toàn nhiệm vụ — để khám phá nhanh và biết nên hỏi gì tiếp. Không dùng để chứng nhận. Em chưa có người dùng thật nào; đó là hướng tiếp theo, cùng với dữ liệu FLEX-2 khi có kết quả.

**8. Em dùng AI thế nào, và ai kiểm chứng?**
Claude (qua Claude Code) giúp viết mã, trích 25 phát hiện từ file NASA và soạn bài. Mỗi phát hiện có trích dẫn file/trang và cờ verified để kiểm tra lại được; mỗi con số trong bài nộp gắn với mã bằng chứng hoặc đầu ra `flame_model.py`. **[ĐIỀN: bạn đã tự đối chiếu những mục nào với file NASA — nói thật mức đó.]** Trong app có một mô hình học máy cổ điển và một LLM qua OpenRouter chỉ ở tab hỏi đáp.

---
*Bonus nếu còn thời gian:* "Con số bất ngờ nhất?" → silicone 0,27 mm cháy hết ở 1 g nhưng ≈ 0 ở 0 g [ev-02]. "Có thấy ngọn lửa cháy ở oxy thấp không?" → thanh PMMA vẫn cháy trong vi trọng lực ở 14,8 % O₂ (một lần chạy, không phải giới hạn thống kê) [ev-04].
