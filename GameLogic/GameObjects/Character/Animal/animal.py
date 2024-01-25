import random

from GameLogic.GameObjects.Character.Animal.Brain import neural_net
from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameUtilities.utility import generate_random_pos
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, CHARACTER_RADIUS


class Animal(Character):
    def __init__(self):
        super().__init__(generate_random_pos(WIDTH, HEIGHT), CHARACTER_RADIUS)

        # Traits
        self.view_range = random.randint(50, 200)
        self.max_perceived = 10

        # Animal internal previous values
        self.energy_prev = 100
        self.hp_prev = 100

        # Animal external observations
        self.chars_in_range = 0
        self.dist_to_closest_char = -1
        self.plants_in_range = 0
        self.dist_to_closest_plant = -1

        # Animal brain elements
        self.layers = [16, 20, 8]
        self.reward = 0
        #     Inputs: [plants in range, dist to the closest plant, chars in range, dist to the closest char, energy, hp
        #              speed, left, right, up, down, eat, deal_dmg, speed_up, slow_down]
        self.brain = neuralNet.NeuralNet(self.layers, [(0, self.max_perceived), (0, self.view_range),
                                                       (0, self.max_perceived), (0, self.view_range),
                                                       (0, 100), (0, 100), (self.min_speed, self.max_speed),
                                                       (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                                                       (0, 1), (0, 1), (0, 1), (0, 1)])


