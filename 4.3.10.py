class ItemAttrs:

    def __init__(self, *args):
        self._attrs = list(args)

    def __check_index(self, key):
        conditions = [isinstance(key, int), -len(self._attrs) <= key < len(self._attrs)]
        if not all(conditions):
            raise IndexError(f'Index error {key}')

    def __getitem__(self, item):
        self.__check_index(item)
        return self._attrs[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self._attrs[key] = value


class Point(ItemAttrs):
    pass


if __name__ == '__main__':
    pt = Point(1, 2.5)
    x = pt[0]  # 1
    y = pt[1]  # 2.5
    pt[0] = 10
    print(pt[0])