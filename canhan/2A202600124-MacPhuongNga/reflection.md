# Individual reflection — Mạc Phương Nga 2A202600124

## 1. Role
Chịu trách nhiệm xây dựng cấu trúc dữ liệu mô phỏng (Mock data) và phát triển hai công cụ cốt lõi: `get_info.py` và `get_review.py`.

## 2. Đóng góp cụ thể
- Mock data: Xây dựng hệ thống dữ liệu JSON cho vinfast_specs.json và vinfast_reviews.json. Đảm bảo dữ liệu đủ độ phức tạp (nested structures) để thử nghiệm khả năng truy xuất sâu của AI.
- `get_info.py`: Viết logic tìm kiếm linh hoạt (theo tên xe, theo thông số, dặc điểm) giúp AI đọc đúng đối tượng mà người đọc đang đề cập.
- `get_review.py`: Xây dựng thuật toán lọc đánh giá theo cảm xúc (Sentiment) và chủ đề (Specs). Đặc biệt là thiết lập cơ chế Fallback Mechanism (nếu không tìm thấy đánh giá cụ thể, hệ thống tự động gợi ý các đánh giá chung hoặc đánh giá của dòng xe tương đương), đảm bảo mạch hội thoại không bị ngắt quãng.

## 3. SPEC mạnh/yếu
- Mạnh nhất: AI Product Canvas - hiện thực hóa được cấu trúc dữ liệu phức tạp và các công cụ truy xuất linh hoạt, cho phép Agent thực hiện chuỗi suy luận đa tầng.
- Yếu nhất: failure modes - ặc dù đã thiết lập các rào cản bằng Prompt Engineering, nhưng hệ thống vẫn còn kẽ hở trước các kỹ thuật tấn công Prompt Injection tinh vi (như đóng vai lãnh đạo để thay đổi dữ liệu). Đây là điểm yếu về tính Trust (Lòng tin) mà nhóm cần giải quyết bằng các lớp Guardrails kỹ thuật chuyên sâu hơn hoặc một mô hình kiểm duyệt (Moderation model) độc lập thay vì chỉ dùng Prompt.

## 4. Đóng góp khác
- Test prompt: Thực hiện test thử nhiều kịch bản, tìm ra lỗi của system_prompt.
## 5. Điều học được
- Sức mạnh của LLM và LangGraph rất lớn: Thay vì cần dự đoán các luồng từ trước, giờ chỉ cần xác định các tools, LLM sẽ làm nhiệm vụ điều hướng dựa trên mô tả tools đó.
- System prompt: Do sử dụng LLM làm điều hướng nên system prompt rất quan trọng! Đáng chú ý nhất là cần loại bỏ các trường hợp outllines; không cho phép tác động vào các file data, log hay các file quan trọng khác từ user input.

## 6. Nếu làm lại
Thêm các lớp Guardrails để tránh các tấn công Prompt Injection.
Cần đặt <constraint> cho system prompt chặt chẽ hơn! 
Define các tools rõ ràng hơn; làm rõ data hơn để câu trả lời rõ ràng hơn.

## 7. AI giúp gì / AI sai gì
- **Giúp:** nhờ Gemini nhận xét luồng và tools hiện tại; gợi ý, tối ưu prompt; nhờ ChatGPT tạo danh sách các test case.
- **Sai/mislead:** Gemini gợi ý thêm feature "Thông tin trạm sạc" vào chatbot — hơi lệch so với scope ban đầu. Feature này phù hợp hơn với Người đang sử dụng xe, có thể phát triển về sau nhưng vượt khả năng thực hiện trong 48h.

  Bài học: AI rất giỏi mở rộng ý tưởng nhưng "mù tịt" về giới hạn nguồn lực của con người. Người làm sản phẩm phải là bộ lọc cuối cùng để giữ Scope tập trung.
