from GameLogic.GameUtilities.colors import PLANT_GREEN
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, PLANT_RADIUS, PLANT_NUTRIENTS
from GameLogic.GameUtilities.utility import generate_random_pos


class Plant:
    def __init__(self):
        self.position = generate_random_pos(WIDTH, HEIGHT)

        self.total_nutrients = PLANT_NUTRIENTS
        self.nutrients = 0.05
        self.growth = 0.01
        self.radius = PLANT_RADIUS
        self.color = PLANT_GREEN
