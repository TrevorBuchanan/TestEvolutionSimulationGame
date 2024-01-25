import random

import pygame

from GameLogic.GameObjects.Character.Animal.animal_manager import AnimalManager
from GameLogic.GameObjects.Character.Animal.Training.epoch import Epoch
from GameLogic.GameObjects.objectManager import ObjectManager
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
        self.skip_amount = 100

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
        self.draw_stats()

    def draw_stats(self):
        write_to_screen(f"Epoch: {self.obj.count}", (10, 10), WHITE)
        write_to_screen(f"Auto Epochs: {self.auto_epochs}", (10, 40), WHITE)
        write_to_screen(f"Skip Amount: {self.skip_amount}", (10, 70), WHITE)

    def check_manual_epoch(self):
        if not self.k1pressed:
            if INPUT.keys[pygame.K_RETURN]:
                self.k1pressed = True
                self.new_epoch = True
        elif not INPUT.keys[pygame.K_RETURN]:
            self.k1pressed = False

    def check_auto_epoch(self):
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
        if not self.k3pressed:
            if INPUT.keys[pygame.K_n]:
                self.k3pressed = True
                self.skip_epochs = True
        elif not INPUT.keys[pygame.K_n]:
            self.k3pressed = False

    def run_auto_epochs(self, game_objects):
        if self.auto_epochs and self.age - self.obj.epoch_time > 0:
            self.run_epoch(game_objects)
            while self.age >= self.obj.epoch_time:
                self.age -= self.obj.epoch_time

    def run_manual_epochs(self, game_objects):
        if self.new_epoch:
            self.run_epoch(game_objects)
            self.new_epoch = False

    def run_skip_epochs(self, game_objects):
        if self.skip_epochs:
            print(f"skip {self.skip_amount} epochs")
            self.skip_epochs = False

    def run_epoch(self, game_objects):
        self.obj.count += 1
        top_rewards = []
        chars_to_reproduce = []

        for game_obj in game_objects:
            if isinstance(game_obj, AnimalManager):
                if len(top_rewards) <= self.obj.top_selection_amount:
                    top_rewards.append(game_obj.obj.reward)
                else:
                    if game_obj.obj.reward > min(top_rewards):
                        top_rewards.remove(min(top_rewards))
                        top_rewards.append(game_obj.obj.reward)

        for game_obj in game_objects:
            if isinstance(game_obj, AnimalManager):
                if game_obj.obj.reward >= min(top_rewards):
                    chars_to_reproduce.append(game_obj)
                else:
                    game_obj.dead = True

        for _ in range(ANIMAL_AMOUNT):
            if self.obj.top_selection_amount > ANIMAL_AMOUNT:
                index = random.randint(0, ANIMAL_AMOUNT - 1)
            else:
                index = random.randint(0, self.obj.top_selection_amount - 1)
            chars_to_reproduce[index].obj.reproduce = True
            chars_to_reproduce[index].reproduce(game_objects)
