import random

from GameLogic.GameObjects.Character.Animal.Brain.layer import Layer
from GameLogic.GameObjects.Character.Animal.animal import Animal
from GameLogic.GameObjects.Enviroment.plant_manager import PlantManager
from GameLogic.GameUtilities.colors import BEIGE, BROWN
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT
from GameLogic.GameUtilities.utility import pt_calc_dist, generate_random_pos, probabilistic_bool


class AnimalManager(CharacterManager):
    """
    CharacterManager object for Animal object
    """

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
        super().draw()

    def set_previous_values(self):
        """
        Sets the previous values to the current values
        """
        self.obj.energy_prev = self.obj.energy
        self.obj.hp_prev = self.obj.hp

    def natural_selection(self):
        """
        Set reproduce action when energy is or above 100
        """
        if self.obj.energy >= 100:
            self.obj.reproduce = True
            self.obj.energy = 90

    def reproduce(self, game_objects):
        """
        Create a new animal (through asexual reproduction - only one animal needed)
        :param game_objects: List of all current game objects
        """
        if self.obj.reproduce:
            # Create new animal (manager) from parent
            new_obj = AnimalManager()
            new_obj.obj.position = generate_random_pos(WIDTH, HEIGHT)  # Random location (switch to near parent)
            # Perform trait mutations
            new_obj.get_offspring_brain(self.obj.brain)
            new_obj.obj.view_range += self.obj.view_range + random.randint(-1, 1)
            # Add new animal (manager) to game objects
            game_objects.append(new_obj)
            self.obj.reproduce = False

    def get_offspring_brain(self, brain):
        """
        Copy a given brain (neural network) and perform mutations to its connections
        :param brain: NeuralNet object
        """
        for i, layer in enumerate(brain.layers):
            new_layer = Layer(layer.numInputs, layer.numOutputs)
            for out_index in range(layer.numOutputs):
                for in_index in range(layer.numInputs):
                    new_layer.weights[in_index][out_index] = layer.weights[in_index][out_index]
                    if probabilistic_bool(self.obj.brain_mutation_chance):
                        new_layer.weights[in_index][out_index] += random.uniform(-self.obj.mutation_amount_limit,
                                                                                 self.obj.mutation_amount_limit)
            for out_index in range(layer.numOutputs):
                new_layer.biases[out_index] = layer.biases[out_index]
                if probabilistic_bool(self.obj.brain_mutation_chance):
                    new_layer.biases[out_index] += random.uniform(-self.obj.mutation_amount_limit,
                                                                  self.obj.mutation_amount_limit)
            self.obj.brain.layers[i] = new_layer

    def set_objects_in_range(self, game_objects):
        """
        Set animals internal and external characteristics and observations according
        to current game state (game_objects)
        :param game_objects: List of all current game objects
        """
        num_chars = 0
        num_plants = 0
        min_plant_dist = self.obj.view_range
        min_char_dist = self.obj.view_range
        # Loop through all game objects
        for game_obj in game_objects:
            # Check if object is a CharacterManager
            if isinstance(game_obj, CharacterManager):
                # Check if object is in range
                if pt_calc_dist(self.obj.position, game_obj.obj.position) < self.obj.view_range and \
                        self.obj.position != game_obj.obj.position:
                    # Increment number of total characters in range
                    num_chars += 1
                    # Set closest character distance if it is minimum
                    if min_char_dist > pt_calc_dist(self.obj.position, game_obj.obj.position):
                        min_char_dist = pt_calc_dist(self.obj.position, game_obj.obj.position)
                    # Stop loop if max perceived is exceeded
                    if num_chars >= self.obj.max_perceived:
                        break
            elif isinstance(game_obj, PlantManager):
                # Check if object is in range
                if pt_calc_dist(self.obj.position, game_obj.obj.position) < \
                        self.obj.view_range and self.obj.position != game_obj.obj.position:
                    # Increment number of total plants in range
                    num_plants += 1
                    # Set closest plant distance if it is minimum
                    if min_plant_dist > pt_calc_dist(self.obj.position, game_obj.obj.position):
                        min_plant_dist = pt_calc_dist(self.obj.position, game_obj.obj.position)
                    # Stop loop if max perceived is exceeded
                    if num_plants >= self.obj.max_perceived:
                        break
        # Set animals observations to calculated observations
        self.obj.plants_in_range = num_plants
        self.obj.dist_to_plant = min_plant_dist
        self.obj.chars_in_range = num_chars
        self.obj.dist_to_closest_char = min_char_dist

    def use_brain(self):
        """
        Run inputs through animals neural network (brain) and set actions accordingly
        """
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
        """
        Calculate reward of result of actions made
        """
        # if self.obj.energy > self.obj.energy_prev:  # Energy went down
        #     self.obj.reward += 0.5  # Value of positive energy change
        # elif self.obj.energy < self.obj.energy_prev:
        #     self.obj.reward -= 1  # Value of negative energy change
        # if self.obj.hp > self.obj.hp_prev:
        #     self.obj.reward += 0.5  # Value of positive hp change
        # elif self.obj.hp < self.obj.hp_prev:
        #     self.obj.reward -= 1  # Value of negative energy change
        # if self.obj.reproduce:
        #     self.obj.reward += 10
        # # Add death penalty when reinforcement learning
        # if self.dead:
        #     self.obj.reward += self.age

        if self.obj.position[0] < 250:
            self.obj.reward += 0.1
