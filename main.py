import pygame
import sys
import os

pygame.init()

FPS = 60

<<<<<<< HEAD
COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (50, 60))
COWBOY_X = 300
COWBOY_Y = 100
COWBOY_speed = 10
COWBOY_facing_right = True
=======
>>>>>>> 8d7fa5d9ecb424162b29d64a2c83fc51589bbd0c

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (100, 100))


COWBOY_POSITION = pygame.Rect(425, 225, 100, 100)

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")




def display_frame(COWBOY_POSITION):
    WIN.blit(COWBOY, (COWBOY_POSITION.x, COWBOY_POSITION.y))
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        COWBOY_X -= COWBOY_speed
        if COWBOY_facing_right:
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            COWBOY_facing_right = False
    if keys[pygame.K_d]:
        COWBOY_X += COWBOY_speed
        if not(COWBOY_facing_right):
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            COWBOY_facing_right = True
    if keys[pygame.K_w]:
        COWBOY_Y -= COWBOY_speed
    if keys[pygame.K_s]:
        COWBOY_Y += COWBOY_speed

    COWBOY_X = max(0, min(COWBOY_X, WIDTH - COWBOY.get_width()))
    COWBOY_Y = max(0, min(COWBOY_Y, HEIGHT - COWBOY.get_height()))
    make_game()
=======
    display_frame(COWBOY_POSITION)
>>>>>>> 8d7fa5d9ecb424162b29d64a2c83fc51589bbd0c

pygame.quit()
sys.exit()