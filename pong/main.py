from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

MAX_SCORE = 5

screen = Screen()


def create_net():
    net = Turtle(shape="square")
    net.color("white")
    net.penup()
    net.pensize(5)
    net.hideturtle()
    net.goto(0, -280)
    net.setheading(90)
    for _ in range(30):
        net.pendown()
        net.forward(20)
        net.penup()
        net.forward(30)
    
    
def setup_screen():
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)
    create_net()



setup_screen()
l_paddle = Paddle("left")
r_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # paddle sends ball back. going to control speeding up from here.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350 or 
        ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        ball.bounce_x()
        ball.speed_up(speed_factor=0.75)

    if ball.xcor() > 375:
        scoreboard.left_point()
        ball.reset_position()
    elif ball.xcor() < -370:
        scoreboard.right_point()
        ball.reset_position()

    if scoreboard.l_score == MAX_SCORE or scoreboard.r_score == MAX_SCORE:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()
