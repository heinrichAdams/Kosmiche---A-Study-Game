import pygame
from settings import *


# <<<<<<<<<<<<<<<<<< PLAYER CLASS

class Player(pygame.sprite.Sprite):

    def __init__(self, position, group):
        super().__init__(group)
        self.image = pygame.Surface((32, 64))
        self.image.fill("Green")
        self.rect = self.image.get_rect(center=position)
        self.move_direction = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self):
        all_input = pygame.key.get_pressed()
        # UP
        if all_input[pygame.K_w]:
            self.move_direction.y = -1
        # DOWN
        elif all_input[pygame.K_s]:
            self.move_direction.y = 1
        else:
            self.move_direction.y = 0
        # LEFT
        if all_input[pygame.K_a]:
            self.move_direction.x = -1
        # RIGHT
        elif all_input[pygame.K_d]:
            self.move_direction.x = 1
        else:
            self.move_direction.x = 0

    def movement(self, delta_time):
        self.position += self.move_direction * self.speed * delta_time
        self.rect.center = self.position

    def update(self, delta_time):
        self.input()
        self.movement(delta_time)

# >>>>>>>>>>>>>>>>>> PLAYER CLASS
