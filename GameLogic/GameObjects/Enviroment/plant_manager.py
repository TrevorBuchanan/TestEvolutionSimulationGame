import pygame

from GameLogic.GameObjects.Enviroment.plant import Plant
from GameLogic.GameUtilities.colors import PLANT_GREEN
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.settings import SCREEN
from GameLogic.GameUtilities.utility import pt_calc_dist


class PlantManager(ObjectManager):
    def __init__(self):
        self.plant = Plant()
        self.being_eaten = False

    def act(self, game_objects):
        self.plant_being_eaten()

    def draw(self):
        pygame.draw.circle(SCREEN, PLANT_GREEN, self.plant.position, self.plant.radius)

    # Food being eaten
    def plant_being_eaten(self, game_objects):
        if pt_calc_dist(main_player.position, self.position) < CHARACTER_RADIUS and self.total_nutrients > 0 \
                and player_eat and main_player.energy < 100:
            if self.total_nutrients > 0:
                self.total_nutrients -= self.nutrients
            if self.radius > 4:
                self.radius -= self.nutrients
            self.total_nutrients -= self.nutrients
            self.radius -= self.nutrients
            if main_player.energy + self.nutrients > 100:
                main_player.energy = 100
            else:
                main_player.energy += self.nutrients
        for n in chars:
            if pt_calc_dist(n.position,
                            self.position) < CHARACTER_RADIUS and self.total_nutrients > 0 and n.energy < 100:
                if self.total_nutrients > 0:
                    self.total_nutrients -= self.nutrients
                if self.radius > 4:
                    self.radius -= self.nutrients
                if n.energy + self.growth >= 100:
                    n.reproduce = True
                    n.energy = 100
                else:
                    n.energy += self.growth
