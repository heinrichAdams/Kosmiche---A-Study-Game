import pygame
from level import Level
from settings import *


# <<<<<<<<<<<<<<<<<< GAME CLASS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption("KosmichE")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()

    def run(self):
        while self.running:
            delta_time = self.clock.tick() / 1000
            self.level.run(delta_time)
            pygame.display.update()


# >>>>>>>>>>>>>>>>>> GAME CLASS


# <<<<<<<<<<<<<<<<<< MAIN

if __name__ == "__main__":
    current_game = Game()
    current_game.run()

# >>>>>>>>>>>>>>>>>> MAIN
