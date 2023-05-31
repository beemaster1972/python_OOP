class Ellipse:
    VARS_NAME = ['x1', 'y1', 'x2', 'y2']

    def __init__(self, *args):
        for _ in range(len(args)):
            setattr(self, self.VARS_NAME[_], args[_])

    def __bool__(self):
        return all([hasattr(self, var) for var in self.VARS_NAME])

    def get_coords(self):
        if not self:
            raise AttributeError('нет координат для извлечения')
        return tuple(getattr(self, var) for var in self.VARS_NAME)


el1 = Ellipse()
el2 = Ellipse(1, 1, 2, 2)
el3 = Ellipse()
el4 = Ellipse(3, 3, 10, 10)
el5 = Ellipse(9, 9)
lst_geom = [el1, el2, el3, el4, el5]
for _, el in enumerate(lst_geom):
    if el:
        el.get_coords()
