import pygame
import time
import random
import numpy as np

pygame.init()
width = 1000
height = 600
row = 30
column = 50
pygame.display.set_caption("Game of Life")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
grid = [[0 for x in range(column)]for y in range(row)]
ngrid = [[0 for x in range(column)] for y in range(row)]


def pattern(n=0):
    if n == 0:  # random
        for i in range(row):
            for j in range(column):
                grid[i][j] = random.randint(0, 1)

    if n == 1:  # glider
        grid[0][0] = grid[0][2] = grid[1][1] = grid[1][2] = grid[2][1] = 1


pattern()


def drawGrid(color, row, column):
    for i in range(1, column):
        pygame.draw.line(win, color,
                         (i * width / column, 0), (i * width / column, height))
    for i in range(1, row):
        pygame.draw.line(win, color,
                         (0, i * height / row), (width, i * height / row))


def colorIt(color, x, y):
    pygame.draw.rect(win, color, (y * width / column, x *
                                  height / row, width / column, height / row))


def neigbhour(x, y):
    count = 0
    for i in range(3):
        for j in range(3):
            if (i != 1 or j != 1) and 0 < x + i <= row and 0 < y + j <= column and grid[x - 1 + i][y - 1 + j] == 1:
                count += 1
    return count


def gameOfLife():
    for i in range(row):
        for j in range(column):
            ngrid[i][j] = neigbhour(i, j)
    for i in range(row):
        for j in range(column):
            if (ngrid[i][j] < 2 or ngrid[i][j] > 3) and grid[i][j] == 1:
                grid[i][j] = 0
                colorIt(black, i, j)
            if ngrid[i][j] == 3 and not grid[i][j]:
                grid[i][j] = 1
                colorIt(yellow, i, j)


def main(run):
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                colorIt(yellow, i, j)
    drawGrid(white, row, column)
    pygame.display.update()
    clock = pygame.time.Clock()
    while run:
        # pygame.time.delay(50)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        gameOfLife()
        drawGrid(white, row, column)
        pygame.display.update()


main(True)
