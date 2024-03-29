class WordString:

    def __init__(self, string=''):
        if self.check_string(string):
            self.__string = string
            self.__words = list(string.split())

    def __len__(self):
        return len(self.__words)

    def __call__(self, *args, **kwargs):
        try:
            return self.__words[args[0]]
        except IndexError:
            return None

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        if self.check_string(string):
            self.__string = string
            self.__words = string.split()

    @staticmethod
    def check_string(string):
        return isinstance(string, str)


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")