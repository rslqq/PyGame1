import pygame

a = input().split()
w, h = int(a[0]), int(a[1])

size = w, h
s = pygame.display.set_mode(size)
pygame.init()


def draw(screen):
    red = (255, 0, 0)

    pygame.draw.rect(screen, red, (1, 1, w - 1, h - 1))


draw(s)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

