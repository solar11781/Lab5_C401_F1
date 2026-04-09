# Individual reflection — Lại Gia Khánh (2A202600375)

## 1. Role
Reporter + Deployment. Phụ trách tổng hợp Final SPEC và deploy chatbot.

## 2. Đóng góp cụ thể
- Tổng hợp và chỉnh sửa Final SPEC vào file markdown.
- Deploy chatbot sử dụng Streamlit Cloud.

## 3. SPEC mạnh/yếu

**Mạnh nhất:**
- **AI Product Canvas (3 cột)** — rõ ràng phân tách Value/Trust/Feasibility từ đầu, giúp team không chỉ biết product giải gì mà còn biết khi AI sai thì user xử thế nào

**Yếu nhất:**
- **Data source freshness** — spec nói "crawl thường xuyên" nhưng không nêu rõ tần suất (daily/weekly?), kiểm tra data quality bằng cách nào, handle chuỗi review outdated hoặc sai lệch

## 4. Đóng góp khác
- Code feature reporting chatbot'answer message và lưu lại những report vào file json ở local.
- Đưa ra một số test case để test chatbot

## 5. Điều học được
- Hiểu rõ được sự quan trọng của quá trình brainstorming và planning cho một AI product.
- Thay vì list features, list failure modes giúp xác định được các risk từ đầu

## 6. Nếu làm lại
- Test system prompt sớm hơn để đưa ra những điều chỉnh giúp system prompt mạnh hơn.
- Phát triển RAG để lưu trữ dữ liệu từ review khách hàng thay vì lưu vào file json giúp tìm kiếm nhanh hơn.

## 7. AI giúp gì / AI sai gì

**Giúp:**
- Sử dụng ChatGPT và Gemini để hỗ trợ trong quá trình brainstorm và planning khi nhận được đề tài.
- ChatGPT và Gemini hỗ trợ trong việc làm rõ Value/Trust/Feasibility từ đầu giúp đi đúng hướng.

**Sai/mislead:**
- ChatGPT gợi ý booking feature nghe hợp lý nhưng scope quá to cho hackathon (cần integration calendar, payment, reminder).
- ChatGPT gợi ý lấy dữ liệu từ API hoặc crawl data từ website nhưng quá trình mất nhiều thời gian, không phù hợp với hackathon ngắn hạn.

Bài học: 
- AI tốt ở brainstorm idea nhưng không biết project constraints.