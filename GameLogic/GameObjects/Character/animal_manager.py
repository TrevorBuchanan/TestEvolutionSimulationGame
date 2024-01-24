from GameLogic.GameObjects.Character.animal import Animal
from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameUtilities.colors import BEIGE
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.utility import pt_calc_dist


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
        # Inputs
        inputs = [self.obj.plants_in_range, self.obj.dist_to_closest_plant, self.obj.chars_in_range,
                  self.obj.dist_to_closest_char, self.obj.energy, self.obj.hp, self.obj.speed, self.obj.left,
                  self.obj.right, self.obj.up, self.obj.down, self.obj.eat, self.obj.deal_dmg, self.obj.speed_up,
                  self.obj.slow_down]

        self.obj.brain.get_outputs(inputs)

    def calculate_reward(self):
        pass
