import pygame
from os.path import join
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from start_menu import start_menu

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Character template test")
running = True
clock = pygame.Clock()

start_menu(display_surface)

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)  

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray14")

    pygame.display.update(dt)

    all_sprites.draw(display_surface)

pygame.quit()
