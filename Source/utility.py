from os import walk

import pygame


def load_folder(file_path):
    surface_array = []
    for folder_name, sub_folder, image_files in walk(file_path):
        for image in image_files:
            animation_path = file_path + "/" + image
            surface = pygame.image.load(animation_path).convert_alpha()
            surface_array.append(surface)

    return surface_array


def parse_txt(file_path):
    with open(file_path) as text:
        line = text.readline()
    return line
