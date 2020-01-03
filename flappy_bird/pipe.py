from .constants import PIPE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import random


class Pipe:
    def __init__(self):
        self._shape = pygame.Surface([PIPE_WIDTH, 1000])
        self._shape.fill(pygame.Color(255, 255, 255))
        self._rect = self._shape.get_rect()
        self._rect.y = random.randint((SCREEN_HEIGHT / 4), (3*SCREEN_HEIGHT / 4))
        self._rect.x = SCREEN_WIDTH
    
        self._horizontal_speed = 5

    def update(self):
        self._rect.x -= self._horizontal_speed

    def draw(self, screen):
        screen.blit(self._shape, [self._rect.x, self._rect.y])
    
    def get_height(self):
        return self._rect.y
