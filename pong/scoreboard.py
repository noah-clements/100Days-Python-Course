from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(200, 250)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def left_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.update_scoreboard()

        
    def reset(self) -> None:
        self.__init__()