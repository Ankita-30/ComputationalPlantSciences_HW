'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as p
import random as r

'''
Variable definitions
'''
# Array to walk in
a = np.zeros((200, 200))

#Possible increments of steps
stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]

#Define probability function to check if walk sticks to structure

def probability(t):
    prob=r.random()
    if prob<t:
        x=True
    else:
        x=False
    return x

#Position to stick to initially
a[100,100]=1
startPos=[]
i=0
im = p.imshow(a, cmap='inferno')

p.ion()
#We want 1000 walker particles to stick to the structure
while i<4000:
    i+=1
    print "Walker running: "+str(i) # Output on command line. Helpful for debugging to see if the loop is running
    
    #Select the starting position of the x-ax
    startX=np.random.randint(0,200)
    startAx=np.random.randint(0,4)
    #Set the starting position from where the random walker starts walking
    if startAx==0: startPos=np.array([0,startX])
    elif startAx==1: startPos=np.array([199,startX])
    elif startAx==2: startPos=np.array([startX,0])
    elif startAx==3: startPos=np.array([startX,199])
    
    # Walk as long no taken position is reached
    while a[startPos[0],startPos[1]] == 0:
        #Randomly choose a step to go
        step=np.array(stepChoices[np.random.randint(0,4)])
        #Add the step to the current position
        startPos=startPos+step
        
        # If the new position is within the array
        if startPos[0]>=0 and startPos[1]>=0 and startPos[0]<200 and startPos[1]<200:
            # If the current position is already taken we want to extend the structure
            if a[startPos[0],startPos[1]] > 0: # Remember we initialized our drawing array with zeros.
                    if probability(0.5)==True:
                        # Set the last position as taken aka stick to the structure. Here we set the value in the array to the distance from the center
                        
                        a[(startPos-np.array(step))[0],(startPos-np.array(step))[1]]=np.linalg.norm(np.array([(startPos-np.array(step))[0],(startPos-np.array(step))[1]])-np.array([100,100]),2)
                        # refresh the image
                        im.set_data(a) # set the data
                        p.draw() # draw the image
                        p.pause(0.001) # give the computer time to draw
        else:
            # else go 1 step back and choose again
            startPos=startPos-np.array(step)
        
p.ioff()
# make a figure of the size of the array
p.figure(2)
# show the array
p.imshow(a,interpolation='bicubic', cmap='inferno')
p.show()

"""
We have implemented the probability function for three values of threshold(t) - 0.2,0.5 and for the same no.of iterations i.e. i = 850 and we get three different figures with
a pattern. Greater probability gives extended sructure with more walks.
"""