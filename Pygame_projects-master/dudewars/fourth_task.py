import pygame
import sys
import random

from pygame.color import THECOLORS

pygame.init()

size = (1201, 801)
screen = pygame.display.set_mode(size)
screen.fill(THECOLORS['black'])

font = pygame.font.SysFont(None, 80)

# try: 
#     with open("data.txt", "r") as file:
#         print("Reading file...")
#         content = file.read()
#         print(content)
       
# except FileNotFoundError:
#     with open("data.txt", "w") as file:
#         file.write("")
#     print("File created")

# cell_size = int(input("Enter cell size: "))
cell_size = 100 # temporarly for debuging purposes 
colors_list = ['black', 'green', 'blue', 'red', 'violet',
               'purple', 'yellow', 'orange', 'brown', 'cyan']
cnt = 0

cols = size[0] // cell_size
rows = size[1] // cell_size
total_cells = cols * rows

# some bullshit idk
# def rand_nums(x, y):
#     with open("data.txt", "w") as file:
#         file.write("")
#     rand_len = size[0] // cell_size
#     # rand_list = []
#     for rand_num in range(1, rand_len):
#         rand_num = random.randint(1, rand_len)
#         # rand_list.append()
#         with open("data.txt", "a") as file:
#             # print(rand_num)
#             file.write(" ")
#             file.write(str(rand_num))
#     # print(rand_list) for debug
#     # return rand_list
#     with open("data.txt", "r") as file:
#         print("Reading file...")
#         content = file.read()
#         numbers = [int(num) for num in content.split()]
#         color_num = random.choice(numbers)
#         #print(type(content))
#         r = pygame.Rect(x, y, cell_size, cell_size)
#         pygame.draw.rect(screen, THECOLORS[colors_list[color_num]], r, width=0)

# def draw_one(cell_x, cell_y):
#     pygame.draw.lines(screen, THECOLORS['white'], False, 
#                       [(cell_x + 20, cell_y + 50), 
#                        (cell_x + 50, cell_y + 20), 
#                        (cell_x + 50, cell_y + 80)], 1)

# old variant
# for x in range(0, size[0] + cell_size, cell_size):
#     pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, size[0]))
# for y in range(0, size[0] + cell_size, cell_size):
#     pygame.draw.line(screen, THECOLORS['white'], (0, y), (size[0], y))

# new variant (filling canvas with lines (cells))
# for pos in range(0, size[0] + cell_size, cell_size):
#     pygame.draw.line(screen, THECOLORS['white'], (pos, 0), (pos, size[0]))
#     pygame.draw.line(screen, THECOLORS['white'], (0, pos), (size[0], pos))
    # draw_one(pos, pos)

# another bullshit, old design
# for x in range(0, size[0] + cell_size, cell_size):  
#     for y in range(0, size[1] + cell_size, cell_size):
#         # print(x, y) for debugging
#         number = x // cell_size + 1
#         text = font.render(str(number), False, THECOLORS['white'])
#         rand_nums(x, y)

#         if (number == rand_nums and cnt < 1): 
#             r = pygame.Rect(x, y, cell_size, cell_size)
#             pygame.draw.rect(screen, THECOLORS[str(rand_nums)], r, width=0)
#             cnt += 1

#         if (number < 10):
#             screen.blit(text, (x + 32, y + 25))
#         else:
#             screen.blit(text, (x + 20, y + 25))

with open("data.txt", "w") as file:
    for _ in range(10):
        rand_num = random.randint(1, total_cells)
        file.write((str(rand_num)) + " ")
    
with open("data.txt", "r") as file:
    cells_to_paint = [int(num) for num in file.read().split()]

color_cell_number = 1 # for tracking 

for y in range(0, size[1], cell_size):
    pygame.draw.line(screen, THECOLORS['white'], (0, y), (size[0], y))  
    for x in range(0, size[0], cell_size):
        pygame.draw.line(screen, THECOLORS['white'], (x, 0), (x, size[0]))

        if color_cell_number in cells_to_paint:
            color = random.choice(colors_list)

            r = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, THECOLORS[color], r)
            pygame.display.flip()

            # text = font.render(str(cell_number), True, THECOLORS["white"])
            # screen.blit(text, (x + 32, y + 25))
        color_cell_number += 1
        number = x // cell_size
        text = font.render(str(number), True, THECOLORS["white"])

        if (number < 10):
            screen.blit(text, (x + 32, y + 25))
        else:
            screen.blit(text, (x + 20, y + 25))
       

        # text = font.render(str(number), True, THECOLORS["white"])
        # screen.blit(text, (x + 32, y + 25))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()