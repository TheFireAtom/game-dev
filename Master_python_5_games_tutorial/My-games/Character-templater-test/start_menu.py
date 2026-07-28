import pygame
import sys
import constants
from os.path import join
from utils import spritesheet_read, update

def start_menu(main_display):

    timer = pygame.time.get_ticks()
    delay = 150
    frame_index = 0
    spritesheet_start_button = pygame.image.load(join("My-games", "Character-templater-test", "assets", "Start_button-Sheet.png")).convert_alpha()
    spritesheet_start_button_scaled = pygame.transform.scale_by(spritesheet_start_button, 4)
    frames_start_button = []
    spritesheet_read(spritesheet_start_button_scaled, frames_start_button)
    #print(frames_start_button)

    #update(timer, delay, frame_index, frames_start_button, spritesheet_start_button_scaled, spritesheet_start_button_scaled.get_frect())

    #print(frames_start_button)

    current_frame = frames_start_button[0]

    while True:

        mouse = pygame.mouse.get_pos()

        main_display.fill("white")

        play_button = spritesheet_start_button_scaled.subsurface(0, 0, constants.FRAME_WIDTH, constants.FRAME_HEIGHT).get_frect()
        quit_button = pygame.Rect(600, 600, 100, 100)

        play_button.center = constants.WINDOW_WIDTH / 2 + 16, constants.WINDOW_HEIGHT / 2 - 32 # idk why I need to do those math operations here

        main_display.blit(current_frame, play_button)

        global local_timer
        local_timer = pygame.time.get_ticks()
        local_delay = 150

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(mouse):
                    # current_frame = update(timer, delay, frame_index, frames_start_button, spritesheet_start_button_scaled, spritesheet_start_button_scaled.get_frect())
                    current_frame = frames_start_button[1]
                    play_button = spritesheet_start_button_scaled.get_frect()
                    return True
                    local_timer = pygame.time.get_ticks()
                if quit_button.collidepoint(mouse):
                    return False
        
        pygame.display.update()