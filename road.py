from turtle import Turtle

START_FIN_COLOR = (20, 51, 6)
STARTING_LINE = -250
FINISH_LINE = 255


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.color(START_FIN_COLOR)
        self.hideturtle()
        self.draws_bottom_outline()
        self.draws_top_outline()
        self.draws_lanes()
        self.draws_curbs()

    def draws_bottom_outline(self):
        self.color(START_FIN_COLOR)
        self.penup()
        self.goto(-300, STARTING_LINE)
        self.pendown()
        coordinates = [(300, STARTING_LINE), (300, -300), (-300, -300), (-300, STARTING_LINE)]
        self.begin_fill()
        for coordinate in coordinates:
            self.goto(coordinate)
        self.end_fill()
        self.draws_lanes()

    def draws_top_outline(self):
        self.color(START_FIN_COLOR)
        self.penup()
        self.goto(-300, FINISH_LINE)
        self.pendown()
        coordinates = [(300, FINISH_LINE), (300, 300), (-300, 300), (-300, FINISH_LINE)]
        self.begin_fill()
        for coordinate in coordinates:
            self.goto(coordinate)
        self.end_fill()

    def draws_lanes(self):
        self.hideturtle()
        # Each ith entry in lanes is the center of the ith lane in the road
        lanes = [-175, -125, -75, -25, 25, 75, 125, 175, 225]
        self.color("yellow")
        self.penup()
        # For each lane, the upper boundary is lanes[i] - 25, lanes[i] + 25
        for lane in lanes:
            self.goto(-300, lane - 25)
            self.setheading(0)
            while self.xcor() < 288:
                self.forward(12)
                self.pendown()
                self.forward(12)
                self.penup()

    def draws_curbs(self):
        self.hideturtle()
        self.color("grey")
        self.width(3)
        y_cor = 252
        for _ in range(2):
            self.penup()
            self.goto(-300, y_cor)
            self.pendown()
            self.goto(300, y_cor)
            y_cor *= -1
