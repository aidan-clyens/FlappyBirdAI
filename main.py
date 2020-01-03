from flappy_bird import Game


def main():
    game = Game()

    for _ in range(50):
        observation = game.step()

    game.quit()


if __name__ == "__main__":
    main()