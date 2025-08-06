from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def Goup(self):
        self.forward(MOVE_DISTANCE)


    def Godown(self):
        self.backward(MOVE_DISTANCE)
    

    def isAtFinish(self):
        if self.ycor()>260:
            return True
        else:
            return False

    def gotoStatring(self):
        self.goto(STARTING_POSITION)



   
