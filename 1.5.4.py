import random as r


class Figures:
    name = ''

    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = a, b
        self.ep = c, d


class Line(Figures):
    name = 'Line'


class Rect(Figures):
    name = 'Rectangle'


class Ellipse(Figures):
    name = 'Ellipse'


elemetns = []

for i in range(217):
    el = r.choice((Line, Rect, Ellipse))(r.randint(0, 1000), r.randint(0, 1000), r.randint(0, 1000), r.randint(0, 1000))
    elemetns.append(el)

for el in elemetns:
    if el.name == 'Line':
        el.sp = (0, 0)
        el.ep = (0, 0)
    print(len(elemetns), el.name, el.sp, el.ep)