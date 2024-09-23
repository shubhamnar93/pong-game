import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from middle_line import Line

line =Line()
score=ScoreBoard()
screen = t.Screen()
screen.setup(width=800, height=600)
screen.title("pong game")
screen.bgcolor("black")
screen.tracer(0)
line.line()

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
screen.listen()
screen.onkeypress(l_paddle.up , "Up")
screen.onkeypress(l_paddle.down , "Down")
screen.onkeypress(r_paddle.up , "w")
screen.onkeypress(r_paddle.down , "s")

b = Ball()

while score.game_on:
    screen.update()
    if score.l_score<10 and score.r_score<10:
        b.move()

    if b.ycor()>=280 or b.ycor()<=-280:
        b.bounce_wall()
    if b.xcor()>=380:
        score.l_scored()
        b.restart()

    if b.xcor()<=-380:
        score.r_scored()
        b.restart()

    if b.distance(l_paddle)<70 and 330 < b.xcor() < 340 or b.distance(r_paddle)<70 and -330 > b.xcor()>-340:
        b.bounce_paddle()

