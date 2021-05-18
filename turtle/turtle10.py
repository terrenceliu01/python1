import turtle
import random
import time
screen=turtle.Screen()
trtl=turtle.Turtle()
screen.setup(420,320)
screen.bgpic('./images/grassField.gif')
trtl.shape('turtle')
trtl.color('darkgoldenrod','black')
s=10
trtl.penup()
trtl.setpos(30,30)
for i in range(28):
    s=s+2
    trtl.stamp()
    trtl.forward(s)
    trtl.right(25)
    time.sleep(0.25)      
    #activated with a break of a 1/4th of a second