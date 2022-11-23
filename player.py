from turtle import Turtle

STARTING_POSITION = (10, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.starting_position()
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def move_up(self):
        current_position = self.ycor()
        self.goto((10, current_position + MOVE_DISTANCE))

    def starting_position(self):
        self.goto(STARTING_POSITION)