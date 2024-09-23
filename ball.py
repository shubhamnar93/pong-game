from random import random
from turtle import Turtle, Screen
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.sety(random.randint(-200, 200))
        Screen().update()
        self.x_update= 5
        self.y_update= 5
        self.sleep=0.02
    def move(self):
        new_x = self.xcor()+self.x_update
        new_y = self.ycor()+self.y_update
        self.goto(new_x, new_y)
        Screen().update()
        time.sleep(self.sleep)
    def bounce_wall(self):
        self.y_update *= -1
    def bounce_paddle(self):
        self.x_update *= -1
        self.sleep*=0.9
    def restart(self):
        self.sety(random.randint(-200, 200))
        self.setx(0)
        self.x_update *= random.choice([-1, 1])
        self.sleep = 0.02




