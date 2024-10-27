from turtle import Turtle

class Ball(Turtle):
   def __init__(self):
      super().__init__()
      self.color('white')
      self.shape('circle')
      self.penup()

      self.x_move = 11
      self.y_move = 11

