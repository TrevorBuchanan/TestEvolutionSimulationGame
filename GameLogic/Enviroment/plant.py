import random

from GameLogic.colors import PLANT_GREEN
from GameLogic.settings import WIDTH, HEIGHT, CHARACTER_RADIUS, PLANT_DECREMENT
from GameLogic.utility import pt_calc_dist, generate_random_pos


class Plant:
    def __init__(self):
        self.position = generate_random_pos(WIDTH, HEIGHT)
        self.nutrients = 10
        self.radius = 10
        self.color = PLANT_GREEN

    # Food being eaten
    def being_eaten(self, player_eat, main_player, chars):
        if pt_calc_dist(main_player.position, self.position) < CHARACTER_RADIUS and self.nutrients > 0 \
                and player_eat and main_player.energy < 100:
            if self.nutrients > 0:
                self.nutrients -= PLANT_DECREMENT
            if self.radius > 4:
                self.radius -= PLANT_DECREMENT
            self.nutrients -= PLANT_DECREMENT
            self.radius -= PLANT_DECREMENT
            if main_player.energy + energy_increment_amount > 100:
                main_player.energy = 100
            else:
                main_player.energy += variables.energy_increment_amount
        for n in chars:
            if myMath.pt_calc_dist(n.position,
                                   self.position) < variables.char_radius and self.nutrients > 0 and n.energy < 100:
                if self.nutrients > 0:
                    self.nutrients -= variables.food_decrement
                if self.radius > 4:
                    self.radius -= variables.food_decrement
                if n.energy + variables.energy_increment_amount >= 100:
                    n.reproduce = True
                    n.energy = 100
                else:
                    n.energy += variables.energy_increment_amount
