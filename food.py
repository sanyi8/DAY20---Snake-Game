from turtle import Turtle
import random

class Food(Turtle): # create food class inherit from turtle

    def __init__(self):
        super().__init__() # initialize the Turtle class
        self.shape("circle")    # setup food specs
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        # use -280 - 280 for range
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
