import pygame


class Game:
    def __init__(self):
        self._screen = pygame.display.set_mode([800, 600])
        self._clock = pygame.time.Clock()

    def draw(self):
        self._screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()
    
    def update(self):
        pass

    def step(self):
        self.poll_events()

        self.update()
        self.draw()

        self._clock.tick(60)
    
    def quit(self):
        pygame.quit()

    def poll_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.quit()
