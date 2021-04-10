from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.gen_scores()

    def gen_scores(self):
        self.goto(-270, 250)
        self.write(f'Level: {self.lvl}', align='left', font=FONT)

    def update_score(self):
        self.clear()
        self.gen_scores()
