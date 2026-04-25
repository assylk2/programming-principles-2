import pygame
pygame.init()
W,H=800,600
screen=pygame.display.set_mode((W,H))
canvas=pygame.Surface((W,H))
canvas.fill((255,255,255))
clock=pygame.time.Clock()
color=(0,0,0)
tool='brush'
start=None
run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: run=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_r: tool='rect'
            if e.key==pygame.K_c: tool='circle'
            if e.key==pygame.K_e: tool='eraser'
            if e.key==pygame.K_b: tool='brush'
            if e.key==pygame.K_1: color=(255,0,0)
            if e.key==pygame.K_2: color=(0,255,0)
            if e.key==pygame.K_3: color=(0,0,255)
        if e.type==pygame.MOUSEBUTTONDOWN:
            start=e.pos
        if e.type==pygame.MOUSEBUTTONUP:
            end=e.pos
            if tool=='rect':
                rect=pygame.Rect(start,(end[0]-start[0],end[1]-start[1]))
                pygame.draw.rect(canvas,color,rect,2)
            if tool=='circle':
                radius=int(((end[0]-start[0])**2+(end[1]-start[1])**2)**0.5)
                pygame.draw.circle(canvas,color,start,radius,2)
    if pygame.mouse.get_pressed()[0]:
        pos=pygame.mouse.get_pos()
        if tool=='brush': pygame.draw.circle(canvas,color,pos,4)
        if tool=='eraser': pygame.draw.circle(canvas,(255,255,255),pos,10)
    screen.blit(canvas,(0,0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()