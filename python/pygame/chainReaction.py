import time
import math
import random
import pygame

pygame.init()
width = 500
height = 500
row = 10
column = 10
pygame.display.set_caption("Chain Reaction")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
grid = [[random.randint(1, 2) for x in range(column)] for y in range(row)]
dgrid = [[random.randint(1, 3) for x in range(column)] for y in range(row)]
# grid = [[0 for x in range(column)] for y in range(row)]
# dgrid = [[0 for x in range(column)] for y in range(row)]
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


def convert(x, y):
    return [y * row // height, x * column // width]


def colorIt(x, y, color=black, n=0):
    if n == 0:
        pygame.draw.rect(win, color, (y * width / column, x *
                                      height / row, width / column, height / row))
        return
    r = 3 * row
    c = 3 * column
    x = 3 * x
    y = 3 * y
    if n > 0:
        pygame.draw.rect(win, color, (y * width / c, x *
                                      height / r, width / c, height / r))
    x += 1
    y += 1
    if n > 1:
        pygame.draw.rect(win, color, (y * width / c, x *
                                      height / r, width / c, height / r))
    x += 1
    y += 1
    if n > 2:
        pygame.draw.rect(win, color, (y * width / c, x *
                                      height / r, width / c, height / r))


def popup(x, y):
    # global turn,color,grid,dgrid
    if (x == 0 or x == row - 1) and (y == 0 or y == column - 1):
        if dgrid[x][y] < 1:
            grid[x][y] = turn
            dgrid[x][y] += 1
            colorIt(x, y, color, dgrid[x][y])
        else:
            dgrid[x][y] = 0
            grid[x][y] = 0
            colorIt(x, y)
            grid[x + pow(-1, x)][y] = turn
            grid[x][y + pow(-1, y)] = turn
            dgrid[x + pow(-1, x)][y] += 1
            dgrid[x][y + pow(-1, y)] += 1
            colorIt(x + pow(-1, x), y, color, dgrid[x + pow(-1, x)][y])
            colorIt(x, y + pow(-1, y), color, dgrid[x][y + pow(-1, y)])
        return

    if x == 0 or y == 0 or x == row - 1 or y == column - 1:
        if dgrid[x][y] < 2:
            grid[x][y] = turn
            dgrid[x][y] += 1
            colorIt(x, y, color, dgrid[x][y])
        else:
            dgrid[x][y] = 0
            grid[x][y] = 0
            colorIt(x, y)
            if y == 0 or y == column - 1:
                grid[x + 1][y] = turn
                grid[x - 1][y] = turn
                grid[x][y + pow(-1, y)] = turn
                dgrid[x + 1][y] += 1
                dgrid[x - 1][y] += 1
                dgrid[x][y + pow(-1, y)] += 1
                colorIt(x + 1, y, color, dgrid[x + 1][y])
                colorIt(x - 1, y, color, dgrid[x - 1][y])
                colorIt(x, y + pow(-1, y), color, dgrid[x][y + pow(-1, y)])
            else:
                grid[x][y + 1] = turn
                grid[x][y - 1] = turn
                grid[x + pow(-1, x)][y] = turn
                dgrid[x][y + 1] += 1
                dgrid[x][y - 1] += 1
                dgrid[x + pow(-1, x)][y] += 1
                colorIt(x, y + 1, color, dgrid[x][y + 1])
                colorIt(x, y - 1, color, dgrid[x][y - 1])
                colorIt(x + pow(-1, x), y, color, dgrid[x + pow(-1, x)][y])
        return

    if dgrid[x][y] < 3:
        grid[x][y] = turn
        dgrid[x][y] += 1
        colorIt(x, y, color, dgrid[x][y])
    else:
        dgrid[x][y] = 0
        grid[x][y] = 0
        colorIt(x, y)
        grid[x + 1][y] = turn
        grid[x - 1][y] = turn
        grid[x][y + 1] = turn
        grid[x][y - 1] = turn
        dgrid[x + 1][y] += 1
        dgrid[x - 1][y] += 1
        dgrid[x][y + 1] += 1
        dgrid[x][y - 1] += 1
        colorIt(x + 1, y, color, dgrid[x + 1][y])
        colorIt(x - 1, y, color, dgrid[x - 1][y])
        colorIt(x, y + 1, color, dgrid[x][y + 1])
        colorIt(x, y - 1, color, dgrid[x][y - 1])


t = True


def iswinner(turn):
    global t
    if t:
        t = False
        return t
    for i in range(row):
        for j in range(column):
            if grid[i][j] == opponent(turn):
                return
    time.sleep(1)
    msg = pygame.font.SysFont(None, 50).render("GAME OVER", True, (255, 0, 0))
    win.fill((255, 255, 255))
    win.blit(msg, [100, 100])
    pygame.display.update()
    time.sleep(1)
    exit()


def opponent(turn):
    if turn == ai:
        return human
    return ai


def changeColor(color):
    if color == red:
        return green
    return red


def play(l):
    global turn, color
    if grid[l[0]][l[1]] != opponent(turn):
        popup(l[0], l[1])
        go = True
        while go:
            go = False
            for x in range(row):
                for y in range(column):
                    a = (x == 0 or x == row - 1) and (y ==
                                                      0 or y == column - 1) and dgrid[x][y] > 1
                    b = (x == 0 or y == 0 or x == row - 1 or y ==
                         column - 1) and dgrid[x][y] > 2
                    c = dgrid[x][y] > 3
                    if a or b or c:
                        go = True
                        popup(x, y)
            pygame.time.delay(200)
            drawGrid(color, row, column)
            pygame.display.update()
            iswinner(turn)
        color = changeColor(color)
        turn = opponent(turn)


def main(run):
    drawGrid(color, row, column)
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                colorIt(i, j, color, dgrid[i][j])
            if grid[i][j] == 2:
                colorIt(i, j, changeColor(color), dgrid[i][j])
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                play(convert(mx, my))
        drawGrid(color, row, column)
        pygame.display.update()
    pygame.quit()


main(True)


# def popup(x, y):
#     drawGrid(color, row, column)
#     pygame.display.update()
#     time.sleep(0.05)
#     # isWinner(turn)
#     if (x == 0 or x == row-1) and (y == 0 or y == column-1):
#         if not mark(x, y, 1):
#             popup(x + pow(-1, x), y)
#             popup(x, y + pow(-1, y))
#         return

#     if x == 0 or y == 0 or x == row-1 or y == column-1:
#         if not mark(x, y, 2):
#             if y == 0 or y == column-1:
#                 popup(x + 1, y)
#                 popup(x - 1, y)
#                 popup(x, y + pow(-1, y))
#             else:
#                 popup(x, y + 1)
#                 popup(x, y - 1)
#                 popup(x + pow(-1, x), y)
#         return

#     if not mark(x, y, 3):
#         popup(x + 1, y)
#         popup(x - 1, y)
#         popup(x, y + 1)
#         popup(x, y - 1)


# def mark(x, y, n):
#     if grid[x][y] == " ":
#         grid[x][y] = turn
#         colorIt(x, y, color, 1)
#         return True
#     for i in range(1, n):
#         if grid[x][y] == turn * i or grid[x][y] == opponent(turn) * i:
#             grid[x][y] = turn * (i + 1)
#             colorIt(x, y, color, i + 1)
#             return True
#     grid[x][y] = " "
#     colorIt(x, y)
#     return False


# def play(l):
#     global turn, color
#     for i in range(1, 4):
#         if grid[l[0]][l[1]] == i * opponent(turn):
#             break
#     else:
#         popup(l[0], l[1])
#         turn = opponent(turn)
#         color = changeColor(color)
#         drawGrid(color, row, column)
#         pygame.display.update()


# def main(run):
#     drawGrid(color, row, column)
#     while run:
#         pygame.time.delay(100)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mx, my = pygame.mouse.get_pos()
#                 play(convert(mx, my))
#         pygame.display.update()
#     pygame.quit()


# main(True)


# def isValid(grid, playerMove, turn):
#     if playerMove.isnumeric():
#         playerMove = int(playerMove)
#         if playerMove in range(0, 100):
#             for i in range(1, 4):
#                 if grid[playerMove // 10][playerMove % 10] == i * opponent(turn):
#                     return False
#             else:
#                 return True
#     return False


# def computer(grid, turn):
#     while True:
#         x = rd.randint(0, 99)
#         if isValid(grid, str(x), turn):
#             return [x // 10, x % 10]


# def move(grid, gameMode, turn):
#     while True:
#         if gameMode:
#             playerMove = input("Player {} : ".format(turn))
#         else:
#             if turn == "X":
#                 cm = computer(grid, turn)
#                 print("Computer : {}{}".format(cm[0], cm[1]))
#                 return cm
#             else:
#                 playerMove = input("You : ")
#         if not isValid(grid, playerMove, turn):
#             print("Please enter a valid input")
#             continue
#         playerMove = int(playerMove)
#         return [playerMove // 10, playerMove % 10]


# def play(grid, gameMode, turn):
#     t = False
#     while True:
#         playerMove = move(grid, gameMode, turn)
#         popup(grid, playerMove[0], playerMove[1], turn)
#         printGrid(grid)
#         if winCheck(grid, turn) and t:
#             if gameMode:
#                 print("Player {} WIN!".format(turn))
#             else:
#                 if turn == "O":
#                     print("You WIN!")
#                 else:
#                     print("Comuter WIN!")
#             break
#         t = True
#         turn = opponent(turn)


# def start(gameMode, turn=rd.choice(["O", "X"])):
#     grid = [[" " for x in range(10)] for y in range(10)]
#     print("Start!")
#     printGrid(grid)
#     play(grid, gameMode, turn)
#     del grid
#     exitCode = input(
#         "Press 0 to Exit!\nPress 1 to change Game Mode\nPress any other key to Continue!")
#     if exitCode == "0":
#         quit()
#     if exitCode == "1":
#         gameMode = 1 - gameMode
#         print("Game Mode changed to", end=" ")
#         if gameMode:
#             print("Player X vs Player O")
#         else:
#             print("You vs Computer")
#     start(gameMode, opponent(turn))


# while True:
#     gameMode = input(
#         "Press 0 for You vs Computer\nPress 1 for Player X vs Player O\n")
#     if gameMode in ["0", "1"]:
#         gameMode = int(gameMode)
#         break


# start(gameMode)
