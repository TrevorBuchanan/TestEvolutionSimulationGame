import pygame

from GameLogic.Character.player import Player
from GameLogic.Character.charManager import CharacterManager
from GameLogic.settings import INPUT


class PlayerManager(CharacterManager):
    def __init__(self):
        super().__init__()
        self.char = Player()

    def act(self, game_objects):
        self.char.draw()
        self.perform_actions()

    # Perform actions
    def perform_actions(self):
        self.player_kill()
        self.player_move()
        self.player_change_speed()
        self.char.move()
        self.char.change_speed()

    # Check if kill
    def player_kill(self):
        if INPUT.keys[pygame.K_SPACE]:
            self.char.kill = True
        else:
            self.char.kill = False

    # Check for move
    def player_move(self):
        if INPUT.keys[pygame.K_a]:  # LEFT
            self.char.left = True
            self.char.right = False
        else:
            self.char.left = False
        if INPUT.keys[pygame.K_d]:  # RIGHT
            self.char.right = True
            self.char.left = False
        else:
            self.char.right = False
        if INPUT.keys[pygame.K_w]:  # UP
            self.char.up = True
            self.char.down = False
        else:
            self.char.up = False
        if INPUT.keys[pygame.K_s]:  # DOWN
            self.char.down = True
            self.char.up = False
        else:
            self.char.down = False

    # Player speed setting input
    def player_change_speed(self):
        if INPUT.keys[pygame.K_p]:
            self.char.speed_up = True
            self.char.slow_down = False
        else:
            self.char.speed_up = False

        if INPUT.keys[pygame.K_o]:
            self.char.slow_down = True
            self.char.speed_up = False
        else:
            self.char.slow_down = False
