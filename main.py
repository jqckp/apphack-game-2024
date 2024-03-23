import pygame
import sys
import os

pygame.init()

FPS = 60

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (50, 60))
COWBOY_X = 300
COWBOY_Y = 100
COWBOY_speed = 10

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

def make_game():
    WIN.fill((0,0,0))
    WIN.blit(COWBOY, (COWBOY_X, COWBOY_Y))
    pygame.display.update()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

pygame.quit()
sys.exit()