class Note:
    __NOTES_NAME = ' до ре ми фа соль ля си '
    __key_note = {-1: '-бемоль', 0: '', 1: '-диез'}

    def __init__(self, name, ton):
        self.name = name
        self.ton = ton

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ton(self):
        return self._ton

    @ton.setter
    def ton(self, value):
        self._ton = value

    def __setattr__(self, key, value):
        if (key == "_name" and hasattr(self, key) and type(value) != str and value not in Note.__NOTES_NAME) or (
                key == "_ton" and not (type(value) == int and -1 <= value <= 1)):
            raise ValueError(f'недопустимое значение {value} аргумента {key}')
        object.__setattr__(self, key, value)

    def __repr__(self):
        return f'(Note({self.name}, {self._ton})'

    def __str__(self):
        return f"{self.name.title()} {self.__key_note[self.ton]}"


class Notes:
    _instance = None
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si")
    __NOTES_NAME = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        for _, arg in enumerate(self.__slots__):
            setattr(self, arg, Note(self.__NOTES_NAME[_], 0))

    @staticmethod
    def _check_index(key):
        if not (isinstance(key, int) and 0 <= key < 7):
            raise IndexError(f'недопустимый индекс {key}')

    def __getitem__(self, item):
        self._check_index(item)
        return getattr(self, self.__slots__[item])

    def __setitem__(self, key, value):
        self._check_index(key)
        note = getattr(self, self.__slots__[key])
        note.ton = value

    def __str__(self):
        return "\n".join([str(getattr(self, v)) for v in self.__slots__])


if __name__ == '__main__':
    notes = Notes()