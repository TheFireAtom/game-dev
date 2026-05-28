import pygame 
import sys

from pygame.color import THECOLORS

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

# Playing with lines
# pygame.draw.lines(screen, THECOLORS['white'], False, [(100, 100), (250, 200), (300, 300)])



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



