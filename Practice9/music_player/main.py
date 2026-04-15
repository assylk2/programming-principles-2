import pygame
import sys
import os
from player import MusicPlayer

pygame.init()

# Увеличиваем ширину до 1000, чтобы влез плейлист справа
WIDTH, HEIGHT = 1000, 750 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("iPhone Music Experience")

player = MusicPlayer()

# Загрузка нового скина плеера
base_path = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(base_path, "images/player_ui.png")
player_bg = pygame.image.load(ui_path)
player_bg = pygame.transform.scale(player_bg, (500, 700)) # Плеер будет слева

# Шрифты
font_list = pygame.font.SysFont("Arial", 22)
font_bold = pygame.font.SysFont("Arial", 24, bold=True)

running = True
while running:
    screen.fill((255, 255, 255)) # Белый чистый фон

    # 1. Рисуем плейлист справа
    pygame.draw.rect(screen, (245, 245, 245), (550, 0, 450, HEIGHT)) # Серый фон для списка
    title_text = font_bold.render("UP NEXT", True, (100, 100, 100))
    screen.blit(title_text, (580, 50))

    for i, track in enumerate(player.playlist):
        name = os.path.basename(track).replace(".mp3", "").replace("_", " ").title()
        color = (255, 45, 85) if i == player.current_index else (50, 50, 50) # Розовый Apple-цвет для активного
        
        track_surf = font_list.render(f"{i+1}. {name}", True, color)
        screen.blit(track_surf, (580, 120 + i * 50))

    # 2. Рисуем корпус плеера слева
    screen.blit(player_bg, (25, 25))

    # 3. Рисуем обложку внутри нового скина
    # Координаты для твоего нового фото (примерно центр белого окна)
    current_cover = player.get_current_cover()
    cover_res = pygame.transform.scale(current_cover, (250, 230)) 
    screen.blit(cover_res, (150, 130)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()

    pygame.display.flip()

pygame.quit()