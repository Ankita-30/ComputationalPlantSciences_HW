# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:22:54 2018

@author: Ankita
"""

import sys
import skimage.morphology as morph
import matplotlib.pyplot as plt
import matplotlib.image as mplimg
import numpy as np
from sklearn.metrics import accuracy_score

sys.setrecursionlimit(3000)

Img=plt.imread('Coral2.png')

a=np.zeros((Img.shape[0], Img.shape[1]))

#Make it binary by keeping the threshold as 0.5 so, <0.5 is black
for jdx, row in enumerate(Img):
    for idx,pixel in enumerate(row):
            if pixel[0] < 0.5:
                a[jdx,idx] = 0
            else:
                a[jdx,idx] = 1


#Skeletonize Image
a=morph.skeletonize(a)

#Make the array support integer datatype
a=np.array(a,dtype='int')

#Save Image
mplimg.imsave('skeleton.png',np.uint8(a))

#Initialize list to store all non-zero pixels
skeleton=[]

#List all non-zero pixels
for m,row in enumerate(a):
    for n,pixel in enumerate(row):
        if pixel==1:
            t=(m,n)
            skeleton.append(t) 

#Initialize a list to store all pixels next to the end-point of a skeleton unit
skwithin=[]

#Initialize a list to store the length of every skeleton unit
length=[]

#Initialize counter
c=0

#Iterate through all non-zero pixels earlier extracted and stored in skeleton
for (i,j) in skeleton:
    
    #List eight pixels surrounding a non-zero pixel
    neigh_pix=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    #Iterate through each of the pixels in the eight-connected neighbourhood
    for x in neigh_pix:
        #Increase counter if it is a non-zero pixel
        if a[x]==1:
            c=c+1
            if c==1:
                y=x #We need to append x to skwithin if it is next to an end-point
        #Else do nothing
        else:
            pass
    #Check the counter/neighborhood for how many non-zero pixels surround every skeleton pixel in the image
    if c==0:
        length.append(1) #It is an isolated pixel so, append its length=1 to the list
    elif c==1: #It is an end-point of a skeleton
        a[i,j]=2 #Make all end-points have a pixel value of 2
        skwithin.append(y)#Append x to skwithin
    else:
        pass
    c=0   

#Def function which checks a list and returns the element which doesn't have a pixel value of 2
def list(v):
    for o in v:
        if a[o]!=2:
            o=(i,j)
    return (i,j)
        
#Def function which checks neighborhood of a pixel and returns number of non-zero pixels and the pixel which will be checked next
def check(i,j,l):
    #Define a global variable for counting no. of non-zero pixels
    b=0
    #Define an empty list
    v=[]
    #Make pixel value at that co-ordinate 2
    a[i,j]=2 
    #Define an eight-connected neighborhood
    neigh_pix=[(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    #Iterate through every pixel in the neighborhood
    for h in neigh_pix:
        #Check if the pixel is non-zero
        if a[h]!=0:
            b=b+1
            v.append(h)
        else: #Do nothing
            pass
   
    if b==2:
        l=l+1
        list(v)
        if (i,j) is None:
            pass
        else:
            check(i,j,l)
    if b==1:
        return l
    
#Calculate length of each skeleton given we know its pixel next to the end-point
for (i,j) in skwithin:
    #Define l which calculates length of each skeleton. 
    #We are not counting the end-points so we initialize it to 2 for both end-points
    l=2
    check(i,j,l)
    length.append(l)

print (length)


    
    
   

   


        




























#7345684035477-IMP!!! -> booking id for flight





            

            
   
        