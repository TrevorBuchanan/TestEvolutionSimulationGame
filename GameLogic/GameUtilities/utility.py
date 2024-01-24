import random
import math

from GameLogic.GameUtilities.settings import FONT, SCREEN


# 2 points distance calculation
def pt_calc_dist(point1, point2):
    return math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))


# Generate random positions
def generate_random_pos(width, height):
    return [random.randint(0, width), random.randint(0, height)]


# Scale a value to a desired range
def scale_to_range(old_min, old_max, new_min, new_max, value):
    return (new_max - new_min) * ((value - old_min) / (old_max - old_min)) + new_min


# Draw text to screen
def write_to_screen(text, position, color):
    t = FONT.render(text, True, color)
    SCREEN.blit(t, position)
