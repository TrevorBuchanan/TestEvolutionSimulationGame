from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameUtilities.settings import WIDTH, HEIGHT, CHARACTER_RADIUS
from GameLogic.GameUtilities.utility import generate_random_pos


class Player(Character):
    """
    Player character object
    """
    def __init__(self):
        super().__init__(generate_random_pos(WIDTH, HEIGHT), CHARACTER_RADIUS)
