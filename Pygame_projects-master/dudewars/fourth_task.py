import pygame
import sys

from pygame.color import THECOLORS

pygame.init()

size = (1201, 801)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

cell_size = int(input("Enter cell size: "))
temp_x = 0
temp_y = 0

def draw_one(cell_x, cell_y):
    pygame.draw.lines(screen, THECOLORS['white'], False, 
                      [(cell_x + 20, cell_y + 50), 
                       (cell_x + 50, cell_y + 20), 
                       (cell_x + 50, cell_y + 80)], 1)


# old variant
# for x in range(0, size[0] + cell_size, cell_size):
#     pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, size[0]))
# for y in range(0, size[0] + cell_size, cell_size):
#     pygame.draw.line(screen, THECOLORS['white'], (0, y), (size[0], y))

# new variant (filling canvas with lines (cells))
for pos in range(0, size[0] + cell_size, cell_size):
    pygame.draw.line(screen, THECOLORS['white'], (pos, 0), (pos, size[0]))
    pygame.draw.line(screen, THECOLORS['white'], (0, pos), (size[0], pos))
    # draw_one(pos, pos)


for x in range(0, size[0] + cell_size, cell_size):  
    for y in range(0, size[0] + cell_size, cell_size):
        print(x, y)
        if (x == 0):
            draw_one(x, y)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()