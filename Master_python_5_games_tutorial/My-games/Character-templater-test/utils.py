import pygame
from constants import FRAME_WIDTH, FRAME_HEIGHT

def spritesheet_read(spritesheet, frames):
    for x in range(int(spritesheet.get_width() / FRAME_WIDTH)):
        frame = spritesheet.subsurface(x*FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)
        frames.append(frame)

def update(timer, delay, frame_index, frames, image, rect):
        if pygame.time.get_ticks() - timer >= delay:
            saved_position = rect.midleft
            frame_index += 1
            image = frames[frame_index % len(frames)]

            rect = image.get_frect(midleft=saved_position)
            timer = pygame.time.get_ticks()