
import skimage.morphology as morph
import matplotlib.pyplot as plt
import matplotlib.image as mplimg
import numpy as np


#Read your image
Img=plt.imread('Coral2.png')

#Create an array with all zeros to store the image in its binary form
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

#Show skeleton
plt.imshow(a)

#Save Image
mplimg.imsave('skeleton.png',np.uint8(a))

#Initialize counter
c=0

#Count all non-zero pixels
#Traverse through the image row by row to count non-zero pixels
for i, row in enumerate(a):
    for j,pixel in enumerate(row):
        if pixel==1:
            c=c+1

#Print the total count of non-zero pixels
print(c)  
