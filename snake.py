from turtle import Turtle

# Define constants to be used in this snake class
# Three square Turtles were used with initial coordinates given in the list below
# The moving distance is assigned to 20
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    # instantiating the Snake class calls the build method of the snake
    def __init__(self):
        self.snake_segment = []
        self.snake_build()
        self.head = self.snake_segment[0]

    # appends each square Turtle shape to the empty list called the snake_segment
    # and moves each segment to their initial position
    def snake_build(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    # add segments to current snake
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.pu()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segment.append(new_segment)

    # extends the snake length by adding to the last segment
    def extend(self):
        self.add_segment(self.snake_segment[-1].pos())

    # makes the last segment of the snake to take the position of the preceding segment and so on.
    # In this way, the full segment of the snake moves in accordance by 20 pace together
    def snake_move(self):
        for snake_index in range(len(self.snake_segment)-1, 0, -1):
            new_x = self.snake_segment[snake_index-1].xcor()
            new_y = self.snake_segment[snake_index-1].ycor()
            self.snake_segment[snake_index].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    # methods for controlling the snake movement.
    # Snake can't move in opposite direction when the current opposite direction is on
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    # removes the current snake and resets with a new snake
    def snake_reset(self):
        for seg in self.snake_segment:
            seg.goto(1000, 1000)
        self.snake_segment.clear()
        self.snake_build()
        self.head = self.snake_segment[0]

