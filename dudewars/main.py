import pygame 
import sys 

from pygame.color import THECOLORS

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['orange'])

font = pygame.font.SysFont('couriernew', 40)
text = font.render(str('Hello there!'), True, THECOLORS['green'])
screen.blit(text, (100, 50))

# avaliable_fonts = pygame.font.get_fonts()
# print(avaliable_fonts)


r = pygame.Rect(0, 0, 100, 100)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    