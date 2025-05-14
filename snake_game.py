from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game - Press 'r' to restart")
s.tracer(0)
s.listen()

# move = True

def start():
    move = True
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    while move:
        s.update()
        time.sleep(0.1)
        snake.move()
        s.onkey(snake.right, "Right")
        s.onkey(snake.left, "Left")
        s.onkey(snake.up, "Up")
        s.onkey(snake.down, "Down")

        # Detect collision with wall
        if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
            move = False
            # scoreboard.game_over()
            scoreboard.reset()

        for seg in snake.snake[1:]:
            if snake.snake[0].distance(seg) < 1:
                move = False
                # scoreboard.game_over()
                scoreboard.reset()

        if snake.snake[0].distance(food) < 15:
            food.refresh()
            scoreboard.refresh()
            snake.add()
    snake.hide()
    food.hide()
    scoreboard.clear()

start()
s.onkey(start, "r")

s.exitonclick()