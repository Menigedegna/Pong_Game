from turtle import Turtle

SCORE_COLOR = "white"
FONT = ("Times New Roman", 15, "normal")
GAME_ALERT = "white"


class ScoreBoard(Turtle):
    """keeps track of score and displays it for both paddles"""
    def __init__(self, screen, score_position):
        super().__init__()
        self.screen = screen
        self.score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(score_position)
        self.reset_score()

    def display_score(self):
        self.write(f"{self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.display_score()
