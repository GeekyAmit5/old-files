import time
import math
import random
import pygame


pygame.init()
width = 500
height = 500
column = 10
row = 10
pygame.display.set_caption("Chain Reaction")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grid = [[(0, 0) for x in range(column)] for y in range(row)]
ai = 1
human = 2
turn = ai
color = red


def drawGrid(color, row, column):
    for i in range(1, column):
        pygame.draw.line(win, color,
                         (i * width / column, 0), (i * width / column, height))
    for i in range(1, row):
        pygame.draw.line(win, color,
                         (0, i * height / row), (width, i * height / row))


def opponent(turn):
    if turn == ai:
        return human
    return ai


def changeColor(color):
    if color == red:
        return green
    return red


def popup(x, y, n):
    if not grid[x][y][0]:
        grid[x][y] = (turn, 0)
        colorIt(x, y, color, 1)
        return True
    for i in range(1, n):
        if grid[x][y][0]:
            grid[x][y] = (turn, i+1)
            colorIt(x, y, color, grid[1][x][y])
            return True
    grid[x][y] = (0, 0)
    colorIt(x, y)
    # pygame.mixer.Sound("laser.wav").play()
    return False


def main(run):
    global grid
    drawGrid(color, row, column)
    clock = pygame.time.Clock()
    q = []
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if not q and event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y = my * row // height, mx * column // width
                if grid[x][y][0] != opponent(turn):
                    q.append((x, y))
        if q:
            x, y = q[0]
            if (x == 0 or x == row-1) and (y == 0 or y == column-1):
                if not popup(x, y, 1):
                    q.append((x + pow(-1, x), y))
                    q.append((x, y + pow(-1, y)))
                if x == 0 or y == 0 or x == row-1 or y == column-1:
                    if not popup(x, y, 2):
                        if y == 0 or y == column-1:
                            q.append((x + 1, y))
                            q.append((x - 1, y))
                            q.append((x, y + pow(-1, y)))
                        else:
                            q.append((x, y + 1))
                            q.append((x, y - 1))
                            q.append((x + pow(-1, x), y))
                if not popup(x, y, 3):
                    q.append((x + 1, y))
                    q.append((x - 1, y))
                    q.append((x, y + 1))
                    q.append((x, y - 1))
        pygame.display.update()
    pygame.quit()


main(True)
