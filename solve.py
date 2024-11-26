from turtle import Screen, Turtle # import Screen and Turtle classes
import time


screen = Screen()
screen.setup(600, 600)  # use keyword arguments (width and height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# where are each of the snake parts
starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

# snake body parts
for position in starting_position:
    body = Turtle("square")
    body.color("white")
    body.penup()
    body.goto(position)
    segments.append(body)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    # for seg_num in range(start=2, stop=0, step=-1)    if we want a range of 2, 1, 0
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)    # second to last position
    segments[0].forward(20)



screen.exitonclick()