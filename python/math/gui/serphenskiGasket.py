import math
import random
import pygame


pygame.init()
width = 1000
height = 600
pygame.display.set_caption("Serphenski Gasket")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colors = [red, white, yellow, green, blue]


def drawIt(tuple):
    pygame.draw.circle(win, random.choice(colors), tuple, 1)

# #random a,b,c,d
# a=(random.randint(0,1000),random.randint(0,600))
# b=(random.randint(0,1000),random.randint(0,600))
# c=(random.randint(0,1000),random.randint(0,600))
# d = (random.randint(0, 1000),random.randint(0, 600))

a = (500, 10)
b = (100, 590)
c = (900, 590)
d = (math.floor((a[0]+b[0]+c[0])/3),math.floor((a[1]+b[1]+c[1])/3))


drawIt(a)
drawIt(b)
drawIt(c)
drawIt(d)


def Serphenski():
    global d
    x = random.choice([a,b,c])
    d = (math.floor((d[0]+x[0])/2),math.floor((d[1] + x[1])/2))
    drawIt(d)


def main(run):
    iteration = 0
    win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
        "Iterations : ", True, white), (10, 10))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Serphenski()
        iteration += 1
        pygame.draw.rect(win, black, (120, 10, 350, 20))
        win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
            str(iteration), True, white), (125, 10))
        pygame.display.update()


main(True)
