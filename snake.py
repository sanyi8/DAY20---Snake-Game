from turtle import Turtle

# where are each of the snake parts
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]    # use globally
MOVE_DISTANCE = 20

class Snake:
    # what should happen when we initialize a new object
    def __init__(self):
        # use self when working in a class!
        self.segments = []  # add self to apply to each segments of each Snake

        # snake body parts
    def create_snake(self):
        for position in STARTING_POSITION:
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
        self.segments[0].forward(MOVE_DISTANCE)

