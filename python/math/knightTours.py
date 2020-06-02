import numpy as np

row = 3
column = 4


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
        total += 1
        print("Tour :", total)
        print(np.matrix(grid), "\n")
        fh.write("Tour : "+str(total)+"\n"+str(np.matrix(grid))+"\n\n")
        return
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 0 and isPossible(x, y, i, j):
                num += 1
                grid[i][j] = num
                tour(i, j)
                grid[i][j] = 0
                num -= 1


fh = open("knightTours.txt", "w")
total = 0
grid = [[0 for x in range(column)]for y in range(row)]
num = 1
for i in range(row):
    for j in range(column):
        grid[i][j] = num
        tour(i, j)
        grid[i][j] = 0
print("Total :", total)
fh.write("Total : "+str(total))
fh.close()
