from turtle import Turtle
from random import randint, choice

COLORS = ["yellow","blue","red","orange","green","aquamarine4","purple","violetred1"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(choice(COLORS))
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        while not random_x % 20 == 0:
            random_x = randint(-280, 280)
        while not random_y % 20 == 0:
            random_y = randint(-280, 280)
        self.goto(random_x, random_y)

    def hide(self):
        self.hideturtle()