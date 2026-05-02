import pygame

def draw_pencil(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)

def draw_rect(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
    pygame.draw.rect(surface, color, rect, size)

def draw_circle(surface, color, start, end, size):
    radius = int(((end[0]-start[0])**2 + (end[1]-start[1])**2)**0.5)
    pygame.draw.circle(surface, color, start, radius, size)

def flood_fill(surface, x, y, new_color):
    target = surface.get_at((x,y))
    if target == new_color:
        return

    w,h = surface.get_size()
    stack = [(x,y)]

    while stack:
        px,py = stack.pop()

        if surface.get_at((px,py)) == target:
            surface.set_at((px,py), new_color)

            if px>0: stack.append((px-1,py))
            if px<w-1: stack.append((px+1,py))
            if py>0: stack.append((px,py-1))
            if py<h-1: stack.append((px,py+1))