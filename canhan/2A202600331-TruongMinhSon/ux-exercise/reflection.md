# Individual Reflection — Trương Minh Sơn (2A202600331)

## 1. Role
**AI Logic Architect & Lead Developer.** Phụ trách thiết kế cấu trúc dữ liệu (Data Schema), xây dựng module tính toán ROI (`battery_calc.py`) và tích hợp logic xử lý vào hệ thống Chatbot/Streamlit.

## 2. Đóng góp cụ thể
* **Phát triển Module ROI chuyên sâu:** Xây dựng Class `BatteryCalculator` xử lý bài toán kinh tế phức tạp giữa việc "Mua đứt" vs "Thuê pin".
* **Thiết kế Logic Tài chính:** Tích hợp các biến số thực tế như **Opportunity Cost** (Chi phí cơ hội từ lãi suất ngân hàng 5%) và **TCO** (Total Cost of Ownership) để so sánh trực tiếp với các dòng xe xăng đối ứng.
* **Xây dựng Data Pipeline:** Chuẩn hóa dữ liệu cho hơn 15 dòng xe (từ VF 3, VF 7 Plus đến các dòng xe máy điện như Klara S 2026) với cơ chế gói cước linh hoạt.
* **Tối ưu hóa UI/UX:** Code logic hiển thị kết quả dưới dạng Markdown Table, giúp AI phản hồi khách hàng một cách trực quan, chuyên nghiệp ngay trên giao diện Demo.
* **Phụ trách Demo:** Phụ trách Demo, show logic code, deep unstanding với các nhóm khác, thuyết trình và trả lời câu hỏi chuyên sâu, handle cases nhận feedback và sửa lỗi 

## 3. SPEC mạnh/yếu
* **Mạnh nhất: Edge Case Handling.** Hệ thống xử lý mượt mà các trường hợp đặc biệt như dòng xe không giới hạn km (`limit: 0`) và đưa ra cảnh báo bảo trì tự động khi người dùng nhập số km di chuyển cực cao (>10,000 km/tháng).
* **Yếu nhất: ROI Assumptions.** Hiện tại, định mức tiêu thụ điện đang được mặc định theo loại phương tiện (15kWh cho ô tô). Nếu có thêm thời gian, em sẽ tách định mức này chi tiết cho từng model xe để độ chính xác đạt mức tuyệt đối.

## 4. Đóng góp khác
* **Git Workflow & Debugging:** Quản lý mã nguồn, xử lý các lỗi xung đột định dạng dòng (LF/CRLF) và đảm bảo tính nhất quán của code khi triển khai.
* **Prompt Engineering:** Hỗ trợ viết System Prompt giúp AI Agent biết cách trích xuất dữ liệu từ module Python để tư vấn khách hàng theo phong cách chuyên gia tài chính.

## 5. Điều học được
Qua dự án, em nhận ra **AI không chỉ là ngôn ngữ, AI là sự kết hợp giữa ngôn ngữ và logic.** Việc sử dụng Python để tính toán con số chính xác, sau đó dùng LLM để diễn giải con số đó chính là chìa khóa để tạo ra một sản phẩm AI thực thụ. Em cũng nắm vững cách tối ưu hóa cấu trúc dữ liệu Dictionary lồng nhau để đảm bảo tốc độ truy xuất đạt $O(1)$.

## 6. Nếu làm lại
Em sẽ bổ sung thêm tính năng **Data Visualization**. Thay vì chỉ trả về bảng dữ liệu, em sẽ tích hợp thêm biểu đồ đường (Line Chart) so sánh chi phí tích lũy giữa xe xăng và xe điện qua các năm. Như thế sẽ làm rõ hơn rất nhiều về lợi ích và nâng cao nhu cầu sử dụng xe Vinfast.
## 7. AI giúp gì / AI sai gì
* **Giúp:** Sử dụng AI để brainstorm các kịch bản thất bại (Failure modes) và các câu hỏi phản biện của giảng viên, từ đó hoàn thiện hàm `calculate_roi_pro` với khả năng xử lý ngoại lệ tốt hơn.
* **Sai/Mislead:** AI từng gợi ý sử dụng các thư viện tài chính phức tạp gây "scope creep". Em đã quyết định tự viết logic toán học thuần túy để giữ cho code gọn nhẹ, dễ kiểm soát và phù hợp với quy mô một bản Prototype.