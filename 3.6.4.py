class Rect:

    def __init__(self, *args):
        self.x, self.y, self.width, self.height = args

    def __hash__(self):
        return hash((self.width, self.height))
