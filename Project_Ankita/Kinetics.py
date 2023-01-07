from visual import *

#Create our object
ball = sphere(pos=(0,0.5,0), color=color.red,radius=0.175)
ballv = vector(0,-7,0)

t=0
dt = 0.01
g=-32

Fgrav=vector(0,g*dt,0)

#loop puts it in motion
while True:
    rate(5)
    ballv = ballv + Fgrav
    ball.pos = ball.pos + ballv*dt
    
    t+=dt
