import time
import math
import random
import pygame


pygame.init()
width = 1300
height = 700
row = 20
column = 38
pygame.display.set_caption("Chain Reaction")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
grid = [[random.choice([" ","X", "XX", "XXX", "O", "OO", "OOO"])
         for x in range(column)] for y in range(row)]
# grid = [[" " for x in range(column)] for y in range(row)]
ai = "X"
human = "O"
turn = ai
color = red


def drawGrid(color, row, column):
    for i in range(1, column):
        pygame.draw.line(win, color,
                         (i * width / column, 0), (i * width / column, height))
    for i in range(1, row):
        pygame.draw.line(win, color,
                         (0, i * height / row), (width, i * height / row))


def convert(x, y):
    return [y * row // height, x * column // width]


def colorIt(x, y, color=black, n=0):
    pygame.draw.rect(win, black, (y * width / column, x *
                                  height / row, width / column, height / row))

    r = 3 * row
    c = 3 * column
    x = 3 * x+1
    y = 3 * y+1

    if n == 1:
        pygame.draw.ellipse(win, color, [y * width / c-3, x *
                                         height / r-3, width / c+6, height / r+6])
    if n == 2:
        pygame.draw.ellipse(win, color, [y * width / c-7, x *
                                         height / r, width / c+5, height / r+5])
        pygame.draw.ellipse(win, color, [y * width / c+7, x *
                                         height / r, width / c+5, height / r+5])
    if n == 3:
        pygame.draw.ellipse(win, color, [y * width / c, x *
                                         height / r-7, width / c+5, height / r+5])
        pygame.draw.ellipse(win, color, [y * width / c-7, x *
                                         height / r+7, width / c+5, height / r+5])
        pygame.draw.ellipse(win, color, [y * width / c+7, x *
                                         height / r+7, width / c+5, height / r+5])


def opponent(turn):
    if turn == ai:
        return human
    return ai


def changeColor(color):
    if color == red:
        return green
    return red


t = True


def isWinner(turn):
    global t
    if t:
        t = False
        return
    for i in range(row):
        for j in range(column):
            for k in range(3):
                if grid[i][j] == (k+1)*opponent(turn):
                    return
    msg = pygame.font.SysFont(None, 100).render("GAME OVER", True, white)
    win.blit(msg, [width//2-210, height//2-35])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()


def popup(x, y):
    drawGrid(color, row, column)
    pygame.display.update()
    # pygame.time.delay(round(314//math.sqrt(row*column)))
    isWinner(turn)
    if (x == 0 or x == row-1) and (y == 0 or y == column-1):
        if not mark(x, y, 1):
            popup(x + pow(-1, x), y)
            popup(x, y + pow(-1, y))
        return

    if x == 0 or y == 0 or x == row-1 or y == column-1:
        if not mark(x, y, 2):
            if y == 0 or y == column-1:
                popup(x + 1, y)
                popup(x - 1, y)
                popup(x, y + pow(-1, y))
            else:
                popup(x, y + 1)
                popup(x, y - 1)
                popup(x + pow(-1, x), y)
        return

    if not mark(x, y, 3):
        popup(x + 1, y)
        popup(x - 1, y)
        popup(x, y + 1)
        popup(x, y - 1)


def mark(x, y, n):
    if grid[x][y] == " ":
        grid[x][y] = turn
        colorIt(x, y, color, 1)
        return True
    for i in range(1, n):
        if grid[x][y] == turn * i or grid[x][y] == opponent(turn) * i:
            grid[x][y] = turn * (i + 1)
            colorIt(x, y, color, i + 1)
            return True
    grid[x][y] = " "
    colorIt(x, y)
    # pygame.mixer.Sound("laser.wav").play()
    return False


def nextTurn():
    global turn, color
    c = 0
    while True:
        i = 3 - c//100
        x = random.randint(0, row-1)
        y = random.randint(0, column-1)
        if grid[x][y] == i*turn:
            popup(x, y)
            break
        c += 1
        if c > 300 and grid[x][y] == " ":
            popup(x, y)
            break
    turn = opponent(turn)
    color = changeColor(color)
    drawGrid(color, row, column)
    pygame.display.update()


def play(l):
    global turn, color
    for i in range(1, 4):
        if grid[l[0]][l[1]] == i * opponent(turn):
            break
    else:
        popup(l[0], l[1])
        turn = opponent(turn)
        color = changeColor(color)
        drawGrid(color, row, column)
        pygame.display.update()
        nextTurn()


def main(run):
    drawGrid(color, row, column)
    clock = pygame.time.Clock()
    while run:
        pygame.time.delay(25)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                play(convert(mx, my))
        pygame.display.update()
    pygame.quit()


main(True)
