import random
import myMath
import variables
import neuralNet
import numpy as np


# Generate random positions
def generate_random_pos():
    x = random.randint(0, variables.WIDTH)
    y = random.randint(0, variables.HEIGHT)
    pos = [x, y]

    return pos


# Generate characters neural nets
def generate_nets(char_amount):
    char_list = []
    for i in range(char_amount):
        temp_net = Character()
        char_list.append(temp_net)

    return char_list


# Remove character
def remove_char(char_list, index):
    char_list.remove(char_list[index])


# Copy char
def copy_char(char, char_list):
    char_list.append(char)


class Character:
    def __init__(self):
        # Char position
        self.position = [0, 0]

        # Char brain
        self.brain = neuralNet.NeuralNet(self)

        # Char ex previous values
        self.chars_in_range_prev = 0
        self.food_in_range_prev = 0
        self.dist_to_food_prev = -1
        self.eat_index_prev = -1

        # Char int previous values
        self.energy_prev = 100
        self.dmg_prev = 100
        self.hp_prev = 100
        self.vel_prev = 0
        self.age_prev = 0

        # Char external observations
        self.chars_in_range = 0
        self.food_in_range = 0
        self.dist_to_food = -1
        self.eat_index = -1

        # Char internal states
        self.energy = 100
        # self.dmg = 100
        self.hp = 100
        self.vel = 0
        self.age = 0

        # Char brain characteristics
        self.layers = 1
        self.learn_rate = 0.9

        # Char external actions
        self.kill = False
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.vel_inc = False
        self.vel_dec = False
        self.reproduce = False

    # ______________________Char functions________________________

    # Preform character actions
    def external_char_actions(self, char_list, radius, border):
        for i in range(len(char_list)):
            # Check for movement
            if self.left and self.position[0] - self.vel - radius > 0:  # LEFT
                self.position[0] -= self.vel
            if self.right and self.position[0] + self.vel + radius < border.width:  # RIGHT
                self.position[0] += self.vel
            if self.up and self.position[1] - self.vel - radius > 0:  # UP
                self.position[1] -= self.vel
            if self.down and self.position[1] + self.vel + radius < border.height:  # DOWN
                self.position[1] += self.vel

    # Check if any characters reproduced
    def natural_selection(self, char_list):
        if self.energy > 100:
            copy_char(self, char_list)
            self.energy = 100

    # Check for characters in range
    def num_chars_in_range(self, main_player, char_list, view_radius):
        num = 0
        if myMath.pt_calc_dist(self.position, main_player.position) < view_radius:
            num += 1
        for i in range(len(char_list)):
            if myMath.pt_calc_dist(self.position, char_list[i].position) < view_radius and \
                    self.position != char_list[i].position:
                num += 1
                if num >= 15:
                    break
        self.chars_in_range = num

    # Check for food in range
    def plants_in_range(self, food_poses, view_radius):
        num = 0
        index = 0
        minim = -1

        for n in food_poses:
            if index == 0:
                minim = myMath.pt_calc_dist(self.position, n.position)
            if myMath.pt_calc_dist(self.position, n.position) < view_radius and self.position != n.position:
                num += 1
                if minim > myMath.pt_calc_dist(self.position, n.position):
                    minim = myMath.pt_calc_dist(self.position, n.position)
                    self.eat_index = index
                if num >= 15:
                    break
            index += 1
        self.food_in_range = num
        self.dist_to_food = minim

    # Run network
    def use_brain(self):
        # Input aray
        i_arr = np.array([self.chars_in_range, self.food_in_range, self.dist_to_food, self.energy, self.hp])
        # Normalize  input array to between 0 and 1
        norm_i_arr = (i_arr - np.min(i_arr)) / (np.max(i_arr) - np.min(i_arr))

        # Layer sizes
        layer_sizes = np.array([len(norm_i_arr), 10, 10, 9])

        self.brain.run_network(norm_i_arr, layer_sizes)
