from .constants import PIPE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

import pygame
import random


class Pipes:
    def __init__(self):
        self._bottom_shape = pygame.Surface([PIPE_WIDTH, 1000])
        self._bottom_shape.fill(pygame.Color(255, 255, 255))
        self._bottom_rect = self._bottom_shape.get_rect()
        self._bottom_rect.y = random.randint((SCREEN_HEIGHT / 4), (3*SCREEN_HEIGHT / 4))
        self._bottom_rect.x = SCREEN_WIDTH
    
        self._top_shape = pygame.Surface([PIPE_WIDTH, 1000])
        self._top_shape.fill(pygame.Color(255, 255, 255))
        self._top_rect = self._top_shape.get_rect()
        self._top_rect.y = self._bottom_rect.y - self._bottom_rect.height - 200
        self._top_rect.x = SCREEN_WIDTH

        self._horizontal_speed = 5

    def update(self):
        self._bottom_rect.x -= self._horizontal_speed
        self._top_rect.x -= self._horizontal_speed

    def draw(self, screen):
        screen.blit(self._bottom_shape, [self._bottom_rect.x, self._bottom_rect.y])
        screen.blit(self._top_shape, [self._top_rect.x, self._top_rect.y])
    
    def collides(self, bird):
        return self._bottom_rect.colliderect(bird) or self._top_rect.colliderect(bird)

    def get_height(self):
        return self._bottom_rect.y
