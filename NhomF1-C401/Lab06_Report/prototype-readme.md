# Prototype — AI VinFast

## Mô tả
Người dùng đưa ra các nhu cầu về xe VinFast của mình, chat bot đưa ra gợi ý dựa trên các thông số kỹ thuật và review thực tế từ người dùng khác.

## Level: Working
- UI build bằng Stitch của Google
- 1 flow chính chạy thật với OpenAI API: nhập mong muốn → nhận gợi ý xe

## Links
- Prototype: demo trên local host bằng streamlit (Link thiết kế UI: https://stitch.withgoogle.com/preview/54587746502445460?node-id=5c51903df2e84f35b1a8f0a556233d1f)
- Prompt test log: xem file `prompts/prompt-tests.md`

## Tools
- UI: Stitch
- AI: Gpt-4o (via OpenAi API)
- Prompt: system prompt + few-shot examples cho 18 test case

## Phân công
| Thành viên | Phần | Output |
|-----------|------|--------|
| Lại Gia Khánh | Canvas + Deployment| NhomF1-C401/Lab06_Report/spec-final.md phần 1, app.py |
| Lê Duy Anh | User stories 4 paths + prompt engineering + mô hình ReAct| NhomF1-C401/Lab06_Report/spec-final.md phần 2, prompt/prompt-tests.md, prompt/system_prompt, tools/tools.py, modules/llm_handler.py, NhomF1-C401/Lab06_Report/prototype.md |
| Trương Minh Sơn | Eval metrics + Tính toán ROI (Pin) | NhomF1-C401/Lab06_Report/spec-final.md phần 3, modules/battery_calc.py |
| Bùi Trần Gia Bảo | Top 3 failure modes + Exception Handling + Backend developer | NhomF1-C401/Lab06_Report/spec-final.md phần 4, modules/data_loader.py, modules/validator.py, modules/llm_handler.py|
| Nguyễn Phạm Trà My | ROI 3 kịch bản + UI prototype | NhomF1-C401/Lab06_Report/spec-final.md phần 5, modules/ui_components.py, app.py|
| Mạc Phương Nga | Mini AI spec + Mock Data + demo slide | NhomF1-C401/Lab06_Report/spec-final.md phần 6, data/, tools/get_info.py, tools/get_review.py, NhomF1-C401/Lab06_Report/feedback.md, NhomF1-C401/Lab06_Report/demo_slides.pdf |

