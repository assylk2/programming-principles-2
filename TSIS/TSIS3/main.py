import pygame
from racer import RacerGame
from ui import *
from persistence import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500,700))
clock = pygame.time.Clock()

state = "menu"
username = ""
selected = load_settings()["selected_car"]
leaderboard = load_leaderboard()

game = RacerGame(screen, selected)

play_btn = Button("PLAY",150,300,200,50)
garage_btn = Button("GARAGE",150,360,200,50)
leader_btn = Button("LEADERBOARD",150,420,200,50)
quit_btn = Button("QUIT",150,480,200,50)

again_btn = Button("AGAIN",150,320,200,50)
menu_btn = Button("MENU",150,380,200,50)
save_btn = Button("SAVE",150,440,200,50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

            if play_btn.is_clicked(event) and username != "":
                game = RacerGame(screen, selected)
                state = "game"

            if garage_btn.is_clicked(event):
                state = "garage"

            if leader_btn.is_clicked(event):
                leaderboard = load_leaderboard()
                state = "leaderboard"

            if quit_btn.is_clicked(event):
                running = False

        elif state == "game":
            if game.game_over:
                state = "game_over"

        elif state == "game_over":
            if again_btn.is_clicked(event):
                game = RacerGame(screen, selected)
                state = "game"

            if menu_btn.is_clicked(event):
                state = "menu"

            if save_btn.is_clicked(event):
                add_score(username, game.score)
                leaderboard = load_leaderboard()
                state = "leaderboard"

        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    state = "menu"

        elif state == "garage":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 3
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 3
                if event.key == pygame.K_RETURN:
                    save_settings(selected)
                    state = "menu"

    # DRAW
    if state == "menu":
        draw_menu(screen, username)
        play_btn.draw(screen)
        garage_btn.draw(screen)
        leader_btn.draw(screen)
        quit_btn.draw(screen)

    elif state == "game":
        game.update()
        game.draw()

    elif state == "game_over":
        draw_game_over(screen, game.score)
        again_btn.draw(screen)
        menu_btn.draw(screen)
        save_btn.draw(screen)

    elif state == "leaderboard":
        draw_leaderboard(screen, leaderboard)

    elif state == "garage":
        screen.fill((0,0,0))
        for i in range(3):
            img = pygame.transform.scale(
                pygame.transform.rotate(pygame.image.load(f"assets/car{i+1}.png"),90),
                (60,120)
            )
            x = 100 + i*120
            screen.blit(img,(x,300))

            if i == selected:
                pygame.draw.rect(screen,(255,255,0),(x,300,60,120),3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()