from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []  # add self to apply to each segments of each Snake
        # where are each of the snake parts
        starting_position = [(0, 0), (-20, 0), (-40, 0)]

        # snake body parts
        for position in starting_position:
            body = Turtle("square")
            body.color("white")
            body.penup()
            body.goto(position)
            self.segments.append(body)   # add current segments to the list of Snake segment

    def move(self):
        # update above range
        for seg_num in range(len(self.segments) - 1, 0, -1):   # move from tail to head
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # second to last position

        self.segments[0].forward(20)

