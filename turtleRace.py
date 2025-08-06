from turtle import Turtle,Screen
import turtle
import random
Winner=""
isPlaying=True
listOfTurtle=[]
Color=["blue","red","orange","green","yellow","lightblue"]
listOfY=[0,40,80,-40,-80,-120]
# print(Tinny)
screen=Screen()
screen.setup(width=500,height=600)
screen.bgcolor("black")
screen.title("My Turtle Graphics Window - Turtle Race Game")
i=0
for TurtleType in range(6):
    TurtleType=Turtle()
    TurtleType.shape("turtle")
    TurtleType.penup()
    TurtleType.color(Color[i])
    TurtleType.goto(x=-240,y=listOfY[i])
    listOfTurtle.append(TurtleType)
    i+=1
user_input = turtle.textinput("Title of the Prompt", "Enter your name:")

while isPlaying:
    for TurtleType in listOfTurtle:
        if TurtleType.xcor()>230:
            Winner=TurtleType.pencolor()
            isPlaying=False
            break
            
        TurtleType.forward(random.randint(0,10))
if Winner==user_input:
    print(f"You win and Winner is {Winner}")
else:
    print(f"You lost and Winner is {Winner}")
screen.exitonclick()
