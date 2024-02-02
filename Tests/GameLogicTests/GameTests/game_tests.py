import unittest

from GameLogic.Game.game import Game


class GameTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.test_game = Game()
