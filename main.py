from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time





#import objects
screen = Screen()
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Score()





#define screen and line
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
score.line()
score.update_scoreboard()


#define keystrokes
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.update()


#keep game going and let me move the fucking god damn paddles
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    #detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_paddle()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle()
    #detect if R-paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()
        score.update_scoreboard()
      

    #detect if L-paddle misses  
    if ball.xcor() < -390:
        ball.reset_position()
        
        score.r_point()
        score.update_scoreboard()



        
        
        
        
    ball.move()
    





screen.exitonclick()