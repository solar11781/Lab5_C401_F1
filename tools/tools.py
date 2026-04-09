from langchain_core.tools import tool

# Kết nối với module của Dev 3 để lấy Vector Database chung của dự án
# (Bạn cần nhắc Dev 3 viết hàm get_vector_db này trong modules/data_loader.py)
from modules.data_loader import get_vector_db

vectorstore = get_vector_db()

@tool
def get_vinfast_specs(query: str) -> str:
    """Công cụ này dùng để lấy thông số kỹ thuật (kích thước, động cơ, tầm hoạt động, giá xe) của các dòng xe VinFast."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3, "filter": {"source": "specs"}})
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs]) if docs else "Không tìm thấy thông số."

@tool
def get_community_reviews(query: str) -> str:
    """Công cụ này dùng để lấy đánh giá thực tế từ người dùng (ưu điểm, nhược điểm, lỗi vặt, trải nghiệm)."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3, "filter": {"source": "reviews"}})
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs]) if docs else "Không tìm thấy đánh giá."

@tool
def get_battery_policy(query: str) -> str:
    """Công cụ này dùng để lấy thông tin chi tiết về giá pin, chính sách thuê pin và mua pin."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query + " thuê pin mua pin chi phí")
    return "\n\n".join([doc.page_content for doc in docs]) if docs else "Không tìm thấy chính sách pin."

# Gom lại thành list để truyền cho LLM
agent_tools = [get_vinfast_specs, get_community_reviews, get_battery_policy]