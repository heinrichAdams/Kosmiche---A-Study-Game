import pygame
from settings import *
from player import Player
from hud import Hud
from question_dialog import QuestionDialog
from sprites import Base
from pytmx.util_pygame import load_pygame

# <<<<<<<<<<<<<<<<<< LEVEL CLASS

class Level:

    def __init__(self):
        self.main_display_surface = pygame.display.get_surface()
        self.master_sprite_group = CameraGroup()
        self.setup()
        self.hud = Hud(self.current_player)
        self.question_dialog = QuestionDialog(self.current_player)

    def popups(self):
        if self.current_player.in_dialogue == True:
            self.question_dialog.display_dialog()

    def setup(self):
        Base((0, 0),
             pygame.image.load("../Graphics/Environment/levels/ground.png").convert_alpha(),
             self.master_sprite_group,
             LAYER["GROUND"])
        self.current_player = Player((640, 360), self.master_sprite_group)

    def run(self, delta_time):
        self.main_display_surface.fill("Black")
        self.master_sprite_group.draw(self.current_player)
        self.master_sprite_group.update(delta_time)
        self.hud.display_inventory()
        self.popups()


# >>>>>>>>>>>>>>>>>> LEVEL CLASS


# <<<<<<<<<<<<<<<<<< LEVEL CLASS

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.main_display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_X/2
        self.offset.y = player.rect.centery - SCREEN_Y/2

        for layer in LAYER.values():
            for sprite in self.sprites():
                if sprite.current_layer == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.main_display_surface.blit(sprite.image, offset_rect)



# >>>>>>>>>>>>>>>>>> LEVEL CLASS