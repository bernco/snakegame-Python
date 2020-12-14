from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.start_score = 0
        self.hideturtle()
        self.pu()
        self.setpos(x=0, y=280)
        self.score_keeper()

    def score_keeper(self):
        self.clear()
        self.write(f"Score = {self.start_score}", False, align=ALIGNMENT, font=FONT)
        self.start_score = self.start_score + 1

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
