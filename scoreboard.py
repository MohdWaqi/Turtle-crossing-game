from turtle import Turtle
FONT = ("Courier", 24, "normal")

############################ Setting up ScoreBoard and Gameover Display ########################


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level:-{self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(-100, 0)
        self.write(arg="GAME OVER!", font=FONT)


