import math

import pygame

from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameObjects.Enviroment.plant_manager import PlantManager
from GameLogic.GameObjects.object_manager import ObjectManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import WIDTH, SCREEN, HEIGHT
from GameLogic.GameUtilities.utility import write_to_screen, pt_calc_dist


class CharacterManager(ObjectManager):
    """
    ObjectManager game object for Character object
    """
    def __init__(self):
        super().__init__()
        self.obj = Character([0, 0], 1)

    def act(self, game_objects):
        super().act(game_objects)
        self.check_dead()
        self.gain_and_loss()
        self.damage_and_eat(game_objects)
        self.move()
        self.change_speed()

    def draw(self):
        # Draw specified characteristics
        pygame.draw.circle(SCREEN, self.obj.color, self.obj.position, self.obj.radius)

    def draw_stats(self):
        # Draw character stats
        write_to_screen(f"Energy: {round(self.obj.energy)}", [WIDTH - 120, 50], WHITE)
        write_to_screen(f"HP: {round(self.obj.hp)}", [WIDTH - 120, 80], WHITE)
        write_to_screen(f"Speed: {round(self.obj.speed, 2)}", [WIDTH - 120, 110], WHITE)
        write_to_screen(f"Age: {math.floor(self.age)}", [WIDTH - 120, 140], WHITE)

    def damage_and_eat(self, game_objects):
        """
        Perform damage to other characters and eating actions
        :param game_objects: List of all current game objects
        """
        if self.obj.deal_dmg or self.obj.eat:
            # Loop through all game objects
            for game_obj in game_objects:

                # Check if object is a character
                if isinstance(game_obj, CharacterManager):
                    if self.obj.deal_dmg and 0 < pt_calc_dist(self.obj.position, game_obj.obj.position) < \
                            self.obj.radius + game_obj.obj.radius and self.obj.energy > 0:
                        if game_obj.obj.hp - self.obj.dmg > 0:
                            game_obj.obj.hp -= self.obj.dmg
                            # Dealing damage cost 1/10th of damage delt
                            if self.obj.energy - 0.1 * self.obj.dmg >= 0:
                                self.obj.energy -= 0.1 * self.obj.dmg
                            else:
                                self.obj.energy = 0
                        else:
                            game_obj.dead = True
                        if game_obj.dead:
                            #          Value for eating char
                            if self.obj.energy + 25 >= 100:
                                self.obj.energy = 100
                            else:
                                self.obj.energy += 25
                if isinstance(game_obj, PlantManager):
                    # Check if character is in range, plant has nutrients, and characters energy is less than 100
                    if self.obj.eat and pt_calc_dist(self.obj.position, game_obj.obj.position) < self.obj.radius \
                            + game_obj.obj.radius and game_obj.obj.total_nutrients > 0 and self.obj.energy < 100:
                        game_obj.obj.total_nutrients -= game_obj.obj.nutrients
                        self.obj.energy += game_obj.obj.nutrients
                        game_obj.obj.being_eaten = True

    def gain_and_loss(self):
        """
        Add gains and losses to energy and hp
        """
        if self.obj.up or self.obj.down or self.obj.right or self.obj.left:
            self.obj.energy -= self.obj.gain_loss * self.obj.speed
        else:
            self.obj.energy -= self.obj.gain_loss

        if self.obj.energy <= 0:
            self.obj.hp -= self.obj.gain_loss * 3
            self.obj.energy = 0

        if self.obj.energy > 0 and self.obj.hp + self.obj.gain_loss <= 100:
            self.obj.hp += self.obj.gain_loss * 3
            self.obj.energy -= self.obj.gain_loss

    def check_dead(self):
        """
        Set object to dead when hp is 0
        """
        if self.obj.hp <= 0:
            self.dead = True

    def move(self):
        """
        Preform character movement
        """
        if self.obj.left and self.obj.position[0] - self.obj.speed - self.obj.radius > 0:  # LEFT
            self.obj.position[0] -= self.obj.speed
        if self.obj.right and self.obj.position[0] + self.obj.speed + self.obj.radius < WIDTH:  # RIGHT
            self.obj.position[0] += self.obj.speed
        if self.obj.up and self.obj.position[1] - self.obj.speed - self.obj.radius > 0:  # UP
            self.obj.position[1] -= self.obj.speed
        if self.obj.down and self.obj.position[1] + self.obj.speed + self.obj.radius < HEIGHT:  # DOWN
            self.obj.position[1] += self.obj.speed

    def change_speed(self):
        """
        Perform speed changes according to speed_up and slow_down
        """
        if self.obj.speed_up:
            self.obj.speed += 0.1
            if self.obj.speed > self.obj.max_speed:
                self.obj.speed = 5

        if self.obj.slow_down:
            self.obj.speed -= 0.1
            if self.obj.speed < self.obj.min_speed:
                self.obj.speed = self.obj.min_speed
