import pygame
from settings import *

# <<<<<<<<<<<<<<<<<< BASE CLASS

class Base(pygame.sprite.Sprite):
    def __init__(self, position, image, group, layer=LAYER["MAIN"]):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.current_layer = layer
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

# >>>>>>>>>>>>>>>>>> BASE CLASS