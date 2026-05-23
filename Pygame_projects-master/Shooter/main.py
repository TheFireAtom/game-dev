import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))
rectangle = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), rectangle, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()

