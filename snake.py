from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.snake = []
        self.s = Screen()
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(0 - i * 20, 0)
            self.snake.append(t)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(MOVE_DISTANCE)

    def add(self):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(t)

    def hide(self):
        for seg in self.snake:
            seg.hideturtle()


