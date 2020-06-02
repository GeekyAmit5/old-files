import math


def isColorable(ver, col):
    for i in adjList[ver]:
        if len(ans) < i:
            continue
        if ans[i] == col:
            return False
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
    print(ans)
    # exit()


n = 4
vertices = [x for x in range(n)]  # vertices
adjList = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]     # adjacency list
# adjList = [[1, 2], [0, 2], [0, 1]]
colors = [x for x in range(5)]
ans = []
color()
