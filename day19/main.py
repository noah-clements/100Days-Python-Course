from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", 
                            prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


contestant = 0
contestants = []
for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=-230, y=((contestant * 60) - 160))
    contestants.append(tim)
    contestant += 1

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in contestants:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle was the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Etch-A-Sketch

# def move_forward():
#     tim.forward(10)

# def move_back():
#     tim.back(10)

# def turn_clockwise():
#     tim.right(10)

# def turn_counterclockwise():
#     tim.left(10)

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="d", fun=turn_clockwise)
# screen.onkey(key="a", fun=turn_counterclockwise)
# screen.onkey(key="c", fun=tim.reset)

screen.exitonclick()
