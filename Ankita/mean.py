import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#Open the file and read each line into an array
with open("output_i") as code:
    DLA8 = []
    for line in code:
    	x=line.rstrip('\n')
    	y=float(x)
        DLA8.append(y)



#Calculate the mean

s=sum(DLA8)
m=float(s)/1000
print "The mean is " + str(m)

#Calculate the standard deviation

#Generate another list with elements of K minus the mean squared
W=[]
for p in DLA8:
    W.append((p-m)**2)

#Add the elements divided by the total number of elements to calculate the variance
v=sum(W)/1000
print "The standard deviation is " + str(v)





