from .constants import PIPE_HORIZONTAL_GAP, PIPE_WIDTH
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import WHITE, BLUE, FONT_PATH, FONT_SIZE
from .bird import Bird
from .pipes import Pipes

import pygame


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("Flappy Bird AI")
        pygame.init()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)

    def reset(self, population=[Bird()]):
        self.birds = population
        self.dead_birds = []
        self.pipes = []
        self.pipes.append(Pipes())

        self.top_score = 0

        self.running = True

    def draw(self):
        self.screen.fill(BLUE)

        for bird in self.birds:
            bird.draw(self.screen)

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.draw_score()

        pygame.display.flip()

    def update(self):
        for bird in self.birds:
            bird.update()

        self.update_pipes()
        self.count_score()
        for pipe in self.pipes:
            pipe.update()

        if self.are_birds_dead():
            self.running = False

    def step(self, action=None):
        self.poll_events()

        self.update()
        self.draw()

        self.clock.tick(60)

        return self.get_observation(), self.get_action()

    def quit(self):
        pygame.quit()

    def poll_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.running = False

    def count_score(self):
        for bird in self.birds:
            for pipe in self.pipes:
                if bird.get_position()[0] > pipe.get_position()[0] \
                        and not pipe.passed:
                    pipe.passed = True
                    bird.score += 1

    def update_pipes(self):
        for pipe in self.pipes:
            if len(self.pipes) < 2:
                if pipe.get_position()[0] < PIPE_HORIZONTAL_GAP:
                    self.pipes.append(Pipes())

            elif pipe.get_position()[0] < -PIPE_WIDTH:
                self.pipes.remove(pipe)

    def draw_score(self):
        for bird in self.birds:
            self.top_score = max(bird.score, self.top_score)

        score_text = self.font.render(str(self.top_score), True, WHITE)
        self.screen.blit(score_text, [20, 5])

    def get_observation(self):
        observations = []

        for bird in self.birds:
            pipe_index = 0
            while self.pipes[pipe_index].passed:
                pipe_index += 1

            next_pipe = self.pipes[pipe_index]

            observation = [
                bird.get_position()[1],
                next_pipe.get_position()[0] - bird.get_position()[0],
                next_pipe.get_position()[1] - bird.get_position()[1],
            ]

            for i in range(len(observation)):
                observation[i] /= SCREEN_HEIGHT

            observations.append(observation)

        return observations

    def get_action(self):
        actions = []
        for bird in self.birds:
            actions.append(bird.last_action)

        return actions

    def are_birds_dead(self):
        for bird in self.birds:
            is_dead = False

            if bird.get_position()[1] > SCREEN_HEIGHT:
                is_dead = True

            for pipe in self.pipes:
                if pipe.collides(bird.rect):
                    is_dead = True

            if is_dead:
                self.birds.remove(bird)
                self.dead_birds.append(bird)

        return len(self.birds) == 0
