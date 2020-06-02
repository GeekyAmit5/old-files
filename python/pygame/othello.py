
import numpy as np
import random as rd

n = 4
grid = [[" " for x in range(n)] for y in range(n)]
grid[(n - 2) // 2][(n - 2) // 2] = grid[(n - 2) // 2 + 1][(n - 2) // 2 + 1] = "X"
grid[(n - 2) // 2][(n - 2) // 2+1] = grid[(n - 2) // 2+1][(n - 2) // 2] = "O"


def printGrid(grid):
    print()
    print("----"*len(grid))
    for i in range(len(grid)):
        print("|", end="")
        for j in range(len(grid)):
            print(" {} ".format(grid[i][j]), end="|")
        print()
        print("----"*len(grid))
    print()


def winCheck(grid):
    for i in range(n):
        for j in range(n):
            if grid == " ":
                return False
    return True


def opponent(turn):
    if turn == "X":
        return "O"
    return "X"


def totalCount(grid, turn):
    c = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == turn:
                c += 1
    return c


def game(grid, x, y, turn):
    grid[x][y] = turn
    for i in range(x, n):
        if i != x and grid[i][y] == opponent(turn):
            grid[i][y] = turn
        else:
            break
    for i in range(0, x):
        if grid[i][y] == opponent(turn):
            grid[i][y] = turn
        else:
            break
    for i in range(y, n):
        if i != y and grid[x][i] == opponent(turn):
            grid[x][i] = turn
        else:
            break
    for i in range(0, y):
        if grid[i][x] == opponent(turn):
            grid[i][x] = turn
        else:
            break

    for i in range(max(x, y), n):
        if i != x and grid[x+i][y+i] == opponent(turn):
            grid[x+i][y+i] = turn
        else:
            break
    for i in range(0, min(x, y)):
        if grid[x+i][y+i] == opponent(turn):
            grid[x+i][y+i] = turn
        else:
            break
    for i in range(0, max(x, y)):
        if i != x and grid[x+i][y+i] == opponent(turn):
            grid[x+i][y+i] = turn
        else:
            break
    for i in range(min(x, y), n):
        if grid[x+i][y+i] == opponent(turn):
            grid[x+i][y+i] = turn
        else:
            break


def move(turn):
    while True:
        playerMove = int(input("Player {} : ".format(turn)))
        if grid[playerMove // 10][playerMove % 10] == " ":
            return [playerMove // 10, playerMove % 10]


def play(turn=rd.choice(["O", "X"])):
    printGrid(grid)
    while winCheck(grid):
        turn = opponent(turn)
        playerMove = move(turn)
        game(grid, playerMove[0], playerMove[1], turn)
        printGrid(grid)
    else:
        print("Player {} WIN!".format(turn))


play()
