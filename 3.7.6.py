class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __len__(self):
        return int(pow((self.x2-self.x1)**2+(self.y2-self.y1)**2, 1/2))
