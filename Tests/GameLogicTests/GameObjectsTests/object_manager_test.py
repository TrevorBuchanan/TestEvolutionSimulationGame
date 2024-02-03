import unittest

from GameLogic.GameObjects.object_manager import ObjectManager


class CharacterManagerTest(unittest.TestCase):
    def test_act(self):
        """
        Test ObjectManager's act() function
        """
        game_objects = []
        test_obj_man = ObjectManager()
        age = 0
        test_obj_man.act(game_objects)
        age += test_obj_man.age_increment
        self.assertEqual(age, test_obj_man.age)

    def test_end_life_if_dead(self):
        """
        Test ObjectManager's end_life_if_dead() function
        """
        game_objects = []
        test_obj_man = ObjectManager()
        game_objects.append(test_obj_man)
        test_obj_man.dead = True
        test_obj_man.end_life_if_dead(game_objects)
        self.assertTrue(len(game_objects) == 0)
