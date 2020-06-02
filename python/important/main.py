import pygame
import time
import random
import numpy as np

pygame.init()
width = 1000
height = 600
row = 30
column = 50
pygame.display.set_caption("Game of Life")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grid = [[0 for x in range(column)] for y in range(row)]
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



def binarySearch(list,target):
    left = 0
    right = len(list)-1
    while left <= right:
        mid = left + math.floor((right - left)/2)
        if list[mid] == target:
            return mid
        if list[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def colorIt(color, x, y):
    pygame.draw.rect(win, color, (y * width / column, x *
                                  height / row, width / column, height / row))


def opponent(turn):
    if turn == ai:
        return human
    return ai


def isWinner(turn):
    pass


def changeColor(color):
    if color == red:
        return green
    return red


def play(l):
    pass


def main(run):
    drawGrid(white, row, column)
    pygame.display.update()
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                play(convert(mx, my))
        drawGrid(white, row, column)
        pygame.display.update()


main(True)
