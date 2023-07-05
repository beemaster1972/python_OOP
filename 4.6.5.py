class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:

    def __repr__(self):
        sep = ", "
        attrs = [str(key) + ": " + str(val) for key, val in self.__dict__.items()]
        return f'{self.__class__.__name__}({sep.join(attrs)})'

    def __str__(self):
        sep = "\n"
        attrs = [str(key) + ": " + str(val) for key, val in self.__dict__.items()]
        return f'{sep.join(attrs)}'


class ShopUserView:

    def __repr__(self):
        sep = ", "
        attrs = [str(key) + ": " + str(val) for key, val in self.__dict__.items() if key != "_id"]
        return f'{self.__class__.__name__}({sep.join(attrs)})'

    def __str__(self):
        sep = "\n"
        attrs = [str(key) + ": " + str(val) for key, val in self.__dict__.items() if key != "_id"]
        return f'{sep.join(attrs)}'


class Book(ShopItem):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


if __name__ == '__main__':
    book = Book("Python ООП", "Балакирев", 2022)
    print(book)
