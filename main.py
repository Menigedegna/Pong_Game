from Game import Game


GAME_TRIGGER_KEY = "space"

if __name__ == '__main__':
    pong_game = Game()
    pong_game.screen.listen()
    pong_game.screen.onkey(key=GAME_TRIGGER_KEY, fun=pong_game.play_one_set)
    # allow user to exit screen
    pong_game.screen.exitonclick()
