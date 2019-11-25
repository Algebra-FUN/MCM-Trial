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

# 综合指数等级 组：Vector
INDEX_LOG_g = np.log10(INDEX_g)

with open('./Analysis/storage/INDEX-list.txt', 'w') as f:
    for item in INDEX_g:
        f.write('{}\n'.format(str(item[0])))

with open('./Analysis/storage/INDEX_LOG-list.txt', 'w') as f:
    for item in INDEX_LOG_g:
        f.write('{}\n'.format(str(item[0])))

print(INDEX_LOG_g)

# huazhu = '0,48,2,256.5,21;0,48,2.45,256.5,35;0,48,2,256.5,58;0,48,2.4,256.5,97;0,48,2.5,256.5,137;0,48,2.5,256.5,160'
# huazhu_M = np.array(list(
#     [list([float(txt) for txt in row.split(',')]) for row in huazhu.split(';')]))

# huazhu_M = np.array([[0,13,10.5,39.625,0],[0,13,11,39.625,0],[0,13,10.5,39.625,0],[0,13,7.33,39.625,0],[0,13,5.5,39.625,0],[0,13,5.5,39.625,0]])
# INDEX_L = huazhu_M.reshape(-1, M.shape[1]) @ (OVPCARECG.reshape(-1, 1)) + C
# RELATE_INDEX_L = INDEX_L / 1000
# print('INDEX_L',INDEX_L)
# print('RELATE_INDEX_L',RELATE_INDEX_L)