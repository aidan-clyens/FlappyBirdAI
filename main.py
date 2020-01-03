from flappy_bird import Game


def main():
    game = Game()

    while True:
        if not game.is_running():
            break

        observation = game.step()

    game.quit()


if __name__ == "__main__":
    main()