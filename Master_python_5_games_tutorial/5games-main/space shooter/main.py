import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
player_direction = 1

# old method
# player_move_left = False
# player_move_right = False

# object surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100

# importing an image
player_surf = pygame.image.load(join("5games-main", "space shooter", "images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(midleft = (0, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load("5games-main/space shooter/images/laser.png")
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

meteor_surf = pygame.image.load("5games-main/space shooter/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surf = pygame.image.load("5games-main/space shooter/images/star.png").convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]



# print(star_position)
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("gray13")
    for pos in star_position:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # old method
    # if player_rect.left <= 0:
    #     player_move_left = False
    #     player_move_right = True
    # elif player_rect.right >= WINDOW_WIDTH:
    #     player_move_left = True
    #     player_move_right = False

    # if player_move_left:
    #     player_rect.left -= 0.2
    # elif player_move_right:
    #     player_rect.right += 0.2

    # new method
    player_rect.x += player_direction * 0.4
    if player_rect.left < 0 or player_rect.right > WINDOW_WIDTH:
        player_direction *= -1
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()
    