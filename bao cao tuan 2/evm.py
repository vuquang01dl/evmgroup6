def calculate_earned_value(cost_budget, percent_complete):
    return cost_budget * percent_complete / 100

def calculate_CPI(EV, AC):
    return EV / AC

def calculate_SPI(EV, PV):
    return EV / PV

def calculate_CV(EV, AC):
    return EV - AC

def calculate_SV(EV, PV):
    return EV - PV

def main():
    # Nhập dữ liệu từ người dùng
    cost_budget = float(input("Nhập ngân sách dự án: "))
    percent_complete = float(input("Nhập phần trăm tiến độ hoàn thành (0-100): "))
    actual_cost = float(input("Nhập chi phí thực tế đến hiện tại: "))
    planned_value = float(input("Nhập giá trị kế hoạch đến hiện tại: "))

    # Tính toán giá trị đã kiếm được (Earned Value)
    EV = calculate_earned_value(cost_budget, percent_complete)

    # Tính toán chỉ số quản lý
    CPI = calculate_CPI(EV, actual_cost)
    SPI = calculate_SPI(EV, planned_value)
    CV = calculate_CV(EV, actual_cost)
    SV = calculate_SV(EV, planned_value)

    # In kết quả
    print("\n--- Chỉ số quản lý ---")
    print("CPI (Cost Performance Index):", CPI)
    print("SPI (Schedule Performance Index):", SPI)
    print("CV (Cost Variance):", CV)
    print("SV (Schedule Variance):", SV)

if __name__ == "__main__":
    main()
