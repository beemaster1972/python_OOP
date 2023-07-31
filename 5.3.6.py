class TupleLimit(tuple):

    def __new__(cls, *args, **kwargs):
        tl = super().__new__(cls, args[0])
        if len(args) > 1:
            tl._max_length = args[1]
        elif len(kwargs) >= 1:
            tl._max_length = kwargs.get('max_length', None)
        else:
            raise TypeError("Missing required argument 'max_length'")

        if not (tl._max_length and len(args[0]) <= tl._max_length):
            raise ValueError('число элементов коллекции превышает заданный предел')
        return tl

    def __repr__(self):
        return " ".join([str(el) for el in self])


if __name__ == '__main__':
    digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)
    try:
        tl = TupleLimit(digits, max_length=5)
        print(tl)
    except Exception as e:
        print(e)
