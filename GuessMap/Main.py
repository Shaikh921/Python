import turtle
import os
import pandas

screen = turtle.Screen()
screen.title("Indian Map Game")

# Build path dynamically
image = os.path.join(os.path.dirname(__file__), "indianMap.gif")

# Confirm image path is correct
print("Loading image from:", image)

screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

filePath = os.path.join(os.path.dirname(__file__), "S.csv")
Data = pandas.read_csv(filePath)
State = Data.state.to_list()
GameIsOn = True
RemaningChances = 10
CorrectGuess = 0


while GameIsOn:

    answer_state = screen.textinput(title="Guess the state", prompt=" What is the Name of another State !")

    if RemaningChances == 0 or CorrectGuess == 28:
        GameIsOn = False
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        if CorrectGuess == 28:
          t.write("You won !", align="center", font=("Arial", 20, "bold")) 
        else:
          t.write("Game Over !", align="center", font=("Arial", 20, "bold"))


    if answer_state not in State:
      RemaningChances-=1


    if answer_state in State:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = Data[Data.state == answer_state]
        Xcor = int(stateData.x)
        Ycor = int(stateData.y)
        t.goto(Xcor, Ycor)
        t.write(answer_state)



screen.exitonclick()