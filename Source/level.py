import pygame
from settings import *
from player import Player
from hud import Hud

# <<<<<<<<<<<<<<<<<< LEVEL CLASS

class Level:

    def __init__(self):
        self.main_display_surface = pygame.display.get_surface()
        self.master_sprite_group = CameraGroup()
        self.setup()
        self.hud = Hud(self.current_player)
    def setup(self):
        self.current_player = Player((640, 360), self.master_sprite_group)

    def run(self, delta_time):
        self.main_display_surface.fill("White")
        self.master_sprite_group.draw()
        self.master_sprite_group.update(delta_time)
        self.hud.display_inventory()


# >>>>>>>>>>>>>>>>>> LEVEL CLASS


# <<<<<<<<<<<<<<<<<< LEVEL CLASS

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.main_display_surface = pygame.display.get_surface()

    def draw(self):
        for sprite in self.sprites():
            self.main_display_surface.blit(sprite.image, sprite.rect)



# >>>>>>>>>>>>>>>>>> LEVEL CLASS