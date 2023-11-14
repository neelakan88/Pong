from turtle import Turtle
from turtle import Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.up()
      

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align = "center", font = ("Courier", 80, "normal"))

    def line(self):
        self.screen.tracer(0)
        self.hideturtle()
        self.up()
        self.goto(0, -300)
        self.left(90)
        self.color("white")
        for i in range(30):
            self.down()
            self.forward(10)
            self.up()
            self.forward(10)
    
    # def update_score(self, l_score, r_score):
    #     self.clear()
    #     self.r_paddle_score = r_score
    #     self.l_paddle_score = l_score
    #     self.player_score()
    #     self.screen.update()

    # def player_score(self):
    #     self.color("white")
    #     self.goto(0, 260)
    #     self.write(arg = f"{self.l_paddle_score}       {self.r_paddle_score}", align = "center", move = False, font = ('Arial', 20, 'normal'))
    #     self.screen.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     if r_paddle_score == 10:
    #         self.write(arg = "Game Over, Right Player Wins!", align = "center", move = False, font = ('Arial', 40, 'normal'))
    #     elif l_paddle_score == 10:
    #         self.write(arg = "Game Over, Left Player Wins!", align = "center", move = False, font = ('Arial', 40, 'normal'))
