import pygame

class Ball:
    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.step = 20

    def draw(self, screen):
        # Метод для отрисовки шара на экране
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, direction):
        # Метод для движения с проверкой границ
        if direction == "up":
            if self.y - self.radius - self.step >= 0:
                self.y -= self.step
        elif direction == "down":
            if self.y + self.radius + self.step <= self.screen_height:
                self.y += self.step
        elif direction == "left":
            if self.x - self.radius - self.step >= 0:
                self.x -= self.step
        elif direction == "right":
            if self.x + self.radius + self.step <= self.screen_width:
                self.x += self.step