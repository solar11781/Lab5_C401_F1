# Individual reflection — Bùi Trần Gia Bảo (2A202600009)

## 1. Role

Backend developer + prompt engineer. Phụ trách code xử lý ngoại lệ, viết system prompt để xử lý những user input không hợp lệ, deploy app và demo app.

## 2. Đóng góp cụ thể

- Tạo data_loader.py và validator.py để xử lý các invalid user input.
- Tạo các test scripts để chạy full workflow (đã bị overwitten bởi các scripts chính)
- Update llm_handler.py, app.py để xử lý user input và handle exception
- Viết các rules trong system prompt để xử lý user input
- Test và deploy app trên Streamlit Cloud
- Demo và giải thích app cho các nhóm khác

## 3. SPEC mạnh/yếu

- Mạnh nhất: Failure modes - nhóm xác định được các rủi ro quan trọng như AI trả lời thông tin xe bị outdated hoặc hallucinate nhưng user không nhận ra. Đồng thời có mitigation rõ ràng như không trả lời khi không chắc chắn, fallback về nguồn chính thức và thêm validation để giảm hallucination.

- Yếu nhất: Phần data và implementation còn đơn giản. Hiện tại chỉ dùng mock data (JSON) nên chưa phản ánh đúng độ phức tạp của hệ thống thực tế (data lớn, update liên tục). Ngoài ra phần ROI vẫn dựa trên assumption, chưa có dữ liệu thực để validate.

## 4. Đóng góp khác

- Chủ động test nhiều edge cases cho chatbot (input rỗng, spam, yêu cầu ngoài scope, input không hợp lệ) để đảm bảo validator và exception handling hoạt động đúng.
- Hỗ trợ debug luồng xử lý giữa validator → llm_handler → UI, đặc biệt là các trường hợp LLM trả về lỗi hoặc format không đúng.
- Thử nghiệm và điều chỉnh system prompt để giảm hallucination và đảm bảo AI không trả lời khi thiếu dữ liệu.

## 5. Điều học được

Trước hackathon nghĩ chỉ cần system prompt chặn được mọi trường hợp user muốn bypass thì app sẽ an toàn.
Sau khi demo và các bạn test app thì có những trường hợp system prompt đã ngăn user giả làm admin và xin lỗi user nhưng state của agent vẫn ghi nhận yêu cầu đó, dẫn đến việc dữ liệu có thể bị thay đổi dù system prompt đã từ chối.

## 6. Nếu làm lại

Sẽ test thêm nhiều test cases hơn. Có thể sẽ hỏi ý kiến của các nhóm khác thay vì chỉ hỏi AI vì users (đặc biệt là QA và tester) có thể nghĩ ra các trường hợp mà thường chưa từng nghĩ tới. Nếu có nhiều thời gian hơn thì sẽ crawl data thật từ trang chính chủ của Vinfast cho spec của xe và các diễn đàn xe cho review của xe. Sau đó sẽ áp dụng RAG cho data để retrieve nhanh hơn vì mock data hiện giờ chỉ là 2 file json nên lúc tìm xe/tìm review mất rất nhiều thời gian.

## 7. AI giúp gì / AI sai gì

- **Giúp:** dùng ChatGPT để brainstorm failure modes, test cases, system prompts — nó gợi ý được những trường hợp mà agent có thể fail hoặc đưa ra những câu trả lời không đúng. Dùng Github Copilot để code và review codes.
- **Sai/mislead:** ChatGPT gợi ý nhiều trường hợp out of scope hoặc lặp lại ý.

  Bài học:
  - Không nên tin hoàn toàn vào output của AI, đặc biệt là các gợi ý về system design hoặc edge cases — cần tự kiểm chứng lại bằng testing thực tế.
  - AI rất hữu ích để brainstorm và tăng tốc coding, nhưng nếu không kiểm soát tốt thì dễ bị lan man hoặc đi sai hướng.
  - Khi build AI product, phần quan trọng không chỉ là model mà là handling failure cases và đảm bảo system không trả lời sai.
