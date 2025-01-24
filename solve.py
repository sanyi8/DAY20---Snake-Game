from turtle import Screen#, Turtle # import Screen and Turtle classes
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600, 600)  # use keyword arguments (width and height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create new object
# use Snake() class from another file
snake = Snake() # store instance from Class()
food = Food()   # get food data from food.py
scoreboard = Scoreboard()   # create scoreboard as an object

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

    # detect collision with food
    if snake.head.distance(food) < 15:
        # print("nom nom nom") # instead of print we add a body
        food.refresh() # update food position
        scoreboard.increase_score() # increase and update score

screen.exitonclick()
