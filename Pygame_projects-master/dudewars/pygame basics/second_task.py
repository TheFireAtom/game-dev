import pygame 
import sys

from pygame.color import THECOLORS

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

r = pygame.Rect(100, 100, 170, 92.5)
pygame.draw.rect(screen, THECOLORS['white'], r, 0)
pygame.draw.rect(screen, THECOLORS['violet'], (100, 100, 170, 92.5), 1)
# Three at the top
pygame.draw.circle(screen, THECOLORS['blue'], (140, 140), 20, 5)
pygame.draw.circle(screen, THECOLORS['black'], (185, 140), 20, 5)
pygame.draw.circle(screen, THECOLORS['red'], (230, 140), 20, 5)
# Two at the bottom
pygame.draw.circle(screen, THECOLORS['yellow'], (162.5, 150), 20, 5)
pygame.draw.circle(screen, THECOLORS['green'], (207.5, 150), 20, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



