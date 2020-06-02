import random
import pygame
import time


def bubbleSort(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                pygame.draw.line(win, black, (10+i, 550), (10+i, 550-l[i]))
                l[i], l[j] = l[j], l[i]
                pygame.draw.line(win, random.choice(colors),
                                 (10+j, 550), (10+j, 550-l[j]))
                pygame.draw.line(win, random.choice(colors),
                                 (10+i, 550), (10+i, 550-l[i]))
                pygame.display.update()


def selectionSort(l):
    for i in range(len(l)):
        min = i
        for j in range(i, len(l)):
            if l[j] < l[min]:
                min = j
        pygame.draw.line(win, black, (10+i, 550), (10+i, 550-l[i]))
        l[min], l[i] = l[i], l[min]
        pygame.draw.line(win, random.choice(colors),
                         (10+min, 550), (10+min, 550-l[min]))
        pygame.draw.line(win, random.choice(colors),
                         (10+i, 550), (10+i, 550-l[i]))
        pygame.display.update()


def insertionSort(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            pygame.draw.line(win, black, (9+j, 550), (9+j, 550-l[j-1]))
            l[j], l[j-1] = l[j-1], l[j]
            pygame.draw.line(win, random.choice(colors),
                             (9+j, 550), (9+j, 550-l[j-1]))
            pygame.draw.line(win, random.choice(colors),
                             (10+j, 550), (10+j, 550-l[j]))
            pygame.display.update()
            j -= 1


def merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if a[i:]:
        c += a[i:]
    else:
        c += b[j:]
    return c


def mergeSort(l):
    if len(l) == 1:
        return l
    else:
        return merge(mergeSort(l[:len(l)//2]), mergeSort(l[len(l)//2:]))


pygame.init()
width = 1300
height = 600
pygame.display.set_caption("Visualising Sorting Algorithms")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, white, yellow, green, blue]
list = [random.randint(1, 500) for x in range(1280)]
for i in range(len(list)):
    pygame.draw.line(win, random.choice(colors),
                     (10+i, 550), (10+i, 550-list[i]))
pygame.display.update()
time.sleep(1)
selectionSort(list)
# bubbleSort(list)
# mergeSort(list)
# insertionSort(list)
# print(list)
time.sleep(1)
