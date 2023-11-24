import pygame

a = input().split()
w, h = int(a[0]), int(a[1])

size = w, h
s = pygame.display.set_mode(size)
pygame.init()


def draw(screen, b, c):
    white = (255, 255, 255)

    pygame.draw.line(screen, white, (0, 0), (b, c), width=5)

    pygame.draw.line(screen, white, (0, c), (b, 0), width=5)


draw(s, w, h)

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

