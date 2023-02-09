class Point:

    # def __new__(cls, *args, **kwargs):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(10, 10)
pt_clone = pt.clone()
print(id(pt), id(pt_clone))
print(pt.x, pt.y, pt_clone.x, pt_clone.y)