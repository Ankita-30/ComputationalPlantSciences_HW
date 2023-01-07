# -*- coding: utf-8 -*-
"""
@author: Ankita
"""
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#load dataset
df=pd.read_csv("sunflower.csv",names=['lat_root', 'tap_root', 'tot_root', 'latRF','tapRF','Treatment'])

features = ['lat_root', 'tap_root', 'tot_root','latRF', 'tapRF']

# Separating out the features
x = df.loc[:, features].values

# Separating out the target
y = df.loc[:,['Treatment']].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

# Get two best features
pca=PCA(n_components=2)

# Fit your data with pca obtained features
principalComponents = pca.fit_transform(x)

# print principal components
print (principalComponents)

# Define your dataframe with two components
principalDF=pd.DataFrame(data=principalComponents, columns=['principal component 1','principal component 2'])

# Print your initial dataframe
print (principalDF)

# Concatenating data along a single axis
finalDf = pd.concat([principalDF, df[['Treatment']]], axis = 1)

# Print your final dataframe
print (finalDf)

# Plot your 2D projection for visualization
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
Treatments = ['Wet', 'Dry']
colors = ['r', 'g']
for Treatment, color in zip(Treatments,colors):
    indicesToKeep = finalDf['Treatment'] == Treatment
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
ax.legend(Treatments)
ax.grid()








