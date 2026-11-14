# submission/ — Workstream C

Deadline: **15 Nov 2026, 23:59 (Asia/Ho_Chi_Minh)** — hôm nay là 14/11.

| File | Nội dung |
|---|---|
| `submission.md` | Tiêu đề, summary, mô tả, dữ liệu NASA, công cụ AI, links (tiếng Anh — dán vào form) |
| `demo_script.md` | Kịch bản video 30 s + phương án 7 slide + Q&A cheat-sheet |
| `fact_check.md` | Bảng đối chiếu từng con số; nguồn và trạng thái ✅ / [CẦN KIỂM TRA] |

## Việc BẮT BUỘC làm trước khi nộp

1. **Đọc lại 2 guide chính thức 2026** (không lấy được từ môi trường này: HTTP 503 và lỗi TLS).
   Xác nhận: giới hạn demo (30 s video / 7 slide), giới hạn ký tự các trường, tiêu chí chấm, yêu cầu khai báo AI.
   https://www.spaceappschallenge.org/resources/project-submission-guide/ ·
   https://www.spaceappschallenge.org/resources/judging-awards-guide
2. Dán link repo công khai, link demo công khai (không cần đăng nhập), link app vào `submission.md` §6.
3. Xác minh Apollo 1 / Mir (không có trong repo) hoặc bỏ ngày tháng — xem `fact_check.md`.
4. Chạy lại `uv run flame_model.py` ngay trước khi nộp; nếu số đổi thì sửa các bảng.
5. Hỏi workstream A: app có gọi LLM lúc chạy không? tên slider? Hỏi B: `evidence.json` đã có bao nhiêu mục verified?

## Gửi workstream khác (không sửa file của họ)
- **A:** màn hình quay demo phải hiện vùng extrapolation bị làm xám; nhãn "demo data" nếu có.
- **B:** cần trích dẫn có số trang cho Apollo 1 và Mir; xác nhận mapping cột "?-g" của PSI-99 là µ-g và các lần chạy 1 g cùng điều kiện.
- **M:** không có yêu cầu mới; chỉ cần báo nếu đổi mô hình trước deadline.
