from turtle import Screen, Turtle # import Screen and Turtle classes
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)  # use keyword arguments (width and height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# use Snake() class from another file
snake = Snake() # store instance from Class()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    snake.move()


screen.exitonclick()