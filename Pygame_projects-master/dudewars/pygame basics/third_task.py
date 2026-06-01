import pygame 
import sys

from pygame.color import THECOLORS

pygame.init()

size = (1001, 1001)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

# Playing with lines
# pygame.draw.lines(screen, THECOLORS['white'], False, [(100, 100), (250, 200), (300, 300)])

cell_size = int(input("Enter cell size: "))

# for x in range(cnt):
#     pygame.draw.line(screen, THECOLORS['white'], new_size[0] / 10, new_size[1] / 10) 

# for x in range(cell_size): 
#     pygame.draw.line(screen, THECOLORS['white'], (100, 0), (100, 1000)) 
#     pygame.draw.line(screen, THECOLORS['white'], (200, 0), (200, 1000)) 

#     pygame.draw.line(screen, THECOLORS['white'], (0, 100), (1000, 100)) 
#     pygame.draw.line(screen, THECOLORS['white'], (0, 200), (1000, 200)) 

count_range = size[0] // cell_size

# for cell in range(int(count_range)):
#     x = cell * cell_size
#     y = cell * cell_size

#     pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, 1000))
#     pygame.draw.line(screen, THECOLORS['white'], (0, y), (1000, y))

# for cell in range(int(count_range)):
#     x = cell * cell_size
#     y = cell * cell_size
    
#     pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, 1000))
#     pygame.draw.line(screen, THECOLORS['white'], (0, y), (1000, y))

for x in range(0, 1000 + cell_size, cell_size):
    pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, 1000))
for y in range(0, 1000 + cell_size, cell_size):
    pygame.draw.line(screen, THECOLORS['white'], (0, y), (1000, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()



