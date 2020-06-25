from flappy_bird import Game
from agent import BirdAgent


def main():
    game = Game()

    for gen in range(5):
        print(f"Generation={gen}")
        population = [BirdAgent() for i in range(5)]
        game.reset(population)

        while True:
            if not game.running:
                break

            observation, action = game.step()

    game.quit()


if __name__ == "__main__":
    main()
