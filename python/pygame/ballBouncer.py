
import random as rd
import numpy as np
import math
import time
import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# containner
x = 300
y = 570
h = 20
w = 200
v = 3

# ball
t = True
s = True
ballX = 0
ballY = 0
ballH = 10
ballW = 10
ballV = 5


def collision():
    return pow(((ballX - x-50) ** 2 + (ballY - y-10) ** 2), 0.5) < 50 or pow(((ballX - x-150) ** 2 + (ballY - y-10) ** 2), 0.5) < 50


def show_score(score, x, y):
    score = pygame.font.Font('freesansbold.ttf', 20).render(
        "Score : " + str(score), True, (255, 255, 255))
    win.blit(score, (x, y))


def main():
    run = True
    global ballX, ballY, t, s, x, y, h, w, ballV, v, ballH
    ballX = rd.randint(0, 100)
    ballY = rd.randint(0, 100)
    score = 0
    while run:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                x = mx
        if ballX < 780 and t:
            ballX += ballV
        else:
            t = False
            ballX -= ballV
            if ballX < 0:
                t = True
        if s:
            ballY += ballV
        else:
            if ballY < 5:
                s = True
        if ballY > 620:
            pygame.time.delay(1000)
            main()
        if collision() or not s:
            ballY -= ballV
            s = False
            score += 1
        win.fill((0, 0, 0))
        show_score(score, 10, 10)
        pygame.draw.rect(win, (255, 0, 0), (x, y, w, h))
        pygame.draw.rect(win, (255, 255, 255), (ballX, ballY, ballW, ballH))
        pygame.display.update()
    pygame.quit()


main()
