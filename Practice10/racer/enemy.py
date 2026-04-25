import pygame, random
class Enemy:
    def __init__(self):
        self.x=random.randint(0,360)
        self.y=-80
        self.w=40; self.h=60
        self.img=pygame.image.load('assets/enemy.png')
        self.img=pygame.transform.scale(self.img,(40,60))
    def update(self):
        self.y+=6
        if self.y>600:
            self.y=-80
            self.x=random.randint(0,360)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    def rect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)