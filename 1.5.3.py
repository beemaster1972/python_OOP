class Point:
    x = 0
    y = 0
    color = 'black'

    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1, 2001, 2):
    p = Point(i, i)
    points.append(p)
points[1].color = 'yellow'
print(len(points), points[1].x, points[1].y, points[1].color)
