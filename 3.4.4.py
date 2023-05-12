class NewList:

    def __init__(self, *args):
        self.__list = list(*args)

    #  Определяем функцию вычитания, в зависимости от направления
    #  если True, то self - other, иначе other - self
    def __subtraction(self, other, direction=True):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError
        other = other if isinstance(other, list) else other.__list
        res = []
        #  Создаем копию вычитаемого, т.к. оригинал может понадобиться в последующих операциях
        minuend = self.__list if direction else other
        subtrahend = other.copy() if direction else self.__list.copy()
        for i, el in enumerate(minuend):
            for j, sub_el in enumerate(subtrahend):
                flag_remove = el is sub_el
                if flag_remove:
                    subtrahend.pop(j)
                    break
            else:
                res.append(el)
        return res

    def __sub__(self, other):
        res = self.__subtraction(other)
        return NewList(res)

    def __rsub__(self, other):
        res = self.__subtraction(other, False)
        return NewList(res)

    def __isub__(self, other):
        self.__list = self.__subtraction(other)
        return self

    def get_list(self):
        return self.__list

lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2
lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], f"метод get_list вернул неверный список {res1.get_list()}"
assert res2.get_list() == [1, -3.4, "abc"], f"метод get_list вернул неверный список {res2.get_list()}"
assert res3.get_list() == [2, 3, 4.5], f"метод get_list вернул неверный список {res3.get_list()}"
assert lst1.get_list() == [-3.4, "abc"], f"метод get_list вернул неверный список {lst1.get_list()}"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], f"метод get_list вернул неверный список {res.get_list()}"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
assert res_4.get_list() == [1, 2], f"метод get_list вернул неверный список {res_4.get_list()}"
