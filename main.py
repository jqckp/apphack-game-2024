import pygame
import sys
import os

pygame.init()

FPS = 60

WIZARD = pygame.image.load(os.path.join('Assets', 'wizard.png'))
WIZARD = pygame.transform.scale(WIZARD, (100, 100))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

def make_game():
    WIN.blit(WIZARD, (300, 100))
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    make_game()

pygame.quit()
sys.exit()