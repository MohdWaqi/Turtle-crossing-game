import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()
    if player.ycor() == 280:
        player.refresh()
        score.increase_level()
        car.level_up()
    for n in car.all_cars:
        if player.distance(n) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()