import turtle
from turtle import Turtle, Screen


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_on=True
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_change()
    def score_change(self):
        self.clear()
        self.goto(x=-100, y=220)
        self.write(f"{self.l_score}", align='center', font=('courier', 50, 'bold'))
        self.goto(x=100, y=220)
        self.write(f"{self.r_score}", align='center', font=('courier', 50, 'bold'))

    def l_scored(self):
        self.l_score+=1
        if self.l_score < 10:
            self.score_change()
        else:
            self.score_change()
            self.goto(x=-175, y= 150)
            self.write("win", align='center', font=('courier', 50, 'bold'))
            self.goto(x=-175, y= 90)
            self.write("(r) play again", align='center', font=('courier', 30, 'bold'))
            self.goto(x=-175, y= 50)
            self.write("(q) quit game", align='center', font=('courier', 30, 'bold'))

            Screen().listen()
            Screen().onkey(self.restart, "r")
            Screen().onkey(self.out, "q")

    def r_scored(self):
        self.r_score+=1
        if self.r_score < 10:
            self.score_change()
        else:
            self.score_change()
            self.goto(x=175, y=150)
            self.write("win", align='center', font=('courier', 50, 'bold'))
            self.goto(x=-175, y= 90)
            self.write("(r) play again", align='center', font=('courier', 30, 'bold'))
            self.goto(x=-175, y= 50)
            self.write("(q) quit game", align='center', font=('courier', 50, 'bold'))

            Screen().listen()
            Screen().onkey(self.restart, "r")
            Screen().onkey(self.out, "q")

    def restart(self):
        self.l_score=0
        self.r_score=0
        self.score_change()
    def out(self):
        self.game_on=False
        turtle.bye()
