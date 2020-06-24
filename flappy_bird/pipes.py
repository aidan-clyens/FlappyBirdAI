from .constants import PIPE_VERTICAL_GAP, PIPE_WIDTH
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT
from .constants import GREEN

import pygame
import random


class Pipes:
    def __init__(self):
        self.bottom_shape = pygame.Surface([PIPE_WIDTH, 1000])
        self.bottom_shape.fill(GREEN)
        self.bottom_rect = self.bottom_shape.get_rect()
        self.bottom_rect.y = random.randint(
            (SCREEN_HEIGHT / 4),
            (3*SCREEN_HEIGHT / 4)
        )
        self.bottom_rect.x = SCREEN_WIDTH

        self.top_shape = pygame.Surface([PIPE_WIDTH, 1000])
        self.top_shape.fill(GREEN)
        self.top_rect = self.top_shape.get_rect()
        self.top_rect.y = self.bottom_rect.y - \
            self.bottom_rect.height - PIPE_VERTICAL_GAP
        self.top_rect.x = SCREEN_WIDTH

        self.horizontal_speed = 5

        self.passed = False

    def update(self):
        self.bottom_rect.x -= self.horizontal_speed
        self.top_rect.x -= self.horizontal_speed

    def draw(self, screen):
        screen.blit(
            self.bottom_shape,
            [self.bottom_rect.x, self.bottom_rect.y]
        )
        screen.blit(
            self.top_shape,
            [self.top_rect.x, self.top_rect.y]
        )

    def collides(self, bird):
        return self.bottom_rect.colliderect(bird) \
            or self.top_rect.colliderect(bird)

    def get_position(self):
        return [self.bottom_rect.x, self.bottom_rect.y]
