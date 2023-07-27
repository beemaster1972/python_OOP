class Point:

    def __init__(self, x=0, y=0):
        self._x, self._y = x, y

    def __repr__(self):
        return f'Point: x = {self._x}, y = {self._y}'


def check_num(val):
    try:
        return int(val)
    except:
        try:
            return float(val)
        except:
            raise TypeError


try:
    x, y = map(check_num, input().split())
    pt = Point(x, y)
except:
    pt = Point()
finally:
    print(pt)
