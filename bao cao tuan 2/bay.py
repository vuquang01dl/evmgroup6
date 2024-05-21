import pymc3 as pm
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
# Xây dựng mô hình Bayesian Networks
with pm.Model() as model:
    # Định nghĩa các biến ngẫu nhiên
    percent_complete = pm.Normal('percent_complete', mu=0.5, sd=0.2)  # Giả định phần trăm tiến độ hoàn thành
    actual_cost = pm.Normal('actual_cost', mu=50000, sd=10000)  # Giả định chi phí thực tế
    planned_value = pm.Normal('planned_value', mu=60000, sd=10000)  # Giả định giá trị kế hoạch

    # Tính toán giá trị đã kiếm được dựa trên phần trăm tiến độ hoàn thành và giá trị kế hoạch
    EV = percent_complete * planned_value

    # Tính toán các chỉ số quản lý
    CPI = EV / actual_cost
    SPI = EV / planned_value
    CV = EV - actual_cost
    SV = EV - planned_value

    # Định nghĩa các phân phối hậu nghiệm cho các biến ngẫu nhiên
    percent_complete_obs = pm.Normal('percent_complete_obs', mu=percent_complete, sd=0.1, observed=percent_complete_data)
    actual_cost_obs = pm.Normal('actual_cost_obs', mu=actual_cost, sd=1000, observed=actual_cost_data)
    planned_value_obs = pm.Normal('planned_value_obs', mu=planned_value, sd=1000, observed=planned_value_data)

    # Tiến hành lấy mẫu từ phân phối hậu nghiệm
    trace = pm.sample(1000, tune=1000)

# In kết quả
pm.summary(trace)
