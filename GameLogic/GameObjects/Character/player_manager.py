import pygame

from GameLogic.GameObjects.Character.player import Player
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.settings import INPUT


class PlayerManager(CharacterManager):
    def __init__(self):
        super().__init__()
        self.obj = Player()

    # Perform actions
    def perform_actions(self, game_objects):
        if self.dead:
            # Dead stuff
            pass
        else:
            super().perform_actions(game_objects)
            self.check_kill()
            self.check_eat()
            self.check_move()
            self.check_change_speed()
            self.obj.move()
            self.obj.change_speed()

    # Check if kill
    def check_kill(self):
        if INPUT.keys[pygame.K_SPACE]:
            self.obj.deal_dmg = True
        else:
            self.obj.deal_dmg = False

    # Check if eat
    def check_eat(self):
        if INPUT.keys[pygame.K_e]:
            self.obj.eat = True
        else:
            self.obj.eat = False

    # Check for move
    def check_move(self):
        if INPUT.keys[pygame.K_a]:  # LEFT
            self.obj.left = True
            self.obj.right = False
        else:
            self.obj.left = False
        if INPUT.keys[pygame.K_d]:  # RIGHT
            self.obj.right = True
            self.obj.left = False
        else:
            self.obj.right = False
        if INPUT.keys[pygame.K_w]:  # UP
            self.obj.up = True
            self.obj.down = False
        else:
            self.obj.up = False
        if INPUT.keys[pygame.K_s]:  # DOWN
            self.obj.down = True
            self.obj.up = False
        else:
            self.obj.down = False

    # Check player speed change
    def check_change_speed(self):
        if INPUT.keys[pygame.K_p]:
            self.obj.speed_up = True
            self.obj.slow_down = False
        else:
            self.obj.speed_up = False

        if INPUT.keys[pygame.K_o]:
            self.obj.slow_down = True
            self.obj.speed_up = False
        else:
            self.obj.slow_down = False
