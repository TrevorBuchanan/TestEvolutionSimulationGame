from GameLogic.GameUtilities.colors import PLANT_GREEN
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT
from GameLogic.GameUtilities.utility import generate_random_pos


class Plant:
    def __init__(self):
        self.position = generate_random_pos(WIDTH, HEIGHT)

        self.total_nutrients = 10
        self.nutrients = 0.03
        self.growth = 0.02
        self.radius = 10
        self.color = PLANT_GREEN
