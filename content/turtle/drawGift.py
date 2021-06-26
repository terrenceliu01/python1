from turtle import *
import time
from random import *

class DrawGift:
    def __init__(self):
        self.winers = set()
        with open("./turtle/names.out") as win:
            line = win.readline()
            if len(line)>=0:
                l = line.split(',')
                self.winers.add(l[0])

        self.screen=Screen()
        self.image = Turtle()
        self.cow = './turtle/holiday38_2.gif'
        self.screen.addshape(self.cow)
        self.image.shape(self.cow)
        self.trtl=Turtle()
        title("华夏中文学校，家庭教育分享座谈会，正在抽奖...")
        self.screen.setup(1125,842)
        self.screen.bgcolor('red')
        self.trtl.penup()
        self.trtl.setpos(-300,260) #80
        self.trtl.pendown()
        self.trtl.pencolor('#E83386') #'#770729' '#E83386'
        self.trtl.hideturtle()
        self.names = []
        with open("./turtle/names.txt") as f:
            for line in f:
                self.names.append(line)
        self.size = len(self.names)
        print(self.size)
        self.flag = True
        self.index = 0
        self.output = open("./turtle/names.out", 'a')

    def stop(self):
        self.flag = False
        self.index = randint(0, self.size)
        while self.index in self.winers:
            self.index = randint(0, self.size)
        self.trtl.clear()
        # print(self.index)
        self.display()
        self.output.write(f"{self.index}, {self.names[self.index]}")

    def draw(self):
        self.trtl.clear()
        if self.flag:
            self.display()
            time.sleep(0.1)
        self.index += 1
        if(self.index>=self.size):
            self.index = 0
        if(self.flag):
            ontimer(self.draw, 20) 

    def display(self):
        self.trtl.clear()
        self.trtl.write(self.names[self.index],font=("Arial", 48, "bold"))

test = DrawGift()
onkey(test.stop, "space")
listen()


test.draw()

mainloop()