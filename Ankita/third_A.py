'''
Libraries
'''
import numpy as np
import matplotlib.pyplot as p

'''
Variable definitions
'''
# Array to walk in
a = np.zeros((200, 200))

#Possible increments of steps
stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]



#Position to stick to initially
a[100,100]=1

i=0
im = p.imshow(a, cmap='inferno')



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
                print startPos   
                a[startPos[0],startPos[1]]=1
                startPos=[100,100]
                print startPos
                im.set_data(a) # set the data
                p.draw() # draw the image
                p.ion()
                p.pause(0.001) # give the computer time to draw
                   
                       
                   
    else:
        # else go 1 step back and choose again
        startPos=startPos-np.array(step)
        
p.ioff()
 # show the array
p.imshow(a,interpolation='bicubic', cmap='inferno')
p.show()

"""
It is different from DLA as it forms a circle which expands with increasing iterations.
"""


