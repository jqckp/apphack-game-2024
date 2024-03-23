import pygame
import sys
import os

pygame.init()

FPS = 60
BLACK = ((0,0,0))

cowboy_speed = 4



COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (50, 60))



COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (75, 75))


COWBOY_POSITION = pygame.Rect(425, 225, 100, 100)

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")



 
def display_frame(COWBOY_POSITION):
    WIN.fill(BLACK)
    WIN.blit(COWBOY, (COWBOY_POSITION.x, COWBOY_POSITION.y))
    pygame.display.update()


def read_player_move(keys):
   
    global COWBOY
    cowboy_facing_right = True
    cowboy_facing_up = False
    cowboy_facing_down = False

    if keys[pygame.K_a]:
        COWBOY_POSITION.x -= cowboy_speed
        COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
        COWBOY = pygame.transform.scale(COWBOY, (75, 75))
        if cowboy_facing_right:
                COWBOY = pygame.transform.flip(COWBOY, True, False)
                
    if keys[pygame.K_d]:
        COWBOY_POSITION.x += cowboy_speed
        COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
        COWBOY = pygame.transform.scale(COWBOY, (75, 75))
        if not(cowboy_facing_right):
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            
    if keys[pygame.K_w]:
        COWBOY_POSITION.y -= cowboy_speed
        if not(cowboy_facing_up):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_up.png'))
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            cowboy_facing_up = True

    if keys[pygame.K_s]:
        if not(cowboy_facing_down):
            COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character_down.png'))
            COWBOY = pygame.transform.scale(COWBOY, (75, 75))
            cowboy_facing_down = True

        COWBOY_POSITION.y += cowboy_speed
        

    COWBOY_POSITION.x = max(0, min(COWBOY_POSITION.x, WIDTH - COWBOY.get_width()))
    COWBOY_POSITION.y = max(0, min(COWBOY_POSITION.y, HEIGHT - COWBOY.get_height()))
    
    

    


clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    read_player_move(pygame.key.get_pressed())
    
    display_frame(COWBOY_POSITION)

pygame.quit()
sys.exit()