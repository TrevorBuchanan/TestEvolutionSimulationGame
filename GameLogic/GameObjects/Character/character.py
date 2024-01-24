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
        self.dmg = 10
        self.gain_loss = 0.005

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

    # Preform character movement
    def move(self):
        if self.left and self.position[0] - self.speed - self.radius > 0:  # LEFT
            self.position[0] -= self.speed
        if self.right and self.position[0] + self.speed + self.radius < WIDTH:  # RIGHT
            self.position[0] += self.speed
        if self.up and self.position[1] - self.speed - self.radius > 0:  # UP
            self.position[1] -= self.speed
        if self.down and self.position[1] + self.speed + self.radius < HEIGHT:  # DOWN
            self.position[1] += self.speed

    # Change speeds
    def change_speed(self):  # Maybe make min and max speed be traits
        if self.speed_up:
            self.speed += 0.1
            if self.speed > 5:
                self.speed = 5

        if self.slow_down:
            self.speed -= 0.1
            if self.speed < 1:
                self.speed = 1
