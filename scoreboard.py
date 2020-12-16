from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.start_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.pu()
        self.setpos(x=0, y=280)
        self.score_keeper()

    # writes the score to the screen
    def score_keeper(self):
        self.clear()
        self.write(f"Score = {self.start_score}. High score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.start_score = self.start_score + 1

    # Looks for the highest score and updates it while resetting the current score to zero
    def reset_score(self):
        if self.start_score > self.high_score:
            self.high_score = self.start_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.start_score = 0
        self.clear()
        self.write(f"Score = {self.start_score}. High score = {self.high_score}", False, align=ALIGNMENT, font=FONT)

