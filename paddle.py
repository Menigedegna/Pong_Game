from turtle import Turtle

MOVE_DISTANCE = 20
PAD_COLOR = (0, 255, 127)
PAD_WIDTH = 10


class Paddle(Turtle):
    """paddle for game, user can interact with the paddle, it can go up and down"""
    def __init__(self, screen, position, up_key, down_key, paddle_height):
        super().__init__()
        self.screen = screen
        self.shape("square")
        self.color(PAD_COLOR)
        self.shapesize(stretch_wid=round(PAD_WIDTH/20, 1), stretch_len=round(paddle_height/20, 1))
        self.penup()
        self.goto(position)
        self.up_key = up_key
        self.down_key = down_key
        self.setheading(90)
        self.direction_up = True

    def move_up(self):
        self.direction_up = True
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.direction_up = False
        self.backward(MOVE_DISTANCE)

    def move_paddle(self):
        self.screen.listen()
        self.screen.onkey(key=self.up_key, fun=self.move_up)
        self.screen.onkey(key=self.down_key, fun=self.move_down)
