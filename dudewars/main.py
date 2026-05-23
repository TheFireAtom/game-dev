import pygame
import sys

from pygame.color import THECOLORS

pygame.init()

# setting canvas size 
size = (1200, 800)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

# setting font size
font = pygame.font.SysFont('coriernew', 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()


