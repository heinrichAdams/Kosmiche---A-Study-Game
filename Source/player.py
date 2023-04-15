import pygame
import sys
from settings import *
from utility import *
from timer import *


# <<<<<<<<<<<<<<<<<< PLAYER CLASS

class Player(pygame.sprite.Sprite):

    def __init__(self, position, group):
        super().__init__(group)
        self.load_player_assets()

        self.current_state = "IDLE_DOWN"
        self.inventory_slot_selected = 0
        self.inventory = {0: "HOE", 1: "WATER_CAN", 2: "SEED_POTATO", 3: "SEED_SUN", 4: "SEED_PUMPKIN", 5: "",
                          6: "", 7: ""}
        self.mouse_button_down = False
        self.speed = 100
        self.timer_list = {"USE_ITEM": Timer(350, self.use_item)}

        self.frame_index = 0
        self.image = self.animations[self.current_state][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        self.move_direction = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(self.rect.center)

    def use_item(self):

        # USE SEED

        if not self.inventory[self.inventory_slot_selected].find("SEED"):
            print(f"Trying to plant {self.inventory[self.inventory_slot_selected]}")

    def load_player_assets(self):
        self.animations = {"UP": [], "DOWN": [], "LEFT": [], "RIGHT": [],
                           "IDLE_UP": [], "IDLE_DOWN": [], "IDLE_LEFT": [], "IDLE_RIGHT": [],
                           "WATER_UP": [], "WATER_DOWN": [], "WATER_LEFT": [], "WATER_RIGHT": [],
                           "HOE_UP": [], "HOE_DOWN": [], "HOE_LEFT": [], "HOE_RIGHT": []}
        for animation in self.animations.keys():
            animation_path = "../Graphics/Character/" + animation
            self.animations[animation] = load_folder(animation_path)
        print(self.animations)

    def get_current_state(self):

        # IDLE

        if self.move_direction.magnitude() == 0:
            if self.current_state == "UP":
                self.current_state = "IDLE_UP"
            elif self.current_state == "DOWN":
                self.current_state = "IDLE_DOWN"
            elif self.current_state == "LEFT":
                self.current_state = "IDLE_LEFT"
            elif self.current_state == "RIGHT":
                self.current_state = "IDLE_RIGHT"

        # USE HOE

        if self.timer_list["USE_ITEM"].active and self.inventory[self.inventory_slot_selected] == "HOE":
            if self.current_state == "IDLE_UP":
                self.current_state = "HOE_UP"
            elif self.current_state == "IDLE_DOWN":
                self.current_state = "HOE_DOWN"
            elif self.current_state == "IDLE_LEFT":
                self.current_state = "HOE_LEFT"
            elif self.current_state == "IDLE_RIGHT":
                self.current_state = "HOE_RIGHT"
        else:
            if self.current_state == "HOE_UP":
                self.current_state = "IDLE_UP"
            elif self.current_state == "HOE_DOWN":
                self.current_state = "IDLE_DOWN"
            elif self.current_state == "HOE_LEFT":
                self.current_state = "IDLE_LEFT"
            elif self.current_state == "HOE_RIGHT":
                self.current_state = "IDLE_RIGHT"

        # USE WATER CAN

        if self.timer_list["USE_ITEM"].active and self.inventory[self.inventory_slot_selected] == "WATER_CAN":
            if self.current_state == "IDLE_UP":
                self.current_state = "WATER_UP"
            elif self.current_state == "IDLE_DOWN":
                self.current_state = "WATER_DOWN"
            elif self.current_state == "IDLE_LEFT":
                self.current_state = "WATER_LEFT"
            elif self.current_state == "IDLE_RIGHT":
                self.current_state = "WATER_RIGHT"
        else:
            if self.current_state == "WATER_UP":
                self.current_state = "IDLE_UP"
            elif self.current_state == "WATER_DOWN":
                self.current_state = "IDLE_DOWN"
            elif self.current_state == "WATER_LEFT":
                self.current_state = "IDLE_LEFT"
            elif self.current_state == "WATER_RIGHT":
                self.current_state = "IDLE_RIGHT"

    def animate(self, delta_time):
        self.frame_index += 4 * delta_time
        if self.frame_index >= len(self.animations[self.current_state]):
            self.frame_index = 0
        self.image = self.animations[self.current_state][int(self.frame_index)]

    def input(self):
        for event in pygame.event.get():

            # QUIT

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # KEYBOARD INPUTS

            if event.type == pygame.KEYDOWN and not self.timer_list["USE_ITEM"].active:

                # UP
                if event.key == pygame.K_w:
                    self.move_direction.y = -1
                    self.current_state = "UP"
                # DOWN
                elif event.key == pygame.K_s:
                    self.move_direction.y = 1
                    self.current_state = "DOWN"
                # LEFT
                if event.key == pygame.K_a:
                    self.current_state = "LEFT"
                    self.move_direction.x = -1
                # RIGHT
                elif event.key == pygame.K_d:
                    self.current_state = "RIGHT"
                    self.move_direction.x = 1

            if event.type == pygame.KEYUP and not self.timer_list["USE_ITEM"].active:
                # UP
                if event.key == pygame.K_w:
                    self.move_direction.y = 0
                # DOWN
                elif event.key == pygame.K_s:
                    self.move_direction.y = 0
                # LEFT
                if event.key == pygame.K_a:
                    self.move_direction.x = 0
                # RIGHT
                elif event.key == pygame.K_d:
                    self.move_direction.x = 0

            # MOUSE INPUTS

            if event.type == pygame.MOUSEBUTTONDOWN and not self.mouse_button_down:
                if pygame.mouse.get_pressed() == (True, False, False):
                    self.timer_list["USE_ITEM"].start()
                    self.move_direction = pygame.math.Vector2()
                    self.frame_index = 0
                self.mouse_button_down = True

            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_button_down:
                self.mouse_button_down = False



    def update_timers(self):
        for timer in self.timer_list.values():
            if timer.active:
                timer.update()

    def movement(self, delta_time):
        if self.move_direction.magnitude() > 0:
            self.move_direction = self.move_direction.normalize()

        # X
        self.position.x += self.move_direction.x * self.speed * delta_time
        self.rect.centerx = self.position.x

        # Y
        self.position.y += self.move_direction.y * self.speed * delta_time
        self.rect.centery = self.position.y

    def update(self, delta_time):
        self.input()
        self.movement(delta_time)
        self.get_current_state()
        self.update_timers()
        self.animate(delta_time)
# >>>>>>>>>>>>>>>>>> PLAYER CLASS
