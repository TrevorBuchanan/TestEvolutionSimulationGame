import pygame

from GameLogic.Character.character import Character
from GameLogic.settings import WIDTH, HEIGHT, CHARACTER_RADIUS
from GameLogic.utility import pt_calc_dist, generate_random_pos


class Player(Character):
    def __init__(self):
        super().__init__(generate_random_pos(WIDTH, HEIGHT), CHARACTER_RADIUS)

    def char_i_in_range(self, net_list, kill_radius):
        kill_index = 0
        for i in range(len(net_list)):
            if pt_calc_dist(self.position, net_list[i].position) < 2 * kill_radius and \
                    self.position != net_list[i].position:
                if self.energy + 10 >= 100:
                    self.energy = 100
                else:
                    self.energy += 10

                return kill_index
            kill_index += 1

        return -1

