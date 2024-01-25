import pygame

from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import SCREEN, WIDTH
from GameLogic.GameUtilities.utility import write_to_screen


class ObjectManager:
    def __init__(self):
        self.obj = None
        self.dead = False

    def act(self, game_objects):
        self.draw()
        self.perform_actions(game_objects)

    def draw(self):
        if self.obj is None:
            raise Exception("Object \'obj\' is not an object")
        pygame.draw.circle(SCREEN, self.obj.color, self.obj.position, self.obj.radius)

    def draw_stats(self):
        raise Exception("Not implemented \'draw_stats\' function")

    def perform_actions(self, game_objects):
        raise Exception("Not implemented \'perform_actions\' function")

    def end_life_if_dead(self, game_objects):
        if self.dead:
            game_objects.remove(self)

