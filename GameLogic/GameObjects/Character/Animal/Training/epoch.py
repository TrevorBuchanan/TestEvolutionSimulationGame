
class Epoch:
    """
    Epoch object (Epoch is period of time, in this case a generation that is made to end and reproduce)
    """

    def __init__(self):
        self.count = 0
        self.top_selection_amount = 15
        self.epoch_time = 3
