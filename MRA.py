import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np


#data
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['PRICE'] = boston.target
df

y = df['PRICE']
X = df[["INDUS", "RM", "PTRATIO", "LSTAT"]]
#intercept
X_con = sm.add_constant(X)

y#ok
X_con#ok X との違いはconstを設定しているか否か

#model
model = sm.OLS(y, X_con) #OLSは最小二乗法
result = model.fit()
result.summary()#ok

#show histgram
sns.displot(result.resid,bins=30)
plt.show()

#show scatter
y_pred = result.predict(X_con)
#setting
plt.figure(figsize=(5,5), dpi=150)
plt.scatter(y, y_pred, s=15)
plt.xlabel('True', fontsize=20),plt.ylabel('Pred', fontsize=20)
plt.plot([0, 50], [0, 50], c='g')
plt.xlim(0, 52), plt.ylim(0,52)
plt.show()#ok

#LinearRegression ver
#numpy実装と同じデータで読み込み
X = boston.data[:,:-1] #説明変数
y = boston.data[:,-1] #目的変数
X_con = sm.add_constant(X)

model_lr = LinearRegression()
model_lr.fit(X_con, y)
model_lr.coef_ = np.array(model_lr.coef_)
print(model_lr.coef_[1:])#比較
print(model_lr.predict(X_con))#比較
print(model_lr.intercept_)
print(model_lr.score(X_con, y))
