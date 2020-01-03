from .constants import PIPE_HORIZONTAL_GAP, PIPE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE, FONT_PATH, FONT_SIZE
from .bird import Bird
from .pipes import Pipes

import pygame


class Game:
    def __init__(self):
        self._screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("Flappy Bird AI")
        pygame.init()

        self._clock = pygame.time.Clock()

        self._birds = []
        self._birds.append(Bird())
        self._pipes = []
        self._pipes.append(Pipes())

        self._font = pygame.font.Font(FONT_PATH, FONT_SIZE)
        self._top_score = 0

        self._running = True

    def draw(self):
        self._screen.fill(BLUE)

        self.draw_score()

        for bird in self._birds:
            bird.draw(self._screen)
        
        for pipe in self._pipes:
            pipe.draw(self._screen)

        pygame.display.flip()
    
    def update(self):
        for bird in self._birds:
            bird.update()
        
        self.update_pipes()
        self.count_score()
        for pipe in self._pipes:
            pipe.update()

        if self.are_birds_dead():
            self._running = False

    def step(self, action=None):
        self.poll_events()

        self.update()
        self.draw()

        self._clock.tick(60)
    
        return self.get_observation()

    def quit(self):
        pygame.quit()

    def poll_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self._running = False

    def count_score(self):
        for bird in self._birds:
            for pipe in self._pipes:
                if bird.get_position()[0] > pipe.get_position()[0] and not pipe.get_passed():
                    pipe.set_passed(True)
                    bird.add_score()

    def update_pipes(self):
        for pipe in self._pipes:
            if len(self._pipes) < 2:
                if pipe.get_position()[0] < PIPE_HORIZONTAL_GAP:
                    self._pipes.append(Pipes())

            elif pipe.get_position()[0] < -PIPE_WIDTH:
                self._pipes.remove(pipe)

    def draw_score(self):
        for bird in self._birds:
            if bird.get_score() > self._top_score:
                self._top_score = bird.get_score()
        
        score_text = self._font.render(str(self._top_score), True, WHITE)
        self._screen.blit(score_text, [20, 5])

    def get_observation(self):
        observations = []

        for bird in self._birds:
            pipe_index = 0
            while self._pipes[pipe_index].get_passed():
                pipe_index += 1

            next_pipe = self._pipes[pipe_index]
            
            observation = [
                bird.get_position()[1],
                next_pipe.get_position()[0] - bird.get_position()[0],
                next_pipe.get_position()[1] - bird.get_position()[1],
            ]

            for i in range(len(observation)):
                observation[i] /= SCREEN_HEIGHT
        
            observations.append(observation)
        
        return observations

    def are_birds_dead(self):
        for bird in self._birds:
            is_dead = False

            if bird.get_position()[1] > SCREEN_HEIGHT:
                is_dead = True

            for pipe in self._pipes:
                if pipe.collides(bird._rect):
                    is_dead = True

            if is_dead:
                self._birds.remove(bird)

        return len(self._birds) == 0

    def is_running(self):
        return self._running
