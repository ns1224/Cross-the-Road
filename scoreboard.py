from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-265, 265)
        self.updates_scoreboard()

    def updates_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increases_level(self):
        self.level += 1
        self.updates_scoreboard()

    def games_over(self):
        self.penup()
        self.color("yellow")
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
