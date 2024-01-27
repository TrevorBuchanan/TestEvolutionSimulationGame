import random

import pygame

from GameLogic.GameObjects.Character.Animal.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.Animal.Training.epoch import Epoch
from GameLogic.GameObjects.object_manager import ObjectManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import ANIMAL_AMOUNT, INPUT
from GameLogic.GameUtilities.utility import write_to_screen


class EpochManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Epoch()
        self.new_epoch = False
        self.auto_epochs = False
        self.skip_epochs = False
        self.skip_amount = 10

        # TEMP
        self.k1pressed = False
        self.k2pressed = False
        self.k3pressed = False

    def act(self, game_objects):
        super().act(game_objects)
        self.check_manual_epoch()
        self.check_auto_epoch()
        self.check_skip_epochs()
        self.run_manual_epochs(game_objects)
        self.run_auto_epochs(game_objects)
        self.run_skip_epochs(game_objects)

    def draw(self):
        # Draws specified object qualities to screen
        self.draw_stats()

    def draw_stats(self):
        # Draw stats to screen
        write_to_screen(f"Epoch: {self.obj.count}", (10, 10), WHITE)
        write_to_screen(f"Auto Epochs: {self.auto_epochs}", (10, 40), WHITE)
        write_to_screen(f"Skip Amount: {self.skip_amount}", (10, 70), WHITE)
        write_to_screen(f"Epoch length: {self.obj.epoch_time}", (10, 100), WHITE)

    def check_manual_epoch(self):
        """
        Check if user has enabled running a manual epoch
        """
        if not self.k1pressed:
            if INPUT.keys[pygame.K_RETURN]:
                self.k1pressed = True
                self.new_epoch = True
        elif not INPUT.keys[pygame.K_RETURN]:
            self.k1pressed = False

    def check_auto_epoch(self):
        """
        Check if user has enabled auto epochs
        """
        if not self.k2pressed:
            if INPUT.keys[pygame.K_m]:
                self.k2pressed = True
                if self.auto_epochs:
                    self.auto_epochs = False
                else:
                    self.auto_epochs = True
        elif not INPUT.keys[pygame.K_m]:
            self.k2pressed = False

    def check_skip_epochs(self):
        """
        Check if user has enabled skipping epochs
        """
        if not self.k3pressed:
            if INPUT.keys[pygame.K_n]:
                self.k3pressed = True
                self.skip_epochs = True
        elif not INPUT.keys[pygame.K_n]:
            self.k3pressed = False

    def run_manual_epochs(self, game_objects):
        """
        Run a manual epoch if enabled
        """
        if self.new_epoch:
            self.run_new_epoch(game_objects)
            self.new_epoch = False

    def run_auto_epochs(self, game_objects):
        """
        Run auto epochs if enabled
        """
        if self.auto_epochs and self.age - self.obj.epoch_time > 0:
            self.run_new_epoch(game_objects)
            while self.age >= self.obj.epoch_time:
                self.age -= self.obj.epoch_time

    def run_skip_epochs(self, game_objects):
        """
        Skip 'skip_amount' of epochs
        """
        if self.skip_epochs:
            target_epoch = self.skip_amount + self.obj.count
            auto_holder = self.auto_epochs
            self.auto_epochs = True
            # Perform 'game loop' for skip_amount
            while self.obj.count < target_epoch:
                # Loop through all game objects
                for game_obj in game_objects:
                    # Perform actions for all objects except for the EpochManager
                    if not isinstance(game_obj, EpochManager):
                        game_obj.act(game_objects)
                    # Run auto epochs
                    else:
                        self.age += self.age_increment
                        self.run_auto_epochs(game_objects)
                # Loop through all game objects
                for game_obj in game_objects:
                    # Remove all dead objects excluding the EpochManager
                    if not isinstance(game_obj, EpochManager):
                        game_obj.end_life_if_dead(game_objects)

            self.auto_epochs = auto_holder
            self.skip_epochs = False

    def run_new_epoch(self, game_objects):
        """
        End the current age and take the best characters from the age to reproduce the next generation from
        :param game_objects: List of all current game objects
        """
        self.obj.count += 1
        top_rewards = []
        chars_to_reproduce = []

        # Loop through all game objects
        for game_obj in game_objects:
            # Check if the game object is an AnimalManager
            if isinstance(game_obj, AnimalManager):
                # Find the specified amount of top award winners for previous epoch
                if len(top_rewards) <= self.obj.top_selection_amount:
                    top_rewards.append(game_obj.obj.reward)
                else:
                    if game_obj.obj.reward > min(top_rewards):
                        top_rewards.remove(min(top_rewards))
                        top_rewards.append(game_obj.obj.reward)

        # Loop through all game objects
        for game_obj in game_objects:
            # Check if the game object is an AnimalManager
            if isinstance(game_obj, AnimalManager):
                # Check if the AnimalManager is in the list of highest award winners and add
                # it to the chars_to_reproduce list
                if game_obj.obj.reward >= min(top_rewards):
                    chars_to_reproduce.append(game_obj)
                game_obj.dead = True

        # Loop with length of desired animal amount
        for _ in range(ANIMAL_AMOUNT):
            # Get a random index of a character to reproduce
            if self.obj.top_selection_amount > ANIMAL_AMOUNT:
                index = random.randint(0, ANIMAL_AMOUNT - 1)
            else:
                index = random.randint(0, self.obj.top_selection_amount - 1)

            # Perform reproduction of character at index
            chars_to_reproduce[index].obj.reproduce = True
            chars_to_reproduce[index].reproduce(game_objects)
