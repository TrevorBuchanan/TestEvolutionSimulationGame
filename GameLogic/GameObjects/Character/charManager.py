from GameLogic.GameObjects.Character.character import Character
from GameLogic.GameObjects.objectManager import ObjectManager


class CharacterManager(ObjectManager):
    def __init__(self):
        self.char = Character([0, 0], 1)
