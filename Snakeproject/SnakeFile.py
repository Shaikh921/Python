from turtle import Turtle, Screen
screen=Screen()
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=10
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    
    def __init__(self):
        self.SegmentList=[]
        self.CreateSnake()
        self.Head=self.SegmentList[0]
    def CreateSnake(self):
        for Position in STARTING_POSITION:
            Block=Turtle("square")
            Block.color("white")
            Block.penup()
            Block.goto(Position)
            self.SegmentList.append(Block)
    def Move(self):
            for segNum in range((len(self.SegmentList)-1),0,-1):
                NewX=self.SegmentList[segNum-1].xcor()
                NewY=self.SegmentList[segNum-1].ycor()
                self.SegmentList[segNum].goto(NewX,NewY)
            self.Head.forward(MOVE_DISTANCE)  
    def Up(self):
        if self.Head.heading() !=DOWN:
            self.Head.setheading(UP)


    def Down(self):
         if self.Head.heading() !=UP:
            self.Head.setheading(DOWN)


    def Left(self):
         if self.Head.heading() !=RIGHT:
            self.Head.setheading(LEFT)


    def Right(self):
         if self.Head.heading() !=LEFT:
            self.Head.setheading(RIGHT)

    def Append(self):
        Block=Turtle("square")
        Block.color("white")
        Block.penup()
        self.SegmentList.append(Block)

    def SelfCollision(self):
        isCollision=False
        for Block in range(1,len(self.SegmentList)):
            if(self.Head.distance(self.SegmentList[Block])<10):
                isCollision=True
        return isCollision


