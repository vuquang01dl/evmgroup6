import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Tạo dữ liệu giả định
data = pd.DataFrame({
    'EVM_result': ['High', 'Low', 'Medium', 'High', 'Low'],
    'Vulnerability_count': [10, 2, 5, 12, 3],
    'Risk_level': ['High', 'Low', 'Medium', 'High', 'Low']
})

# Xây dựng mô hình Bayesian Network
model = BayesianNetwork([('EVM_result', 'Risk_level'), ('Vulnerability_count', 'Risk_level')])
cpd_evm = TabularCPD(variable='EVM_result', variable_card=3, values=[[0.4], [0.3], [0.3]])
cpd_vuln = TabularCPD(variable='Vulnerability_count', variable_card=5, values=[[0.2], [0.4], [0.2], [0.1], [0.1]])
cpd_risk = TabularCPD(variable='Risk_level', variable_card=3, values=[[0.2, 0.6, 0.2],
                                                                       [0.7, 0.1, 0.2],
                                                                       [0.1, 0.3, 0.6]],
                      evidence=['EVM_result', 'Vulnerability_count'], evidence_card=[3, 5])
model.add_cpds(cpd_evm, cpd_vuln, cpd_risk)

# In thông tin mô hình
print("Cấu trúc mô hình:")
print(model.edges())
print("\nBảng xác suất có điều kiện cho các biến:")
print(model.get_cpds())

# Dự đoán rủi ro bảo mật
inference = VariableElimination(model)
query = inference.map_query(variables=['Risk_level'], evidence={'EVM_result': 'High', 'Vulnerability_count': 8})
print("\nDự đoán rủi ro bảo mật khi EVM_result là High và Vulnerability_count là 8:")
print(query)
