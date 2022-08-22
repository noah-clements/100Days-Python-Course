from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, side="left") -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=.8)
        self.speed("fastest")
        self.penup()
        self.side = side
        if self.side in ('l', 'left'):
            self.goto((-370, 0))
        else:
            self.goto((370, 0))
        
    def up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 260:
            self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -260:
            self.goto(self.xcor(), new_y)
