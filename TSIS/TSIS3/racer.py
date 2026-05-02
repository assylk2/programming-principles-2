import pygame
import random

WIDTH, HEIGHT = 500, 700

class RacerGame:
    def __init__(self, screen, car_index):
        self.screen = screen
        self.game_over = False
        self.score = 0

        self.speed = 5
        self.level = 1

        self.coin_sound = pygame.mixer.Sound("assets/coin.wav")
        self.crash_sound = pygame.mixer.Sound("assets/crash.wav")

        self.car_imgs = [
            pygame.transform.scale(pygame.transform.rotate(pygame.image.load("assets/car1.png"),90),(60,120)),
            pygame.transform.scale(pygame.transform.rotate(pygame.image.load("assets/car2.png"),90),(60,120)),
            pygame.transform.scale(pygame.transform.rotate(pygame.image.load("assets/car3.png"),90),(60,120))
        ]

        self.car = self.car_imgs[car_index]
        self.x = 220
        self.y = 520

        self.enemy = pygame.transform.scale(
            pygame.transform.rotate(pygame.image.load("assets/enemy.png"),90),(60,120)
        )
        self.enemy_x = random.randint(150,350)
        self.enemy_y = -150

        self.coin_imgs = [
            pygame.transform.scale(pygame.image.load(f"assets/coin{i}.png"),(30,30))
            for i in range(1,7)
        ]
        self.coin_frame = 0
        self.coin_timer = 0
        self.coin_x = random.randint(150,350)
        self.coin_y = -50

        self.road = pygame.transform.scale(pygame.image.load("assets/road.png"),(500,700))
        self.road_y1 = 0
        self.road_y2 = -700

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]: self.x -= 5
        if keys[pygame.K_RIGHT]: self.x += 5
        self.x = max(150, min(350, self.x))

        self.level = self.score // 50 + 1
        self.speed = 5 + self.level

        self.road_y1 += self.speed
        self.road_y2 += self.speed

        if self.road_y1 >= HEIGHT: self.road_y1 = -HEIGHT
        if self.road_y2 >= HEIGHT: self.road_y2 = -HEIGHT

        self.enemy_y += self.speed + 1
        if self.enemy_y > HEIGHT:
            self.enemy_y = -150
            self.enemy_x = random.randint(150,350)

        self.coin_y += self.speed - 1
        self.coin_timer += 1

        if self.coin_timer % 7 == 0:
            self.coin_frame = (self.coin_frame + 1) % len(self.coin_imgs)

        if self.coin_y > HEIGHT:
            self.coin_y = -50
            self.coin_x = random.randint(150,350)

        player = pygame.Rect(self.x,self.y,60,120)
        enemy = pygame.Rect(self.enemy_x,self.enemy_y,60,120)
        coin = pygame.Rect(self.coin_x,self.coin_y,30,30)

        if player.colliderect(enemy):
            self.crash_sound.play()
            self.game_over = True

        if player.colliderect(coin):
            self.coin_sound.play()
            self.score += 10
            self.coin_y = -50

    def draw(self):
        self.screen.blit(self.road,(0,self.road_y1))
        self.screen.blit(self.road,(0,self.road_y2))
        self.screen.blit(self.car,(self.x,self.y))
        self.screen.blit(self.enemy,(self.enemy_x,self.enemy_y))
        self.screen.blit(self.coin_imgs[self.coin_frame],(self.coin_x,self.coin_y))