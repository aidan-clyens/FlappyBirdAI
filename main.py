from flappy_bird import Game
from agent import BirdAgent


def main():
    population_size = 5
    generation_count = 5

    game = Game()
    population = [BirdAgent() for i in range(population_size)]
    for bird in population:
        bird.reset()

    for gen in range(generation_count):
        print(f"Generation={gen}")
        for bird in population:
            bird.reset()
        game.reset(population)

        observations = []
        actions = []
        while True:
            if not game.running:
                break

            observation, action = game.step()
            observations.append(observation)
            actions.append(action)

        observations = observations[:-1]
        actions = actions[:-1]
        population = game.dead_birds

    game.quit()


if __name__ == "__main__":
    main()
