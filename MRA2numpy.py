from array import array
import numpy as np
import pandas as pd


#boston data
from sklearn.datasets import load_boston

boston = load_boston()
X = boston.data[:,:-1] #説明変数
y = boston.data[:,-1] #目的変数

#model最小二乗法を用いる
class MRA():
    def __init__(self):
        self.coef_ = None 

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1) #X = 配列, 0 = 挿入する配列の位置, 1 = 挿入する配列, 軸
        self.coef_ = np.linalg.inv(X.T @ X) @ X.T @ y #行列の定義


    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)
        return X @ self.coef_

lr = MRA()
lr.fit(X, y)
print(lr.predict(X))#比較
lr.coef_ = np.array(lr.coef_)
print(lr.coef_[1:])#比較

