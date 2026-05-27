import pygame 
import sys

from pygame.color import THECOLORS

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

r = pygame.Rect(100, 100, 100, 100)
pygame.draw.rect(screen, THECOLORS['green'], r, 0)
pygame.draw.line(screen, THECOLORS['red'], (102, 100), (150, 20), 5)
pygame.draw.line(screen, THECOLORS['red'], (198, 100), (150, 20), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



