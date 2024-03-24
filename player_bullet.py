import math
import os
import pygame

class Player_Bullet():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 30
        self.creation = False
        self.dir = 0
        
    def left(self, WIN):
        if not(self.creation):
            self.y += 24
            self.x += 6
        self.x -= self.speed
        self.creation = True
        self.dir = 1
        
        bullet = pygame.image.load(os.path.join('Assets', 'Bullet.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (14, 2))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def right(self, WIN):
        if not(self.creation):
            self.y += 25
            self.x += 18
        self.x += self.speed
        self.creation = True
        self.dir = 2

        bullet = pygame.image.load(os.path.join('Assets', 'Bullet_vertical.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (14, 2))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def up(self, WIN):
        if not(self.creation):
            self.x += 6
            self.y += 10
        self.y -= self.speed
        self.creation = True
        self.dir = 3

        bullet = pygame.image.load(os.path.join('Assets', 'Bullet_vertical.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (2, 14))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()
    def down(self, WIN):
        self.y += self.speed
        if not(self.creation):
            self.x += 35
            self.y += 20
        self.creation = True
        self.dir = 4

        bullet = pygame.image.load(os.path.join('Assets', 'Bullet.png')).convert_alpha()
        bullet = pygame.transform.scale(bullet, (2, 14))
        WIN.blit(bullet,(int(self.x), int(self.y)))
        pygame.display.update()