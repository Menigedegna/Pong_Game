from turtle import Turtle

BG_COLOR = "black"
TXT_COLOR = "white"
FONT = ("Times New Roman", 15, "normal")
ALERT_WIDTH = 50
ALERT_HEIGHT = 100


class GameStatus(Turtle):
    """keeps track of game status and informs user progress: game is on, reset game, game is over"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_wid=ALERT_WIDTH/20, stretch_len=ALERT_HEIGHT/20)

    def display_status(self, text):
        self.color(BG_COLOR)
        self.stamp()
        self.color(TXT_COLOR)
        self.write(f"{text}", align="center", font=FONT)
