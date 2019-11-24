from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import numpy as np
from matplotlib import pyplot as plt

from parse_to_Matrix import to_Matrix as load

# load初始数据:Matrix
M = load()

# 初始化PCA对象:PCA
# 设定主成分为5
pca = PCA(n_components=5)

# 初始设计矩阵：Martix
A = np.array(M)

# 对 A 标准化
for j in range(M.shape[1]):
    # 标准化列向量
    A[:,j] = StandardScaler().fit_transform(A[:,j].reshape(-1,1)).flatten()

# 主成分分析
pca.fit(A)

# 标准正交特征向量组:Vector_Group
eta_g = pca.get_covariance()
# 贡献度组:Vector
ratio_v = pca.explained_variance_ratio_

print('eta_g',eta_g)
print('ratio_v',ratio_v)

# 标准化变量回归方程参数组：Vector
SVRECG = ratio_v.reshape(1,-1) @ eta_g

# 计算原始变量的主成分回归方程
# 常数项
CIORE = np.average(M)
# 列向量方差 Sigma 组：Vector
sigma_g = np.array([np.std(M[:,j],ddof=1) for j in range(M.shape[1])])
# 原始变量的主成分回归方程参数组：Vector
OVPCARECG = SVRECG @ np.diag(sigma_g)

# Print on screen
print('OVPCARECG',OVPCARECG)
print('CIORE',CIORE)

# 综合指数 组：Vector
INDEX_g = M @ (OVPCARECG.reshape(-1,1)) + CIORE

print('INDEX_g',INDEX_g)

# 综合指数等级 组：Vector
INDEX_LOG_g = np.log10(INDEX_g)
print(INDEX_LOG_g)
