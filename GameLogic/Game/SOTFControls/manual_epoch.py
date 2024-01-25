import random

from GameLogic.GameObjects.Character.animal_manager import AnimalManager
from GameLogic.GameUtilities.settings import ANIMAL_AMOUNT, WIDTH, HEIGHT
from GameLogic.GameUtilities.utility import generate_random_pos


class ManualEpoch:
    @staticmethod
    def epoch(game_objects, top_rewards):
        chars_to_reproduce = []
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
