import pygame
from utility import *
from settings import *


# <<<<<<<<<<<<<<<<<< DIALOG CLASS

class QuestionDialog:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.question_card_image = None
        self.false_button_image = None
        self.false_button_highlighted_image = None
        self.true_button_image = None
        self.true_button_highlighted_image = None
        self.correct_image = None
        self.incorrect_image = None

        self.player = player
        self.load_dialog_assets()

    def load_dialog_assets(self):
        self.question_card_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/QUESTION_CARD/0.png").convert_alpha()
        self.false_button_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/FALSE_BUTTON/0.png").convert_alpha()
        self.false_button_highlighted_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/FALSE_BUTTON_HIGHLIGHTED/0.png").convert_alpha()
        self.true_button_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/TRUE_BUTTON/0.png").convert_alpha()
        self.true_button_highlighted_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/TRUE_BUTTON_HIGHLIGHTED/0.png").convert_alpha()
        self.correct_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/CORRECT/0.png").convert_alpha()
        self.incorrect_image = pygame.image.load(
            "../Graphics/UI/QUESTION_DIALOG/INCORRECT/0.png").convert_alpha()

    def display_dialog(self):
        # card
        self.display_surface.blit(self.question_card_image, QUESTION_CARD)

        # true button
        if self.player.mouse_above_true:
            self.display_surface.blit(self.true_button_highlighted_image, TRUE_SELECTED)

        # false button
        if self.player.mouse_above_false:
            self.display_surface.blit(self.false_button_highlighted_image, FALSE_SELECTED)

# >>>>>>>>>>>>>>>>>> DIALOG CLASS
