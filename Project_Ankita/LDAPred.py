# -*- coding: utf-8 -*-
"""
@author: Ankita
"""
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# load training dataset
df=pd.read_csv("sunflower.csv",names=['lat_root', 'tap_root', 'tot_root', 'latRF','tapRF','Treatment'])

# load testing dataset
tst=pd.read_csv("Check.csv", names=['lat_root', 'tap_root', 'tot_root', 'latRF','tapRF','Treatment'])

features = ['lat_root', 'tap_root', 'tot_root','latRF', 'tapRF']

# Separating out the features for training set
x = df.loc[:, features].values

# Separating out the features for testing set
xt= tst.loc[:, features].values

# Separating out the target for training set
z = df.loc[:,['Treatment']].values

# Separating out the target for testing set
zt = tst.loc[:,['Treatment']].values

# Standardizing the features for training set
x = StandardScaler().fit_transform(x)

# Standardizing the features for testing set
xt = StandardScaler().fit_transform(xt)

#Initialize list to store binary predictions for training set
y=[]

#Initialize list to store binary predictions for testing set
yt=[]

# Convert treatment to binary for training set
for k in z:
    if k=='Dry':
        k=0
        y.append(k)
    else:
        k=1
        y.append(k)

# Convert treatment to binary for testing set
for kt in zt:
    if kt=='Dry':
        kt=0
        yt.append(kt)
    else:
        kt=1
        yt.append(kt)
        
# Do PCA to get two best features
pca=PCA(n_components=4)

# Initialize lists to plot prediction score of training data
score=[]

# Initialize lists to plot prediction score of testing data
scoret=[]

# This keeps count of X-axis in our plot
index=[]

# Iterate through x dataset
for i in range(2,len(x)):
    # Fit your data with pca selected features
    temp_x = pca.fit_transform(x[:i,:])
    temp_xt = pca.fit_transform(xt[:i,:])
    clf = LDA()
    # Build your LDA model with fitted data after PCA
    clf.fit(temp_x,y[:i]) 
    # Predict accuracy of model with training data
    pred = clf.predict(temp_x)
    # Predict accuracy of model with testing data
    predt = clf.predict(temp_xt)
    # Record result for training data
    result = accuracy_score(pred,y[:i])
    # Record result for testing data
    resultt = accuracy_score(predt,yt[:i])
    # Append score to list for training data
    score.append(result)
    # Append score to list for testing data
    scoret.append(resultt)
    
# Plot prediction accuracy		
index = [ i for i in range(2,len(x))]

# Training set
plt.figure(1)
plt.ylim(0,1.2)
plt.scatter(index,score, color='purple')
plt.show()

print (score)

#Test Set
plt.figure(2)
plt.ylim(0,1.2)
plt.scatter(index,scoret, color='green')
plt.show()

print (scoret)















	


    

	
    
    
    
    
        




        










