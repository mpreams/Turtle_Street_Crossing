from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.score = 1

    def post(self):
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.post()

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)

