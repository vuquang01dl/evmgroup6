import numpy as np

# Số lượng mẫu
num_samples = 1000

# Tạo mẫu cho phần trăm tiến độ hoàn thành (percent_complete) từ phân phối chuẩn
percent_complete_mean = 0.5
percent_complete_sd = 0.2
percent_complete_data = np.random.normal(percent_complete_mean, percent_complete_sd, num_samples)

# Tạo mẫu cho chi phí thực tế (actual_cost) từ phân phối chuẩn
actual_cost_mean = 50000
actual_cost_sd = 10000
actual_cost_data = np.random.normal(actual_cost_mean, actual_cost_sd, num_samples)

# Tạo mẫu cho giá trị kế hoạch (planned_value) từ phân phối chuẩn
planned_value_mean = 60000
planned_value_sd = 10000
planned_value_data = np.random.normal(planned_value_mean, planned_value_sd, num_samples)

# In ra một số mẫu
print("Mẫu dữ liệu phần trăm tiến độ hoàn thành (percent_complete):", percent_complete_data[:5])
print("Mẫu dữ liệu chi phí thực tế (actual_cost):", actual_cost_data[:5])
print("Mẫu dữ liệu giá trị kế hoạch (planned_value):", planned_value_data[:5])
