import math

n = 3
vertices = [node(x) for x in range(n)]
A = [[0, 1, 0], [1, 0, 1], [1, 0, 0]]


class node:
    def __init__(self, num):
        node.num = num
        node.color = None


def isColourable(ver, col):
    for i in range(n):
        if A[ver][i] and col == vertices[i].color:
            return False
    return True


def color():
    pass


vertices[0].color = 'yellow'
for i in range(n):
    if vertices[i]
