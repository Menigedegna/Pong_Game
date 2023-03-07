from turtle import Screen, Turtle
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
from game_status import GameStatus
import time

FONT = ("Times New Roman", 20, "normal")
MARGIN = 30
TOP_MARIN = 10
SPEED_RANGE = [0.5, 0.3, 0.1, 0.08, 0.05]
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_BG_COLOR = "black"
WINDOW_TITLE = "Pong Game"
DASH_COLOR = "white"
ONE_ROUND_GAMES = 15
DELAY = 0.06
PADDLE_HEIGHT = 60


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
    dash_width = 8
    dash_line.pensize(dash_width)
    dash_size = 10
    number_dash = round(SCREEN_HEIGHT / (2 * dash_size))
    for _ in range(number_dash):
        dash_line.forward(dash_size)
        dash_line.pendown()
        dash_line.forward(dash_size)
        dash_line.penup()


def reset_game():
    """resets ball position when ball goes over vertical borders"""
    global ball, game_status, screen, min_distance_reached, number_games
    ball.reset_ball()
    game_status.display_status("reset game")
    screen.update()
    time.sleep(1)
    game_status.clear()
    min_distance_reached = False
    number_games += 1


if __name__ == '__main__':

    '''CONFIGURE SCREEN'''
    screen = Screen()
    screen.bgcolor(SCREEN_BG_COLOR)
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title(WINDOW_TITLE)
    screen.tracer(0)
    y_min = -1 * round(SCREEN_HEIGHT / 2) + MARGIN
    y_max = -1 * y_min
    x_min = -1 * round(SCREEN_WIDTH / 2) + MARGIN
    x_max = -1 * x_min

    '''DRAW DASH LINE AT CENTER OF SCREEN'''
    draw_dash_line()
    screen.update()

    '''DISPLAY SCORE'''
    # Display left score
    x_position = -1 * round(SCREEN_WIDTH / 4)
    left_score_position = (x_position, y_max)
    left_score_board = ScoreBoard(screen=screen, score_position=left_score_position)

    # Display right score
    right_score_position = (-1 * x_position, y_max)
    right_score_board = ScoreBoard(screen=screen, score_position=right_score_position)
    screen.update()

    '''DISPLAY PADDLE'''
    # Display left paddle
    left_position = (x_min, 0)
    left_paddle = Paddle(screen=screen,
                         position=left_position,
                         up_key="w",
                         down_key="s",
                         paddle_height=PADDLE_HEIGHT)
    # Display right paddle
    right_position = (x_max, 0)
    right_paddle = Paddle(screen=screen,
                          position=right_position,
                          up_key="Up",
                          down_key="Down",
                          paddle_height=PADDLE_HEIGHT)
    screen.update()

    # create ball
    ball = Ball(screen=screen, x_min=x_min, y_min=y_min, margin=MARGIN)

    # start game status
    game_status = GameStatus(screen=screen)
    time.sleep(0.8)
    game_status.display_status("GAME IS ON")
    screen.update()
    time.sleep(1)
    game_status.clear()

    min_distance_reached = False
    number_games = 0

    while number_games < ONE_ROUND_GAMES:
        time.sleep(DELAY)
        left_paddle.move_paddle()
        right_paddle.move_paddle()
        ball.move_ball()
        screen.update()

        # ball has to travel some distance before we detect collision with top margin
        if not min_distance_reached:
            min_distance_reached = ball.ycor() < y_max - 100

        if min_distance_reached:
            # if there is a collision with horizontal walls
            if ball.ycor() < y_min or ball.ycor() > y_max:
                ball.bounce("wall")

        # if there is collision with left wall
        if ball.xcor() <= x_min:
            # if left paddle catches it => ball bounces
            if left_paddle.ycor() + PADDLE_HEIGHT/2 > ball.ycor() > left_paddle.ycor() - PADDLE_HEIGHT/2:
                ball.bounce("paddle")
            else:
                # game is reset and score goes to the right
                right_score_board.add_score()
                reset_game()

        # if there is collision with right wall
        if ball.xcor() >= x_max:
            # if right paddle catches it => ball bounces
            if right_paddle.ycor() + PADDLE_HEIGHT/2 > ball.ycor() > right_paddle.ycor() - PADDLE_HEIGHT/2:
                ball.bounce("paddle")
            else:
                # game is reset and score goes to the left
                left_score_board.add_score()
                reset_game()

    game_status.display_status("GAME OVER")

    # allow user to exit screen
    screen.exitonclick()
