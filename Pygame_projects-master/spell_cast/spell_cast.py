import pygame
import sys
from random import randint

# classes
class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # file imports
        mage_walk_1 = pygame.image.load("images/mage/mage1.png").convert_alpha()
        mage_walk_2 = pygame.image.load("images/mage/mage2.png").convert_alpha()
        mage_walk_3 = pygame.image.load("images/mage/mage3.png").convert_alpha()
        mage_walk_4 = pygame.image.load("images/mage/mage4.png").convert_alpha()
        mage_jump = pygame.image.load("images/mage/mage5.png").convert_alpha()

        # mage variables
        # variables for mage animation
        self.current_frame = 0
        self.animation_speed = 100
        self.mage_walk = [mage_walk_1, mage_walk_2, mage_walk_3, mage_walk_4]
        self.mage_jump = mage_jump
        self.image = self.mage_walk[self.current_frame]
        self.last_update = pygame.time.get_ticks()
        self.player_speed = 3
        self.direction = 1
        self.last_fire_time = 0
        self.fire_delay = 2000
        self.gravity = 0
        self.bottom_pos = 330

        # mage rectangle
        # self.rect = pygame.Rect(300, 300, 48, 100)
        self.rect = pygame.Rect(300, 300, 60, 60)
        self.x_position_old = self.rect.x
        self.x_position_new = self.rect.x
    
        # mage methods
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = -1
            self.rect.x -= self.player_speed
        elif keys[pygame.K_d]:
            self.direction = 1
            self.rect.x += self.player_speed
        if keys[pygame.K_SPACE]:
            self.fire_projectile()
        if keys[pygame.K_w] and self.rect.bottom >= self.bottom_pos:
            self.gravity = -20

    # def move_left(self):
    #     self.rect.x -= self.player_speed
    # def move_right(self):
    #     self.rect.x += self.player_speed

    def animation_state(self):
        now = pygame.time.get_ticks()
        on_ground = self.rect.y > 100

        if on_ground:
            if (now - self.last_update > self.animation_speed):
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % (len(self.mage_walk))
                self.image = self.mage_walk[self.current_frame]       
        else:
            self.image = self.mage_walk[0]
            
    def draw(self, screen):
        if self.direction == -1:
            screen.blit(self.image, self.rect)     
        elif self.direction == 1:
            self.image = pygame.transform.flip(self.mage_walk[self.current_frame], True, False)
            screen.blit(self.image, self.rect)   

    def fire_projectile(self):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_fire_time > self.fire_delay:

            projectile = Projectile("fireball", self.rect.centerx, self.rect.centery, self.direction)
            all_sprites.add(projectile)
            projectiles.add(projectile)

            self.last_fire_time = current_time

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.bottom_pos:
            self.rect.bottom = self.bottom_pos

    def update(self):
        self.player_input()
        self.animation_state()
        self.apply_gravity()
        self.draw(screen)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "goblin":
            goblin_1_surf = pygame.image.load("images/goblin/goblin1.png").convert_alpha()
            goblin_2_surf = pygame.image.load("images/goblin/goblin2.png").convert_alpha()
            goblin_3_surf = pygame.image.load("images/goblin/goblin3.png").convert_alpha()
            goblin_4_surf = pygame.image.load("images/goblin/goblin4.png").convert_alpha()
            self.frames = [goblin_1_surf, goblin_2_surf, goblin_3_surf, goblin_4_surf]
            y_pos = 260
            self.rect = pygame.Rect(900, y_pos, 80, 100)
        else:
            bat_1_surf = pygame.image.load("images/bat/bat1.png").convert_alpha()
            bat_2_surf = pygame.image.load("images/bat/bat2.png").convert_alpha()
            bat_3_surf = pygame.image.load("images/bat/bat3.png").convert_alpha()
            bat_4_surf = pygame.image.load("images/bat/bat4.png").convert_alpha()
            self.frames = [bat_1_surf, bat_2_surf, bat_3_surf, bat_4_surf]
            y_pos = 160
            # self.rect = pygame.Rect(900, y_pos, 118, 76)
            self.rect = pygame.Rect(900, y_pos, 90, 76)
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        # self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
        self.type = type

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def bat_position(self):
        if self.type == "bat":
            bat_bool = True
            last_bat_spawn_type = pygame.time.get_ticks()
            move_time = 1000
            now = pygame.time.get_ticks()
            if now - last_bat_spawn_type > move_time:
                if bat_bool:
                    self.rect.y -= 2
                    bat_bool = False
                elif bat_bool == False:
                    self.rect.y += 1
                    bat_bool = True
                last_bat_spawn_type = now
                
    def update(self):
        self.animation_state()
        self.bat_position()
        self.rect.x -= 3
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()         

class Projectile(pygame.sprite.Sprite):
    def __init__(self, type, x, y, direction):
        super().__init__()

        if type == "fireball":
            fireball_surf_1 = pygame.image.load("images/fireball/red_fireball1.png")
            fireball_surf_2 = pygame.image.load("images/fireball/red_fireball2.png")
            fireball_surf_3 = pygame.image.load("images/fireball/red_fireball3.png")
            fireball_surf_4 = pygame.image.load("images/fireball/red_fireball4.png")
            self.frames = [fireball_surf_1, fireball_surf_2, fireball_surf_3, fireball_surf_4]
        if type == "iceball":
            iceball_surf_1 = pygame.image.load("images/fireball/red_iceball1.png")
            iceball_surf_2 = pygame.image.load("images/fireball/red_iceball2.png")
            iceball_surf_3 = pygame.image.load("images/fireball/red_iceball3.png")
            iceball_surf_4 = pygame.image.load("images/fireball/red_iceball4.png")
            self.frames = [iceball_surf_1, iceball_surf_2, iceball_surf_3, iceball_surf_4]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = pygame.Rect(x, y, 32, 48)
        self.prev_x_position = x
        self.rect.center = (x, y)
        self.direction = direction
        self.projectile_speed = 3

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): 
            self.animation_index = 4
        elif self.animation_index < len(self.frames):
            self.image = self.frames[int(self.animation_index)]

    def projectile_direction(self):
        self.rect.x += self.projectile_speed * self.direction       

    def destroy(self):
        if self.rect.x <= -100 or self.rect.x >= 800:
            self.kill()
    
    def update(self):
        self.animation_state()
        self.projectile_direction()
        self.destroy() 

class Interface(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        # loading images
        if type == "heart":
            heart_full_1 = pygame.image.load("images/heart/full/heart_hp_full1.png")
            heart_full_2 = pygame.image.load("images/heart/full/heart_hp_full2.png")
            heart_full_3 = pygame.image.load("images/heart/full/heart_hp_full3.png")
            heart_full_4 = pygame.image.load("images/heart/full/heart_hp_full4.png")
            self.frames = [heart_full_1, heart_full_2, heart_full_3, heart_full_4]
            self.x = x
            self.y = y
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
         
# functions  
def game_over_screen():
    # mage model transformation and creating a rectangle for it 
    mage_1_title_surf = pygame.transform.scale2x(mage_1_surf)
    mage_1_title_rect = mage_1_title_surf.get_rect()

    # rendering text and creating rectangles for it 
    title_surf_1 = main_font.render("Spellcast 2D", False, BLACK).convert_alpha()
    title_surf_2 = main_font.render("Press \"ENTER\" to play", False, BLACK).convert_alpha()
    title_rect_1 = title_surf_1.get_rect()
    title_rect_2 = title_surf_2.get_rect()

    # drawing screen and positioning images
    screen.fill(PURPLE)
    title_rect_1.center = (400, 50)
    title_rect_2.center = (400, 340)
    mage_1_title_rect.center = (400, 210)
    screen.blit(title_surf_1, title_rect_1)
    screen.blit(title_surf_2, title_rect_2)
    screen.blit(mage_1_title_surf, mage_1_title_rect)

def draw_game():
    # file imports
    cave_background_surf = pygame.image.load("images/cave_background/cave_background.png").convert_alpha()
    stone_ground_surf = pygame.image.load("images/stone_ground/stone_ground.png").convert_alpha()

    # drawing screen and positioning images
    
    # mage_1_rect.center = (400, 350)
    # goblin_1_rect.center = (150, 330)
    # bat_1_rect.center = (650, 300)

    # drawing every image
    screen.blit(cave_background_surf, (0, 0))
    screen.blit(stone_ground_surf, (0, 300))
    all_sprites.draw(screen)
    all_sprites.update()
    
    # screen.blit(mage_1_surf, mage_1_rect)
    # screen.blit(goblin_1_surf, goblin_1_rect)
    # screen.blit(bat_1_surf, bat_1_rect)

def enemies_spawn():
    global last_spawn_time, spawn_delay

    now = pygame.time.get_ticks()
    if now - last_spawn_time > spawn_delay:
        spawn_chance = enemies_types[randint(0, 3)]
        new_enemy = Enemy(spawn_chance)
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)
        last_spawn_time = now

def projectile_collision():
    for projectile in projectiles:
        collided_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
        if collided_enemies:
            projectile.kill()
            for enemy in collided_enemies:
                enemy.kill()

def player_collision():
    global game_active, collide_counter
    hearts = [heart_1, heart_2, heart_3]

    for enemy in enemies:
        enemy_collide = pygame.sprite.spritecollide(mage, enemies, False)
        if enemy_collide and collide_counter == 0:
            enemy.kill()
            heart_3.kill()
            collide_counter += 1
        elif enemy_collide and collide_counter == 1:
            enemy.kill()
            heart_2.kill()
            collide_counter += 1
        elif enemy_collide and collide_counter >= 2:
            heart_1.kill()
            game_active = False
            
def restart_game():
    global collide_counter

    cave_background_surf = pygame.image.load("images/cave_background/cave_background.png").convert_alpha()
    stone_ground_surf = pygame.image.load("images/stone_ground/stone_ground.png").convert_alpha()

    collide_counter = 0

    all_sprites.empty()
    enemies.empty()
    projectiles.empty()
    interface.empty()

    initialize_game_start()

    screen.blit(cave_background_surf, (0, 0))
    screen.blit(stone_ground_surf, (0, 300))
    all_sprites.draw(screen)
    all_sprites.update()

def initialize_game_start():
    global mage, heart_1, heart_2, heart_3
    mage = Mage()
    # on the left
    heart_1 = Interface("heart", 50, 100)
    heart_2 = Interface("heart", 120, 100)
    heart_3 = Interface("heart", 190, 100)
    # on the right
    # heart_1 = Interface("heart", 600, 100)
    # heart_2 = Interface("heart", 670, 100)
    # heart_3 = Interface("heart", 740, 100)
    all_sprites.add(mage)
    all_sprites.add(heart_1, heart_2, heart_3)
    interface.add(heart_1, heart_2, heart_3)
    
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = "#5B115B"

# initialization                    
pygame.init()
screen_width = 800
screen_height = 400
game_active = False 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spellcast 2D") 

# global file imports
# player
main_font = pygame.font.Font("fonts/VisitorRus.ttf", 60)
mage_1_surf = pygame.image.load("images/mage/mage1.png").convert_alpha()

# enemies
goblin_1_surf = pygame.image.load("images/goblin/goblin1.png").convert_alpha()
bat_1_surf = pygame.image.load("images/bat/bat1.png").convert_alpha()

# rectangles creation
mage_1_rect = mage_1_surf.get_rect()
goblin_1_rect = goblin_1_surf.get_rect()
bat_1_rect = bat_1_surf.get_rect()

# enemies randomizer
enemies_types = ["goblin", "bat", "goblin", "bat"]
spawn_chance = enemies_types[randint(0, 3)]
spawn_delay = 2000
last_spawn_time = pygame.time.get_ticks()

# sprites group
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
interface = pygame.sprite.Group()

# variables
collide_counter = 0

# running game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit() 
             
        if game_active == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         mage.move_left()
        #     elif event.key == pygame.K_d:
        #         mage.move_right()
            
    if game_active:
        enemies_spawn()
        draw_game()
        projectile_collision()
        player_collision()
    else:
        restart_game()
        game_over_screen()
        

    pygame.display.update()
    clock.tick(60)
        











