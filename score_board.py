from turtle import Turtle


class Score_board(Turtle):
 def __init__(self):
   super().__init__()
   self.color('white')
   self.penup()
   self.hideturtle()
   self.goto(0,250)
   self.write('score', align ='center' ,font =('courier',25,'normal'))
   self.r_scor =0
   self.l_scor =0
   self.cl_score()
    
 def r_score(self):
      self.r_scor += 1
      self.cl_score()
 def l_score(self):
      self.l_scor += 1
      self.cl_score()
 def cl_score(self):
      self.clear()
      self.goto(101,251)
      self.write(f'{self.r_scor}', align = 'center' ,font =('courier',41,'normal'))
      self.goto(-101,251)
      self.write(f'{self.l_scor }', align = 'center' ,font =('courier',41,'normal'))
      
    
    

   

