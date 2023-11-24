import pygame

a = input().split()
w, h = int(a[0]), int(a[1])
s1 = w // h

size = w, w
s = pygame.display.set_mode(size)
s.fill(pygame.Color("white"))
pygame.init()


def draw():
    for x in range(0, size[0], s1 * 2):
        for y in range(size[0] - s1, -s1 * 2, -s1 * 2):
            for shift in (0, s1):
                pygame.draw.rect(s, pygame.Color("black"), pygame.Rect((x + shift, y - shift), (s1,) * 2))
    pygame.display.flip()


draw()


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

