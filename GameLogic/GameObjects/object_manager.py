class ObjectManager:
    def __init__(self):
        self.obj = None
        self.dead = False
        self.age = 0
        self.age_increment = 0.005

    def act(self, game_objects):
        """
        Perform object's actions
        :param game_objects: List of all current game objects
        """
        self.age += self.age_increment

    def draw(self):
        """
        Draws specified object qualities to the screen
        """
        pass

    def draw_stats(self):
        """
        Writes object's statistics to the screen
        """
        raise Exception("Not implemented \'draw_stats\' function")

    def end_life_if_dead(self, game_objects):
        """
        Remove game object if object is dead
        :param game_objects: List of all current game objects
        """
        if self.dead:
            game_objects.remove(self)

