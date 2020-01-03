import pygame


class Bird:
    def __init__(self):
        self._shape = pygame.Surface([50, 50])
        self._shape.fill(pygame.Color(255, 255, 255))
        self._rect = self._shape.get_rect()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self._shape, [self._rect.x, self._rect.y])
