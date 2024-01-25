class ObjectManager:
    def __init__(self):
        self.obj = None
        self.dead = False
        self.age = 0

    def act(self, game_objects):
        self.age += 0.005

    def draw(self):
        raise Exception("Not implemented \'draw\' function")

    def draw_stats(self):
        raise Exception("Not implemented \'draw_stats\' function")

    def end_life_if_dead(self, game_objects):
        if self.dead:
            game_objects.remove(self)

