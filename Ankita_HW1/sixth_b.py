'''
Libraries
'''
import numpy as np
#import matplotlib.pyplot as plt
import math as m

#Define a fucntion FD to calculate the fractal dimension
def FD():
    '''
    Variable definitions
    '''
    # Array to walk in
    a = np.zeros((200, 200))

    #Possible increments of steps
    stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]

    #Position to stick to initially
    a[199,100]=1
    startPos=[]
    i=0
    
    #Define a list of distance values
    L=[]
    
    #We want 4000 walker particles to stick to the structure
    while i<1000:
        i+=1
        
        #Select the starting position of the x-ax
        startX=np.random.randint(0,200)
        
        #Set the starting position from where the random walker starts walking
        startPos=np.array([0,startX])
        
        
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
                    # Set the last position as taken aka stick to the structure. Here we set the value in the array to the distance from the center
                    a[(startPos-np.array(step))[0],(startPos-np.array(step))[1]]=np.linalg.norm(np.array([(startPos-np.array(step))[0],(startPos-np.array(step))[1]])-np.array([100,100]),2)
                    #Calculate the distance from (199,100)
                    
                    r=((startPos[0]-199)**2) + ((startPos[1]-100)**2)
                    #print "r is " + str(r)
                    
                    #Add the value to list
                    L.append(r)
                    
            else:
                startPos=startPos-np.array(step)
                    
		               
    #Add all values in the list
    
    x=sum(L)
    
    F=float(x)/i
    
    R=m.sqrt((F))
    print "R = " + str(R)
    #Calculate fractal dimension which is logarithm of S(R) to the base of R.
    d=m.log(i,R)
    
    
    return d


print FD()

