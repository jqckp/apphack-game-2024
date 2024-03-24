import pygame
import os
import random




class goblin:

    
    def __init__(self):
        self.x_coord = random.randint(0, 600)
        self.y_coord = random.randint(0, 600)
        self.GOBLIN = pygame.image.load(os.path.join('Assets', 'Goblin_enemy.png'))
        self.GOBLIN = pygame.transform.scale(self.GOBLIN, (75, 75))
        self.GOBLIN_POSITION = self.GOBLIN.get_rect(center = (self.x_coord, self.y_coord))
        self.projectile_speed = 5
        self.damage = 3
        self.projectile_size = (10, 10)
        self.shots_to_kill = 3
        self.health = 3

    def attack(self):
        print("I am attacking")
        
    def alerted(self):
        pass

    def get_x_pos(self):
        return self.x_coord
    
    def get_y_pos(self):
        return self.y_coord