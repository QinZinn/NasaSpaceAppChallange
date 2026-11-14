# submission/ — Workstream C

**Hạn nộp để được chấm giải Hà Nội: 11:00 Chủ nhật 15/11/2026.**

| File | Nội dung |
|---|---|
| `submission.md` | 8 ô của form (Project Name, High-Level Summary, Project Demo, Final Project, Project Details, Use of AI, NASA Data, References), tiếng Anh; số liệu gắn `ev-NN` / `in-NN` / `[model]` |
| `demo_script.md` | Demo 7 slide (kể cả bìa), nội dung từng slide; slide 4 = thông điệp chính "0 trên 17" (in-02) |
| `pitch_5min.md` | Kịch bản nói ~6 phút 20 giây tiếng Việt, chia theo 5 tiêu chí + 8 câu hỏi giám khảo |
| `fact_check.md` | Đối chiếu từng con số; danh sách việc còn mở |

## Quy tắc đã áp dụng
- Apollo 1 và Mir chỉ dùng chi tiết trong ev-26, ev-27; không nêu tên phi hành gia; Mir: lửa "tự tắt" sau khi phi hành đoàn dùng bình bọt.
- Thông điệp chính in-02 luôn đi kèm caveat: chỉ giọt nhiên liệu lỏng; "không tự tắt" gồm cả Disruption.
- Preset "Exploration atmosphere" (34 % O₂, 0,7 atm) là minh họa, không phải số liệu khí quyển của NASA; điều kiện này nằm trong vùng test FLEX của in-02. Về khí quyển thám hiểm chỉ nói định tính theo ev-14. Demo vùng ngoại suy: kéo O₂ lên 40 % và áp suất lên 3 atm.
- pypdf đã bỏ khỏi References.

## Việc còn lại (theo thứ tự)
1. Làm 7 slide theo `demo_script.md`, xuất link công khai, mở thử bằng cửa sổ ẩn danh, dán vào §3 của `submission.md`.
2. Dán link repo (công khai?) / app vào §4; kiểm giới hạn ký tự từng ô trên form.
3. Điền mức bạn tự kiểm evidence (§6; câu hỏi 8 của pitch). Xác nhận bản demo có `OPENROUTER_API_KEY` (model mặc định đã là `z-ai/glm-5.3-flash`).
4. Chạy lại `uv run flame_model.py` trước khi nộp; số khác thì sửa các file.
5. Xóa khối ghi chú đầu `submission.md` trước khi dán vào form.
