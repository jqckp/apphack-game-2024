import math
import os
import pygame

class Player_Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.creation = False
        self.dir = 0
        
    def left(self, WIN):
        if not(self.creation):
            self.y += 20
        self.x -= self.speed
        self.creation = True
        self.dir = 1
        
        bullet = pygame.image.load(os.path.join('Assets', 'Player_Character.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (25, 25))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def right(self, WIN):
        if not(self.creation):
            self.y += 20
        self.x += self.speed
        self.creation = True
        self.dir = 2

        bullet = pygame.image.load(os.path.join('Assets', 'Player_Character.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (25, 25))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def up(self, WIN):
        self.y -= self.speed
        self.creation = True
        self.dir = 3

        bullet = pygame.image.load(os.path.join('Assets', 'Player_Character.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (25, 25))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def down(self, WIN):
        self.y += self.speed
        if not(self.creation):
            self.x += 50
        self.creation = True
        self.dir = 4

        bullet = pygame.image.load(os.path.join('Assets', 'Player_Character.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (25, 25))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()