import time
import random
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkeypress(player.move_up, 'Up')

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_running = False

    if player.ycor() >= player.finish_line:
        player.starting_position()
        scoreboard.level_up()
        car_manager.level_up()

    car_manager.remove_cars_past_screen()

screen.exitonclick()
