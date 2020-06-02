import math
import random
import pygame


pygame.init()
width = 1000
height = 600
pygame.display.set_caption("Visualising Pi")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# colors = [red, white, yellow, green, blue]


win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
    "Points : ", True, white), (10, 10))
win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
    "Pi : ", True, white), (10, 40))
pygame.draw.rect(win, white, (300, 10, 580, 580), 1)
pygame.draw.circle(win, white, (590, 300), 290, 1)


def main(run):
    total = 0
    inside = 0
    pi = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        x = random.randint(300, 880)
        y = random.randint(10, 590)
        if (x-590)**2 + (y-300)**2 <= 290**2:
            inside += 1
            pygame.draw.circle(win, green, (x, y), 1)
        else:
            pygame.draw.circle(win, red, (x, y), 1)
        total += 1
        pi = 4*inside/total
        pygame.draw.rect(win, black, (85, 10, 200, 20))
        pygame.draw.rect(win, black, (50, 40, 245, 20))
        win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
            str(total), True, white), (90, 10))
        win.blit(pygame.font.Font('freesansbold.ttf', 20).render(
            str(pi), True, white), (55, 40))
        pygame.display.update()


main(True)
