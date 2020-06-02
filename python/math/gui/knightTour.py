import time
import pygame
import numpy as np
import math


pygame.init()
width = 500
height = 500
row = 4
column = 5
pygame.display.set_caption("Knight Tour")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grid = [[0 for x in range(column)]for y in range(row)]
num = 1
total = 0


def drawGrid(color, row, column):
    for i in range(1, column):
        pygame.draw.line(win, color,
                         (math.floor(i * width / column), 0), (math.floor(i * width / column), height))
    for i in range(1, row):
        pygame.draw.line(win, color,
                         (0, math.floor(i * height / row)), (width, math.floor(i * height / row)))


def writeIt(color, x, y, n):
    r = 3 * row
    c = 3 * column
    x = 3 * x+1
    y = 3 * y+1
    score = pygame.font.Font(
        'freesansbold.ttf', 20).render(str(n), True, color)
    win.blit(score, (math.floor(y * width / c+3), math.floor(x * height / r)))


def colorIt(color, x, y):
    pygame.draw.rect(win, color, (math.floor(3 + y * width / column), math.floor(3 + x *
                                                                                 height / row), math.floor(width / column - 4), math.floor(height / row - 4)))


def isPossible(x, y, a, b):
    if a == 2+x or b == 2 + y or a == x-2 or b == y-2:
        if a == 1+x or b == 1 + y or a == x-1 or b == y-1:
            return True
    return False


def empty():
    global grid
    for i in range(row):
        for j in range(column):
            if not grid[i][j]:
                return False
    return True


def tour(x, y):
    global grid, num, total
    if empty():
        print(np.matrix(grid), "\n")
        total += 1
        time.sleep(1)
    else:
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and isPossible(x, y, i, j):
                    num += 1
                    grid[i][j] = num
                    colorIt(green, i, j)
                    writeIt(black, i, j, grid[i][j])
                    pygame.display.update()
                    tour(i, j)
                    grid[i][j] = 0
                    num -= 1
                    colorIt(red, i, j)
                    pygame.display.update()


def main(run):
    global num
    win.fill(white)
    drawGrid(black, row, column)
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for i in range(row):
            for j in range(column):
                colorIt(green, i, j)
                writeIt(black, i, j, num)
                pygame.display.update()
                grid[i][j] = num
                tour(i, j)
                grid[i][j] = 0
        print("Total : ", total)
        break
        pygame.display.update()
    pygame.quit()


main(True)
