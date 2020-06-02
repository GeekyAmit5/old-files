import math


def isColorable(ver, col):
    for i in adjList[ver]:
        try:
            if ans[i] == col:
                return False
        except:
            pass
    return True


def color():
    global ans
    for i in vertices:
        if len(ans) <= i:
            for j in colors:
                if isColorable(i, j):
                    ans.append(j)
                    color()
                    ans.pop()
            return
    print("Coloring Scheme".ljust(20), ":", ans)
    print("Chromatic Number".ljust(20), ":", len(set(ans)))
    exit()


n = 10
vertices = [x for x in range(n)]  # vertices
# C4
# adjList = [[1, 3], [2, 0], [3, 1], [0, 2]]     # adjacency list
# K4
# adjList = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
# Petersen
adjList = [[4, 6, 1], [0, 7, 2], [1, 8, 3], [2, 4, 9], [0, 3, 5],
           [4, 7, 8], [0, 8, 9], [1, 5, 9], [2, 6, 5], [3, 6, 7]]  # n=10

ans = []
colors = []
i = 0
while True:
    colors.append(i)
    color()
    i += 1
