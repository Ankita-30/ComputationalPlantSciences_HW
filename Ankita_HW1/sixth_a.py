'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as plt
import math as m

#Define a function to calculate the fractal dimension

def FD():
    '''
    Variable definitions
    '''
    # Array to walk in initialized as 'a' with only zeros
    a = np.zeros((200, 200))

    #Possible increments of steps
    stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]

    #Position to stick to initially and mark it as taken. 
    a[100,100]=1  

    # For now we start in the middle
    startPos=np.array([100,100])

    #Define list of distance values
    L=[]
    
    '''
    Program Execution
    '''
    # turn on interactive plotting
    plt.ion()
    #We walk 1000 steps
    i=0 #step variable
    while i<1000: # while the variable i is smaller that 1000, we increase its value
        i+=1
        #Randomly choose a step to go
        step=np.array(stepChoices[np.random.randint(0,4)])
        #Add the step to the current position
        startPos=startPos+step
        # If the new position is within the array
        if startPos[0]>=0 and startPos[1]>=0 and startPos[0]<200 and startPos[1]<200:
            # Set the last position as taken aka stick to the structure  
            a[(startPos-step)[0],(startPos-step)[1]]=1
            #calculate distance from center
            #r=np.linalg.norm(np.array([(startPos)[0],(startPos)[1]])-np.array([100,100]),2)
            r=((startPos[0]-100)**2) + ((startPos[1]-100)**2)
            #Add the distance to your list
            L.append(r)
            
             
        else:
            # else go 1 step back and choose again
            startPos=startPos-step
    

    #Add all values in the list
    x=sum(L)
    #print summation of distance from the centre (ri)
    #print "Sum of all distance values from the centre is " + str(x)
    #print division of the sum by the size of the cluster. Size of the cluster is total no. of pixels/walks according to my program (I am not sure if it is right).
    F=float(x)/i
    #print "On dividing the sum by size of cluster, we get " + str(F)
    R=m.sqrt((F))
    #print "R = " + str(R)
    #Calculate fractal dimension which is logarithm of S(R) to the base of R.
    d=m.log(i,10)/m.log(R,10)
    #print "Fractal dimension is " + str(d)
    return d
print FD()







    







