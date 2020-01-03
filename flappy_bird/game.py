from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .bird import Bird
from .pipes import Pipes

import pygame


class Game:
    def __init__(self):
        self._screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self._clock = pygame.time.Clock()

        self._bird = Bird()
        self._pipes = []
        self._pipes.append(Pipes())

        self._running = True

    def draw(self):
        self._screen.fill(pygame.Color(0, 0, 0))

        self._bird.draw(self._screen)
        
        for pipe in self._pipes:
            pipe.draw(self._screen)

        pygame.display.flip()
    
    def update(self):
        self._bird.update()
        
        for pipe in self._pipes:
            pipe.update()

        if self.is_bird_dead():
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

    def get_observation(self):
        return None
    
    def is_bird_dead(self):
        if self._bird.get_height() > SCREEN_HEIGHT:
            return True

        for pipe in self._pipes:
            if pipe.collides(self._bird._rect):
                return True

        return False

    def is_running(self):
        return self._running
