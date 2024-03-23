import pygame
import sys
import os

pygame.init()

FPS = 60


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

    display_frame(COWBOY_POSITION)

pygame.quit()
sys.exit()