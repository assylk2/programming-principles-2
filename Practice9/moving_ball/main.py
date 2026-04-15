import pygame
import sys
from ball import Ball  # Импортируем наш класс

pygame.init()

# Настройки окна
W, H = 800, 600
screen = pygame.display.set_mode((W, H))

# Создаем экземпляр шара
my_ball = Ball(W//2, H//2, 25, (76, 153, 0), W, H)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.move("up")
            elif event.key == pygame.K_DOWN:
                my_ball.move("down")
            elif event.key == pygame.K_LEFT:
                my_ball.move("left")
            elif event.key == pygame.K_RIGHT:
                my_ball.move("right")

    screen.fill((255, 255, 255))
    my_ball.draw(screen)  # Шар сам себя рисует
    pygame.display.flip()
    clock.tick(60)