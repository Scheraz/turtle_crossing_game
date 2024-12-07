from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 0
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level {self.score}", align= "center", font=FONT)

    def update_points(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.write("Game Over!", align = "center", font = FONT)

