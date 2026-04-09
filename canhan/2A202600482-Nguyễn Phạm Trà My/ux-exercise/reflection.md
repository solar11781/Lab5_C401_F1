# Individual reflection — Nguyễn Phạm Trà My 2A202600482
## 1. Role
UI/UX Designer + Data Engineer. Phụ trách thiết kế giao diện người dùng, xây dựng cấu trúc Dataset cho chatbot và thiết kế quy trình vận hành (Workflow) hệ thống.

## 2. Đóng góp cụ thể
- **Thiết kế giao diện:** Hoàn thiện bộ UI/UX trên Figma cho chatbot ViVin với phong cách hiện đại, tối ưu hóa trải nghiệm chat và các thành phần hiển thị thông tin (ví dụ như lịch sử chat).
- **Xây dựng Dataset:** Tổng hợp và chuẩn hóa tập dữ liệu mẫu (SFT - Supervised Fine-tuning) bao gồm các cặp câu hỏi-trả lời đa dạng để huấn luyện bot hiểu đúng ý định người dùng.
- **Thiết kế Workflow:** Xây dựng sơ đồ luồng nghiệp vụ (Workflow) từ bước tiếp nhận input, xử lý qua bộ lọc trung gian đến khi trả về output cuối cùng cho người dùng.

## 3. SPEC mạnh/yếu
- **Mạnh nhất: Data Structure & Logic Flow** — Nhóm đã xây dựng được một cấu trúc dữ liệu rất chặt chẽ, giúp chatbot phân loại được ý định người dùng (Intent Classification) chính xác ngay từ đầu, từ đó kích hoạt đúng workflow tương ứng.
- **Yếu nhất: Data Diversity** — Dataset hiện tại vẫn tập trung nhiều vào các kịch bản lý tưởng. Khi người dùng sử dụng nhiều tiếng lóng hoặc cách diễn đạt quá phức tạp, quy trình xử lý đôi khi bị nghẽn hoặc trả về kết quả mặc định do dữ liệu huấn luyện chưa bao phủ hết các biến thể ngôn ngữ.

## 4. Đóng góp khác
- Xây dựng hệ thống Design System nhất quán giúp việc chuyển đổi từ bản thiết kế sang code của team Frontend diễn ra nhanh chóng.
- Góp ý và điều chỉnh các bước trong Workflow để giảm thiểu latency, loại bỏ các bước xử lý trung gian không cần thiết giúp tăng tốc độ phản hồi của ViVin.

## 5. Điều học được
Thiết kế cho AI không chỉ là vẽ giao diện đẹp, mà là thiết kế sự tin tưởng. Cách chatbot hiển thị trạng thái "đang suy nghĩ" hay cách nó trình bày các gợi ý cá nhân hóa có ảnh hưởng rất lớn đến trải nghiệm người dùng. Đồng thời, việc làm Dataset khiến em biết được đầu vào quyết định rất lớn đến trí thông minh của chatbot.

## 6. Nếu làm lại
Sẽ dành thêm thời gian để xây dựng một quy trình "Human-in-the-loop" trong workflow. Tức là có một bước để người dùng hoặc admin có thể điều chỉnh dữ liệu sai ngay lập tức, giúp cập nhật dataset liên tục (Continuous Learning) thay vì phải đợi các đợt cập nhật lớn. Hiện tại nhóm chỉ đang dừng lại ở việc người dùng select báo cáo những lỗi phổ biến.

## 7. AI giúp gì / AI sai gì
- **Giúp:** Sử dụng các công cụ AI để tự động hóa việc sinh thêm các biến thể câu hỏi cho dataset, giúp tiết kiệm thời gian chuẩn bị dữ liệu.
- **Sai/mislead:** AI gợi ý một workflow quá cồng kềnh với nhiều lớp kiểm tra chồng chéo, làm tăng đáng kể thời gian phản hồi (latency). Bài học là: AI giúp mở rộng ý tưởng, nhưng con người phải là bộ lọc để tối ưu hóa quy trình thực tế.
