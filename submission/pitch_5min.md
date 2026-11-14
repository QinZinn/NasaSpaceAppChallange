# Pitch trực tiếp — Flame in Freefall (5–7 phút, tiếng Việt)

Dùng cho buổi chấm trực tiếp tại Hà Nội (hạn nộp bài: **11:00 Chủ nhật 15/11/2026**). Slide và bài nộp bằng tiếng Anh, lời nói bằng tiếng Việt.
Giữ nguyên thuật ngữ tiếng Anh cho tên riêng (SAFFIRE-II, FLEX, ROC-AUC, Disruption…). ~140 từ/phút → khoảng 900 từ.
`[ev-NN]` = evidence, `[in-NN]` = insight FLEX, `[model]` = `uv run flame_model.py` (14/11/2026). Không đọc các ký hiệu này thành lời.
**Thông điệp chính (nhắc ở mở đầu và ở phần Validity): "0 trên 17 thí nghiệm giọt tự tắt ở 0,7 atm với 30–34 % O₂."** [in-02]

| Phần | Tiêu chí | Slide | Thời lượng |
|---|---|---|---|
| Mở đầu | — | 1, 2 | 0:45 |
| 1 | **Impact** | 2, 7 | 0:45 |
| 2 | **Creativity** | 5 | 0:50 |
| 3 | **Validity** | 3, 4, 6 | 1:50 |
| 4 | **Relevance** | 2, 4 | 0:40 |
| 5 | **Presentation** (demo trực tiếp) | app | 1:10 |
| Kết | — | 7 | 0:20 |
| | | | **≈ 6:20** |

---

## Mở đầu (0:00–0:45) — slide 1, 2

"Xin chào các thầy cô, em là Zinnn.
Năm 1967, trong một buổi thử trên bệ phóng, cabin Apollo 1 chứa 100 % oxy. Một đám cháy chớp nhoáng lan nhanh đến mức phi hành đoàn không kịp mở cửa; cửa khi đó cần 90 giây để mở, sau này NASA thay bằng cửa mở trong 3 giây [ev-26]. Năm 1997 trên trạm Mir, một bình tạo oxy bốc cháy: ngọn lửa dài khoảng ba feet cháy vài phút, chắn đường tới một trong hai tàu Soyuz thoát hiểm, khói dày mất nhiều giờ mới hút hết. Phi hành đoàn dùng ba bình bọt, và theo bài của NASA thì ngọn lửa cuối cùng *tự tắt* [ev-27].
Căn cứ trên Mặt Trăng và Sao Hỏa cũng là môi trường kín. Câu hỏi của em: lửa trong vi trọng lực hành xử thế nào, và dữ liệu NASA nói chắc được đến đâu? Nếu thầy cô chỉ nhớ một điều: **trong 17 thí nghiệm giọt nhiên liệu ở khoảng 0,7 atm với 30–34 % oxy, không giọt nào tự tắt.**"

## 1. Impact (0:45–1:30) — slide 2, 7

"Chính NASA viết rằng trước Saffire, các thí nghiệm cháy vi trọng lực chỉ dùng mẫu từ 10 cm trở xuống, nên thiết kế tàu dựa nhiều vào tiêu chuẩn mặt đất — một rủi ro cố hữu lớn dần khi tàu đi xa [ev-12].
Công cụ của em giúp kỹ sư thiết kế khí quyển hay sinh viên tự khám phá: oxy, áp suất, CO₂, heli hay nitơ đẩy ngọn lửa về phía tắt hay cháy mạnh — và quan trọng nhất, dữ liệu NASA dừng ở đâu. Em nói rõ: đây là công cụ khám phá, không phải công cụ chứng nhận an toàn."

## 2. Creativity (1:30–2:20) — slide 5

"Em ghép ba thứ trong một app.
Một: bản đồ rủi ro từ 274 thí nghiệm giọt cháy thật trên ISS, mỗi dự đoán có khoảng tin cậy 90 % và các thí nghiệm NASA gần nhất.
Hai: 27 phát hiện có trích dẫn từ dữ liệu và tài liệu NASA, xếp hạng theo mức liên quan, cộng sáu xu hướng tính tự động từ dữ liệu FLEX.
Ba: tab Ask the Data — một LLM chỉ được trả lời từ các phát hiện đó và kết quả mô hình, và phải gắn mã nguồn sau mỗi câu.
Điểm khác biệt: ô nào nằm ngoài vùng dữ liệu NASA thì app tô xám và gọi đúng tên là ngoại suy, thay vì vẽ một bản đồ đẹp nhưng không có căn cứ."

## 3. Validity (2:20–4:10) — slide 3, 4, 6

"Bằng chứng trực tiếp 0 g so với 1 g là SAFFIRE-II. Mẫu 5 × 29 cm, luồng khí 20 cm/s, oxy khoảng 22 %. Màng silicone 0,27 mm cháy hết ở 1 g nhưng gần như không cháy trong vi trọng lực. Vải cotton-fiberglass lại cháy hết cả 29 cm trong không gian, tốc độ lan 2,1 và 2,6 mm/s. PMMA dày chỉ hỏng khoảng 10 cm [ev-01, ev-02, ev-06]. Thử ở 1 g có thể sai theo cả hai chiều — nhưng toàn bộ Saffire I đến III chỉ có hai mẫu lớn và chín mẫu nhỏ, nên em chỉ kết luận cho những mẫu đó [ev-19].

Kết quả chính của em đến từ dữ liệu FLEX, 274 thí nghiệm giọt. Ở khoảng 0,7 atm với 30–34 % oxy, **0 trên 17 thí nghiệm tự tắt** — 8 heptan, 9 metanol [in-02]. Hướng này khớp với mô tả định tính của NASA về khí quyển thám hiểm: oxy cao, áp suất thấp [ev-14]; NASA không đưa con số cụ thể nên em chỉ nói về hướng, không nói là khớp số.
Hai điều đi kèm. Oxy là đòn bẩy mạnh nhất: heptan tự tắt 11 trên 14 test ở ≤ 16 % oxy, 5 trên 17 ở 20–22 %, 0 trên 3 ở 23–30 % [in-01]. Còn áp suất thấp tự nó gần như không đổi gì: theo mô hình, xác suất tự tắt của heptan là 43 % ở 21 % oxy, 1 atm; 41 % ở 21 %, 0,7 atm; chỉ còn 2 % khi oxy lên 30 % [in-05].

Giới hạn, em nói to: chỉ là giọt nhiên liệu lỏng, không nói gì trực tiếp về vật liệu rắn. 'Không tự tắt' không có nghĩa là cháy êm đến hết: 15 trong 17 test kết thúc bằng Disruption, 2 test metanol cháy hết giọt. Chỉ 17 test, một dải áp suất, chỉ có nitơ.
Về mô hình: hồi quy logistic và ridge, bootstrap 200 lần, cross-validation chia theo ngày thử: ROC-AUC 0,881, balanced accuracy 0,762, R² của K 0,71. Chỉ 19 % lưới mặc định nằm trong vùng NASA đã thử; 81 % còn lại là ngoại suy và bị tô xám."

## 4. Relevance (4:10–4:50) — slide 2, 4

"Thử thách yêu cầu tóm tắt, xếp hạng và diễn giải dữ liệu cháy vi trọng lực của NASA cho an toàn cháy trên Mặt Trăng và Sao Hỏa; app làm ba việc đó.
Về khí quyển thám hiểm, em chỉ nói định tính như NASA: oxy cao, áp suất thấp, và Saffire I đến III chưa phủ loại khí quyển này [ev-14]. App có nút 'Exploration atmosphere' nhưng đó chỉ là minh họa, chưa có nguồn; app ghi rõ như vậy và mô hình xem đó là ngoại suy.
Về chất dập lửa: CO₂ là chất dập dùng ở phía Mỹ của ISS và có thể kém hiệu quả hơn mong đợi trong vi trọng lực [ev-16]; trong FLEX, heptan trong heli cháy nhanh hơn trong CO₂ (K trung vị 0,65 so với 0,50 mm²/s) [ev-23]."

## 5. Presentation — demo trực tiếp (4:50–6:00) — mở app

1. (15 s) Bấm **ISS preset**, Methanol: "Không khí ISS, giọt 3 mm: 72 % tự tắt, khoảng 62–81 % [model]." Chuyển sang Heptane: "43 %."
2. (20 s) Bấm **Exploration atmosphere**: "Nút này là minh họa, không phải con số của NASA — app ghi 'illustrative, needs a cited source' và vùng này bị tô xám, tức ngoại suy." Chỉ vào ô cảnh báo Extrapolation.
3. (15 s) Hộp **Key findings** ở đầu tab 1 (mặc định đã mở): chỉ vào dòng về 17 test.
4. (20 s) Tab **Evidence Ranking**, mở thẻ ev-02: "điều kiện, con số, trích dẫn."
5. (20 s) Tab **Ask the Data**, bấm câu mẫu "How did fabric burn in microgravity compared with normal gravity?" — chỉ vào mã `[ev-01]`. *Nếu tab báo 'off' vì không có API key: nói thẳng "tab này cần khóa API; hai tab còn lại không cần" và bỏ bước này.*

Dự phòng: 3 ảnh chụp trong `app/screenshots/` (slide 5) phòng khi mạng hỏng.

## Kết (6:00–6:20) — slide 7

"Tóm lại: dữ liệu mở của NASA, một mô hình nói thật về giới hạn của mình, và bằng chứng kiểm chứng được. AI em dùng để viết mã và soạn bài là Claude; trong app có mô hình học máy scikit-learn và một LLM qua OpenRouter ở tab hỏi đáp, chỉ trả lời từ bằng chứng có trích dẫn. Em xin cảm ơn và sẵn sàng nhận câu hỏi."

---

# 8 câu hỏi giám khảo dễ hỏi — và cách trả lời

**1. Mô hình có dự đoán được cháy vải, nhựa, hay cháy thật trong căn cứ không?**
Không. Mô hình chỉ về giọt nhiên liệu lỏng (metanol, heptan) trong điều kiện FLEX. Vải và nhựa nằm ở tab Evidence như bằng chứng có trích dẫn. Em không tuyên bố gì về cháy thật.

**2. ROC-AUC 0,881 nghĩa là gì? Có bị overfit không?**
AUC đo khả năng xếp một ngọn lửa tự tắt cao hơn một ngọn không tắt; 0,881 là kết quả cross-validation 5 fold *nhóm theo ngày thử* trên 261 thí nghiệm có đủ đầu vào [model]. Chia theo ngày để các thí nghiệm gần nhau không rò rỉ giữa tập huấn luyện và kiểm tra. Nhưng dữ liệu nhỏ, một thiết bị, hai loại nhiên liệu, nên em chỉ coi nó là độ chính xác *trong điều kiện FLEX*.

**3. "0 trên 17" có nghĩa là trong khí quyển đó lửa luôn cháy hết và nguy hiểm hơn không? Và vì sao giọt lỏng lại liên quan đến Mặt Trăng, Sao Hỏa?**
Không hẳn. "Không tự tắt" ở đây gồm cả test kết thúc bằng Disruption: 15 trong 17 là Disruption, 2 metanol cháy hết giọt [in-02]. Đó là quan sát về giọt lỏng ở 17 test, một dải áp suất, chỉ nitơ — không nói gì trực tiếp về vật liệu rắn hay về một căn cứ thật. Em dùng giọt lỏng vì đó là bảng duy nhất đủ nhãn để học máy (274 hàng); giá trị của nó là chỉ ra xu hướng (oxy cao → hết tự tắt, [in-01]) và chỉ rõ vùng chưa có dữ liệu.

**4. 81 % lưới là ngoại suy — app còn ích gì? Nút "Exploration atmosphere" lấy số ở đâu?**
Chính con số 81 % là một kết quả: phần lớn không gian điều kiện của một căn cứ chưa được thử, và app không giấu mà tô xám. Trong vùng dữ liệu (19 %), người dùng thấy xu hướng kèm khoảng tin cậy. Nút Exploration là minh họa, chưa có nguồn — app ghi rõ và em không trình bày nó như số liệu NASA; em chỉ nói định tính "oxy cao, áp suất thấp" theo NASA [ev-14].

**5. LLM có bịa không?**
Có thể sai, nên em hạn chế nó: nhiệt độ 0, chỉ nhận danh sách bằng chứng, các insight và đầu ra mô hình, phải gắn mã sau mỗi câu; app báo nếu mã không tồn tại hoặc câu trả lời không có nguồn, và dán nhãn "AI summary, check the cited sources". Nguồn sự thật là tab Evidence. Tab này tắt khi không có API key.

**6. SAFFIRE-II chỉ có vài mẫu, sao kết luận được 0 g khác 1 g?**
Em chỉ kết luận cho *những mẫu đó*: silicone mỏng cháy hết ở 1 g nhưng ≈ 0 ở 0 g, vải cháy hết ở cả hai. Không phải quy luật tổng quát — bài Saffire nói cần nhiều mẫu và vật liệu hơn [ev-19]. Em cũng ghi chú một mẫu SIBAL kế hoạch 30 cm/s nhưng PSI-99 ghi 20 cm/s [ev-01].

**7. Ai sẽ dùng, và tác động thực tế là gì?**
Nhà thiết kế khí quyển, sinh viên, người làm an toàn nhiệm vụ — để khám phá nhanh và biết nên hỏi gì tiếp. Không dùng để chứng nhận. Em chưa có người dùng thật; hướng tiếp theo là dữ liệu FLEX-2 khi có kết quả.

**8. Em dùng AI thế nào, và ai kiểm chứng?**
Claude (qua Claude Code) giúp viết mã, trích 27 phát hiện từ file và trang NASA, và soạn bài. Mỗi phát hiện có trích dẫn và cờ verified để kiểm tra lại; sáu insight tính bằng script `scripts/make_insights.py` từ dữ liệu FLEX; mỗi số trong bài nộp gắn với mã bằng chứng, insight hoặc đầu ra `flame_model.py`. **[ĐIỀN: bạn đã tự đối chiếu những mục nào với nguồn — nói đúng mức đó.]** Trong app: mô hình học máy cổ điển và một LLM qua OpenRouter chỉ ở tab hỏi đáp.

---
*Bonus:* "Bình bọt trên Mir có dập được lửa không?" → Theo bài NASA, phi hành đoàn dùng ba bình bọt và ngọn lửa cuối cùng tự tắt; em không kết luận bình bọt đã dập được nó [ev-27]. "Apollo 1 có phải vi trọng lực không?" → Không, đó là thử nghiệm mặt đất ở 1 g; nó cho thấy nguy cơ của khí quyển 100 % oxy [ev-26]. "Con số bất ngờ nhất?" → silicone 0,27 mm cháy hết ở 1 g nhưng ≈ 0 ở 0 g [ev-02].
