# coin.py
import pygame
import random

class Coin:
    def __init__(self):
        self.x = random.randint(20, 380)
        self.y = -20
        self.w = 20
        self.h = 20

        # Load coin image
        self.img = pygame.image.load("assets/coin.png")
        self.img = pygame.transform.scale(self.img, (20, 20))

    def update(self):
        self.y += 5

    def draw(self, screen):
        screen.blit(self.img, (self.x - 10, self.y - 10))

    def rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, self.w, self.h)