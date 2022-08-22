from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
        
    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
        
    def reached_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
        
    def next_level(self):
        self.goto(STARTING_POSITION)
