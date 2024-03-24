import random
import pygame 

import sys
import os
import button
import player_bullet
from skeleton import skeleton
import math

pygame.init()

FPS = 60
BLACK = ((0,0,0))

in_level_0 = True
in_level_1 = False
in_level_2 = False
in_level_3 = False

CB_SCALE_W = 40
CB_SCALE_H = 48
TREE_SCALE_H = 80

cowboy_speed = 4

skeletons = [skeleton(), skeleton(), skeleton()]

COWBOY = pygame.image.load(os.path.join('Assets', "Player_Character.png"))
COWBOY = pygame.transform.scale(COWBOY, (CB_SCALE_W, CB_SCALE_H))

ob = []

COWBOY_POSITION = pygame.Rect(0, 0, CB_SCALE_W, CB_SCALE_H)

FIRE_img = pygame.image.load(os.path.join('Assets', 'fire.png'))
FIRE = pygame.transform.scale(FIRE_img, (50, 50))

GAME_SQUARE = pygame.image.load(os.path.join('Assets', 'Grass_Background_dirtpaths.png'))
GAME_SQUARE = pygame.transform.scale(GAME_SQUARE, (630, 630))

GAME_SQUARE_1 = pygame.image.load(os.path.join('Assets', 'Grass_Background_Pond.png'))
GAME_SQUARE_1 = pygame.transform.scale(GAME_SQUARE_1, (630, 630))

GAME_SQUARE_2 = pygame.image.load(os.path.join('Assets', 'Grass_Background_Rocks.png'))
GAME_SQUARE_2 = pygame.transform.scale(GAME_SQUARE_2, (630, 630))

GAME_SQUARE_3 = pygame.image.load(os.path.join('Assets', 'Dungeon_Background.png'))
GAME_SQUARE_3 = pygame.transform.scale(GAME_SQUARE_3, (630, 630))

WIDTH, HEIGHT = 630, 630
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

cowboy_facing_right = True
cowboy_facing_left = False
cowboy_facing_up = False
cowboy_facing_down = False

level_0 = [['a', 0, 0, 0, 'c', 0, 0, 3, 'a', 0, 'a', 0, 0], 
           [0, 'b', 0, 0, 0, 0, 0, 'c', 0, 0, 0, 'a', 0], 
           ['d', 'c', 'd', 'a', 'b', 'a', 0, 'a','b', 0, 0, 0, 0], 
           ['a', 'a', 0, 'b', 0, 0, 0, 0, 0,'b', 0, 'c', 0], 
           [0, 'a', 'c', 0, 0, 0, 0, 0, 0, 0,'c', 0, 0], 
           [1, 0, 'd', 0, 0, 0, 0, 0, 0, 0,'d', 0, 2], 
           [0, 0, 0, 0, 0, 'f', 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 'd', 0, 0, 0, 0, 0, 0, 0,'d', 0, 0],
           ['c', 'b', 'c', 0, 0, 0, 0, 0, 0, 0,'c', 'd', 0],
           [0, 0, 0, 'b', 0, 0, 0, 0, 0,'b', 0, 0, 'd'],
           [0, 'a', 0, 0, 'b', 'a', 0, 'a','b', 'c', 0, 'b', 0],
           ['d', 0, 0, 0, 0, 0, 0, 0, 0, 'c', 0, 'b', 0],
           [0, 'c', 0, 'a', 0, 0, 9, 0, 'd', 0, 0, 'c', 0]]

level_1 = [[0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 5, 5, 5],
            [0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5],
            [0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
            [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

level_2= [['a', 'c', 'a','d', 0, 0, 0, 0, 0, 0, 'c', 'd', 'a'],
            ['b','d','b', 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'a'],
            ['c', 'a', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'd', 'c'],
            ['d', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'd'],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'b'],
            ['a', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'd', 'a'],
            ['b', 'c', 0, 0, 0, 0, 0, 0, 0, 'a', 'b', 'b', 'c'],
            ['a', 'd', 'c', 'a', 0, 0, 0, 0, 'd', 'b', 'c', 'a', 'd'],
            ['b', 'b', 'd', 'b', 'd', 0, 0, 0, 'a', 'c', 'd', 'c', 'a']]
level_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 'f', 0, 0, 'd', 0, 0, 0, 0, 0, 0, 'f', 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 'f', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'f', 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]]

init_y = 6
for row in range(len(level_0)):
    init_x = 6
    for column in range(len(level_0[row])):
        if level_0[row][column] == 9:
            COWBOY_POSITION.x = init_x
            COWBOY_POSITION.y = init_y
        init_x += 48
    init_y += 48

clock = pygame.time.Clock()
running = True

def rock():
    random_number = random.randint(1, 4)
    return "Rock" + str(random_number) + ".png"

def load_level_0(COWBOY_POSITION):
    global level_0_rect
    global level_1_rect
    global level_2_rect
    global level_3_rect

    global in_level_0
    global in_level_1
    global in_level_2
    global in_level_3

    init_x = 6
    init_y = 6

    WIN.blit(GAME_SQUARE, (0, 0))
    WIN.blit(COWBOY, COWBOY_POSITION)

    for row in range(len(level_0)):
        init_x = 6
        for column in range(len(level_0[row])):
            if level_0[row][column] == 'a':
                tree_img = pygame.image.load(os.path.join('Assets', 'Tree_Hole_left.png'))
                tree_img = pygame.transform.scale(tree_img, (CB_SCALE_W, TREE_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, TREE_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(tree_img, ROCK_POSITION)
            if level_0[row][column] == 'b':
                tree_img = pygame.image.load(os.path.join('Assets', 'Tree_Hole_right.png'))
                tree_img = pygame.transform.scale(tree_img, (CB_SCALE_W, TREE_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, TREE_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(tree_img, ROCK_POSITION)
            if level_0[row][column] == 'c':
                tree_img = pygame.image.load(os.path.join('Assets', 'Tree_Plain_right.png'))
                tree_img = pygame.transform.scale(tree_img, (CB_SCALE_W, TREE_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, TREE_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(tree_img, ROCK_POSITION)
            if level_0[row][column] == 'd':
                tree_img = pygame.image.load(os.path.join('Assets', 'Tree_Stump_left.png'))
                tree_img = pygame.transform.scale(tree_img, (CB_SCALE_W, TREE_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, TREE_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(tree_img, ROCK_POSITION)
            if level_0[row][column] == 'f':
                FIRE_img = pygame.image.load(os.path.join('Assets', 'fire.png'))
                FIRE_img = pygame.transform.scale(FIRE_img, (100, 100))
                FIRE_POS = pygame.Rect(init_x, init_y, 100, 100)
                WIN.blit(FIRE_img, FIRE_POS)
            if level_0[row][column] == 1:
                level_1_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            if level_0[row][column] == 2:
                level_2_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            if level_0[row][column] == 3:
                level_3_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            init_x += 48
        init_y += 48

    for i in range (len(skeletons)):
        WIN.blit(skeletons[i].SKELETON, skeletons[i].SKELETON_POSITION)
        if (COWBOY_POSITION.colliderect(skeletons[i].SKELETON_POSITION)):
            print("you lose!")
    
        distance = math.sqrt((COWBOY_POSITION.x - skeletons[i].get_x_pos())**2 + (COWBOY_POSITION.y - skeletons[i].get_y_pos())**2)
        if distance < 200:
            print("Moving towards player")

    if (COWBOY_POSITION.colliderect(level_2_rect)):
        in_level_0 = False
        in_level_1 = False
        in_level_2 = True
        in_level_3 = False
        COWBOY_POSITION.x = 6
    elif (COWBOY_POSITION.colliderect(level_1_rect)):
        in_level_0 = False
        in_level_1 = True
        in_level_2 = False
        in_level_3 = False
        COWBOY_POSITION.x = WIDTH - COWBOY.get_width()
    elif (COWBOY_POSITION.colliderect(level_3_rect)):
        in_level_0 = False
        in_level_1 = False
        in_level_2 = False
        in_level_3 = True
        COWBOY_POSITION.x = WIDTH/2 + COWBOY.get_width()
        COWBOY_POSITION.y = HEIGHT - COWBOY.get_height()

    

    pygame.display.update()

def load_level_1():
    global level_0_rect
    global level_1_rect
    global level_2_rect
    global level_3_rect

    global in_level_0
    global in_level_1
    global in_level_2
    global in_level_3

    init_x = 6
    init_y = 6

    WIN.fill(BLACK)
    WIN.blit(GAME_SQUARE_1, (0, 0))
    WIN.blit(COWBOY, COWBOY_POSITION)

    for row in range(len(level_1)):
        init_x = 6
        for column in range(len(level_1[row])):
            if level_1[row][column] == 5:
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock1.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_1[row][column] == 5:
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock2.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_1[row][column] == 'c':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock3.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_1[row][column] == 'd':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock4.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_1[row][column] == 9:
                level_0_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            init_x += 48
        init_y += 48
    
    if (COWBOY_POSITION.colliderect(level_0_rect)):
        in_level_0 = True
        in_level_1 = False
        in_level_2 = False
        in_level_3 = False
        COWBOY_POSITION.x = 6
    pygame.display.update()

def load_level_2():
    global level_0_rect
    global level_1_rect
    global level_2_rect
    global level_3_rect

    global in_level_0
    global in_level_1
    global in_level_2
    global in_level_3

    init_x = 6
    init_y = 6

    WIN.fill(BLACK)
    WIN.blit(GAME_SQUARE_2, (0, 0))
    WIN.blit(COWBOY, COWBOY_POSITION)

    for row in range(len(level_2)):
        init_x = 6
        for column in range(len(level_2[row])):
            if level_2[row][column] == 'a':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock1.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_2[row][column] == 'b':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock2.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_2[row][column] == 'c':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock3.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_2[row][column] == 'a':
                rock_img = pygame.image.load(os.path.join('Assets', 'Rock4.png'))
                rock_img = pygame.transform.scale(rock_img, (CB_SCALE_W, CB_SCALE_H))
                ROCK_POSITION = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_2[row][column] == 9:
                level_0_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            init_x += 48
        init_y += 48
    
    if (COWBOY_POSITION.colliderect(level_0_rect)):
        in_level_0 = True
        in_level_1 = False
        in_level_2 = False
        in_level_3 = False
        COWBOY_POSITION.x = WIDTH - COWBOY.get_width()
    pygame.display.update()

def load_level_3():
    global level_0_rect
    global level_1_rect
    global level_2_rect
    global level_3_rect

    global in_level_0
    global in_level_1
    global in_level_2
    global in_level_3

    init_x = 6
    init_y = 6

    WIN.fill(BLACK)
    WIN.blit(GAME_SQUARE_3, (0, 0))
    WIN.blit(COWBOY, COWBOY_POSITION)

    for row in range(len(level_3)):
        init_x = 6
        for column in range(len(level_3[row])):
            if level_3[row][column] == 'd':
                rock_img = pygame.image.load(os.path.join('Assets', 'dragon.png'))
                rock_img = pygame.transform.scale(rock_img, (200, 400))
                ROCK_POSITION = pygame.Rect(init_x, init_y, 200, 400)
                ob.append(ROCK_POSITION)
                WIN.blit(rock_img, ROCK_POSITION)
            if level_0[row][column] == 'f':
                FIRE_img = pygame.image.load(os.path.join('Assets', 'fire.png'))
                FIRE_img = pygame.transform.scale(FIRE_img, (100, 100))
                FIRE_POS = pygame.Rect(init_x, init_y, 100, 100)
                WIN.blit(FIRE_img, FIRE_POS)
            if level_3[row][column] == 9:
                level_0_rect = pygame.Rect(init_x, init_y, CB_SCALE_W, CB_SCALE_H)
            init_x += 48
        init_y += 48
    
    if (COWBOY_POSITION.colliderect(level_0_rect)):
        in_level_0 = True
        in_level_1 = False
        in_level_2 = False
        in_level_3 = False
        COWBOY_POSITION.x = WIDTH/2 - COWBOY.get_width()
        COWBOY_POSITION.y = 6
    pygame.display.update()

def read_player_move(keys):
   
    global COWBOY
    global cowboy_facing_right
    global cowboy_facing_left
    global cowboy_facing_up
    global cowboy_facing_down

    if keys[pygame.K_a]:
        COWBOY_POSITION.x -= cowboy_speed
        if not(cowboy_facing_left):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
            COWBOY = pygame.transform.scale(COWBOY, (CB_SCALE_W, CB_SCALE_H))
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            cowboy_facing_left = True
            cowboy_facing_up = False
            cowboy_facing_down = False
            cowboy_facing_right = False
                
    if keys[pygame.K_d]:
        COWBOY_POSITION.x += cowboy_speed
        if not(cowboy_facing_right):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
            COWBOY = pygame.transform.scale(COWBOY, (CB_SCALE_W, CB_SCALE_H))
            cowboy_facing_right = True
            cowboy_facing_up = False
            cowboy_facing_down = False
            cowboy_facing_left = False
            
    if keys[pygame.K_w]:
        COWBOY_POSITION.y -= cowboy_speed
        if not(cowboy_facing_up):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_up.png'))
            COWBOY = pygame.transform.scale(COWBOY, (CB_SCALE_W, CB_SCALE_H))
            cowboy_facing_up = True
            cowboy_facing_down = False
            cowboy_facing_right = False
            cowboy_facing_left = False

    if keys[pygame.K_s]:
        COWBOY_POSITION.y += cowboy_speed
        if not(cowboy_facing_down):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_down.png'))
            COWBOY = pygame.transform.scale(COWBOY, (CB_SCALE_W, CB_SCALE_H))
            cowboy_facing_down = True
            cowboy_facing_left = False
            cowboy_facing_up = False
            cowboy_facing_right = False
        

    COWBOY_POSITION.x = max(0, min(COWBOY_POSITION.x, WIDTH - COWBOY.get_width()))
    COWBOY_POSITION.y = max(0, min(COWBOY_POSITION.y, HEIGHT - COWBOY.get_height()))

def play():
    

    pygame.display.set_caption("Play")
    pygame.mixer.music.load(os.path.join('Assets','2021-08-16_-_8_Bit_Adventure_-_www.FesliyanStudios.com.mp3'))
    pygame.mixer.music.play(-1)

    player_bullets = []

    global running
    global clock
    global WIN

    gun_sound = pygame.mixer.Sound(os.path.join('Assets','9mm-pistol-shoot-short-reverb-7152.mp3'))

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gun_sound.play()
                    player_bullets.append(player_bullet.Player_Bullet(COWBOY_POSITION.x, COWBOY_POSITION.y))

        read_player_move(pygame.key.get_pressed())
        if in_level_1:
            load_level_1()

        if in_level_2:
            load_level_2()
        
        if in_level_3:
            load_level_3()

        if in_level_0:
            load_level_0(COWBOY_POSITION)
        
        for bullet in player_bullets:
            if cowboy_facing_right and not(bullet.creation):
                bullet.right(WIN)
            elif  cowboy_facing_left and not(bullet.creation):
                bullet.left(WIN)
            elif  cowboy_facing_up and not(bullet.creation):
                bullet.up(WIN)
            elif  cowboy_facing_down and not(bullet.creation):
                bullet.down(WIN)
            elif bullet.dir == 2 and bullet.creation:
                bullet.right(WIN)
            elif  bullet.dir == 1 and bullet.creation:
                bullet.left(WIN)
            elif  bullet.dir == 3 and bullet.creation:
                bullet.up(WIN)
            elif  bullet.dir == 4 and bullet.creation:
                bullet.down(WIN)
            if bullet.x > 650 or bullet.x < -50 or bullet.y > 650 or bullet.y < -50:
                player_bullets.remove(bullet)


def main_menu():
    global running
    global clock

    clock.tick(FPS)

    pygame.display.set_caption("Menu")
    start_screen = pygame.image.load(os.path.join('Assets', 'Start_Screen_Background.png'))
    start_screen = pygame.transform.scale(start_screen, (WIDTH, HEIGHT))
    play_img = pygame.image.load(os.path.join('Assets', 'Start_Button.png'))
    play_button = button.Button(170, 250, play_img, 5)
    pygame.mixer.music.load(os.path.join('Assets','SLOWER2019-01-02_-_8_Bit_Menu_-_David_Renda_-_FesliyanStudios.com.mp3'))
    pygame.mixer.music.play(-1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        WIN.blit(start_screen, (0, 0))
        if play_button.draw(WIN):
            pygame.mixer.music.stop()
            play()
        pygame.display.update()
main_menu()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()