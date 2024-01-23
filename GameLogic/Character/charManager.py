from GameLogic.Character.character import Character


class CharacterManager:
    def __init__(self):
        self.char = Character([0, 0], 1)

    def act(self, game_objects):
        raise Exception("Not Implemented \'act\' function")
