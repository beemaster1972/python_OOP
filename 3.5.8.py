class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, r):
        if not isinstance(r, (MoneyR, MoneyD, MoneyE)):
            raise ValueError('Для регистрации нужно указывать объект классов MoneyX')
        r.cb = cls


class Money:

    def __init__(self, balance=0):
        self.__volume = balance
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, cb):
        self.__cb = cb

    def __setattr__(self, key, value):
        if 'volume' in key and isinstance(value, (int, float)):
            object.__setattr__(self, key, value)
        elif 'cb' in key:  # and (value is None or isinstance(value, CentralBank)):
            object.__setattr__(self, key, value)
        else:
            raise ValueError(f"Неверный тип данных для {key} --> {type(value)}")

    def get_other(self, other):
        try:
            return other.volume * other.cb.rates[self.currency]
        except:
            raise ValueError(f"Неизвестен курс валют {other.currency}.")

    def __eq__(self, other):
        vol = self.get_other(other)
        try:
            return 0 <= abs(self.volume * self.cb.rates[other.currency] - vol) <= 0.1
        except:
            raise ValueError(f"Неизвестен курс валют {self.currency}.")

    def __gt__(self, other):
        vol = self.get_other(other)
        try:
            return abs(self.volume * self.cb.rates[other.currency] - vol) > 0.1
        except:
            raise ValueError(f"Неизвестен курс валют {self.currency}.")

    def __ge__(self, other):
        vol = self.get_other(other)
        try:
            print(abs(self.volume * self.cb.rates[other.currency] - vol))
            print(self.volume * self.cb.rates[other.currency], self.currency, vol, other.currency)
            return abs(self.volume * self.cb.rates[other.currency] - vol) >= 0.1
        except:
            raise ValueError("Неизвестен курс валют.")

    def __repr__(self):
        return str(self.volume) + ' ' + self.currency

class MoneyR(Money):
    currency = 'rub'



class MoneyD(Money):
    currency = 'dollar'



class MoneyE(Money):
    currency = 'euro'



d1 = MoneyD(1)
d2 = MoneyR(72.6)
CentralBank.register(d1)
CentralBank.register(d2)
res = d1 >= d2
print(res)