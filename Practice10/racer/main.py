import pygame, random
from player import Player
from coin import Coin
from enemy import Enemy
pygame.init()
W,H=400,600
screen=pygame.display.set_mode((W,H))
font=pygame.font.SysFont(None,30)
big=pygame.font.SysFont(None,45)
clock=pygame.time.Clock()
player=Player()
enemy=Enemy()
coins=[]
score=0
menu=True
run=True
while run:
    while menu:
        screen.fill((0,0,0))
        screen.blit(big.render('RACER',1,(255,255,255)),(140,200))
        screen.blit(font.render('Press SPACE',1,(255,255,255)),(135,260))
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type==pygame.QUIT: run=False; menu=False
            if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
                menu=False
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
    keys=pygame.key.get_pressed()
    player.move(keys)
    enemy.update()
    if random.randint(1,40)==1:
        coins.append(Coin())
    for c in coins[:]:
        c.update()
        if c.rect().colliderect(player.rect()):
            score+=1; coins.remove(c)
        elif c.y>H:
            coins.remove(c)
    if enemy.rect().colliderect(player.rect()):
        screen.fill((0,0,0))
        screen.blit(big.render('GAME OVER',1,(255,0,0)),(95,250))
        pygame.display.flip()
        pygame.time.delay(2000)
        run=False
    screen.fill((50,50,50))
    player.draw(screen)
    enemy.draw(screen)
    for c in coins: c.draw(screen)
    screen.blit(font.render(f'Coins: {score}',1,(255,255,255)),(280,10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()