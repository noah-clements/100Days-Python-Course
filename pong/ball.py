from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        # self.shapesize(20)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.8
        
        
    def bounce_y(self):
        self.y_move *= -1

    def speed_up(self, speed_factor=0.8):
        # self.x_move *= 1.2
        # self.y_move *= 1.2
        self.ball_speed *= speed_factor

    def reset_position(self) -> None:
        self.hideturtle()
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1
        # self.y_move = 10
        # if self.x_move < 1:
        #     self.x_move = 10
        # else:
        #     self.x_move = -10
        self.showturtle()

