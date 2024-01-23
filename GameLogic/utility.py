import random
import math


# 2 points distance calculation
def pt_calc_dist(point1, point2):
    return math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))


# Generate random positions
def generate_random_pos(width, height):
    return [random.randint(0, width), random.randint(0, height)]
