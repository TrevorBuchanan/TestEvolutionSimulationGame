class ObjectManager:
    def __init__(self):
        self.obj = None
        self.dead = False

    def act(self, game_objects):
        raise Exception("Not implemented \'perform_actions\' function")

    def draw(self):
        raise Exception("Not implemented \'draw\' function")

    def draw_stats(self):
        raise Exception("Not implemented \'draw_stats\' function")

    def end_life_if_dead(self, game_objects):
        if self.dead:
            game_objects.remove(self)

