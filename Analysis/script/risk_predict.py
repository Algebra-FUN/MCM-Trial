import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# 数据集
dataset_x = np.array([2017,2017.5,2018,2018.5,2019,2019.5]).reshape(-1,1)
dataset_y = np.array([[10.64981931]
 ,[10.65029871]
 ,[10.64981931]
 ,[10.64677987]
 ,[10.64502525]
 ,[10.64502525]])

x = np.arange(np.min(dataset_x),np.max(dataset_x),0.1).reshape(-1,1)

linear = linear_model.LinearRegression()
linear.fit(dataset_x,dataset_y)
print('coef',linear.coef_)

plt.plot(dataset_x,dataset_y,'r')
plt.plot(x,linear.predict(x),'b')
plt.show()