import pygame
from sys import exit

pygame.init()
display = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner")

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)