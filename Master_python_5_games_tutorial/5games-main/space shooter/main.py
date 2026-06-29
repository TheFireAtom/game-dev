import pygame
#from pygame import Surface, FRect
from typing import cast
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.image = pygame.image.load(join("5games-main", "space shooter", "images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(midleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.player_direction = pygame.Vector2(0, 0)
        self.player_speed = 300

    def update(self, dt):
        # print("Ship is being updated")
        assert self.rect is not None
        keys = pygame.key.get_pressed()
        self.player_direction.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.player_direction.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.player_speed * dt

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()

# old method
# player_move_left = False
# player_move_right = False

# object surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# importing images

laser_surf = pygame.image.load("5games-main/space shooter/images/laser.png")
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

meteor_surf = pygame.image.load("5games-main/space shooter/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surf = pygame.image.load("5games-main/space shooter/images/star.png").convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

# rect 
# plain_rect = pygame.FRect(left, top, width, height)

pygame.key.set_repeat(0)

# print(star_position)
while running:
    dt = clock.tick() / 1000
    # print(clock.get_fps())

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # draw the game
    display_surface.fill("gray13")
    for pos in star_position:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
    