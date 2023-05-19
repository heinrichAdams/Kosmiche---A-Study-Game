import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from seed import Seed

# <<<<<<<<<<<<<<<<<< FARMABLE GROUND CLASS

class FarmableGround:
    def __init__(self, master_sprite_group):
        self.activated_tiles = None
        self.master_sprite_group = master_sprite_group
        self.soil_sprites = pygame.sprite.Group()
        self.plant_sprites = pygame.sprite.Group()
        self.grid = None

        self.soil_surface = pygame.image.load("../Graphics/Environment/SOIL_TILES/0.png")

        self.create_grid()
        self.create_farmable_tiles()

    def create_grid(self):
        ground = pygame.image.load("../Graphics/Tiled/NewTiled/KosmicheNewMap.png")
        horizontal_tiles = ground.get_width() // TILE_SIZE
        vertical_tiles = ground.get_height() // TILE_SIZE

        self.grid = [[[] for column in range(horizontal_tiles)] for row in range(vertical_tiles)]
        for x, y, _ in load_pygame("../Graphics/Tiled/NewTiled/KosmicheNewMap.tmx").get_layer_by_name("FarmableGround").tiles():
            self.grid[y][x].append("Farmable")

    def create_farmable_tiles(self):
        self.activated_tiles = []
        for row_index, row in enumerate(self.grid):
            for column_index, cell in enumerate(row):
                if "Farmable" in cell:
                    x_pos = column_index * TILE_SIZE
                    y_pos = row_index * TILE_SIZE
                    rect = pygame.Rect(x_pos, y_pos, TILE_SIZE, TILE_SIZE)
                    self.activated_tiles.append(rect)

    def is_hit(self, hit_location):
        for rect in self.activated_tiles:
            if rect.collidepoint(hit_location):
                x_pos = rect.x // TILE_SIZE
                y_pos = rect.y // TILE_SIZE
                if "Farmable" in self.grid[y_pos][x_pos] and "x" not in self.grid[y_pos][x_pos]:
                    self.grid[y_pos][x_pos].append("x")
                    self.create_visible_tiles()

    def create_visible_tiles(self):
        self.soil_sprites.empty()
        for row_index, row in enumerate(self.grid):
            for column_index, cell in enumerate(row):
                if "x" in cell:
                    SoilTile((column_index * TILE_SIZE, row_index * TILE_SIZE),
                             self.soil_surface,
                             [self.master_sprite_group, self.soil_sprites])

    def plant_seed(self, position, seed):
        for sprite in self.soil_sprites.sprites():
            if sprite.rect.collidepoint(position):
                x_pos = sprite.rect.x // TILE_SIZE
                y_pos = sprite.rect.y // TILE_SIZE

                if "seed" not in self.grid[y_pos][x_pos]:
                    self.grid[y_pos][x_pos].append("seed")
                    self.grid[y_pos][x_pos].append(Seed(seed, [self.master_sprite_group, self.plant_sprites], sprite))

    def water_plant(self, position):
        for sprite in self.soil_sprites.sprites():
            if sprite.rect.collidepoint(position):
                x_pos = sprite.rect.x // TILE_SIZE
                y_pos = sprite.rect.y // TILE_SIZE

                if "seed" in self.grid[y_pos][x_pos]:
                    print(self.grid[y_pos][x_pos])
                    self.grid[y_pos][x_pos][3].grow()

    def harvest_plant(self, position):
        for sprite in self.soil_sprites.sprites():
            if sprite.rect.collidepoint(position):
                x_pos = sprite.rect.x // TILE_SIZE
                y_pos = sprite.rect.y // TILE_SIZE

                if "seed" in self.grid[y_pos][x_pos]:
                    print(self.grid[y_pos][x_pos])
                    return self.grid[y_pos][x_pos][3].harvest()


# >>>>>>>>>>>>>>>>>> FARMABLE GROUND CLASS

# <<<<<<<<<<<<<<<<<< SOIL TILE CLASS

class SoilTile(pygame.sprite.Sprite):
    def __init__(self, position, surface, groups):
        super().__init__(groups)
        self.image = surface
        self.surface = surface
        self.position = position
        self.rect = self.surface.get_rect(topleft=self.position)
        self.current_layer = LAYER["FERTILE_GROUND"]

# >>>>>>>>>>>>>>>>>> SOIL TILE CLASS