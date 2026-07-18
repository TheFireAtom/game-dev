import pygame
from os.path import join
from random import randint

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
FRAME_WIDTH, FRAME_HEIGHT = 128, 128
main_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.Clock()

max_coins = 5
coins = []
coin_timer = pygame.time.get_ticks()
coin_delay = 150

all_sprites = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

def spritesheet_read(self, spritesheet, frames):
    for x in range(int(spritesheet.get_width() / FRAME_WIDTH)):
        frame = spritesheet.subsurface(x*FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)
        frames.append(frame)

def spawncoin():
    global coin_timer
    if len(coins) < max_coins:
        if pygame.time.get_ticks() - coin_timer >= coin_delay:
            for i in range(max_coins):
                x = randint(10, WINDOW_WIDTH-10)
                y = randint(10, WINDOW_HEIGHT-10)
                coin = Coin(x, y)
                coins.append(coin)
                coin_group.add(coin)

            coin_timer = pygame.time.get_ticks()
        
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        # self.frame_width = 128
        # self.frame_height = 128

        self.spritesheet_coin = pygame.image.load(join("My-games", "Character-templater-test", "assets", "coin_flip-Sheet.png")).convert_alpha()

        self.spritesheet_coin_scaled = pygame.transform.scale_by(self.spritesheet_coin, 4)
        self.image = self.spritesheet_coin_scaled.subsurface(0, 0, FRAME_WIDTH, FRAME_HEIGHT)
        self.rect = self.image.get_frect()    

        self.frames_coinflip = []    

        spritesheet_read(self, self.spritesheet_coin_scaled, self.frames_coinflip)

        self.rect.x = x
        self.rect.y = y
    
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

        # self.frame_width = 128
        # self.frame_height = 128

        self.frames_walk_right = []
        self.frames_walk_left = []
        # self.frames_idle_right = []
        # self.frames_idle_left = []
        self.frames_idle = []
        self.frames_jump = []

        self.image = self.spritesheet_walk_right_scaled.subsurface(0, 0, FRAME_WIDTH, FRAME_HEIGHT)
        self.rect = self.image.get_frect()

        self.spritesheet_walk_left_scaled = pygame.transform.flip(self.spritesheet_walk_right_scaled, True, False)

        spritesheet_read(self, self.spritesheet_walk_right_scaled, self.frames_walk_right)
        spritesheet_read(self, self.spritesheet_walk_left_scaled, self.frames_walk_left)
        spritesheet_read(self, self.spritesheet_idle_scaled, self.frames_idle)
        spritesheet_read(self, self.spritesheet_jump_scaled, self.frames_jump)
        
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

player = Player(all_sprites)

while running:
    dt = clock.tick(60) / 1000
    clock.get_fps()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_display.fill("white")

    spawncoin()
    
    all_sprites.draw(main_display)
    coin_group.draw(main_display)

    player.update()
    player.controls()

    pygame.sprite.spritecollide(player, coin_group, True)

    pygame.display.update()

pygame.quit()