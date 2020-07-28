# to place 8 queens on chessboard so that no queen attack each other
import pygame


def doIt(x, y, n):
    grid[x][y] -= 4*n

    for i in range(order):
        grid[i][y] += n
        grid[x][i] += n

    if x+y < order:
        for i in range(x+y+1):
            grid[x+y-i][i] += n
    else:
        for i in range(2*order-x-y-1):
            grid[order-1-i][i-order+x+y+1] += n
    x -= y
    if x >= 0:
        for i in range(order - x):
            grid[x+i][i] += n
    else:
        for i in range(order + x):
            grid[i][i-x] += n


def place():
    global grid, num
    if num == order:
        pygame.time.delay(500)
    else:
        for i in range(order):
            if not grid[num][i]:
                num += 1
                grid[num-1][i] = num
                # pygame.time.delay(100)
                win.blit(queen, (3 + i * width / order, 3 + (num-1) *
                                 height / order, width / order - 3, height / order - 3))
                pygame.display.update()
                doIt(num-1, i, -1)
                place()
                # pygame.time.delay(100)
                num -= 1
                grid[num][i] = 0
                colorIt(num, i)
                pygame.display.update()
                doIt(num, i, 1)


def colorIt(x, y, color=(0, 0, 0)):
    pygame.draw.rect(win, color, (3 + y * width / order, 3 + x *
                                  height / order, width / order - 3, height / order - 3))


def drawGrid(order, color=(255, 255, 255)):
    for i in range(1, order):
        pygame.draw.line(win, color,
                         (i * width / order, 0), (i * width / order, height), 2)
    for i in range(1, order):
        pygame.draw.line(win, color,
                         (0, i * height / order), (width, i * height / order), 2)


pygame.init()
width = 800
height = 700
order = 8
pygame.display.set_caption("8 Queen's")
win = pygame.display.set_mode((width, height))
grid = [[0 for x in range(order)] for y in range(order)]
num = 0
queen = pygame.image.load("python/math/gui/8queens/queen.png")
drawGrid(order)
pygame.display.update()
place()
