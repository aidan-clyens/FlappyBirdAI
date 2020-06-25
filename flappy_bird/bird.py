from .constants import BIRD_SIZE
from .constants import GRAVITY_ACCELERATION, FLY_ACCELERATION
from .constants import YELLOW

import pygame


class Bird:
    def __init__(self):
        self.shape = pygame.Surface([BIRD_SIZE, BIRD_SIZE])
        self.shape.fill(YELLOW)

    def reset(self):
        self.rect = self.shape.get_rect()
        self.rect.y = 100
        self.rect.x = 200

        self.vertical_speed = 0

        self.last_action = 0
        self.score = 0

    def update(self, fly=False):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_SPACE] or fly:
            self.last_action = 1
            self.fly()
        else:
            self.last_action = 0

        self.vertical_speed += GRAVITY_ACCELERATION

        self.rect.y += self.vertical_speed

    def draw(self, screen):
        screen.blit(self.shape, [self.rect.x, self.rect.y])

    def fly(self):
        self.vertical_speed -= FLY_ACCELERATION

    def collides(self, pipe):
        return self.rect.colliderect(pipe)

    def get_position(self):
        return [self.rect.x, self.rect.y]
