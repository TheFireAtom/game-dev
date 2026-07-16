import pygame
from os.path import join

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
main_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.Clock()

def spritesheet_read(self, spritesheet, frames):
    for x in range(int(spritesheet.get_width() / self.frame_width)):
        frame = spritesheet.subsurface(x*self.frame_width, 0, self.frame_width, self.frame_height)
        frames.append(frame)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.is_active = True


class Player(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.facing_right = True

        self.spritesheet_right = pygame.image.load(join("My-games", "Character-templater-test", "assets", "fight_man_walk-Sheet.png")).convert_alpha()
        self.spritesheet_idle = pygame.image.load(join("My-games", "Character-templater-test", "assets", "fight_man_idle-Sheet.png")).convert_alpha()
        self.spritesheet_shoot = pygame.image.load(join("My-games", "Character-templater-test", "assets", "fight_man_walk_and_fire-Sheet.png")).convert_alpha()

        self.spritesheet_right_scaled = pygame.transform.scale_by(self.spritesheet_right, 4)
        self.spritesheet_idle_right_scaled = pygame.transform.scale_by(self.spritesheet_idle, 4)
        
        self.frame_width = 128
        self.frame_height = 128
        self.frames_right = []
        self.frames_left = []
        self.frames_idle_right = []
        self.frames_idle_left = []
        
        self.image = self.spritesheet_right_scaled.subsurface(0, 0, self.frame_width, self.frame_height)
        self.rect = self.image.get_frect()

        self.keys = pygame.key.get_pressed()

        self.player_speed = 300
        self.player_direction = pygame.Vector2(0, 0)

        spritesheet_read(self, self.spritesheet_right_scaled, self.frames_right)

        # for x in range(int(self.spritesheet_right_scaled.get_width() / self.frame_width)):
        #     frame = self.spritesheet_right_scaled.subsurface(x*self.frame_width, 0, self.frame_width, self.frame_height)
        #     self.frames_right.append(frame)
        # #print(len(self.frames_right))

        self.spritesheet_left_scaled = pygame.transform.flip(self.spritesheet_right_scaled, True, False)

        spritesheet_read(self, self.spritesheet_left_scaled, self.frames_left)

        spritesheet_read(self, self.spritesheet_idle_right_scaled, self.frames_idle_right)

        self.spritesheet_idle_left_scaled = pygame.transform.flip(self.spritesheet_idle_right_scaled, True, False)

        spritesheet_read(self, self.spritesheet_idle_left_scaled, self.frames_idle_right)

        self.timer = pygame.time.get_ticks()
        self.delay = 75
        self.frame_index = 0

    def update(self):
        if pygame.time.get_ticks() - self.timer >= self.delay:
            saved_position = self.rect.midleft
            self.frame_index += 1 
            if self.player_direction.x > 0:
                self.image = self.frames_right[self.frame_index % len(self.frames_right)]
            elif self.player_direction.x < 0:
                self.image = self.frames_left[self.frame_index % len(self.frames_left)]
            elif self.facing_right:
                self.image = self.frames_idle_right[self.frame_index % len(self.frames_idle_right)]
            elif self.facing_right == False:
                self.image = self.frames_idle_left[self.frame_index % len(self.frames_idle_left)]
            
            self.rect = self.image.get_frect(midleft=saved_position)
            self.timer = pygame.time.get_ticks()

    def controls(self):
        
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_d]:
            self.facing_right = True
        elif self.keys[pygame.K_a]:
            self.facing_right = False
        elif self.keys[pygame.K_SPACE]:
            self.shoot_projectile()

        self.player_direction.x = self.keys[pygame.K_d] - self.keys[pygame.K_a]
        self.player_direction.y = self.keys[pygame.K_s] - self.keys[pygame.K_w]

        


        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.player_speed * dt

    def shoot_projectile()

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

while running: 
    dt = clock.tick(60) / 1000
    clock.get_fps()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_display.fill("gray12")

    all_sprites.draw(main_display)

    player.controls()
    player.update()

    pygame.display.update()

pygame.quit()