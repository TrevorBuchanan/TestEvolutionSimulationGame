import pygame

from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameObjects.Character.player_manager import PlayerManager
from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameUtilities.colors import PLANT_GREEN
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.settings import SCREEN, PLANT_RADIUS, PLANT_NUTRIENTS
from GameLogic.GameUtilities.utility import pt_calc_dist, scale_to_range


class PlantManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Plant()
        self.being_eaten = False

    def perform_actions(self, game_objects):
        self.plant_being_eaten(game_objects)
        self.grow()
        self.normalize_radius()

    # Plant growth
    def grow(self):
        if self.obj.total_nutrients + self.obj.growth <= PLANT_NUTRIENTS:
            self.obj.total_nutrients += self.obj.growth

    # Plant being eaten
    def plant_being_eaten(self, game_objects):
        # Loop through all game objects
        for game_obj in game_objects:
            # Check if object is a character
            if isinstance(game_obj, CharacterManager):
                # Check if character is in range, plant has nutrients, and characters energy is less than 100
                if game_obj.obj.eat and pt_calc_dist(game_obj.obj.position, self.obj.position) < game_obj.obj.radius \
                        + self.obj.radius and self.obj.total_nutrients > 0:  # and obj.char.energy < 100
                    # If plant still has nutrients, give nutrients to character
                    if self.obj.total_nutrients > 0:
                        self.obj.total_nutrients -= self.obj.nutrients
                        game_obj.obj.energy += self.obj.nutrients

                    if not isinstance(game_obj, PlayerManager):
                        if game_obj.obj.energy + self.obj.nutrients >= 100:
                            game_obj.obj.reproduce = True

    def normalize_radius(self):
        min_radius = 4
        max_radius = PLANT_RADIUS
        min_nutrients = 0
        max_nutrients = PLANT_NUTRIENTS
        self.obj.radius = scale_to_range(min_nutrients, max_nutrients,
                                         min_radius, max_radius, self.obj.total_nutrients)
