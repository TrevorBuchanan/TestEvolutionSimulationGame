import pygame

from GameLogic.GameObjects.Character.Animal.Brain.layer import Layer
from GameLogic.GameObjects.Character.Animal.animal import Animal
from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameUtilities.colors import BEIGE, BROWN
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, SCREEN
from GameLogic.GameUtilities.utility import pt_calc_dist, generate_random_pos


class AnimalManager(CharacterManager):
    def __init__(self):
        super().__init__()
        self.obj = Animal()
        self.obj.color = BEIGE

    def act(self, game_objects):
        self.set_previous_values()
        super().act(game_objects)
        self.reproduce(game_objects)
        self.set_objects_in_range(game_objects)
        self.use_brain()
        self.calculate_reward()
        if self.obj.deal_dmg:
            self.obj.color = BROWN
        else:
            self.obj.color = BEIGE

    def draw(self):
        pygame.draw.circle(SCREEN, self.obj.color, self.obj.position, self.obj.radius)

    def set_previous_values(self):
        self.obj.energy_prev = self.obj.energy
        self.obj.hp_prev = self.obj.hp

    # Check if any characters reproduced
    def natural_selection(self):
        if self.obj.energy > 100:
            self.obj.reproduce = True
            self.obj.energy = 90

    def reproduce(self, game_objects):
        if self.obj.reproduce:
            new_obj = AnimalManager()
            new_obj.copy_brain(self.obj.brain)
            new_obj.obj.position = generate_random_pos(WIDTH, HEIGHT)
            game_objects.append(new_obj)
            self.obj.reproduce = False

    def copy_brain(self, brain):
        for i, layer in enumerate(brain.layers):
            new_layer = Layer(layer.numInputs, layer.numOutputs)
            for out_index in range(layer.numOutputs):
                for in_index in range(layer.numInputs):
                    new_layer.weights[in_index][out_index] = layer.weights[in_index][out_index]
            for out_index in range(layer.numOutputs):
                new_layer.biases[out_index] = layer.biases[out_index]
            self.obj.brain.layers[i] = new_layer

    # Check for characters in range
    def set_objects_in_range(self, game_objects):
        num_chars = 0
        num_plants = 0
        min_plant_dist = self.obj.view_range
        min_char_dist = self.obj.view_range
        switch = True
        for game_obj in game_objects:
            if isinstance(game_obj, CharacterManager):
                if pt_calc_dist(self.obj.position, game_obj.obj.position) < self.obj.view_range and \
                        self.obj.position != game_obj.obj.position:
                    num_chars += 1
                    if num_chars >= self.obj.max_perceived:
                        break
            elif isinstance(game_obj, Plant):
                if switch:
                    min_plant_dist = pt_calc_dist(self.obj.position, game_obj.position)
                    switch = False
                if pt_calc_dist(self.obj.position,
                                game_obj.position) < self.obj.view_range and self.obj.position != game_obj.position:
                    num_plants += 1
                    if min_plant_dist > pt_calc_dist(self.obj.position, game_obj.position):
                        min_plant_dist = pt_calc_dist(self.obj.position, game_obj.position)
                    if num_plants >= self.obj.max_perceived:
                        break
        self.obj.plants_in_range = num_plants
        self.obj.dist_to_plant = min_plant_dist
        self.obj.chars_in_range = num_chars
        self.obj.dist_to_closest_char = min_char_dist

    # Run network
    def use_brain(self):
        inputs = [self.obj.plants_in_range, self.obj.dist_to_closest_plant, self.obj.chars_in_range,
                  self.obj.dist_to_closest_char, self.obj.energy, self.obj.hp, self.obj.speed, self.obj.left,
                  self.obj.right, self.obj.up, self.obj.down, self.obj.eat, self.obj.deal_dmg, self.obj.speed_up,
                  self.obj.slow_down, self.obj.reproduce]
        outputs = self.obj.brain.get_outputs(inputs)

        if outputs[0] > 0.5:
            self.obj.left = True
        if outputs[1] > 0.5:
            self.obj.right = True
        if outputs[2] > 0.5:
            self.obj.up = True
        if outputs[3] > 0.5:
            self.obj.down = True
        if outputs[4] > 0.5:
            self.obj.eat = True
        if outputs[5] > 0.5:
            self.obj.deal_dmg = True
        if outputs[6] > 0.5:
            self.obj.speed_up = True
        if outputs[7] > 0.5:
            self.obj.slow_down = True

    def calculate_reward(self):
        if self.obj.energy > self.obj.energy_prev:  # Energy went down
            self.obj.reward += 0.1  # Value of positive energy change
        elif self.obj.energy < self.obj.energy_prev:
            self.obj.reward -= 0.5  # Value of negative energy change
        if self.obj.hp > self.obj.hp_prev:
            self.obj.reward += 0.1  # Value of positive hp change
        elif self.obj.hp < self.obj.hp_prev:
            self.obj.reward -= 0.5  # Value of negative energy change
        if self.obj.reproduce:
            self.obj.reward += 10
        # Add death penalty when reinforcement learning
        if self.dead:
            self.obj.reward += self.age
