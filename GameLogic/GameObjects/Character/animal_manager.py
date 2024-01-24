import pygame

from GameLogic.GameObjects.Character.animal import Animal
from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameUtilities.colors import BEIGE, WHITE
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.settings import SCREEN
from GameLogic.GameUtilities.utility import pt_calc_dist, write_to_screen


class AnimalManager(CharacterManager):
    def __init__(self):
        super().__init__()
        self.obj = Animal()
        self.obj.color = BEIGE

    def perform_actions(self, game_objects):
        super().perform_actions(game_objects)
        self.set_objects_in_range(game_objects)
        self.obj.move()

    # Check if any characters reproduced
    def natural_selection(self):
        if self.obj.energy > 100:
            self.obj.reproduce = True
            self.obj.energy = 90

    # Check for characters in range
    def set_objects_in_range(self, game_objects):
        num_chars = 0
        num_plants = 0
        eat_index = 0
        min_plant_dist = 0
        for obj in game_objects:
            if isinstance(obj, CharacterManager):
                if pt_calc_dist(self.obj.position, obj.obj.position) < self.obj.view_range and \
                        self.obj.position != obj.obj.position:
                    num_chars += 1
                    if num_chars >= 15:
                        break
            elif isinstance(obj, Plant):
                if eat_index == 0:
                    min_plant_dist = pt_calc_dist(self.obj.position, obj.position)
                if pt_calc_dist(self.obj.position,
                                obj.position) < self.obj.view_range and self.obj.position != obj.position:
                    num_plants += 1
                    if min_plant_dist > pt_calc_dist(self.obj.position, obj.position):
                        min_plant_dist = pt_calc_dist(self.obj.position, obj.position)
                        self.obj.eat_index = eat_index
                    if num_plants >= 15:
                        break
                eat_index += 1

        self.obj.plants_in_range = num_plants
        self.obj.dist_to_food = min_plant_dist
        self.obj.chars_in_range = num_chars

    # Run network
    def use_brain(self):
        pass
        # # Input aray
        # i_arr = np.array([self.chars_in_range, self.food_in_range, self.dist_to_food, self.energy, self.hp])
        #
        # # Normalize  input array to between 0 and 1
        # norm_i_arr = (i_arr - np.min(i_arr)) / (np.max(i_arr) - np.min(i_arr))
        #
        # # Layer sizes
        # layer_sizes = np.array([len(norm_i_arr), 10, 10, 9])
        #
        # self.brain.run_network(norm_i_arr, layer_sizes)
