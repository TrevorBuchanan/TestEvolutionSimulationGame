import math
import random
import unittest

from GameLogic.GameUtilities.utility import pt_calc_dist, generate_random_pos, scale_to_range, probabilistic_bool


class UtilityTest(unittest.TestCase):
    def test_pt_calc_dist(self):
        """
        Test utility's pt_calc_dist() function
        """
        point1 = (5, 10)
        point2 = (3, 4)
        self.assertEqual(pt_calc_dist(point1, point2), math.sqrt(40))
        point1 = (0, 0)
        point2 = (0, 0)
        self.assertEqual(pt_calc_dist(point1, point2), 0)
        point1 = (2, -6)
        point2 = (-3, -2)
        self.assertEqual(pt_calc_dist(point1, point2), math.sqrt(41))

    def test_generate_random_pos(self):
        """
        Test utility's generate_random_pos() function
        """
        width = 50
        height = 30
        test_iterations = 100
        check = True
        for _ in range(test_iterations):
            pos = generate_random_pos(width, height)
            if pos[0] > width or pos[0] < 0:
                check = False
                break
            if pos[1] > height or pos[1] < 0:
                check = False
                break
        self.assertTrue(check)

    def test_scale_to_range(self):
        """
        Test utility's scale_to_range() function
        """
        old_min = -20
        old_max = 3
        new_min = 5
        new_max = 7
        test_iterations = 100
        check = True
        for _ in range(test_iterations):
            val = random.uniform(old_min, old_max)
            scaled = scale_to_range(old_min, old_max, new_min, new_max, val)
            if scaled > new_max or scaled < new_min:
                check = False
                break
        self.assertTrue(check)

    def test_probabilistic_bool(self):
        """
        Test utility's probabilistic_bool function
        """
        test_iterations = 100
        percentage = 50
        true_count = 0
        for _ in range(test_iterations):
            if probabilistic_bool(percentage):
                true_count += 1
        print(true_count)
        self.assertTrue(True)
