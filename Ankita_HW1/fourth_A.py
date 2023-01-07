"""
import libraries
"""
import numpy as np
import matplotlib.pyplot as p
import random
import math as m

j=0
L=[]
while j<10:
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
    while i < 6000:

        i = i + 1
        

        """
        Randomly choose a step to go
        """
        step1 = np.array(stepChoices1[np.random.randint(0, 4)])
        step2 = np.array(stepChoices2[np.random.randint(0, 4)])

        """
        Add the step to the start position
        """

        startPos1 = startPos1 + step1
        startPos2 = startPos2 + step2
        """
        They will cross each other when they are together at the same co-ordinate hence, startPos1=startPos2
        """
        if startPos1[0]==startPos2[0] and startPos1[1]==startPos2[1]:
            c=c+1
            #print "They meet here hence, increasing the count:" + str(c)
            #print startPos1
            #print startPos2
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
            
            """
            We have hashed this out as it slows the program down.
            Remove the hashes to see the walkers moving live
            """

            #a[(startPos1)[0], (startPos1)[1]] = 1
            #a[(startPos2)[0], (startPos2)[1]] = 1

            # """
            # Set the data
            # """
            #im.set_data(a)

            # """
            # Draw the image
            # """
            #p.draw()

            # """
            # Pause for computer to draw
            # """
            #p.pause(0.001)
            # """
            # Show the image
            # """

            #p.imshow(a, interpolation='bicubic', cmap='viridis')
            #a[(startPos1)[0], (startPos1)[1]] = 0
            #a[(startPos2)[0], (startPos2)[1]] = 0
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



