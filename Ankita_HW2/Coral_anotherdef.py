# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:27:24 2018

@author: Ankita
"""
"""
I have used python 3.6 as I worked on my lab computer which has python 3. Also, cv2 doesnt run on python 2.7.
First, I skeletonize binary image of corals and count total no. of non zero pixels (c) using the code named 'skeleton.py'.
So, I am left with a number of not-connected lines where each line is the skeleton of a coral unit.
I have performed component labelling in cv2 which will label every individual non-connected skeleton/coral unit by a separate colour.
I have defined average length as total no. of pixels in all coral unit skeletons divided by total no. of coral units/skeletons.

"""

import skimage.morphology as morph
import matplotlib.pyplot as plt
import matplotlib.image as mplimg
import numpy as np
import cv2

#Read image in cv2
a=cv2.imread('skeleton.png')

#Make skeleton black and white
img_threshold = a.copy()
for i in range(img_threshold.shape[0]):
	for j in range(img_threshold.shape[1]):
		if img_threshold[i][j]<170:
			img_threshold[i][j]=0
		else:
			img_threshold[i][j]=255


#Component labelling for black and white skeleton (No. of components give us the number of skeleton units)
img_copy = img_threshold.copy()

#img_lbl = cv2.threshold(img_copy, 0, 255, cv2.THRESH_BINARY)[1]  #ensure binary
ret, labels = cv2.connectedComponents(img_copy)

#Map component labels to hue val
label_hue = np.uint8(120 * labels / np.max(labels))
blank_ch = 255 * np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

#Cvt to BGR for display
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

#Set bg label to black
labeled_img[label_hue == 0] = 0

print(ret) #This line prints the number of components

#Save component labelled image
cv2.imwrite('Component_labelled.png',labeled_img)

#number of components = number of skeletons
#c has been obtained from 'skeleton.py'

#Calculate average length which is total no. of non-zero pixels divided by the number of components/skeleton units
avg_length = c/float(ret)







