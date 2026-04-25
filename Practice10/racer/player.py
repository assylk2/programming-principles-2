import pygame
class Player:
    def __init__(self):
        self.x=180; self.y=500
        self.img=pygame.image.load('assets/player.png')
        self.img=pygame.transform.scale(self.img,(40,60))
    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x-=5
        if keys[pygame.K_RIGHT]: self.x+=5
        self.x=max(0,min(360,self.x))
    def draw(self, screen):
        screen.blit(self.img,(self.x,self.y))
    def rect(self):
        return pygame.Rect(self.x,self.y,40,60)