import re
class PhoneNumber:

    def __init__(self, number, fio):
        if self.__check(number):
            self.__number = number
        self.__fio = fio
        self.__indx = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.__check(number):
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__fio = fio

    @property
    def indx(self):
        return self.__indx

    @indx.setter
    def indx(self, indx):
        self.__indx = indx

    def __check(self, number):
        