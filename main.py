import pygame
import sys
import os

pygame.init()

FPS = 60

clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaghetti Fantasy")

MAIN_SPRITE = pygame.image.load(os.path.join(''))

running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()