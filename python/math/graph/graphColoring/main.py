import math
import pygame
import time


def drawGraph():
    for i in vertices:
        pygame.draw.circle(
            win, black, (coordinates[i][0], coordinates[i][1]), 10)
        for j in adjList[i]:
            pygame.draw.line(
                win, black, (coordinates[i][0], coordinates[i][1]), (coordinates[j][0], coordinates[j][1]), 3)



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
                    pygame.draw.circle(
                        win, j, (coordinates[i][0], coordinates[i][1]), 8)
                    pygame.display.update()
                    pygame.time.delay(25)
                    color()
                    ans.pop()
                    pygame.draw.circle(
                        win, black, (coordinates[i][0], coordinates[i][1]), 8)
                    pygame.display.update()
                    pygame.time.delay(25)
            return
    time.sleep(0.5)
    # exit()


pygame.init()
width = 1000
height = 600
pygame.display.set_caption("Graph Coloring")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
n = 10
vertices = [x for x in range(n)]  # vertices
adjList = [[4, 6, 1], [0, 7, 2], [1, 8, 3], [2, 4, 9], [0, 3, 5],
           [4, 7, 8], [0, 8, 9], [1, 5, 9], [2, 6, 5], [3, 6, 7]]
colors = [red, green, yellow]
ans = []
coordinates = []
win.fill(white)
drawGraph()
pygame.display.update()
color()
