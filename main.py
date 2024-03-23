import pygame
import sys
import os

pygame.init()

FPS = 60

WIZARD = pygame.image.load(os.path.join('Assets', 'Player_Character.png'))
WIZARD = pygame.transform.scale(WIZARD, (100, 100))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

def display_frame():
    WIN.blit(WIZARD, (300, 100))
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_frame()

pygame.quit()
sys.exit()