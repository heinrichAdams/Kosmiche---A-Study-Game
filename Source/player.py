import pygame
from settings import *
from utility import *


# <<<<<<<<<<<<<<<<<< PLAYER CLASS

class Player(pygame.sprite.Sprite):

    def __init__(self, position, group):
        super().__init__(group)
        self.load_player_assets()

        self.current_state = "IDLE_DOWN"
        self.frame_index = 0

        self.image = self.animations[self.current_state][self.frame_index]
        self.rect = self.image.get_rect(center=position)

        self.move_direction = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 100

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
        if self.move_direction.magnitude() == 0:
            if self.current_state == "UP":
                self.current_state = "IDLE_UP"
            elif self.current_state == "DOWN":
                self.current_state = "IDLE_DOWN"
            elif self.current_state == "LEFT":
                self.current_state = "IDLE_LEFT"
            elif self.current_state == "RIGHT":
                self.current_state = "IDLE_RIGHT"

    def animate(self, delta_time):
        self.frame_index += 4 * delta_time
        if self.frame_index >= len(self.animations[self.current_state]):
            self.frame_index = 0
        self.image = self.animations[self.current_state][int(self.frame_index)]

    def input(self):
        all_input = pygame.key.get_pressed()
        # UP
        if all_input[pygame.K_w]:
            self.move_direction.y = -1
            self.current_state = "UP"
        # DOWN
        elif all_input[pygame.K_s]:
            self.move_direction.y = 1
            self.current_state = "DOWN"
        else:
            self.move_direction.y = 0
        # LEFT
        if all_input[pygame.K_a]:
            self.current_state = "LEFT"
            self.move_direction.x = -1
        # RIGHT
        elif all_input[pygame.K_d]:
            self.current_state = "RIGHT"
            self.move_direction.x = 1
        else:
            self.move_direction.x = 0

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
        self.animate(delta_time)
# >>>>>>>>>>>>>>>>>> PLAYER CLASS
