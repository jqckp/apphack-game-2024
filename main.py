import pygame
import sys
import os

pygame.init()

FPS = 60
BLACK = ((0,0,0))

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (50, 60))
COWBOY_X = 300
COWBOY_Y = 100
COWBOY_speed = 4
COWBOY_facing_right = True

COWBOY = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
COWBOY = pygame.transform.scale(COWBOY, (75, 75))


COWBOY_POSITION = pygame.Rect(425, 225, 100, 100)

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")




def display_frame(COWBOY_POSITION):
    WIN.fill(BLACK)
    WIN.blit(COWBOY, (COWBOY_POSITION.x, COWBOY_POSITION.y))
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        COWBOY_POSITION.x -= COWBOY_speed
        if COWBOY_facing_right:
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            COWBOY_facing_right = False
    if keys[pygame.K_d]:
        COWBOY_POSITION.x += COWBOY_speed
        if not(COWBOY_facing_right):
            COWBOY = pygame.transform.flip(COWBOY, True, False)
            COWBOY_facing_right = True
    if keys[pygame.K_w]:
        COWBOY_POSITION.y -= COWBOY_speed
    if keys[pygame.K_s]:
        COWBOY_POSITION.y += COWBOY_speed

    COWBOY_POSITION.x = max(0, min(COWBOY_POSITION.x, WIDTH - COWBOY.get_width()))
    COWBOY_POSITION.y = max(0, min(COWBOY_POSITION.y, HEIGHT - COWBOY.get_height()))
    display_frame(COWBOY_POSITION)

pygame.quit()
sys.exit()