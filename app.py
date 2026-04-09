import streamlit as st
import time
from datetime import datetime
from modules.ui_components import (
    inject_custom_css,
    render_sidebar_content,
    init_report_state,
    render_chat_messages,
    render_report_dialog,
)
from modules.llm_handler import VinFastLLMHandler
from modules.validator import handle_exception

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Vivin Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INITIALIZE SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "ViVin xin chào, anh/chị đang có nhu cầu mua loại xe nào?"}]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "chat"
if "loading" not in st.session_state:
    st.session_state.loading = False

init_report_state()
llm_agent = VinFastLLMHandler()

# 3. SETUP CSS & HEADER
inject_custom_css()

# 4. SIDEBAR
with st.sidebar:
    render_sidebar_content()

# 5. PAGE CONTENT
if st.session_state.current_page == "chat":
    if st.session_state.report_submitted:
        st.success("Report sent. Thank you for your feedback.")
        st.session_state.report_submitted = False

    render_chat_messages(st.session_state.messages)
    
    if st.session_state.loading:
        st.markdown('<div class="msg-wrapper bot"><div class="avatar">🤖</div><div class="bubble">...</div></div>', unsafe_allow_html=True)

    # Khung nhập liệu tối ưu
    with st.form(key="chat_input_final", clear_on_submit=True):
        cols = st.columns([0.88, 0.12])
        user_msg = cols[0].text_input("Input", placeholder="Hỏi ViVin tại đây...", label_visibility="collapsed")
        submit = cols[1].form_submit_button("SEND")

    if submit and user_msg:
        check = handle_exception(user_msg)
        if check["status"] == "ok":
            st.session_state.messages.append({"role": "user", "content": user_msg})
            st.session_state.loading = True
            st.rerun()
        else:
            st.error(check["message"])

elif st.session_state.current_page == "history":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("📋 Lịch sử trò chuyện")
    if not st.session_state.chat_history:
        st.info("Chưa có lịch sử trò chuyện.")
    else:
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.expander(f"Hội thoại ngày {chat['time']}"):
                for m in chat['messages']:
                    st.write(f"**{m['role'].upper()}**: {m['content']}")

elif st.session_state.current_page == "account":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.title("👤 Thông tin cá nhân")
    st.info("Tính năng đang được cập nhật.")

# 6. AI RESPONSE LOGIC
if st.session_state.report_target_idx is not None:
    render_report_dialog(st.session_state.messages)

if st.session_state.loading:
    time.sleep(0.5)
    last_user_msg = st.session_state.messages[-1]["content"]
    response = llm_agent.get_response(last_user_msg, session_id="session_f1")
    st.session_state.messages.append({"role": "bot", "content": response})
    st.session_state.loading = False
    st.rerun()
