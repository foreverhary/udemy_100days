import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manger = CarManager()
screen.listen()
screen.onkeypress(player.go_up, 'Up')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.create_cars()
    car_manger.move_cars()


screen.exitonclick()