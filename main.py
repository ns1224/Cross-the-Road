import time
from turtle import Screen
from road import Road
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing - NSC")
screen.bgcolor("black")
screen.tracer(0)
screen.colormode(255)


road = Road()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.ups_player, "Up")
screen.onkey(player.downs_player, "Down")
screen.onkey(player.slide_left, "Left")
screen.onkey(player.slide_right, "Right")


game_is_on = True
while game_is_on:
    # Loop runs every 0.1 sec.
    time.sleep(0.1)
    screen.update()

    # Create new car
    car_manager.creates_cars()
    car_manager.moves_car()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            game_is_on = False
            scoreboard.games_over()

    # Detect player crossing
    if player.ycor() > 255:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increases_level()

    # Increase car speed upon crossing


screen.exitonclick()

