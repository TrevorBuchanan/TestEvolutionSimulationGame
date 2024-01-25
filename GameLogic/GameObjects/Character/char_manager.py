from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameObjects.Enviroment.plant_manager import PlantManager
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import WIDTH
from GameLogic.GameUtilities.utility import write_to_screen, pt_calc_dist


class CharacterManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Character([0, 0], 1)

    # Draw player stats
    def draw_stats(self):
        write_to_screen(f"Energy: {round(self.obj.energy)}", [WIDTH - 120, 50], WHITE)
        write_to_screen(f"HP: {round(self.obj.hp)}", [WIDTH - 120, 80], WHITE)
        write_to_screen(f"Speed: {round(self.obj.speed, 2)}", [WIDTH - 120, 110], WHITE)
        write_to_screen(f"Age: {round(self.obj.age)}", [WIDTH - 120, 140], WHITE)

    def perform_actions(self, game_objects):
        self.check_dead()
        self.gain_and_loss()
        self.damage_and_eat(game_objects)
        self.obj.age += 0.005

    # Damage other characters and eat
    def damage_and_eat(self, game_objects):
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

    # Decrement energy
    def gain_and_loss(self):
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

    # Check if dead
    def check_dead(self):
        if self.obj.hp <= 0:
            self.dead = True
