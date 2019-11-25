from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import numpy as np

# load初始数据:Matrix
M = np.array([[6040.5,15.68,7.89102857e-05,75],
[3568.1352,-20.02,0.00014587,72],
[3060,5.92,0.00032229,54],
[10958.7041,9.76,-31.60559997,29],
[1000,2.98,0.00197241,48],
[1000,23.53,0.00244744,40]])

# 初始化PCA对象:PCA
# 设定主成分为4
pca = PCA(n_components=4)

# 初始设计矩阵：Martix
A = np.array(M)

# 对 A 标准化
for j in range(M.shape[1]):
    # 标准化列向量
    A[:, j] = StandardScaler().fit_transform(A[:, j].reshape(-1, 1)).flatten()

# 主成分分析
pca.fit(A)

# 标准正交特征向量组:Vector_Group
eta_g = pca.get_covariance()
# 贡献度组:Vector
ratio_v = pca.explained_variance_ratio_

# 标准化变量回归方程参数组：Vector
SVRECG = ratio_v.reshape(1, -1) @ eta_g

# 计算原始变量的主成分回归方程
# 列向量算术平均值 mu 组 :Vector
mu_g = np.array([np.average(M[:,j]) for j in range(M.shape[1])])
# 列向量方差 Sigma 组：Vector
sigma_g = np.array([np.std(M[:, j], ddof=1) for j in range(M.shape[1])])
# 原始变量的主成分回归方程参数组：Vector
OVPCARECG = SVRECG @ np.diag(sigma_g)
# 常数项
C = mu_g.reshape(1,-1) @ OVPCARECG.reshape(-1,1)

# 综合指数 组：Vector
INDEX_g = M @ (OVPCARECG.reshape(-1, 1)) + C

# # 综合指数等级 组：Vector
# INDEX_LOG_g = np.log10(INDEX_g)

print('eta_g',eta_g)
print('ratio_v',ratio_v)
print('OVPCARECG',OVPCARECG)
print('C',C)
print('INDEX_g',INDEX_g)