from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=("Courier", 24, "bold"))
