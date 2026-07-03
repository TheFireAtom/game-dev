import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")
running = True
clock = pygame.Clock()

spritesheet = pygame.image.load(join("My-games", "Platformer", "assets", "Guy-Sheet.png")).convert_alpha()

frame = spritesheet.subsurface(0, 0, 32, 32)



while running:
    dt = clock.tick(60) 
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray12")

    pygame.display.update()