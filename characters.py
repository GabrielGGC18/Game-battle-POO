import pygame
from abc import ABC, abstractmethod
from strategies import MoveStrategy
import os 

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

class Character(ABC):
    def __init__(self, name, img, power, life, strategy: MoveStrategy):
        self.name = name
        self.original_image = pygame.image.load(img)
        # Redimensionar para 80x80 pixels
        self.image = pygame.transform.scale(self.original_image, (80, 80))
        self.power = power
        self.life = life
        self.max_life = life
        self.strategy = strategy
        self.special_move_text = ""
        self.special_move_timer = 0

    @abstractmethod
    def special_move(self): pass

    def move(self, x, y, keys):
        return self.strategy.move(x, y, keys)

class Goku(Character):
    def special_move(self):
        self.special_move_text = "Kamehameha 10x!"
        self.special_move_timer = 60
        return "Kamehameha 10x!"

class Naruto(Character):
    def special_move(self):
        self.special_move_text = "Odama Rasengan!"
        self.special_move_timer = 60
        return "Odama Rasengan!"

class CharacterFactory:
    @staticmethod
    def create(type_, strategy):
        if type_ == "goku":
            return Goku("Goku", "assets/goku.png", 100, 200, strategy)
        elif type_ == "naruto":
            return Naruto("Naruto", "assets/naruto.png", 90, 180, strategy)
        else:
            raise ValueError("Personagem desconhecido")
