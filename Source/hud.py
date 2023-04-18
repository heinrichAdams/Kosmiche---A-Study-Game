import pygame
from utility import *
from settings import *


# <<<<<<<<<<<<<<<<<< HUD CLASS

class Hud:
    def __init__(self, player):

        self.main_gui_overlay = None

        self.pumpkin_seed_image = None
        self.sun_seed_image = None
        self.potato_seed_image = None
        self.water_can_image = None
        self.hoe_image = None
        self.inventory_slot_empty_image = None

        # HUD
        self.hud_surface = pygame.display.get_surface()
        self.player = player
        self.load_hud_assets()
        self.inventory = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        self.inventory_slot_positions = [(445, 658), (486, 658), (527, 658), (568, 658), (609, 658)
                                         , (650, 658), (691, 658), (732, 658)]

    def load_hud_assets(self):
        self.main_gui_overlay = pygame.image.load(
            "../Graphics/UI/HUD/MAIN_GUI_OVERLAY/0.png").convert_alpha()

        self.inventory_slot_empty_image = pygame.image.load(
            "../Graphics/UI/HUD/INVENTORY_SLOT_EMPTY/0.png").convert_alpha()

        self.inventory_slot_selected_image = pygame.image.load(
            "../Graphics/UI/HUD/INVENTORY_SLOT_SELECTED/0.png").convert_alpha()

        self.hoe_image = pygame.image.load("../Graphics/UI/HUD/ITEM_HOE/0.png").convert_alpha()
        self.water_can_image = pygame.image.load("../Graphics/UI/HUD/ITEM_WATER_CAN/0.png").convert_alpha()
        self.potato_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_POTATO_SEED/0.png").convert_alpha()
        self.sun_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_SUN_SEED/0.png").convert_alpha()
        self.pumpkin_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_PUMPKIN_SEED/0.png").convert_alpha()

    def display_inventory(self):
        self.hud_surface.blit(self.main_gui_overlay, (0, 0))

        index = 0
        for slot in self.player.inventory.values():
            if slot == "HOE":
                self.hud_surface.blit(self.hoe_image, self.inventory_slot_positions[index])
            elif slot == "WATER_CAN":
                self.hud_surface.blit(self.water_can_image, self.inventory_slot_positions[index])
            elif slot == "SEED_POTATO":
                self.hud_surface.blit(self.potato_seed_image, self.inventory_slot_positions[index])
            elif slot == "SEED_SUN":
                self.hud_surface.blit(self.sun_seed_image, self.inventory_slot_positions[index])
            elif slot == "SEED_PUMPKIN":
                self.hud_surface.blit(self.pumpkin_seed_image, self.inventory_slot_positions[index])
            else:
                self.hud_surface.blit(self.inventory_slot_empty_image, self.inventory_slot_positions[index])
            if self.player.inventory_slot_selected == index:
                self.hud_surface.blit(self.inventory_slot_selected_image, self.inventory_slot_positions[index])

            index += 1

# >>>>>>>>>>>>>>>>>> HUD CLASS
