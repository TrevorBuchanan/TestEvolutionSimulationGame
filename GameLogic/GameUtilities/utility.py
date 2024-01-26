import random
import math

from GameLogic.GameUtilities.settings import FONT, SCREEN


def pt_calc_dist(point1, point2):
    """
    Calculated the distance between 2 points
    :param point1: x,y coordinate (2-tuple)
    :param point2: x,y coordinate (2-tuple)
    :return: Distance between the 2 given points
    """
    return math.sqrt(math.pow((point1[0] - point2[0]), 2) + math.pow((point1[1] - point2[1]), 2))


def generate_random_pos(width, height):
    """
    Generate a random position within width and height
    :param width: Limit of width of generated position
    :param height: Limit of height of generated position
    :return: Result random position (2-tuple)
    """
    return [random.randint(0, width), random.randint(0, height)]


def scale_to_range(old_min, old_max, new_min, new_max, value):
    """
    Scale a value to a desired range
    :param old_min: Minimum of value's previous range
    :param old_max: Maximum of value's previous range
    :param new_min: Minimum of value's desired range
    :param new_max: Maximum of value's desired range
    :param value: value to be scaled
    :return: The scaled value in specified range
    """
    return (new_max - new_min) * ((value - old_min) / (old_max - old_min)) + new_min


def write_to_screen(text, position, color):
    """
    Draw text to screen
    :param text: Content to write to screen (string)
    :param position: Top left start of text (2-tuple)
    :param color: Color of text on screen (3-tuple)
    """
    t = FONT.render(text, True, color)
    SCREEN.blit(t, position)


def probabilistic_bool(percentage):
    """
    Generate a boolean value based on given percentage
    :param percentage: Percent in range [0, 100]
    :return: True 'percentage' percent of the time, False otherwise
    """
    if 0 <= percentage <= 100:
        if random.uniform(0, 1) <= (percentage / 100):
            return True
    else:
        raise Exception("percentage is out of usable range [0, 100]")
    return False
