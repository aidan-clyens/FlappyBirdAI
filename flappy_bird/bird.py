from .constants import SCREEN_HEIGHT, BIRD_SIZE
import pygame


class Bird:
    def __init__(self):
        self._shape = pygame.Surface([BIRD_SIZE, BIRD_SIZE])
        self._shape.fill(pygame.Color(255, 255, 255))
        self._rect = self._shape.get_rect()
        self._rect.y = 100
        self._rect.x = 200

        self._vertical_speed = 0

    def update(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE]:
            self.fly()

        self._vertical_speed += 2

        self._rect.y += self._vertical_speed

    def draw(self, screen):
        screen.blit(self._shape, [self._rect.x, self._rect.y])

    def fly(self):
        self._vertical_speed -= 6

    def is_dead(self):
        if self._rect.y > SCREEN_HEIGHT:
            return True
        
        return False

    def get_height(self):
        return self._rect.y
