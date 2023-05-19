import pygame
from utility import *
from settings import *


# <<<<<<<<<<<<<<<<<< SEED CLASS

class Seed(pygame.sprite.Sprite):

    def __init__(self, seed_type, groups, soil):
        super().__init__(groups)
        self.seed_type = seed_type
        self.soil = soil
        self.frames = load_folder(f"../Graphics/Environment/CROPS/{self.seed_type}")
        self.growth_level = 0
        self.max_growth_level = len(self.frames) - 1

        self.image = self.frames[self.growth_level]
        self.surface = self.frames[self.growth_level]
        self.rect = self.surface.get_rect(center=self.soil.rect.center)
        self.current_layer = LAYER["PLANT"]
        self.growth_progress = 0

    def grow(self):
        self.growth_progress += 1
        if self.growth_progress >= 10:
            if self.growth_level < self.max_growth_level:
                self.growth_level += 1
                self.image = self.frames[self.growth_level]
                self.surface = self.frames[self.growth_level]
                self.rect = self.surface.get_rect(center=self.soil.rect.center)
                self.growth_progress = 0

    def harvest(self):
       if self.growth_level >= self.max_growth_level:
           self.kill()
           return self.seed_type


# >>>>>>>>>>>>>>>>>> SEED CLASS
