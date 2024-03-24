import pygame
import os
import random




class skeleton:

    
    def __init__(self):
        self.x_coord = random.randint(0, 600)
        self.y_coord = random.randint(0, 600)
        self.SKELETON = pygame.image.load(os.path.join('Assets', 'Skeleton_Enemy.png'))
        self.SKELETON = pygame.transform.scale(self.SKELETON, (75, 75))
        self.SKELETON_POSITION = self.SKELETON.get_rect(center = (self.x_coord, self.y_coord))
        self.projectile_speed = 5
        self.damage = 3
        self.projectile_size = (10, 10)
        self.shots_to_kill = 3
        self.health = 3
        


    
    


