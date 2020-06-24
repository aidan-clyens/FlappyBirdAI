from flappy_bird import Game


def main():
    game = Game()

    while True:
        if not game.running:
            break

        observation, action = game.step()

    game.quit()


if __name__ == "__main__":
    main()
