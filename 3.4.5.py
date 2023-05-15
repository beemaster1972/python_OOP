class ListMath:

    def __init__(self, lst: list = []):
        self.lst_math = [el for el in lst if type(el) in (int, float)]

    @staticmethod
    def check_operand(value):
        if not isinstance(value, (int, float)):
            raise ArithmeticError("Второй операнд должен быть int или float")
        return True
    # def __setattr__(self, key, value):
    #     object.__setattr__(self, key, value)

    def __add__(self, other):
        if self.check_operand(other):
            return ListMath([el+other for el in self.lst_math])

    def __radd__(self, other):
        if self.check_operand(other):
            return self.__add__(other)

    def __iadd__(self, other):
        if self.check_operand(other):
            self.lst_math = self.__add__(other).lst_math
        return self

    def __sub__(self, other):
        if self.check_operand(other):
            return ListMath([el-other for el in self.lst_math])

    def __rsub__(self, other):
        if self.check_operand(other):
            return ListMath([other - el for el in self.lst_math])

    def __isub__(self, other):
        if self.check_operand(other):
            self.lst_math = self.__sub__(other).lst_math
            return self

    def __mul__(self, other):
        if self.check_operand(other):
            return ListMath([el * other for el in self.lst_math])

    def __rmul__(self, other):
        if self.check_operand(other):
            return self.__mul__(other)

    def __imul__(self, other):
        if self.check_operand(other):
            self.lst_math = self.__mul__(other).lst_math
            return self

    def __truediv__(self, other):
        if self.check_operand(other):
            return ListMath([el/other for el in self.lst_math])

    def __rtruediv__(self, other):
        if self.check_operand(other):
            return ListMath([other/el for el in self.lst_math])

    def __itruediv__(self, other):
        if self.check_operand(other):
            self.lst_math = self.__truediv__(other).lst_math
            return self


lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0