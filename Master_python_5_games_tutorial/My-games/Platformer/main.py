import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")
running = True
clock = pygame.Clock()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)

        spritesheet = pygame.image.load(join("My-games", "Platformer", "assets", "Guy-Sheet")).convert_alpha()
        self.frame_width = 32
        self.frame_height = 32

        animations = ["idle", "walk", "jump", "hurt"]
        
        self.frames = {anim: [] for anim in animations}

        frames_per_row = spritesheet.get_width() // self.frame_width

        for row, anim_name in enumerate(animations):
            y = row * self.frame_height
            for col in range(frames_per_row):
                x = col * self.frame_width
                frame = spritesheet.subsurface(x, y, self.frame_width, self.frame_height)
                self.frames[anim_name].append(frame)

        self.current_animation = "idle"
        self.current_frame = 0
        self.image = self.frames[self.current_animation][0]

        self.rect = self.image.get_frect(midleft=(WINDOW_WIDTH, WINDOW_HEIGHT))
        
        assert self.image is not None
        assert self.rect is not None

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

while running:
    dt = clock.tick(60) 
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray12")

    all_sprites.draw(display_surface)

    pygame.display.update()
            
pygame.quit()