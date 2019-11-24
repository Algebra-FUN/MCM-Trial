from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from parse_to_Matrix import to_Matrix as M
import numpy as np


pca = PCA(n_components=5)
U = M()
X = M()
for i in range(len(X[0, :])):
    X[:, i] = StandardScaler().fit_transform(X[:, i].reshape(-1, 1)).flatten()
pca.fit(X)
Y = pca.fit_transform(X)
X_cov = pca.get_covariance()
print(Y)
print('covariance',X_cov)
exp_var_ratio = pca.explained_variance_ratio_
print(exp_var_ratio.reshape(1,-1))
result = exp_var_ratio.reshape(1,-1) @ X_cov
print(result)
const = np.average(U)
sigmas = np.array([np.std(U[:,i],ddof=1) for i in range(len(U[0,:]))])
print('const',const)
print('sigmas',sigmas)
final = result @ np.diag(sigmas)
print('final',final)
