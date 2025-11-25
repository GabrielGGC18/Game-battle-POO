import pygame
from abc import ABC, abstractmethod

class MoveStrategy(ABC):
    @abstractmethod
    def move(self, x, y, keys, screen_width=800, screen_height=369): pass

class NormalMove(MoveStrategy):
    def move(self, x, y, keys, screen_width=800, screen_height=369):
        vel = 10
        if keys[pygame.K_UP]: y -= vel
        if keys[pygame.K_DOWN]: y += vel
        if keys[pygame.K_LEFT]: x -= vel
        if keys[pygame.K_RIGHT]: x += vel
        return x, y

class FastMove(MoveStrategy):
    def move(self, x, y, keys, screen_width=800, screen_height=369):
        vel = 20
        if keys[pygame.K_UP]: y -= vel
        if keys[pygame.K_DOWN]: y += vel
        if keys[pygame.K_LEFT]: x -= vel
        if keys[pygame.K_RIGHT]: x += vel
        return x, y
