import json
from langchain_core.tools import tool

from tools.get_info import get_vehicle_info
from tools.get_review import get_vehicle_reviews
from modules.battery_calc import BatteryCalculator

@tool
def get_vinfast_specs(model_name: str, specs: list = None) -> str:
    """Công cụ này dùng để lấy thông số kỹ thuật (kích thước, động cơ, tầm hoạt động, giá xe) của xe VinFast.
    Nhập tên xe (ví dụ: 'VF 5 Plus') và danh sách thông số cần tìm (ví dụ: ['dung_luong', 'gia_xe']).
    """
    result = get_vehicle_info(model_name, specs)
    return json.dumps(result, ensure_ascii=False, indent=2)

@tool
def get_community_reviews(model_name: str, specs: list = None, react: str = None) -> str:
    """Công cụ này dùng để lấy đánh giá thực tế từ người dùng.
    react có thể là 'positive', 'negative', hoặc 'neutral'.
    specs là list các tính năng cần review (ví dụ: ['sac_nhanh', 'cach_am']).
    """
    result = get_vehicle_reviews(model_name, specs, react)
    return json.dumps(result, ensure_ascii=False, indent=2)

@tool
def calculate_battery_roi(model_name: str, km_per_month: int) -> str:
    """Công cụ này dùng để tính toán chi phí thuê pin, mua pin và điểm hòa vốn dựa trên số km di chuyển mỗi tháng."""
    calc = BatteryCalculator(specs_data={}) # Không dùng tham số specs_data bên trong code
    result = calc.calculate_roi_pro(model_name, km_per_month)
    return json.dumps(result, ensure_ascii=False, indent=2)

# Gom lại thành list để truyền cho LLM
agent_tools = [get_vinfast_specs, get_community_reviews, calculate_battery_roi]