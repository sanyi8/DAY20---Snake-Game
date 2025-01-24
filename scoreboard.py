import turtle
from idlelib.configdialog import font_sample_text
from turtle import Turtle   # inherit from turtle

# remove hard coded pieces from body with constants
ALIGNMENT = "center"
FONT = ("Helvetica", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # now Scoreboard class can do everything what Turtle can do
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()