import pygame
from itertools import cycle, islice


a = input().split()
w, h = int(a[0]), int(a[1])

size = w, w

pygame.init()
screen = pygame.display.set_mode((size[0] * h * 2, ) * 2)


def draw():
    colors = cycle((pygame.Color(255, 0, 0), pygame.Color(0, 255, 0), pygame.Color(0, 0, 255)))
    dopt = size[0] * h
    posled = iter(tuple(islice(colors, h))[::-1])
    for i in range(h, 0, -1):
        pygame.draw.circle(screen, next(posled), (dopt, ) * 2, size[0] * i)
    pygame.display.flip()


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()