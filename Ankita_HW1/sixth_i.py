'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as p
import math as m

def FD():

    '''
    Variable definitions
    '''
    # Array to walk in
    a = np.zeros((200, 200))
    
    #Possible increments of steps
    stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]
    
    
    
    #Position to stick to initially
    a[100,100]=1
    
    j=0
    
    #Define an empty list of distance values
    L=[]
    
    
    startPos=[100,100]
        
    # Walk as long no taken position is reached
    while a[startPos[0],startPos[1]] == 1:  
        #Randomly choose a step to go
        step=np.array(stepChoices[np.random.randint(0,4)])
        #Add the step to the current position
        startPos=startPos+step
            
           
            
        # If the new position is within the array
        if startPos[0]>=0 and startPos[1]>=0 and startPos[0]<200 and startPos[1]<200:
                 
    
            # If the current position is not taken we want to extend the structure
                
               
            if a[startPos[0],startPos[1]]== 0: # Remember we initialized our drawing array with zeros.
                    # Set the last position as taken aka stick to the structure. 
                    if j<1000:
                        j=j+1
                        a[startPos[0],startPos[1]]=1
                        #Calculate distance from centre of cluster
                        r=((startPos[0]-100)**2) + ((startPos[1]-100)**2)
                        startPos=[100,100]
                        L.append(r)
                           
                       
        else:
            # else go 1 step back and choose again
            startPos=startPos-np.array(step)
    #Add all values in the list
    
    x=sum(L)
    
    
    F=float(x)/j
    
    
    R=m.sqrt((F))
    
    #Calculate fractal dimension which is logarithm of S(R) to the base of R.
    d=m.log(j,R)
    
    
    return d


print FD()