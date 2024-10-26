from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board

import time

window = Screen()
window.bgcolor('black')
window.setup(800,600)
window.title('Ping Pong Game')
window.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))
ball = Ball()
score_board = Score_board()

window.listen()
window.onkey(r_paddle.go_up,'w')
window.onkey(r_paddle.go_down,'s')
window.onkey(l_paddle.go_up,'w')
window.onkey(l_paddle.go_down,'s')


game_on = True
default_sleep=0

while game_on:
   window.update()
   time.sleep(default_sleep)
   ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

   
   if ball.ycor() >= 280  or ball.ycor() <= -280:
      ball.y_move *= -1
      
   if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50)  or (ball.xcor() <= -330 
      and
      ball.distance(l_paddle) <= 50):
      ball.x_move *= -1
      default_sleep *= 0.9
      

   if ball.xcor() >400:
      default_sleep= 0.1
      ball.penup()
      ball.goto(0,0)
      ball.y_move *= -1
      score_board.l_score()
      
   if ball.xcor() < -400:
      default_sleep =0
      
      ball.penup()
      ball.goto(0,0)
      ball.y_move *= -1
      score_board.r_score()
      
