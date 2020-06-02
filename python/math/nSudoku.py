import time
import pygame
import numpy as np
import math
import sys

sys.setrecursionlimit(10000)

pygame.init()
width = 1300
height = 700
order = 36
pygame.display.set_caption("Sudoku")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# generate a sudoku
grid = [[0 for x in range(order)]for y in range(order)]
total = 0


def isPossible(x, y, n):
    for i in range(order):
        if grid[x][i] == n or grid[i][y] == n:
            return False
    for i in range(round(math.sqrt(order))):
        for j in range(round(math.sqrt(order))):
            if grid[(x//round(math.sqrt(order)))*round(math.sqrt(order))+i][(y//round(math.sqrt(order)))*round(math.sqrt(order))+j] == n:
                return False
    return True


def writeIt(color, x, y, n):
    r = 3 * order
    c = 3 * order
    x = 3 * x+1
    y = 3 * y+1
    score = pygame.font.Font(
        'freesansbold.ttf', 20).render(str(n), True, color)
    win.blit(score, (y * width / c+3, x * height / r))


def colorIt(color, x, y):
    # pygame.time.delay(100)
    pygame.draw.rect(win, color, (3 + y * width / order, 3 + x *
                                  height / order, width / order - 4, height / order - 4))


def solve():
    global grid, total
    for i in range(order):
        for j in range(order):
            if grid[i][j] == 0:
                for n in range(1, order+1):
                    if isPossible(i, j, n):
                        grid[i][j] = n
                        colorIt(green, i, j)
                        writeIt(black, i, j, grid[i][j])
                        pygame.display.update()
                        solve()
                        grid[i][j] = 0
                        colorIt(red, i, j)
                        pygame.display.update()
                return
    print(np.matrix(grid), "\n")
    total += 1
    print("Total :", total, end="\n\n")
    # time.sleep(1)
    # pygame.quit()


def drawGrid(color, order):
    for i in range(1, order):
        if not i % round(math.sqrt(order)):
            pygame.draw.line(win, color, (i * width / order, 0),
                             (i * width / order, height), 4)
        else:
            pygame.draw.line(win, color,
                             (i * width / order, 0), (i * width / order, height), 2)
    for i in range(1, order):
        if not i % round(math.sqrt(order)):
            pygame.draw.line(win, color,
                             (0, i * height / order), (width, i * height / order), 4)
        else:
            pygame.draw.line(win, color,
                             (0, i * height / order), (width, i * height / order), 2)


def main():
    win.fill(white)
    drawGrid(black, order)
    for i in range(order):
        for j in range(order):
            if grid[i][j]:
                writeIt(blue, i, j, grid[i][j])
    pygame.display.update()


main()
solve()
