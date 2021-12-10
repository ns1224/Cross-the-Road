from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
START_LINE_Y = -275
FINISH_LINE_Y = 255


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.go_to_start()
        self.setheading(90)

    def moves_player(self):
        if self.ycor() < 250:
            self.goto(0, self.ycor() + MOVE_DISTANCE)

    def go_to_start(self):
        self.penup()
        self.goto(0, START_LINE_Y)
