from turtle import Turtle

# where are each of the snake parts
# TWEAKS:
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]    # use globally
MOVE_DISTANCE = 20
# to remove backwards as head is front
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # what should happen when we initialize a new object
    def __init__(self):
        # use self when working in a class!
        self.segments = []  # add self to apply to each segments of each Snake
        self.create_snake()
        self.head = self.segments[0]

        # snake body parts
    def create_snake(self):
        for position in STARTING_POSITION:  # constant
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(position)
            self.segments.append(body)   # add current segments to the list of Snake segment

    def move(self):
        # update with self as this is class
        for seg_num in range(len(self.segments) - 1, 0, -1):   # move from tail to head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # second to last position
        self.head.forward(MOVE_DISTANCE)

    # control
    #       snake.setheading(90)
    # FIX: control the first segment of the snake
    #       self.segments[0].setheading(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:   # heading() is a method!
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)