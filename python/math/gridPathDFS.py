import time
import pygame
import math
import random
import sys

sys.setrecursionlimit(100000)


def drawGrid(row, column, color=(0, 0, 0)):
    for i in range(1, column):
        pygame.draw.line(win, color,
                         (round(i * width / column), 0), (round(i * width / column), height))
    for i in range(1, row):
        pygame.draw.line(win, color,
                         (0, round(i * height / row)), (width, round(i * height / row)))


def writeIt(x, y, n, color=(0, 0, 0)):
    r = 3 * row
    c = 3 * column
    x = 3 * x+1
    y = 3 * y+1
    score = pygame.font.Font(
        'freesansbold.ttf', 10).render(str(n), True, color)
    win.blit(score, (round(y * width / c+3), round(x * height / r)))


def colorIt(x, y, color=(0, 0, 0)):
    pygame.draw.rect(win, color, (round(3 + y * width / column), round(3 + x *
                                                                       height / row), round(width / column - 4), round(height / row - 4)))


def isPossible(x, y, a, b):
    if a == 2+x or b == 2 + y or a == x-2 or b == y-2:
        if a == 1+x or b == 1 + y or a == x-1 or b == y-1:
            return True
    return False


def tour(x, y):
    global grid
    # pygame.time.delay(100)
    if (x, y) == destination:
        time.sleep(1)
        exit()
    else:
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and isPossible(x, y, i, j):
                    grid[i][j] = 1
                    colorIt(i, j, green)
                    pygame.display.update()
                    tour(i, j)
                    grid[i][j] = 0
                    colorIt(i, j, red)
                    pygame.display.update()


pygame.init()
width = 700
height = 700
row = 50
column = 50
pygame.display.set_caption("Grid Path")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
source = (random.randint(0, 49), random.randint(0, 49))
destination = (random.randint(0, 49), random.randint(0, 49))
grid = [[0 for x in range(column)] for y in range(row)]
win.fill(white)
drawGrid(row, column)
grid[source[0]][source[1]] = 1
colorIt(source[0], source[1], blue)
colorIt(destination[0], destination[1], black)
pygame.display.update()
tour(source[0], source[1])
