from GameLogic.GameUtilities.colors import DULL_RED
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT


class Character:
    def __init__(self, initial_position, radius):
        # Char position
        self.position = initial_position

        # Char characteristics
        self.radius = radius

        # Char traits
        self.color = DULL_RED
        self.dmg = 2
        self.gain_loss = 0.01
        self.min_speed = 1
        self.max_speed = 5

        # Char internal states
        self.energy = 100
        self.hp = 100
        self.speed = 1

        # Char external actions
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.deal_dmg = False
        self.eat = False
        self.speed_up = False
        self.slow_down = False
        self.reproduce = False