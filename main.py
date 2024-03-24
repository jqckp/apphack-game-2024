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



cowboy_speed = 4

skeletons = [skeleton(), skeleton(), skeleton()]

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (75, 75))

GAME_SQUARE = pygame.image.load(os.path.join('Assets', 'Grass_Background_105x105.png'))
GAME_SQUARE = pygame.transform.scale(GAME_SQUARE, (600, 600))

COWBOY_POSITION = pygame.Rect(125, 25, 75, 75)
COWBOY_POSITION = COWBOY.get_rect(center = (300, 300))

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

cowboy_facing_right = True
cowboy_facing_left = False
cowboy_facing_up = False
cowboy_facing_down = False

clock = pygame.time.Clock()
running = True

def display_frame(COWBOY_POSITION):
    WIN.fill(BLACK)
    WIN.blit(GAME_SQUARE, (0, 0))
    WIN.blit(COWBOY, COWBOY_POSITION)

    for i in range (len(skeletons)):
        WIN.blit(skeletons[i].SKELETON, skeletons[i].SKELETON_POSITION)
        if (COWBOY_POSITION.colliderect(skeletons[i].SKELETON_POSITION)):
            print("you lose!")
    
        distance = math.sqrt((COWBOY_POSITION.x - skeletons[i].get_x_pos())**2 + (COWBOY_POSITION.y - skeletons[i].get_y_pos())**2)
        if distance < 200:
            print("Moving towards player")


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
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            cowboy_facing_left = True
            cowboy_facing_up = False
            cowboy_facing_down = False
            cowboy_facing_right = False
                
    if keys[pygame.K_d]:
        COWBOY_POSITION.x += cowboy_speed
        if not(cowboy_facing_right):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            cowboy_facing_right = True
            cowboy_facing_up = False
            cowboy_facing_down = False
            cowboy_facing_left = False
            
    if keys[pygame.K_w]:
        COWBOY_POSITION.y -= cowboy_speed
        if not(cowboy_facing_up):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_up.png'))
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            cowboy_facing_up = True
            cowboy_facing_down = False
            cowboy_facing_right = False
            cowboy_facing_left = False

    if keys[pygame.K_s]:
        COWBOY_POSITION.y += cowboy_speed
        if not(cowboy_facing_down):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_down.png'))
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            cowboy_facing_down = True
            cowboy_facing_left = False
            cowboy_facing_up = False
            cowboy_facing_right = False
        

    COWBOY_POSITION.x = max(0, min(COWBOY_POSITION.x, WIDTH - COWBOY.get_width()))
    COWBOY_POSITION.y = max(0, min(COWBOY_POSITION.y, HEIGHT - COWBOY.get_height()))

def play():
    

    pygame.display.set_caption("Play")
    pygame.mixer.music.load(os.path.join('Assets','2019-01-15_-_You_Just_Got_Pwned_-_David_Fesliyan.mp3'))
    pygame.mixer.music.play(-1)

    player_bullets = []

    global running
    global clock
    global WIN

    click_sound = pygame.mixer.Sound(os.path.join('Assets','9mm-pistol-shoot-short-reverb-7152.mp3'))

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_sound.play()
                    player_bullets.append(player_bullet.Player_Bullet(COWBOY_POSITION.x, COWBOY_POSITION.y))

        read_player_move(pygame.key.get_pressed())
        
        display_frame(COWBOY_POSITION)

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