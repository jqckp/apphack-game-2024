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
=======

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (100, 100))


COWBOY_POSITION = pygame.Rect(425, 225, 100, 100)
>>>>>>> acf7ec176d8e9435e7b59fb26467e7f4538e709d

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

<<<<<<< HEAD
def make_game():
    WIN.fill((0,0,0))
    WIN.blit(COWBOY, (COWBOY_X, COWBOY_Y))
    pygame.display.update()
=======



def display_frame(COWBOY_POSITION):
    WIN.blit(COWBOY, (COWBOY_POSITION.x, COWBOY_POSITION.y))
    pygame.display.flip()
>>>>>>> acf7ec176d8e9435e7b59fb26467e7f4538e709d

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        COWBOY_X -= COWBOY_speed
        COWBOY = pygame.transform.flip(COWBOY, True, False)
    if keys[pygame.K_RIGHT]:
        COWBOY_X += COWBOY_speed
        COWBOY = pygame.transform.flip(COWBOY, True, False)
    if keys[pygame.K_UP]:
        COWBOY_Y -= COWBOY_speed
    if keys[pygame.K_DOWN]:
        COWBOY_Y += COWBOY_speed

    COWBOY_X = max(0, min(COWBOY_X, WIDTH - COWBOY.get_width()))
    COWBOY_Y = max(0, min(COWBOY_Y, HEIGHT - COWBOY.get_height()))
    make_game()
=======
    display_frame(COWBOY_POSITION)
>>>>>>> acf7ec176d8e9435e7b59fb26467e7f4538e709d

pygame.quit()
sys.exit()