import pygame
import datetime
import os
from tools import *

pygame.init()

WIDTH, HEIGHT = 1100, 700
TOOLBAR_W = 110
COLORBAR_H = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint FINAL (icons folder)")

clock = pygame.time.Clock()

# 📦 base path
BASE_DIR = os.path.dirname(__file__)
ICON_DIR = os.path.join(BASE_DIR, "assets", "icons")

# 🧠 tools (иконкалармен сәйкес болуы керек)
tools = [
    "pencil", "brush",
    "eraser", "fill",
    "picker", "zoom",
    "line", "rect",
    "ellipse", "text"
]

# 🎨 load icons
icons = {}
for t in tools:
    path = os.path.join(ICON_DIR, f"{t}.png")
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.smoothscale(img, (30, 30))
    icons[t] = img

# 🎨 canvas
canvas = pygame.Surface((WIDTH-TOOLBAR_W, HEIGHT-COLORBAR_H))
canvas.fill((255,255,255))

# 🎨 colors
colors = [
    (0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),
    (255,255,0),(0,255,255),(255,0,255)
]
color = (0,0,0)

# 🧰 toolbar buttons
TOOL_SIZE = 50
buttons = []

for i, t in enumerate(tools):
    col = i % 2
    row = i // 2
    x = 5 + col*(TOOL_SIZE+5)
    y = 5 + row*(TOOL_SIZE+5)
    rect = pygame.Rect(x, y, TOOL_SIZE, TOOL_SIZE)
    buttons.append((t, rect))

# 🧠 state
tool = "pencil"
drawing = False
start = None
last = None
brush = 3

# 🔤 text
font = pygame.font.SysFont(None, 30)
typing = False
text = ""
text_pos = (0,0)

running = True
while running:
    screen.fill((180,180,180))

    # canvas
    screen.blit(canvas, (TOOLBAR_W, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1: brush = 2
            if event.key == pygame.K_2: brush = 5
            if event.key == pygame.K_3: brush = 10

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                name = datetime.datetime.now().strftime("img_%H%M%S.png")
                pygame.image.save(canvas, name)

            if typing:
                if event.key == pygame.K_RETURN:
                    canvas.blit(font.render(text, True, color), text_pos)
                    typing = False

                elif event.key == pygame.K_ESCAPE:
                    typing = False

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode

        # mouse down
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # toolbar
            for t, rect in buttons:
                if rect.collidepoint(x, y):
                    tool = t

            # colors
            for i, c in enumerate(colors):
                rect = pygame.Rect(TOOLBAR_W + i*50, HEIGHT-COLORBAR_H+10, 40, 40)
                if rect.collidepoint(x, y):
                    color = c

            # canvas
            if x > TOOLBAR_W and y < HEIGHT-COLORBAR_H:
                cx, cy = x - TOOLBAR_W, y

                if tool == "fill":
                    flood_fill(canvas, cx, cy, color)

                elif tool == "text":
                    typing = True
                    text = ""
                    text_pos = (cx, cy)

                else:
                    drawing = True
                    start = (cx, cy)
                    last = (cx, cy)

        # mouse up
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                x, y = event.pos
                cx, cy = x - TOOLBAR_W, y

                if tool == "line":
                    draw_line(canvas, color, start, (cx, cy), brush)

                elif tool == "rect":
                    draw_rect(canvas, color, start, (cx, cy), brush)

                elif tool == "ellipse":
                    draw_circle(canvas, color, start, (cx, cy), brush)

                drawing = False

        # motion
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                cx, cy = x - TOOLBAR_W, y

                if tool == "pencil":
                    draw_pencil(canvas, color, last, (cx, cy), brush)
                    last = (cx, cy)

                elif tool == "brush":
                    pygame.draw.circle(canvas, color, (cx, cy), brush)

                elif tool == "eraser":
                    pygame.draw.circle(canvas, (255,255,255), (cx, cy), brush*2)

    # toolbar draw
    pygame.draw.rect(screen, (200,200,200), (0,0,TOOLBAR_W,HEIGHT))

    for t, rect in buttons:
        pygame.draw.rect(screen, (230,230,230), rect)
        pygame.draw.rect(screen, (0,0,0), rect, 1)

        if t == tool:
            pygame.draw.rect(screen, (0,0,0), rect, 3)

        screen.blit(icons[t], icons[t].get_rect(center=rect.center))

    # color palette
    for i, c in enumerate(colors):
        rect = pygame.Rect(TOOLBAR_W + i*50, HEIGHT-COLORBAR_H+10, 40, 40)
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 1)

    # text preview
    if typing:
        screen.blit(font.render(text, True, color),
                    (text_pos[0]+TOOLBAR_W, text_pos[1]))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()