import pygame

from GameLogic.GameObjects.Character.Player.player_manager import PlayerManager
from GameLogic.GameUtilities import colors
from GameLogic.GameUtilities.settings import SCREEN, INPUT


class Game:
    def __init__(self):
        self.game_objects = []

    def run_game(self):
        # Fill the background
        SCREEN.fill(colors.DARK_GREEN)

        # Get user inputs
        INPUT.keys = pygame.key.get_pressed()

        # All game object actions
        for game_obj in self.game_objects:
            game_obj.act(self.game_objects)

        # Handle object removal and appends
        for game_obj in self.game_objects:
            game_obj.end_life_if_dead(self.game_objects)
