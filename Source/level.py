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
        self.collision_sprite_group = pygame.sprite.Group()
        self.setup()
        self.hud = Hud(self.current_player)
        self.question_dialog = QuestionDialog(self.current_player)

    def popups(self):
        if self.current_player.in_dialogue == True:
            self.question_dialog.display_dialog()

    def setup(self):
        tmx_data = load_pygame("../Graphics/Tiled/NewTiled/KosmicheNewMap.tmx")

        # Ground Tiles

        for x, y, surface in tmx_data.get_layer_by_name("Ground").tiles():
            Base((x * TILE_SIZE, y * TILE_SIZE), surface, self.master_sprite_group, LAYER["GROUND"])

        # Path Tiles

        for x, y, surface in tmx_data.get_layer_by_name("Pathway").tiles():
            Base((x * TILE_SIZE, y * TILE_SIZE), surface, self.master_sprite_group, LAYER["PATH"])

        # Scene Objects

        for obj in tmx_data.objects:
            print(obj.name + " STARTING")

            # Building Floors

            if obj.type == "BuildingFloorPlan":
                if obj.name == "House":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["HOUSE_LEVEL_1"])
                if obj.name == "Shop":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["HOUSE_LEVEL_1"])


            # Building Floor Objects

            if obj.type == "FloorFurniture":
                if obj.name == "NoticeBoards":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["HOUSE_LEVEL_2"])
                if obj.name == "Carpets":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["HOUSE_LEVEL_2"])
                if obj.name == "BookShelves":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["HOUSE_LEVEL_2"])
                if obj.name == "Fireplace":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["HOUSE_LEVEL_2"])
            print(obj.name + " SUCCEEDED")

            # Building Main Furniture Objects

            if obj.type == "Furniture":
                if obj.name == "Bed":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["HOUSE_LEVEL_2"])
                if obj.name == "SideTable":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["HOUSE_LEVEL_2"])
                if obj.name == "Table":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])
                if obj.name == "Chairs":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])
                if obj.name == "Counter":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])
                if obj.name == "DisplayShelves":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])
                if obj.name == "Flowerpots":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["HOUSE_LEVEL_2"])

            # Building Fences

            if obj.type == "Fences":
                if obj.name == "Fences":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])

            # Building Foliage

            if obj.type == "Foliage":
                if obj.name == "Flowers":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["PLANT"])
                if obj.name == "Mushrooms":
                    Base((obj.x, obj.y), obj.image, self.master_sprite_group,
                         LAYER["PLANT"])
                if obj.name == "Hedge":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])
                if obj.name == "Trees":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["MAIN"])

            # Setting Up Colliders

            if obj.type == "ColliderClass":
                if obj.name == "Collider":
                    Base((obj.x, obj.y), obj.image, [self.master_sprite_group, self.collision_sprite_group],
                         LAYER["INVISIBLE"])

            print(obj.name + " SUCCEEDED")


        # Draw Player

        self.current_player = Player((640, 360), self.master_sprite_group, self.collision_sprite_group)

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
        self.offset.x = player.rect.centerx - SCREEN_X / 2
        self.offset.y = player.rect.centery - SCREEN_Y / 2

        for layer in LAYER.values():
            for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
                if sprite.current_layer == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.main_display_surface.blit(sprite.image, offset_rect)

# >>>>>>>>>>>>>>>>>> LEVEL CLASS
