from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()


def setup_screen():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game - Press Space to stop/restart")
    screen.tracer(0)


setup_screen()
snake = Snake()
scoreboard = Scoreboard()

screen.update()
game_is_on = True

def reset():
    global game_is_on
    game_is_on = True
    screen.clear()
    setup_screen()
    scoreboard.reset()
    snake.reset()
    play()


def start_stop():
    global game_is_on
    if game_is_on:
        game_is_on = False
        scoreboard.game_over()
    else:
        reset()


def set_listeners():
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="space", fun=start_stop)


def play():
    set_listeners()
    food = Food()
    global game_is_on
    while game_is_on:
        time.sleep(0.1)
        snake.move()
        screen.update()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_score()
            snake.enlarge()

        # detect collision with wall
        if (not -280 < snake.head.xcor() < 280 or
                not -280 < snake.head.ycor() < 280):
            # game_is_on = False
            # scoreboard.game_over()
            reset()

        # detect collision with self
        # if head collides with any segment, game over
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                # game_is_on = False
                # scoreboard.game_over()
                reset()

play()
screen.exitonclick()
