import pygame

from GameLogic.Game.SOTFControls.manual_epoch import ManualEpoch
from GameLogic.GameObjects.Character.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.player_manager import PlayerManager
from GameLogic.GameUtilities import colors
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import SCREEN, INPUT, WIDTH, HEIGHT
from GameLogic.GameUtilities.utility import generate_random_pos, write_to_screen


class Game:
    def __init__(self):
        self.game_objects = []

        # ******* TEMP ********
        self.new_epoch = False
        self.epoch = 0
        self.pressed = False

    def run_game(self):
        # Fill the background
        SCREEN.fill(colors.DARK_GREEN)

        # Get user inputs
        INPUT.keys = pygame.key.get_pressed()

        # *******TEMP********
        top_rewards = []
        # *******TEMP********

        # All game object actions
        for game_obj in self.game_objects:
            game_obj.act(self.game_objects)
            if isinstance(game_obj, PlayerManager):
                game_obj.draw_stats()

            # *******TEMP********
            if isinstance(game_obj, AnimalManager):
                if len(top_rewards) <= 10:
                    top_rewards.append(game_obj.obj.reward)
                else:
                    if game_obj.obj.reward > min(top_rewards):
                        top_rewards.remove(min(top_rewards))
                        top_rewards.append(game_obj.obj.reward)
            # *******TEMP********

        # *******TEMP********
        if not self.pressed:
            if INPUT.keys[pygame.K_RETURN]:
                self.pressed = True
                self.new_epoch = True
        elif not INPUT.keys[pygame.K_RETURN]:
            self.pressed = False

        if self.new_epoch:
            self.epoch += 1
            ManualEpoch.epoch(self.game_objects, top_rewards)
            self.new_epoch = False
        write_to_screen(f"Epoch: {self.epoch}", (10, 10), WHITE)
        # *******TEMP********

        # Handle object removal and appends
        for game_obj in self.game_objects:
            game_obj.end_life_if_dead(self.game_objects)
