from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        RandomX=random.randint(-270,270)
        RandomY=random.randint(-270,270)
        self.goto(RandomX,RandomY)
        
    def Refresh(self):
        RandomX=random.randint(-280,280)
        RandomY=random.randint(-280,280)
        self.goto(RandomX,RandomY)
