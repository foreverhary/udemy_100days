from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f"score : {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
