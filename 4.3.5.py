class SellItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None

    def __repr__(self):
        
        return f'{self.__class__.__name__}()'

class House(SellItem):

    pass
