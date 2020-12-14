from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(0)
        self.new_food()

    def new_food(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
