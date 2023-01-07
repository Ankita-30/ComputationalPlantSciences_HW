from visual import *
from math import sin, cos

initialHeight = 6.5
initialVelocity = 24
Angle = 45

#Set up display window
scene1 = display(title = "Projectile",x=0,y=0, width=800,height=600,range=10,background=color.white,
                 center=(10,initialHeight,0))

#Create our object
table=box(pos=(-1,initialHeight - 1,0),size=(5,1,4))
ball = sphere(pos=(0,initialHeight,0),radius=0.75,
               color=color.green,make_trail=true)



floor=box(pos=(0,0,0),size=(100,0.25,10))

t=0
dt=0.01
g=-32

Fgrav=vector(0,g*dt,0)+vector(0,-0.025,0)

ballv= vector(initialVelocity*cos(Angle*pi/180),
              initialVelocity*sin(Angle*pi/180),0)

#loop puts it in motion
while True:
    rate(40)
    ballv = ballv + Fgrav
    ball.pos = ball.pos + ballv*dt

   
    if ball.y<0:
        print "ball1.pos = ",ball.pos,"t= ",t
       
        break
    
    t+=dt
        
    
              
