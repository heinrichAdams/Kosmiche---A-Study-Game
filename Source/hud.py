import pygame
from utility import *
from settings import *


# <<<<<<<<<<<<<<<<<< HUD CLASS

class Hud:
    def __init__(self, player):
        self.pumpkin_seed_image = None
        self.beet_seed_image = None
        self.potato_seed_image = None
        self.water_can_image = None
        self.hoe_image = None
        self.inventory_slot_selected_image = None
        self.inventory_slot_unselected_image = None

        self.hud_surface = pygame.display.get_surface()
        self.player = player
        self.load_hud_assets()
        self.inventory = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        self.inventory_slot_positions = [(300, 625), (400, 625), (500, 625), (600, 625), (700, 625)
                                         , (800, 625), (900, 625), (1000, 625)]

        print(f"PUMPKIN SEED : {self.pumpkin_seed_image}")

    def load_hud_assets(self):
        self.inventory_slot_unselected_image = pygame.image.load(
            "../Graphics/UI/INVENTORY_SLOT_UNSELECTED/0.png").convert_alpha()
        self.inventory_slot_unselected_image = pygame.transform.rotozoom(self.inventory_slot_unselected_image, 0, 2)

        self.inventory_slot_selected_image = pygame.image.load(
            "../Graphics/UI/INVENTORY_SLOT_SELECTED/0.png").convert_alpha()
        self.inventory_slot_selected_image = pygame.transform.rotozoom(self.inventory_slot_selected_image, 0, 2)

        self.hoe_image = pygame.image.load("../Graphics/UI/ITEM_HOE/0.png").convert_alpha()
        self.water_can_image = pygame.image.load("../Graphics/UI/ITEM_WATER_CAN/0.png").convert_alpha()
        self.potato_seed_image = pygame.image.load("../Graphics/UI/ITEM_POTATO_SEED/0.png").convert_alpha()
        self.beet_seed_image = pygame.image.load("../Graphics/UI/ITEM_BEET_SEED/0.png").convert_alpha()
        self.pumpkin_seed_image = pygame.image.load("../Graphics/UI/ITEM_PUMPKIN_SEED/0.png").convert_alpha()

    def display_inventory(self):
        for slot in self.inventory.keys():
            if slot == self.player.inventory_slot_selected:
                self.inventory[slot] = self.inventory_slot_selected_image
            else:
                self.inventory[slot] = self.inventory_slot_unselected_image
        i = 0
        for slot in self.inventory.values():
            self.hud_surface.blit(slot, self.inventory_slot_positions[i])
            i += 1

# >>>>>>>>>>>>>>>>>> HUD CLASS
