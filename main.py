import pygame
import sys
import os
import button

pygame.init()

FPS = 60
BLACK = ((0,0,0))

cowboy_speed = 4
cowboy_facing_right = True

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (50, 60))

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (75, 75))

COWBOY_POSITION = pygame.Rect(425, 225, 100, 100)

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

clock = pygame.time.Clock()
running = True

def display_frame(COWBOY_POSITION):
    WIN.fill(BLACK)
    WIN.blit(COWBOY, (COWBOY_POSITION.x, COWBOY_POSITION.y))
    pygame.display.flip()

def read_player_move(keys):
   
    global COWBOY
    global cowboy_facing_right
    
    #keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        COWBOY_POSITION.x -= cowboy_speed
        if cowboy_facing_right:
                COWBOY = pygame.transform.flip(COWBOY, True, False)
                cowboy_facing_right = False
    if keys[pygame.K_d]:
        COWBOY_POSITION.x += cowboy_speed
        if not(cowboy_facing_right):
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            cowboy_facing_right = True
    if keys[pygame.K_w]:
        COWBOY_POSITION.y -= cowboy_speed
    if keys[pygame.K_s]:
        COWBOY_POSITION.y += cowboy_speed
    COWBOY_POSITION.x = max(0, min(COWBOY_POSITION.x, WIDTH - COWBOY.get_width()))
    COWBOY_POSITION.y = max(0, min(COWBOY_POSITION.y, HEIGHT - COWBOY.get_height()))

def play():
    pygame.display.set_caption("Play")
    pygame.mixer.music.load(os.path.join('Assets','2019-01-15_-_You_Just_Got_Pwned_-_David_Fesliyan.mp3'))
    pygame.mixer.music.play(-1)
    global running
    global clock
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        read_player_move(pygame.key.get_pressed())
        
        display_frame(COWBOY_POSITION)

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