from abc import ABC, abstractmethod


class Model(ABC):
    _ID = 0

    def __new__(cls, *args, **kwargs):
        cls._ID += 1
        return super().__new__(cls)

    @abstractmethod
    def get_pk(self): ...

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self._ID

    def get_pk(self):
        return self._id


if __name__ == '__main__':
    admin = ModelForm('admin', 'admin')
    root = ModelForm('root', '123456')
    lst = [admin, root]
    for el in lst:
        print(el.get_pk())
        print(el.get_info())
