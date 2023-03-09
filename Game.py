from turtle import Screen, Turtle
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
import time

# variables for screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_BG_COLOR = "black"
WINDOW_TITLE = "Pong Game"

# border margin variable
MARGIN = 30

# variables of dash line
DASH_LINE_WIDTH = 3
DASH_LINE_HEIGHT = 10
DASH_COLOR = (227, 207, 87)

# game variables
DELAY = 0.06
MAX_NUMBER_ROUNDS = 15

# variable of paddles
PADDLE_HEIGHT = 60

# variables for game status display
STATUS_BG_COLOR = "black"
STATUS_TXT_COLOR = (0, 128, 128)
STATUS_FONT = ("Times New Roman", 15, "normal")
STATUS_ALERT_WIDTH = 100
STATUS_ALERT_HEIGHT = 100


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor(SCREEN_BG_COLOR)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.title(WINDOW_TITLE)
        self.screen.tracer(0)
        self.y_min = -1 * round(SCREEN_HEIGHT / 2) + MARGIN
        self.y_max = -1 * self.y_min
        self.x_min = -1 * round(SCREEN_WIDTH / 2) + MARGIN
        self.x_max = -1 * self.x_min
        self.screen.colormode(255)

        '''DRAW DASH LINE AT CENTER OF SCREEN'''
        draw_dash_line()
        self.screen.update()

        '''DISPLAY SCORE'''
        # Display left score
        x_position = -1 * round(SCREEN_WIDTH / 4)
        left_score_position = (x_position, self.y_max)
        self.left_score_board = ScoreBoard(screen=self.screen, score_position=left_score_position)

        # Display right score
        right_score_position = (-1 * x_position, self.y_max)
        self.right_score_board = ScoreBoard(screen=self.screen, score_position=right_score_position)
        self.screen.update()

        '''DISPLAY PADDLE'''
        # Display left paddle
        left_position = (self.x_min, 0)
        self.left_paddle = Paddle(screen=self.screen,
                                  position=left_position,
                                  up_key="w",
                                  down_key="s",
                                  paddle_height=PADDLE_HEIGHT)
        # Display right paddle
        right_position = (self.x_max, 0)
        self.right_paddle = Paddle(screen=self.screen,
                                   position=right_position,
                                   up_key="Up",
                                   down_key="Down",
                                   paddle_height=PADDLE_HEIGHT)
        self.screen.update()

        # create ball
        self.ball = Ball(screen=self.screen, x_min=self.x_min, y_min=self.y_min, margin=MARGIN)

        # create turtle to display game status
        self.status = Turtle(shape="square")
        self.status.hideturtle()
        self.status.shapesize(stretch_wid=STATUS_ALERT_WIDTH / 20, stretch_len=STATUS_ALERT_HEIGHT / 20)
        # set variable to calculate distance reached by ball when first thrown
        self.min_distance_reached = False
        # track number of rounds
        self.round_number = 1

    def play_one_round(self):
        time.sleep(DELAY)
        self.left_paddle.move_paddle()
        self.right_paddle.move_paddle()
        self.ball.move_ball()
        self.screen.update()

        # ball has to travel some distance before we detect collision with top margin
        if not self.min_distance_reached:
            self.min_distance_reached = self.ball.ycor() < self.y_max - 100

        if self.min_distance_reached:
            # if there is a collision with horizontal walls
            if self.ball.ycor() < self.y_min or self.ball.ycor() > self.y_max:
                self.ball.bounce("wall")

        # if there is collision with left wall
        if self.ball.xcor() <= self.x_min:
            # if left paddle catches it => ball bounces
            if self.left_paddle.ycor() + PADDLE_HEIGHT / 2 \
                    > self.ball.ycor() \
                    > self.left_paddle.ycor() - PADDLE_HEIGHT / 2:
                self.ball.bounce("paddle")
            else:
                # game is reset and score goes to the right
                self.right_score_board.add_score()
                self.reset_game()

        # if there is collision with right wall
        if self.ball.xcor() >= self.x_max:
            # if right paddle catches it => ball bounces
            if self.right_paddle.ycor() + PADDLE_HEIGHT / 2 \
                    > self.ball.ycor() \
                    > self.right_paddle.ycor() - PADDLE_HEIGHT / 2:
                self.ball.bounce("paddle")
            else:
                # game is reset and score goes to the left
                self.left_score_board.add_score()
                self.reset_game()

    def play_one_set(self):
        self.left_score_board.reset_score()
        self.right_score_board.reset_score()
        self.round_number = 1
        self.status.clear()
        time.sleep(0.8)
        self.display_status(f"ROUND: {self.round_number}")
        self.screen.update()
        time.sleep(1)
        self.status.clear()
        while self.round_number < MAX_NUMBER_ROUNDS:
            self.play_one_round()
        # after one round of game
        self.display_status("GAME OVER")

    def display_status(self, text):
        """display status of the game: game is on, reset game or game over"""
        self.status.color(STATUS_BG_COLOR)
        self.status.stamp()
        self.status.color(STATUS_TXT_COLOR)
        self.status.write(f"{text}", align="center", font=STATUS_FONT)

    def reset_game(self):
        """resets ball position when ball goes over vertical borders"""
        self.ball.reset_ball()
        self.round_number += 1
        self.display_status(f"ROUND: {self.round_number}")
        self.screen.update()
        time.sleep(1)
        self.status.clear()
        self.min_distance_reached = False


def draw_dash_line():
    """draw dash line in the middle of the screen"""
    x_center = 0
    y_height = round(SCREEN_HEIGHT / 2)
    dash_line = Turtle()
    dash_line.hideturtle()
    dash_line.speed("fastest")

    # move turtle to position
    dash_line.penup()
    dash_line.goto(x_center, y_height)

    # draw dash line diving the screen in two
    dash_line.setheading(270)
    dash_line.pencolor(DASH_COLOR)
    dash_line.pensize(DASH_LINE_WIDTH)
    number_dash = round(SCREEN_HEIGHT / (2 * DASH_LINE_WIDTH))
    for _ in range(number_dash):
        dash_line.forward(DASH_LINE_HEIGHT)
        dash_line.pendown()
        dash_line.forward(DASH_LINE_HEIGHT)
        dash_line.penup()
