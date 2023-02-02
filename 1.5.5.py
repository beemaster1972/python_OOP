# class TriangleCheker:
#
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if any([not isinstance(self.a, (int, float)), not isinstance(self.b, (int, float)),
#                not isinstance(self.c, (int, float)), type(self.a) == bool, type(self.b) == bool, type(self.c) == bool])\
#                 or any([self.a <= 0, self.b <= 0, self.c <= 0]):
#             return 1
#         elif any((self.a >= (self.b + self.c), self.b >= (self.a + self.c), self.c >= (self.b + self.a))):
#             return 2
#         else:
#             return 3


from itertools import permutations


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        params = self.__dict__.values()

        if not all(map(lambda x: type(x) in (int, float) and x > 0, params)):
            return 1

        if not all(map(lambda x: x[0] + x[1] > x[2], permutations(params, 3))):
            return 2

        return 3

a, b, c = map(int, input().split())
tr = TriangleCheker('3', True, 5)
print(tr.is_triangle())
