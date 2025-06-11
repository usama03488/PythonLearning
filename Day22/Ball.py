from turtle import Turtle


class ball(Turtle):
   IsBounced = False
   IsCollided=False
   def __init__(self,position):
       super().__init__()
       self.shape("circle")
       self.color("white")
       self.penup()
       self.shapesize(2, 2)
       self.goto(position)
       self.x_move=10
       self.y_move=10


   def CheckPosition(self):
       if(self.ycor() ==250 or self.ycor()== -250):
           self.Bounce_Yaxis()
       if(self.xcor() >350 or self.xcor() < -350):
           #self.Bounce_Xaxis()
           self.IsCollided=True
           print("Game Over")
   def Distance(self,paddle):

       return self.distance(paddle)
   def move(self):
       newX=self.xcor() +self.x_move
       newY=self.ycor()+ self.y_move
       self.goto(newX,newY)
   def Bounce_Yaxis(self):
       self.y_move=-self.y_move
   def Bounce_Xaxis(self):
       self.x_move=-self.x_move

   def Bounce_Upward(self):
       newX = self.xcor() + 10
       newY = self.ycor() + 10
       self.goto(newX, newY)



