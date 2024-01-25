import pygame

from GameLogic.GameObjects.SOTFControls.epoch_manager import EpochManager
from GameLogic.GameObjects.Character.player_manager import PlayerManager
from GameLogic.GameUtilities import colors
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import SCREEN, INPUT
from GameLogic.GameUtilities.utility import write_to_screen


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
            if isinstance(game_obj, PlayerManager):
                game_obj.draw_stats()

        # Handle object removal and appends
        for game_obj in self.game_objects:
            game_obj.end_life_if_dead(self.game_objects)
