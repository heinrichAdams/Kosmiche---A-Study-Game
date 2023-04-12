import pygame,sys
from settings import *

# <<<<<<<<<<<<<<<<<< GAME CLASS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
        pygame.display.set_caption("KosmichE")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            delta_time = self.clock.tick() / 1000
            pygame.display.update()

# >>>>>>>>>>>>>>>>>> GAME CLASS


# <<<<<<<<<<<<<<<<<< MAIN

if __name__ == "__main__":
    current_game = Game()
    current_game.run()

# >>>>>>>>>>>>>>>>>> MAIN