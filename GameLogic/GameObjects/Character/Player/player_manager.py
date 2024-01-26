import pygame

from GameLogic.GameObjects.Character.Player.player import Player
from GameLogic.GameObjects.Character.char_manager import CharacterManager
from GameLogic.GameUtilities.settings import INPUT


class PlayerManager(CharacterManager):
    """
    CharacterManager object for Player object
    """
    def __init__(self):
        super().__init__()
        self.obj = Player()

    def act(self, game_objects):
        # Perform actions
        super().act(game_objects)
        if self.dead:
            # Dead stuff
            pass
        else:
            self.check_deal_dmg()
            self.check_eat()
            self.check_move()
            self.check_change_speed()

    def draw(self):
        # Draw qualities to the screen
        super().draw()
        super().draw_stats()

    def check_deal_dmg(self):
        """
        Check for deal_dmg user input and set deal_dmg action accordingly
        """
        if INPUT.keys[pygame.K_SPACE]:
            self.obj.deal_dmg = True
        else:
            self.obj.deal_dmg = False

    def check_eat(self):
        """
        Check for eat user input and set eat action accordingly
        """
        if INPUT.keys[pygame.K_e]:
            self.obj.eat = True
        else:
            self.obj.eat = False

    def check_move(self):
        """
        Check for movement input and set move direction accordingly
        """
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

    def check_change_speed(self):
        """
        Check for speed change input and set actions accordingly
        """
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
