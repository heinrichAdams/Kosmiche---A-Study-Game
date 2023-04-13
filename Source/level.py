import pygame
from settings import *
from player import Player


# <<<<<<<<<<<<<<<<<< LEVEL CLASS

class Level:

    def __init__(self):
        self.main_display_surface = pygame.display.get_surface()
        self.master_sprite_group = pygame.sprite.Group()
        self.setup()

    def setup(self):
        self.current_player = Player((640, 360), self.master_sprite_group)

    def run(self, delta_time):
        self.main_display_surface.fill("White")
        self.master_sprite_group.draw(self.main_display_surface)
        self.master_sprite_group.update(delta_time)

# >>>>>>>>>>>>>>>>>> LEVEL CLASS
