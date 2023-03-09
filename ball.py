from turtle import Turtle
from random import randint, choice
BALL_COLOR = (255, 215, 0)
BALL_DIAMETER = 10
MOVE_DISTANCE = 10


class Ball(Turtle):
    """ball for game, is constantly moving and bounces off paddles and horizontal borders"""
    def __init__(self, screen, y_min, x_min, margin):
        super().__init__()
        self.screen = screen

        # create ball
        self.y_min = y_min
        self.x_min = x_min
        self.margin = margin
        self.shape("circle")
        self.shapesize(stretch_wid=BALL_DIAMETER/20, stretch_len=BALL_DIAMETER/20, outline=5)
        self.color(BALL_COLOR, "white")
        self.reset_ball()

    def reset_ball(self):
        # set random position for ball at the top of screen
        position = (randint(self.x_min, -1*self.x_min), -1*self.y_min + self.margin)
        self.penup()
        self.goto(position)

        # get random point on either left or right wall and set direction
        y_random = randint(self.y_min, -1*self.y_min)
        x_random = choice([self.x_min, -1*self.x_min])
        random_point = (x_random, y_random)
        random_angle = self.towards(random_point)
        self.setheading(random_angle)

    def move_ball(self):
        # self.goto(self.xcor()+MOVE_DISTANCE, self.ycor()+MOVE_DISTANCE)
        self.forward(MOVE_DISTANCE)

    def bounce(self, collision_object):
        if collision_object == "wall":
            self.setheading(360-self.heading())
        else:
            self.setheading(180-self.heading())
