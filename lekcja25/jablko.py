import pygame
import random

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("lekcja25/images/apple.png")
        self.rect = pygame.Rect(random.randrange(0, 24)*32 , random.randrange(0, 18)*32 , 32 , 32)