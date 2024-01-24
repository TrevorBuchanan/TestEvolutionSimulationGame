from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.settings import PLANT_RADIUS, PLANT_NUTRIENTS
from GameLogic.GameUtilities.utility import scale_to_range


class PlantManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Plant()
        self.being_eaten = False

    def perform_actions(self, game_objects):
        self.get_eaten()
        self.grow()
        self.normalize_radius()

    # Plant growth
    def grow(self):
        if self.obj.total_nutrients + self.obj.growth <= PLANT_NUTRIENTS:
            self.obj.total_nutrients += self.obj.growth

    # Plant being eaten
    def get_eaten(self):
        if self.being_eaten:
            self.obj.total_nutrients -= self.obj.nutrients
            self.being_eaten = False

    def normalize_radius(self):
        min_radius = 4
        max_radius = PLANT_RADIUS
        min_nutrients = 0
        max_nutrients = PLANT_NUTRIENTS
        self.obj.radius = scale_to_range(min_nutrients, max_nutrients,
                                         min_radius, max_radius, self.obj.total_nutrients)
