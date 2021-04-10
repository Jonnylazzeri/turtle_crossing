import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            player.game_over()
            game_is_on = False

    if player.ycor() > 270:
        player.reset_player()
        scoreboard.lvl += 1
        scoreboard.update_score()
        car_manager.increase_difficulty()

screen.exitonclick()