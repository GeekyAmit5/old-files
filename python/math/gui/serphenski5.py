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
# e = (random.randint(0, 1000),random.randint(0, 600))
# f = (random.randint(0, 1000),random.randint(0, 600))


a = (100,100)
b = (900,100)
c = (100,500)
d = (900,500)
e = (450,250)
f = (300,300)


drawIt(a)
drawIt(b)
drawIt(c)
drawIt(d)
drawIt(e)
drawIt(f)


def Serphenski():
    global f
    x = random.choice([a,b,c,d,e])
    f = (math.floor((f[0]+x[0])/4),math.floor((f[1] + x[1])/4))
    drawIt(f)


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
