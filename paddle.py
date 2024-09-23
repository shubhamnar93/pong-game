from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self, cordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        # self.setheading(90)
        self.penup()
        self.goto(cordinates)
        Screen().update()
    def up(self):
        if self.ycor()< 260:
            self.sety(self.ycor() +20)
    def down(self):
        if self.ycor()> -240:
            self.sety(self.ycor() - 20)
