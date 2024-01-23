from GameLogic.Character.animal import Animal
from GameLogic.Enviroment.plant import Plant
from GameLogic.colors import BEIGE
from GameLogic.Character.charManager import CharacterManager
from GameLogic.utility import pt_calc_dist


class AnimalManager(CharacterManager):
    def __init__(self):
        super().__init__()
        self.char = Animal()
        self.char.color = BEIGE

    def act(self, game_objects):
        self.char.draw()
        self.perform_actions(game_objects)

    def perform_actions(self, game_objects):
        self.set_objects_in_range(game_objects)
        self.char.move()

    # Check if any characters reproduced
    def natural_selection(self):
        if self.char.energy > 100:
            self.char.reproduce = True
            self.char.energy = 90

    # Check for characters in range
    def set_objects_in_range(self, game_objects):
        num_chars = 0
        num_plants = 0
        eat_index = 0
        min_plant_dist = 0
        for obj in game_objects:
            if isinstance(obj, CharacterManager):
                if pt_calc_dist(self.char.position, obj.char.position) < self.char.view_range and \
                        self.char.position != obj.char.position:
                    num_chars += 1
                    if num_chars >= 15:
                        break
            elif isinstance(obj, Plant):
                if eat_index == 0:
                    min_plant_dist = pt_calc_dist(self.char.position, obj.position)
                if pt_calc_dist(self.char.position,
                                obj.position) < self.char.view_range and self.char.position != obj.position:
                    num_plants += 1
                    if min_plant_dist > pt_calc_dist(self.char.position, obj.position):
                        min_plant_dist = pt_calc_dist(self.char.position, obj.position)
                        self.char.eat_index = eat_index
                    if num_plants >= 15:
                        break
                eat_index += 1

        self.char.plants_in_range = num_plants
        self.char.dist_to_food = min_plant_dist
        self.char.chars_in_range = num_chars

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
