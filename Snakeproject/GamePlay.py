from turtle import Turtle,Screen
import time
from SnakeFile import Snake
from food import Food
from Scoarboard import ScoardBoradClass

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

Mysnake=Snake()
Myfood=Food()
ScoarBoard= ScoardBoradClass()

screen.listen()
screen.onkey(Mysnake.Up,"Up")
screen.onkey(Mysnake.Down,"Down")
screen.onkey(Mysnake.Left,"Left")
screen.onkey(Mysnake.Right,"Right")
Score=0
GameOn=True
while GameOn:
    screen.update()
    time.sleep(.1)
    Mysnake.Move()
    if Mysnake.Head.distance(Myfood)<20:
        Myfood.Refresh()
        Mysnake.Append()
        ScoarBoard.Update()
    if Mysnake.Head.xcor()>295 or Mysnake.Head.xcor()<-295 or Mysnake.Head.ycor()>295 or Mysnake.Head.ycor()<-295 or Mysnake.SelfCollision():
        GameOn=False
        ScoarBoard.GameOver()
    

    # Nokia 3310

    # if Mysnake.Head.xcor()>285 :
    #     Ycor=Mysnake.Head.ycor()
    #     Mysnake.Head.goto(-285,Ycor)
    # if Mysnake.Head.xcor()<-285 :
    #     Ycor=Mysnake.Head.ycor()
    #     Mysnake.Head.goto(285,Ycor)

    # if Mysnake.Head.ycor()>285 :
    #     Xcor=Mysnake.Head.xcor()
    #     Mysnake.Head.goto(Xcor,-285)
    # if Mysnake.Head.ycor()<-285 :
    #     Xcor=Mysnake.Head.ycor()
    #     Mysnake.Head.goto(Xcor,285)
    # if Mysnake.SelfCollision():
    #     GameOn=False
    #     ScoarBoard.GameOver()

screen.exitonclick()