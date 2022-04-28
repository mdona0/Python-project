import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import PCA
from pandas import plotting
import matplotlib.ticker as ticker


#data of wine
url = "https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/wine.txt"
urllib.request.urlretrieve(url, 'wine.txt') 


#比較用
X = pd.read_csv('wine.txt', sep="\t", index_col=0) 

pca = PCA()
X_ = (X - X.mean(axis=0))/X.std(axis=0) 
X_new = pca.fit_transform(X_)
print (pca.explained_variance_)
print (pca.explained_variance_ratio_) 
print (pca.components_)


#data ,tabcut, index name
df = pd.read_csv('wine.txt', sep="\t", index_col=0)
df.head() #ok

plotting.scatter_matrix(df.iloc[:, 1:], figsize=(8, 8), c=list(df.iloc[:, 0]), alpha=0.5)
#c is color, alpha is clear degree
plt.show()# ok

#normalize matrix & define formula
dfs = df.iloc[:, 1:].apply(lambda x: (x-x.mean())/x.std(), axis=0)
dfs.head()#ok

#PCA
pca = PCA()
pca.fit(dfs)
#tranform to PCA
feature = pca.transform(dfs)
#PCA point, ok
pd.DataFrame(feature, columns=["PC{}".format(x + 1) for x in range(len(dfs.columns))])
#plot data 1 & 2
plt.figure(figsize=(6, 6))
plt.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(df.iloc[:, 0]))
plt.grid(), plt.xlabel("PC1"), plt.ylabel("PC2")
plt.show()#ok

#malti data
plotting.scatter_matrix(pd.DataFrame(feature, columns=["PC{}".format(x + 1) for x in range(len(dfs.columns))]),figsize=(8 ,8), c=list(df.iloc[:, 0]), alpha=0.5)
plt.show()#ok

#Contribution rate
pd.DataFrame(pca.explained_variance_ratio_, index=["PC{}".format(x + 1) for x in range(len(dfs.columns))])

#show contribution rate
plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
plt.plot([0] + list(np.cumsum(pca.explained_variance_ratio_)), "-o")
plt.show()#ok

