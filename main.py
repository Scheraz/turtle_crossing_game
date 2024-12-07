import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

score.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.reset_position()
            score.clear()
            score.game_over()
            game_is_on = False

    if player.ycor() > 250:
        score.update_points()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()