import pygame


class Bird:
    def __init__(self):
        self._shape = pygame.Surface([50, 50])
        self._shape.fill(pygame.Color(255, 255, 255))
        self._rect = self._shape.get_rect()
        self._rect.y = 100
        self._rect.x = 200

        self._vertical_speed = 0

    def update(self):
        self._vertical_speed += 2

        self._rect.y += self._vertical_speed

    def draw(self, screen):
        screen.blit(self._shape, [self._rect.x, self._rect.y])
