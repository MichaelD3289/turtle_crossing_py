import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

game_is_running = True
while game_is_running:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()