import random

from GameLogic.GameObjects.Character.Brain import neuralNet
from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameUtilities.utility import generate_random_pos
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, CHARACTER_RADIUS


class Animal(Character):
    def __init__(self):
        super().__init__(generate_random_pos(WIDTH, HEIGHT), CHARACTER_RADIUS)

        # Brain
        self.brain = neuralNet.NeuralNet()

        # Traits
        self.view_range = random.randint(50, 200)

        # Animal external previous values
        self.chars_in_range_prev = 0
        self.plants_in_range_prev = 0
        self.dist_to_food_prev = -1

        # Animal internal previous values
        self.energy_prev = 100
        self.dmg_prev = 100
        self.hp_prev = 100
        self.speed_prev = 0

        # Animal external observations
        self.chars_in_range = 0
        self.plants_in_range = 0
        self.dist_to_food = -1

        # Animal brain characteristics
        self.layers = [3, 3, 3]

        # Animal external actions
        self.reproduce = False
