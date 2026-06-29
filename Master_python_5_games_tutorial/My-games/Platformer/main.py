import pygame
from os.path import join
import sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")
running = True
clock = pygame.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.animation = pygame.image.load_animation(join("My-games", "Platformer", "assets", "Mushroom.gif"))

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

while running:
    dt = clock.tick(60) 
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
            