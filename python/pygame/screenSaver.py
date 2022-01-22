
import random as rd
import numpy as np
import math
import time
import pygame


class rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def display(self, x, y):
        pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))


pygame.init()
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

h = 80
w = 50
xv = 0.25
yv = 0.15
x = rd.randint(0, width-w)
y = rd.randint(0, height-h)

rect1 = rect(w, h)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0, 0, 0))
    rect1.display(x, y)
    x += xv
    y += yv
    if x > width - w or x < 0:
        xv = -xv
    if y > height - h or y < 0:
        yv = -yv
    # pygame.time.delay(1)
    pygame.display.update()

pygame.quit()
