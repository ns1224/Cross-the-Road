from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
START_LINE_Y = -275
FINISH_LINE_Y = 255
LEFT_BOUND = -250
RIGHT_BOUND = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.go_to_start()
        self.setheading(90)

    def ups_player(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def downs_player(self):
        if self.ycor() > START_LINE_Y:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def slide_left(self):
        if self.xcor() > LEFT_BOUND:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def slide_right(self):
        if self.xcor() < RIGHT_BOUND:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def go_to_start(self):
        self.penup()
        self.goto(0, START_LINE_Y)
