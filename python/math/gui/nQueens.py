# to place n queens on n by n board so that no queen attack each other

import time
import numpy as np


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
    global grid, num, total
    if num == order:
        sol = [[0 for x in range(order)] for y in range(order)]
        for i in range(order):
            for j in range(order):
                if grid[i][j] > 0:
                    sol[i][j] = grid[i][j]
        print(np.matrix(sol), "\n")
        total += 1
        # exit()
    else:
        for i in range(order):
            if not grid[num][i]:
                num += 1
                grid[num-1][i] = num
                doIt(num-1, i, -1)
                place()
                num -= 1
                grid[num][i] = 0
                doIt(num, i, 1)


order = int(input("How Many Queens? "))
grid = [[0 for x in range(order)] for y in range(order)]
num = 0
total = 0
t0 = time.time()
place()
t1 = time.time()
print("Total :", total)
print("Time  :", t1-t0)
