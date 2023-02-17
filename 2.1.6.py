class Book:

    def __init__(self, autor: str, title: str, price: int = 0):
        if self.__check_price(price):
            self.__price = price
        self.__title = title
        self.__author = autor

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        if self.__check_price(price):
            self.__price = price

    @classmethod
    def __check_price(cls, price):
        return type(price) in (int, ) and price >= 0

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
