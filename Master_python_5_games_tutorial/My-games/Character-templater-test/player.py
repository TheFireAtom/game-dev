import pygame
from os.path import join
from constants import FRAME_WIDTH, FRAME_HEIGHT
from utils import spritesheet_read

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.facing_right = True

        self.spritesheet_walk_right = pygame.image.load(join("My-games", "Character-templater-test", "assets", "32x32_chibi_template_run_walk_new_anim-Sheet.png")).convert_alpha()
        self.spritesheet_idle = pygame.image.load(join("My-games", "Character-templater-test", "assets", "32x32_chibi_template_idle-Sheet.png")).convert_alpha()
        self.spritesheet_jump = pygame.image.load(join("My-games", "Character-templater-test", "assets", "32x32_chibi_template_jump-Sheet.png")).convert_alpha()
        
        self.spritesheet_walk_right_scaled = pygame.transform.scale_by(self.spritesheet_walk_right, 4)
        self.spritesheet_idle_scaled = pygame.transform.scale_by(self.spritesheet_idle, 4)
        self.spritesheet_jump_scaled = pygame.transform.scale_by(self.spritesheet_jump, 4)

        self.frames_walk_right = []
        self.frames_walk_left = []
        self.frames_idle = []
        self.frames_jump = []

        self.image = self.spritesheet_walk_right_scaled.subsurface(0, 0, FRAME_WIDTH, FRAME_HEIGHT)
        self.rect = self.image.get_frect()

        self.spritesheet_walk_left_scaled = pygame.transform.flip(self.spritesheet_walk_right_scaled, True, False)

        spritesheet_read(self.spritesheet_walk_right_scaled, self.frames_walk_right)
        spritesheet_read(self.spritesheet_walk_left_scaled, self.frames_walk_left)
        spritesheet_read(self.spritesheet_idle_scaled, self.frames_idle)
        spritesheet_read(self.spritesheet_jump_scaled, self.frames_jump)
        
        self.keys = pygame.key.get_pressed()

        self.player_speed = 300
        self.player_direction = pygame.Vector2(0, 0)

        self.timer = pygame.time.get_ticks()
        self.delay = 75
        self.frame_index = 0

    def update(self):

        self.keys = pygame.key.get_pressed()

        if pygame.time.get_ticks() - self.timer >= self.delay:
            saved_position = self.rect.midleft
            self.frame_index += 1 

            # if self.player_direction.x > 0 and self.player_direction.y != 0:
            #     self.image = self.frames_jump[self.frame_index % len(self.frames_jump)]
            # elif self.player_direction.x < 0 and self.player_direction.y != 0:
            #     self.image = self.frames_jump[self.frame_index % len(self.frames_jump)]
            if self.player_direction.x > 0:
                self.image = self.frames_walk_right[self.frame_index % len(self.frames_walk_right)]
            elif self.player_direction.x < 0:
                self.image = self.frames_walk_left[self.frame_index % len(self.frames_walk_left)]
            elif self.player_direction.y != 0:
                self.image = self.frames_jump[self.frame_index % len(self.frames_jump)]
            else:
                self.image = self.frames_idle[self.frame_index % len(self.frames_idle)]
            # elif self.facing_right:
            #     self.image = self.frames_idle_right[self.frame_index % len(self.frames_idle_right)]
            # elif self.facing_right == False:
            #     self.image = self.frames_idle_left[self.frame_index % len(self.frames_idle_left)]

            self.rect = self.image.get_frect(midleft=saved_position)
            self.timer = pygame.time.get_ticks()

    def controls(self):

        if self.keys[pygame.K_d]:
            self.facing_right = True
        elif self.keys[pygame.K_a]:
            self.facing_right = False
        # if self.keys[pygame.K_SPACE]:
        #     self.projectile_active = True
        #     self.shoot_projectile()

        self.player_direction.x = self.keys[pygame.K_d] - self.keys[pygame.K_a]
        self.player_direction.y = self.keys[pygame.K_s] - self.keys[pygame.K_w]

        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.player_speed * dt

    # def collision(self) {

    #     if pyga
    # }