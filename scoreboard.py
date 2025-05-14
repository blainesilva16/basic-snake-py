from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.file = open("data_snake_game.txt", "r")
        self.high_score = int(self.file.read())
        self.file.close()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.file = open("data_snake_game.txt", "w")
            self.file.write(f"{self.high_score}")
            self.file.close()
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER. PRESS 'r' TO RESTART", False, ALIGNMENT, FONT)

