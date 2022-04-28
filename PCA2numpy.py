import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt



#data of wine
url = "https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/wine.txt"
urllib.request.urlretrieve(url, 'wine.txt') 

#data ,tabcut, index name
X = pd.read_csv('wine.txt', sep="\t", index_col=0)
X.head() #ok

n = len(X)

class PCA:
    def __init__(self):
        pass
    def fit_transform_eig(self, X):
        X = (X - X.mean(axis=0))/X.std(axis=0) #標準化
        #cov = np.cov(X.T)   #転置行列の共分散行列を求める
        cov = (X - X.mean(axis=0)).T @ (X - X.mean(axis=0)) 
        cov = cov / n
        l, v = np.linalg.eig(cov) #固有値,固有ベクトルを求める
        self.explained_variance_ = l  #固有値(主成分の分散)
        #寄与率,分散比の定義
        self.explained_variance_ratio_ =  self.explained_variance_ / self.explained_variance_.sum()
        self.components_ = v #共分散行列の固有ベクトル
        return X.dot(v)

pca = PCA()
X_new = pca.fit_transform_eig(X)
print (pca.explained_variance_) 
print (pca.explained_variance_ratio_) 
print (pca.components_) 

X_new.head()
X_new = pd.DataFrame(X_new)

X_new.iloc[:, 0]

#plot data 1 & 2
plt.figure(figsize=(6, 6))
plt.scatter(X_new.iloc[:,0], X_new.iloc[:,1], alpha=0.8, c=list(X.iloc[:, 0]))
plt.grid(), plt.xlabel("PC1"), plt.ylabel("PC2")
plt.show()#ok

