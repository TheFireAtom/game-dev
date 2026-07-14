import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Character template test")
running = True
clock = pygame.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.spritesheet_right = pygame.image.load(join("My-games", "Character-templater-test", "assets", "Character-template-moving-right-Sheet.png")).convert_alpha()
        self.spritesheet_left = pygame.image.load(join("My-games", "Character-templater-test", "assets", "Character-template-moving-left-Sheet.png")).convert_alpha()

        self.frame_width = 32
        self.frame_height = 32

        self.walk = []        

        self.player_direction = pygame.Vector2(0, 0)
        self.player_speed = 1.5

        

        self.timer = pygame.time.get_ticks()
        self.animation_delay = 125
        self.frame_index = 0

        # self.spritesheet_right_scaled = pygame.transform.scale_by(self.spritesheet_right, 4)
        # self.spritesheet_left_scaled = pygame.transform.scale_by(self.spritesheet_left, 4)

        for current_frame in range(self.spritesheet_right_scaled.get_width() // self.frame_width):
            print(self.spritesheet_right_scaled.get_width() // self.frame_width)
            frame = self.spritesheet_right_scaled.subsurface(current_frame * self.frame_width, 0, self.frame_width, self.frame_height)
            self.walk.append(frame)
    
        self.image = self.walk[0]
        self.rect = self.image.get_frect(midleft=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
    def update(self, dt):
        if pygame.time.get_ticks() - self.timer >= self.animation_delay:
            saved_position = self.rect.midleft
            self.frame_index += 1
            self.image = self.walk[self.frame_index % len(self.walk)]
            self.rect = self.image.get_frect(midleft=saved_position)
            self.timer = pygame.time.get_ticks()
        # for anim, frame in rframes:
        #     frame = self.spritesheet_right.subsurfaace

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
