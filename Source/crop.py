import pygame
from utility import *
from seed import *


# <<<<<<<<<<<<<<<<<< CROP CLASS

class Crop(pygame.sprite.Sprite, Seed):

    def __init__(self, group, seed_type):
        super().__init__(group)
        self.seed_type = seed_type

# >>>>>>>>>>>>>>>>>> CROP CLASS
