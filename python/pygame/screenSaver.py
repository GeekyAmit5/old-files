
import random as rd
import numpy as np
import math
import time
import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")

x = rd.randint(0, 450)
y = rd.randint(0, 450)
h = 50
w = 30
v = 0.3

t = True
s = True

run = True
while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x < 470 and t:
        x += v
    else:
        t = False
        x -= v
        if x < 0:
            t = True

    if y < 450 and s:
        y += v
    else:
        s = False
        y -= v
        if y < 0:
            s = True

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))
    pygame.display.update()

pygame.quit()


# keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= v
#     if keys[pygame.K_RIGHT] and x < 400:
#         x += v
