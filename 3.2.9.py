class InputDigits:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        inp = self.fn()
        return [int(x) for x in inp.split()]

@InputDigits
def input_dg():
    return input()


res = input_dg()
