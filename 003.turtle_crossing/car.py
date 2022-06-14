from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(choice(COLORS))
        random_y = randint(-250, 250)
        self.goto(300, random_y)
        self.move_distance = randint(1, 5)
