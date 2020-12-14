from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SLEEP_TIME = 0.1
scoreboard = Scoreboard()
# decorates the screen
my_screen = Screen()

food = Food()

my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Bernco Snake Game")

# hides the current animation of the screen for irregular Turtle movement
my_screen.tracer(0)

# Creates the snake object
my_snake = Snake()
is_game_on = True

# Screen waits for events from the keyboard. Using the arrow keys you can control the snake
my_screen.listen()
my_screen.onkey(key="Up", fun=my_snake.up)
my_screen.onkey(key="Down", fun=my_snake.down)
my_screen.onkey(key="Left", fun=my_snake.left)
my_screen.onkey(key="Right", fun=my_snake.right)

while is_game_on:
    # now refreshes the screen to cancel out the animation hiding by the tracer method of the screen
    my_screen.update()
    # delay for 0.5 seconds before moving the snake
    time.sleep(SLEEP_TIME)
    my_snake.snake_move()

    # detects collision with food
    # checks if the distance between the head of the snake and the food is so close. i.e when they tough
    if my_snake.head.distance(food) < 15:
        food.new_food()
        my_snake.extend()
        scoreboard.score_keeper()

    # detects collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 \
            or my_snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # detects collision with body

my_screen.exitonclick()
