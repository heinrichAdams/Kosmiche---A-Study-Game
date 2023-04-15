import pygame
from utility import *
from settings import *


# <<<<<<<<<<<<<<<<<< HUD CLASS

class Hud:
    def __init__(self, player):

        # Busy implementing new gui overlay

        self.main_gui_overlay = None

        self.pumpkin_seed_image = None
        self.sun_seed_image = None
        self.potato_seed_image = None
        self.water_can_image = None
        self.hoe_image = None
        self.inventory_slot_empty_image = None


        self.hud_surface = pygame.display.get_surface()
        self.player = player
        self.load_hud_assets()
        self.inventory = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
        self.inventory_slot_positions = [(300, 625), (400, 625), (500, 625), (600, 625), (700, 625)
                                         , (800, 625), (900, 625), (1000, 625)]

        print(f"PUMPKIN SEED : {self.pumpkin_seed_image}")

    def load_hud_assets(self):
        self.main_gui_overlay = pygame.image.load(
            "../Graphics/UI/HUD/MAIN_GUI_OVERLAY/0.png").convert_alpha()

        self.main_gui_overlay = pygame.transform.rotozoom(self.main_gui_overlay, 0, 1.25)

        self.inventory_slot_empty_image = pygame.image.load(
            "../Graphics/UI/HUD/INVENTORY_SLOT_EMPTY/0.png").convert_alpha()


        self.hoe_image = pygame.image.load("../Graphics/UI/HUD/ITEM_HOE/0.png").convert_alpha()
        self.water_can_image = pygame.image.load("../Graphics/UI/HUD/ITEM_WATER_CAN/0.png").convert_alpha()
        self.potato_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_POTATO_SEED/0.png").convert_alpha()
        self.sun_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_SUN_SEED/0.png").convert_alpha()
        self.pumpkin_seed_image = pygame.image.load("../Graphics/UI/HUD/ITEM_PUMPKIN_SEED/0.png").convert_alpha()

    def display_inventory(self):
        self.hud_surface.blit(self.main_gui_overlay, (0,0))
        print("show inventory")
# >>>>>>>>>>>>>>>>>> HUD CLASS
