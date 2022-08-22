from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')
SCORE_POSITION = (0, 280)


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.color("white")
        self.score = 0
        try:
            with open("data.txt") as score_file:
                self.high_score = int(score_file.read())
        except:
            print("Error reading score file.")
            self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   |   High Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)
        
    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score_file:
                score_file.write(str(self.high_score))
 

    def game_over(self):
        self.save_high_score()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self) -> None:
        self.save_high_score()
        self.score = 0
        self.goto(SCORE_POSITION)
        self.update_scoreboard()
