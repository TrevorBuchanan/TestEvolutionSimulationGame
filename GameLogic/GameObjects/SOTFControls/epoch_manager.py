import random

import pygame

from GameLogic.GameObjects.Character.animal_manager import AnimalManager
from GameLogic.GameObjects.SOTFControls.epoch import Epoch
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import ANIMAL_AMOUNT, INPUT
from GameLogic.GameUtilities.utility import write_to_screen


class EpochManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Epoch()
        self.new_epoch = False
        self.pressed = False

    def act(self, game_objects):
        self.check_epoch()
        if self.new_epoch:
            self.run_epoch(game_objects)
        self.draw_stats()

    def draw_stats(self):
        write_to_screen(f"Epoch: {self.obj.count}", (10, 10), WHITE)

    def check_epoch(self):
        if not self.pressed:
            if INPUT.keys[pygame.K_RETURN]:
                self.pressed = True
                self.new_epoch = True
        elif not INPUT.keys[pygame.K_RETURN]:
            self.pressed = False

    def run_epoch(self, game_objects):
        self.obj.count += 1
        self.new_epoch = False
        top_rewards = []
        chars_to_reproduce = []

        for game_obj in game_objects:
            if isinstance(game_obj, AnimalManager):
                if len(top_rewards) <= 10:
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
            index = random.randint(0, 9)
            chars_to_reproduce[index].obj.reproduce = True
            chars_to_reproduce[index].reproduce(game_objects)
