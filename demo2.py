import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Đọc dữ liệu từ file Excel
data = pd.read_excel('evm.xlsx')

# Bước 1: Xác định các biến và mối quan hệ
variables = [
    "So_luong_nhan_su", 
    "Thoi_gian_phat_trien", 
    "Phan_mem_phuc_tap", 
    "On_dinh_yeu_cau", 
    "Kinh_nghiem_nhan_su", 
    "Chi_phi"
]

edges = [
    ("So_luong_nhan_su", "Thoi_gian_phat_trien"),
    ("Phan_mem_phuc_tap", "Thoi_gian_phat_trien"),
    ("Phan_mem_phuc_tap", "Chi_phi"),
    ("On_dinh_yeu_cau", "Thoi_gian_phat_trien"),
    ("On_dinh_yeu_cau", "Chi_phi"),
    ("Kinh_nghiem_nhan_su", "Thoi_gian_phat_trien"),
    ("Kinh_nghiem_nhan_su", "Chi_phi"),
    ("Thoi_gian_phat_trien", "Chi_phi")
]

# Tạo mô hình mạng Bayesian
model = BayesianNetwork(edges)

# Bước 2: Xây dựng CPD cho từng biến
# Vì không có dữ liệu cụ thể, sử dụng các giá trị mặc định cho các CPD
cpd_so_luong_nhan_su = TabularCPD(variable="So_luong_nhan_su", variable_card=3, values=[[0.3], [0.5], [0.2]])
cpd_phan_mem_phuc_tap = TabularCPD(variable="Phan_mem_phuc_tap", variable_card=2, values=[[0.6], [0.4]])
cpd_on_dinh_yeu_cau = TabularCPD(variable="On_dinh_yeu_cau", variable_card=2, values=[[0.7], [0.3]])
cpd_kinh_nghiem_nhan_su = TabularCPD(variable="Kinh_nghiem_nhan_su", variable_card=3, values=[[0.4], [0.4], [0.2]])

# Các CPD cho biến phụ thuộc
cpd_thoi_gian_phat_trien = TabularCPD(variable="Thoi_gian_phat_trien", variable_card=3,
                                      values=[[0.1] * 36,
                                              [0.3] * 36,
                                              [0.6] * 36],
                                      evidence=["So_luong_nhan_su", "Phan_mem_phuc_tap", "On_dinh_yeu_cau", "Kinh_nghiem_nhan_su"],
                                      evidence_card=[3, 2, 2, 3])

cpd_chi_phi = TabularCPD(variable="Chi_phi", variable_card=3,
                         values=[[0.8] * 36,  # Tăng xác suất cho chi phí thấp
                                 [0.15] * 36,
                                 [0.05] * 36],
                         evidence=["Thoi_gian_phat_trien", "Phan_mem_phuc_tap", "On_dinh_yeu_cau", "Kinh_nghiem_nhan_su"],
                         evidence_card=[3, 2, 2, 3])

# Thêm các CPD vào mô hình
model.add_cpds(cpd_so_luong_nhan_su, cpd_phan_mem_phuc_tap, cpd_on_dinh_yeu_cau, cpd_kinh_nghiem_nhan_su, cpd_thoi_gian_phat_trien, cpd_chi_phi)

# Kiểm tra tính hợp lệ của mô hình
assert model.check_model()

# Bước 3: Tích hợp EVM và suy luận
# Giả sử chúng ta có các giá trị EVM như PV, EV, AC từ file Excel
PV = data["PV"].iloc[5]
EV = data["EV"].iloc[5]
AC = data["AC"].iloc[5]

# Tính toán các chỉ số EVM
CPI = EV / AC
SPI = EV / PV

# Đưa các chỉ số này vào mạng Bayesian dưới dạng bằng chứng
inference = VariableElimination(model)

# Vì dữ liệu của bạn không chứa thông tin về các biến khác, 
# chúng ta sẽ sử dụng các giá trị giả định cho bằng chứng để minh họa
evidence = {
    "So_luong_nhan_su": 1,  # giả sử trạng thái 0 cho So_luong_nhan_su
    "Thoi_gian_phat_trien": 1,  # giả sử trạng thái 0 cho Thoi_gian_phat_trien
    "Phan_mem_phuc_tap": 0,  # giả sử trạng thái 0 cho Phan_mem_phuc_tap
    "On_dinh_yeu_cau": 1,  # giả sử trạng thái 0 cho On_dinh_yeu_cau
    "Kinh_nghiem_nhan_su": 2  # giả sử trạng thái 2 cho Kinh_nghiem_nhan_su
}

# Suy luận chi phí dựa trên các bằng chứng hiện tại
posterior = inference.map_query(variables=["Chi_phi"], evidence=evidence)

print(posterior)
