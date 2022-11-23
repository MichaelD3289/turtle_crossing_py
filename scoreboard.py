from turtle import Turtle

LEVEL_POSITION = (-215, 260)
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.color('black')
        self.hideturtle()
        self.score = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align='center', font=FONT)

    def level_up(self):
        self.score += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=FONT)