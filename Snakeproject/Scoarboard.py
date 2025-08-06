from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")

class ScoardBoradClass (Turtle):
    def __init__(self):
        super().__init__()
        self.Score=0
        self.color("white")
        self.penup()
        self.goto(x=0,y=260)
        self.UpdateScoarboard()
        self.hideturtle()
    

    def UpdateScoarboard(self):
        self.write(f"Score: {self.Score}",align=ALIGNMENT, font=FONT)

    def Update(self):
        self.Score+=1
        self.clear()
        self.UpdateScoarboard()

    def GameOver(self):
        self.goto(0,0)
        self.write(f"GAME OVER !",align=ALIGNMENT, font=FONT)

        


