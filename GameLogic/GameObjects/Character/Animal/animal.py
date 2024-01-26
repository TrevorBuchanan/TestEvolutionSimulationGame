import random

from GameLogic.GameObjects.Character.Animal.Brain import neural_net
from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameUtilities.utility import generate_random_pos
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, CHARACTER_RADIUS


class Animal(Character):
    """
    Animal character object
    """
    def __init__(self):
        super().__init__(generate_random_pos(WIDTH, HEIGHT), CHARACTER_RADIUS)

        # Traits
        self.view_range = random.randint(50, 200)
        self.max_perceived = 10
        self.brain_mutation_chance = 1
        self.mutation_amount_limit = 0.5

        # Animal internal previous states
        self.energy_prev = self.energy
        self.hp_prev = self.hp

        # Animal external observations
        self.chars_in_range = 0
        self.dist_to_closest_char = self.view_range
        self.plants_in_range = 0
        self.dist_to_closest_plant = self.view_range

        # Animal brain elements
        self.layers = [16, 20, 8]
        self.reward = 0
        #     Inputs: [plants in range, dist to the closest plant, chars in range, dist to the closest char, energy, hp
        #              speed, left, right, up, down, eat, deal_dmg, speed_up, slow_down]
        self.brain = neural_net.NeuralNet(self.layers, [(0, self.max_perceived), (0, self.view_range),
                                                        (0, self.max_perceived), (0, self.view_range),
                                                        (0, 100), (0, 100), (self.min_speed, self.max_speed),
                                                        (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                                                        (0, 1), (0, 1), (0, 1), (0, 1)])
