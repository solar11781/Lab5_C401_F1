import streamlit as st
import time
from datetime import datetime

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Vivin Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CHÍNH XÁC MÀU SẮC TỪ PALETTE CỦA ANH
COLOR_MAIN_BG = "#F3F8FF"
COLOR_BOT_BUBBLE = "#DEECFF"
COLOR_USER_BUBBLE = "#C6CFFF"
COLOR_ACCENT_HOVER = "#E8D3FF"
COLOR_SIDEBAR_NAVY = "#172B53"
COLOR_YELLOW_BTN = "#FFEB3B"

# 3. INITIALIZE SESSION STATE (LƯU TRỮ THẬT)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "bot", "content": "ViVin xin chào, anh/chị đang có nhu cầu mua loại xe nào?"}]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "chat"
if "loading" not in st.session_state:
    st.session_state.loading = False

# 4. CUSTOM CSS (FIX LỆCH KHUNG, BỎ SHADOW, ĐÚNG MÀU)
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    font-family: 'Inter', sans-serif;
    background-color: {COLOR_MAIN_BG} !important;
}}

[data-testid="stHeader"], [data-testid="collapsedControl"], footer {{ display: none; }}

/* Khung nội dung chính - Căn chỉnh để không bị lệch */
.block-container {{
    max-width: 1000px !important;
    padding: 2rem 1rem 150px 1rem !important;
    margin: 0 auto !important;
}}

/* SIDEBAR STYLING */
[data-testid="stSidebar"] {{
    background-color: {COLOR_SIDEBAR_NAVY} !important;
    border-right: 2px solid {COLOR_ACCENT_HOVER} !important;
}}

.sidebar-title {{ font-size: 24px; font-weight: 800; color: white; text-align: center; margin: 20px 0; }}

/* Nút Sidebar chung */
[data-testid="stSidebar"] .stButton > button {{
    width: 100%;
    background-color: transparent;
    border: none;
    color: rgba(255,255,255,0.7);
    padding: 12px 20px;
    text-align: left;
    justify-content: flex-start;
    font-weight: 500;
    margin-bottom: 8px;
}}

/* HIGHLIGHT NÚT NEW CHAT (MÀU VÀNG) */
.new-chat-container .stButton > button {{
    background-color: {COLOR_YELLOW_BTN} !important;
    color: {COLOR_SIDEBAR_NAVY} !important;
    font-weight: 800 !important;
    border-radius: 12px !important;
    justify-content: center !important;
    box-shadow: none !important;
}}

/* HIGHLIGHT NÚT ĐANG CHỌN  */
div.stButton > button[kind="primary"] {{
    background-color: {COLOR_ACCENT_HOVER} !important;
    color: {COLOR_SIDEBAR_NAVY} !important;
    font-weight: 700 !important;
}}

/* CHAT AREA & BUBBLES - GIÃN CÁCH TỐT */
.chat-container {{ display: flex; flex-direction: column; gap: 25px; }}
.msg-wrapper {{ display: flex; gap: 15px; max-width: 85%; align-items: flex-start; }}
.msg-wrapper.bot {{ align-self: flex-start; }}
.msg-wrapper.user {{ align-self: flex-end; flex-direction: row-reverse; }}

.avatar {{ font-size: 24px; flex-shrink: 0; padding-top: 5px; }}

.bubble {{
    padding: 14px 18px;
    border-radius: 15px;
    font-size: 15px;
    line-height: 1.5;
    box-shadow: none !important; /* XÓA BỎ SHADOW XÁM THEO YÊU CẦU */
}}

/* Đúng màu Palette: Bot = #DEECFF, User = #C6CFFF */
.bot .bubble {{ background-color: {COLOR_BOT_BUBBLE}; color: {COLOR_SIDEBAR_NAVY}; border-top-left-radius: 2px; }}
.user .bubble {{ background-color: {COLOR_USER_BUBBLE}; color: {COLOR_SIDEBAR_NAVY}; border-top-right-radius: 2px; }}

.msg-subtext {{ font-size: 10px; color: #888; margin-top: 5px; font-weight: 500; }}

/* FIXED INPUT FORM - TRIỆT TIÊU LỆCH KHUNG */
[data-testid="stForm"] {{
    position: fixed !important;
    bottom: 30px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 80% !important;
    max-width: 850px !important;
    height: 70px !important;
    background-color: white !important;
    border: 1px solid {COLOR_ACCENT_HOVER} !important;
    border-radius: 16px !important;
    padding: 0 20px !important;
    z-index: 9999 !important;
    overflow: hidden !important;
    box-shadow: none !important; /* XÓA BỎ SHADOW */
}}

/* Bù trừ vị trí form khi sidebar mở để nằm chính giữa vùng chat */
@media (min-width: 768px) {{
    [data-testid="stForm"] {{ left: calc(50% + 130px) !important; }}
}}

[data-testid="stForm"] .stHorizontalBlock {{ align-items: center !important; height: 100%; }}
[data-testid="stTextInput"] input {{ color: {COLOR_SIDEBAR_NAVY} !important; border: none !important; background-color: transparent !important; }}

[data-testid="stFormSubmitButton"] > button {{
    background-color: {COLOR_SIDEBAR_NAVY} !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: bold !important;
    height: 44px !important;
    margin-top: 15px !important;
}}
</style>
""", unsafe_allow_html=True)

# 5. SIDEBAR CONSTRUCTION
with st.sidebar:
    st.markdown('<div class="sidebar-title">VIVIN</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="new-chat-container">', unsafe_allow_html=True)
    if st.button("New Chat", use_container_width=True):
        # Lưu vào lịch sử thật
        if len(st.session_state.messages) > 1:
            st.session_state.chat_history.append({
                "time": datetime.now().strftime("%H:%M - %d/%m"),
                "messages": st.session_state.messages.copy()
            })
        st.session_state.messages = [{"role": "bot", "content": "ViVin xin chào, anh/chị đang có nhu cầu mua loại xe nào?"}]
        st.session_state.current_page = "chat"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation Highlight
    chat_type = "primary" if st.session_state.current_page == "chat" else "secondary"
    if st.button("Current Chat", type=chat_type, use_container_width=True):
        st.session_state.current_page = "chat"
        st.rerun()

    hist_type = "primary" if st.session_state.current_page == "history" else "secondary"
    if st.button("History", type=hist_type, use_container_width=True):
        st.session_state.current_page = "history"
        st.rerun()

    acc_type = "primary" if st.session_state.current_page == "account" else "secondary"
    if st.button("Account", type=acc_type, use_container_width=True):
        st.session_state.current_page = "account"
        st.rerun()

# 6. PAGE ROUTING
if st.session_state.current_page == "chat":
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        role_class = "bot" if msg["role"] == "bot" else "user"
        # Đưa đúng icon 🤖 và 👤 quay trở lại
        icon = "🤖" if msg["role"] == "bot" else "👤"
        st.markdown(f"""
            <div class="msg-wrapper {role_class}">
                <div class="avatar">{icon}</div>
                <div class="msg-content">
                    <div class="bubble">{msg['content']}</div>
                    <div class="msg-subtext">{"VIVIN" if msg["role"]=="bot" else "YOU"} • JUST NOW</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.loading:
        st.markdown('<div class="msg-wrapper bot"><div class="avatar">🤖</div><div class="bubble">...</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.form(key="chat_input_final", clear_on_submit=True):
        cols = st.columns([0.9, 0.1])
        user_msg = cols[0].text_input("Input", placeholder="Hỏi ViVin tại đây...", label_visibility="collapsed")
        submit = cols[1].form_submit_button("SEND")

    if submit and user_msg:
        st.session_state.messages.append({"role": "user", "content": user_msg})
        st.session_state.loading = True
        st.rerun()

elif st.session_state.current_page == "history":
    st.title("History")
    if not st.session_state.chat_history:
        st.info("Chưa có lịch sử trò chuyện.")
    else:
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.expander(f"Hội thoại ngày {chat['time']}"):
                for m in chat['messages']:
                    st.write(f"**{m['role'].upper()}**: {m['content']}")

# 7. LOGIC XỬ LÝ AI
if st.session_state.loading:
    time.sleep(1)
    st.session_state.messages.append({"role": "bot", "content": "Dạ, em đã nhận thông tin. Anh/chị cần xem báo giá hay thông số kỹ thuật ạ?"})
    st.session_state.loading = False
    st.rerun()
