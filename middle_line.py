from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=300)
        self.pendown()
        self.setheading(270)
        self.hideturtle()
    def line(self):
        while self.ycor()>-300:
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()