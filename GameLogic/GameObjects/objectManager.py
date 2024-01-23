
class ObjectManager:

    def act(self, game_objects):
        self.draw()
        self.perform_actions(game_objects)

    def draw(self):
        raise Exception("Not implemented \'draw\' function")

    def perform_actions(self, game_objects):
        raise Exception("Not implemented \'perform_actions\' function")
