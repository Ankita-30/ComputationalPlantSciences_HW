"""
import libraries
"""
import numpy as np
import matplotlib.pyplot as p
import random
import math as m

j=0
L=[]
while j<20:
    j+=1
    """
    Define your array
    """
    a = np.zeros((200, 200))

    """
    Define start positions of two walks
    """
    startPos1 = [50, 50]
    startPos2 = [75, 75]

    """
    Define your random walks
    """
    stepChoices1 = [[5, 0], [0, -5], [-5, 0], [0, 5]]
    stepChoices2 = [[-5, 0], [0, 5], [5, 0], [0, -5]]

    """
    Put image on a variable
    """
    im = p.imshow(a, interpolation='bicubic', cmap='viridis')

    """
    Turn on interactive plotting
    """
    p.ion()


    """
    Walk 6000 steps
    """
    i = 0



    """
    Define count as no. of times walkers cross
    """
    c = 0
    while i < 500:

        i = i + 1
        

        """
        Randomly choose a step to go
        """
        step1 = np.array(stepChoices1[np.random.randint(0, 4)])
        step2 = np.array(stepChoices2[np.random.randint(0, 4)])

        startPos1 = startPos1 + step1
        startPos2 = startPos2 + step2
        """
        Add the step to the start position
        """

        
        """
        The walker shouldn't go beyond the borders
        """

        if (startPos1[0] >= 0
                and startPos1[1] >= 0
                and startPos1[0] < 200
                and startPos1[1] < 200
                and startPos2[0] >= 0
                and startPos2[1] >= 0
                and startPos2[0] < 200
                and startPos2[1] < 200):
            
            
            a[(startPos1)[0], (startPos1)[1]] = 1

            """ Defnn of walker crossing:
            #Walker 1 emerging from startPos1 is tracing a path (wherever it has moved, the array value at that point is 1).
            #So, walker2 emerging from startPos2 will cross its path when its position is at a point where the array value is already 1.
            """
            
            if a[(startPos2)[0], (startPos2)[1]]==1:
                
               
                c=c+1
              
        else:
        	
            startPos1 = startPos1 - np.array(step1)
            startPos2 = startPos2 - np.array(step2)
    p.ioff()



    #print "They have crossed the following no. of times " + str(c)
    L.append(c)
print "List of walker crossings:"
print L

#Calculate mean of the values in list
M=float(sum(L))/j
print "Mean is " + str(M)

#Calculate variance of the values in list
W=[]
for p in L:
    W.append((p-M)**2)

#Add the elements divided by the total number of elements to calculate the variance
v=sum(W)/float(j)
print "Variance is " + str(v)

#Calculate satndard deviation
d=m.sqrt(v)
print "Standard deviation is " + str(d)

"""
Calculating the average is a useful characteristic of the process as we have variable values each time ranging from 0 to 11. Running it just once will give us an 
inaccurate result hence, average  of 15 such values of walker crossings is a more useful quantity.
"""



