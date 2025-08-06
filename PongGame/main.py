import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

myPlayer=Player()

screen.listen()
screen.onkey(myPlayer.Goup,"Up")
screen.onkey(Player.Godown,"Down")

carManager=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.createCar()
    carManager.moveCars()

    for Car in carManager.allCars:
       if Car.distance(myPlayer) < 20:
                game_is_on=False
                
    if myPlayer.isAtFinish():
       myPlayer.gotoStatring()
       carManager.increaseSpeed()

screen.exitonclick()
