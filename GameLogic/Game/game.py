import pygame

from GameLogic import colors
from GameLogic.settings import SCREEN, INPUT


class Game:
    def __init__(self):
        self.game_objects = []

    def run_game(self):
        # Fill the background
        SCREEN.fill(colors.DARK_GREEN)

        # Get user inputs
        INPUT.keys = pygame.key.get_pressed()

        # All game object actions
        for obj in self.game_objects:
            obj.act(self.game_objects)
