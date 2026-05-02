import pygame

pygame.font.init()

FONT_BIG = pygame.font.Font(None, 60)
FONT_MED = pygame.font.Font(None, 35)

class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        color = (100,100,100) if self.rect.collidepoint(mouse) else (60,60,60)

        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2, border_radius=10)

        text = FONT_MED.render(self.text, True, (255,255,255))
        screen.blit(text, (self.rect.x+20, self.rect.y+10))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


def draw_menu(screen, username):
    screen.fill((10,0,20))
    title = FONT_BIG.render("RACER", True, (0,255,100))
    screen.blit(title,(150,80))

    label = FONT_MED.render("Username:", True, (255,255,255))
    screen.blit(label,(160,170))

    pygame.draw.rect(screen,(255,255,255),(150,210,200,40),2)
    txt = FONT_MED.render(username,True,(255,255,255))
    screen.blit(txt,(160,215))


def draw_game_over(screen, score):
    screen.fill((20,0,20))
    t = FONT_BIG.render("GAME OVER", True, (255,0,0))
    s = FONT_MED.render(f"Score: {score}", True, (255,255,255))
    screen.blit(t,(120,150))
    screen.blit(s,(180,230))


def draw_leaderboard(screen, data):
    screen.fill((0,0,0))
    title = FONT_BIG.render("TOP 5", True, (255,255,0))
    screen.blit(title,(150,40))

    box = pygame.Rect(50,120,400,400)
    pygame.draw.rect(screen,(50,50,50),box, border_radius=10)
    pygame.draw.rect(screen,(255,255,255),box,2, border_radius=10)

    y=150
    for i,e in enumerate(data):
        txt = FONT_MED.render(f"{i+1}. {e['name']} - {e['score']}",True,(255,255,255))
        screen.blit(txt,(80,y))
        y+=60