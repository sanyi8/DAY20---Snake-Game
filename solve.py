from turtle import Screen, Turtle # import Screen and Turtle classes
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)  # use keyword arguments (width and height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create new object
# use Snake() class from another file
snake = Snake() # store instance from Class()

# control setup
screen.listen()     # listen to screen
screen.onkey(snake.up, "Up")    # call method when key pressed
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # this often screen refresh
    # for seg in segments:
    #     seg.forward(20)

    snake.move()

screen.exitonclick()
