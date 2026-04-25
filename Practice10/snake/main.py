import pygame
import random
import os

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 700, 500
CELL = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32, bold=True)
big_font = pygame.font.SysFont("arial", 48, bold=True)

# ---------------- COLORS ----------------
BG = (230, 220, 150)
BORDER = (160, 140, 70)
BODY = (70, 170, 90)
BODY_DARK = (50, 130, 70)
TEXT = (0, 0, 0)
RED = (220, 60, 60)

# ---------------- PATH ----------------
base = os.path.dirname(__file__)
assets = os.path.join(base, "assets")

# ---------------- IMAGES ----------------
head_img = pygame.image.load(os.path.join(assets, "head.png")).convert_alpha()
food_img = pygame.image.load(os.path.join(assets, "food.png")).convert_alpha()

head_img = pygame.transform.scale(head_img, (42, 42))
food_img = pygame.transform.scale(food_img, (25, 25))

# ---------------- BEST SCORE ----------------
best_score = 0

# ---------------- FUNCTIONS ----------------
def angle(dx, dy):
    base = 270   # change if needed
    if dx > 0:
        return base
    if dx < 0:
        return base + 180
    if dy < 0:
        return base + 90
    if dy > 0:
        return base - 90
    return base

def draw_body(x, y):
    pygame.draw.rect(screen, BODY, (x, y, CELL, CELL), border_radius=8)
    pygame.draw.rect(screen, BODY_DARK, (x+3, y+3, CELL-6, CELL-6), 2, border_radius=8)

def new_food(snake):
    while True:
        x = random.randrange(25, WIDTH - 25, CELL)
        y = random.randrange(125, HEIGHT - 25, CELL)
        if (x, y) not in snake:
            return (x, y)

def reset_game():
    snake = [(250, 250), (225, 250), (200, 250)]
    dx, dy = CELL, 0
    score = 0
    level = 1
    speed = 10
    food = new_food(snake)
    return snake, dx, dy, score, level, speed, food

def draw_scene(snake, food, score, level, dx, dy):
    screen.fill(BORDER)
    pygame.draw.rect(screen, BG, (15, 15, WIDTH - 30, HEIGHT - 30))

    # Text
    screen.blit(font.render(f"Score: {score}", True, TEXT), (30, 20))
    screen.blit(font.render(f"Level: {level}", True, TEXT), (30, 55))
    screen.blit(font.render(f"Best: {best_score}", True, TEXT), (500, 20))

    # Body
    for part in snake[1:]:
        draw_body(part[0], part[1])

    # Head
    hx, hy = snake[0]
    rotated = pygame.transform.rotate(head_img, angle(dx, dy))
    rect = rotated.get_rect(center=(hx + CELL//2, hy + CELL//2))
    screen.blit(rotated, rect.topleft)

    # Food
    screen.blit(food_img, food)

def game_over(score):
    screen.fill((20, 20, 20))
    screen.blit(big_font.render("GAME OVER", True, RED), (220, 180))
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (290, 250))
    screen.blit(font.render("Press R to Restart", True, (255,255,255)), (220, 320))
    pygame.display.flip()

# ---------------- START ----------------
snake, dx, dy, score, level, speed, food = reset_game()

running = True
gameover = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

        if gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                snake, dx, dy, score, level, speed, food = reset_game()
                gameover = False

    if not gameover:
        head = (snake[0][0] + dx, snake[0][1] + dy)

        if (
            head[0] < 25 or head[0] >= WIDTH - 25 or
            head[1] < 125 or head[1] >= HEIGHT - 25 or
            head in snake[:-1]
        ):
            gameover = True
            if score > best_score:
                best_score = score
        else:
            snake.insert(0, head)

            if head == food:
                score += 1
                if score % 4 == 0:
                    level += 1
                    speed += 2
                food = new_food(snake)
            else:
                snake.pop()

            draw_scene(snake, food, score, level, dx, dy)
            pygame.display.flip()
            clock.tick(speed)
    else:
        game_over(score)

pygame.quit()