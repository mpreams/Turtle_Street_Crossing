import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(screen.bye, "Escape")
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_car()
    cars_manager.move()
    scoreboard.post()

    if player.again():
        cars_manager.faster()
        scoreboard.level_up()

    for car in cars_manager.cars:
        if player.distance(car) < 21.777:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()

