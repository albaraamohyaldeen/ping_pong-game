from turtle import Turtle

class Paddle(Turtle):
   def __init__(self, position):
      super().__init__()
      
      self.color('white')
      self.shape('square')
      self.penup()
      self.goto(position)
      self.shapesize(stretch_wid =5, stretch_len =5)

   def go_up(self):
         
         self.goto(self.xcor(), self.ycor()+40)

   def go_down(self):
         self.goto(self.xcor(), self.ycor()-40)
      
