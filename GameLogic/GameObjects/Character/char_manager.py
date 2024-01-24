from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameObjects.objectManager import ObjectManager
from GameLogic.GameUtilities.colors import WHITE
from GameLogic.GameUtilities.settings import WIDTH
from GameLogic.GameUtilities.utility import write_to_screen


class CharacterManager(ObjectManager):
    def __init__(self):
        super().__init__()
        self.obj = Character([0, 0], 1)

    # Draw player stats
    def draw_stats(self):
        write_to_screen(f"Energy: {round(self.obj.energy)}", [WIDTH - 120, 50], WHITE)
        write_to_screen(f"HP: {round(self.obj.hp)}", [WIDTH - 120, 80], WHITE)
        write_to_screen(f"Speed: {round(self.obj.speed, 2)}", [WIDTH - 120, 110], WHITE)

    def perform_actions(self, game_objects):
        self.loss()
        self.kill(game_objects)

    # Kill other character
    def kill(self, game_objects):
        if self.obj.kill:
            print("kill")
            pass

    # Decrement energy
    def loss(self):
        if self.obj.up or self.obj.down or self.obj.right or self.obj.left:
            self.obj.energy -= self.obj.loss * self.obj.speed
        else:
            self.obj.energy -= self.obj.loss

        if self.obj.energy <= 0:
            self.obj.hp -= self.obj.loss
            self.obj.energy = 0
