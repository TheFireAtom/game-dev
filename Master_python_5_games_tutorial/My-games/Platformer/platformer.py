import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer")
running = True
clock = pygame.Clock()
# timer = pygame.time.get_ticks()


class Player(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)

        self.spritesheet = pygame.image.load(join("My-games", "Platformer", "assets", "Guy-Sheet.png")).convert_alpha()

        self.frame_width = 80
        self.frame_height = 80
        self.test = 16

        self.player_direction = pygame.Vector2(0, 0)
        self.player_speed = 0.5

        self.timer = pygame.time.get_ticks()
        self.animation_delay = 125

        # (self.test, self.test)
        self.spritesheet_scaled = pygame.transform.scale_by(self.spritesheet, 5)

        print("width: ", self.spritesheet_scaled.get_width(), "height: ", self.spritesheet_scaled.get_height())

        animations = ["idle", "jump", "move", "hurt"]
        self.current_frame = 0
        self.animation_speed = 0.15
        # print(animations)
        
        self.frames = {anim: [] for anim in animations}
        #print(self.frames)

        frames_per_row = self.spritesheet_scaled.get_width() // self.frame_width

        print("frames per row: ", frames_per_row)

        self.keys = pygame.key.get_pressed()

        for row, anim_name in enumerate(animations):
            y = row * self.frame_height
            for col in range(frames_per_row):
                x = col * self.frame_width
                frame = self.spritesheet_scaled.subsurface(x, y, self.frame_width, self.frame_height)
                print(frame)
                self.frames[anim_name].append(frame)
                print(len(self.frames))

        self.current_animation = "idle"

        # print("Frames length: ", len(self.frames))
    
        self.image = self.frames[self.current_animation][0]

        self.rect = self.spritesheet_scaled.get_frect(midleft=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        assert self.image is not None
        assert self.rect is not None

    def controls(self):
        assert self.rect is not None
        self.keys = pygame.key.get_pressed()
        self.player_direction.x = self.keys[pygame.K_d] - self.keys[pygame.K_a]
        self.player_direction.y = self.keys[pygame.K_s] - self.keys[pygame.K_w]

        self.player_direction.normalize() if self.player_direction else self.player_direction

        self.rect.center += self.player_direction * self.player_speed * dt

    def update(self):

        current_time = pygame.time.get_ticks()
        animation_state = 0

        if current_time - self.timer >= self.animation_delay:
            for x in range(2):
                animation_state += x
                # print(animation_state)
                self.timer = current_time

            if self.keys[pygame.K_d] or self.keys[pygame.K_a]:
                self.image = self.frames["move"][animation_state]

            elif self.keys[pygame.K_s] or self.keys[pygame.K_w]:
                self.image = self.frames["jump"][animation_state]
            
            else: 
                self.image = self.frames["idle"][animation_state]
    

    # So what I need to do is: 1. Move character when wasd is pressed
    # 2. If w is pressed I need to move char.y a little high, like by N 
    # 3. If a or d is pressed I need to move character left or right
    # 4. Also, I need to change frames somehow.

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

while running:
    dt = clock.tick(60) 
    #print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("gray12")

    all_sprites.draw(display_surface)
    
    player.controls()
    player.update()

    pygame.display.update()
            
pygame.quit()
