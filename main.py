from turtle import Screen, Turtle # import Screen and Turtle classes

is_game_on = False
screen = Screen()
screen.setup(600, 600)  # use keyword arguments (width and height)
screen.bgcolor("black")
screen.title("My Snake Game")

# snake head
snake = Turtle("square")
snake.penup()
snake.color("lightgreen")
snake.goto(x=0,y=0)

# food in belly starts with 2 and will add each food one to it
# food = []
# setup body length
body_length = []     # list of placeholders for two parts
x_position = -20    # start position for next body parts

for _ in range(2):
    # add snake body
    body_object = Turtle("square")
    body_object.penup()
    body_object.color("white")
    body_object.goto(x=x_position, y=0)
    body_length.append(body_object)
    x_position -= 20    # space between body squares


screen.exitonclick()